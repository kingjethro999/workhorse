"""
Universal Asynchronous Stdio MCP Client.
Spawns external tool processes and executes calls over JSON-RPC 2.0.
"""
import asyncio
import json
import os
from typing import Dict, Any, List, Optional
from workhorse.mcp.protocol import JSONRPCRequest, JSONRPCResponse, MCPTool

class StdioMCPClient:
    def __init__(self, server_name: str, command: str, args: List[str], env: Optional[Dict[str, str]] = None):
        self.server_name = server_name
        self.command = command
        self.args = args
        self.env = env or {}
        self.process: Optional[asyncio.subprocess.Process] = None
        self._request_id = 0
        self.tools: List[MCPTool] = []
        self.is_connected = False

    async def connect(self):
        """Spawns server subprocess and performs MCP handshake."""
        full_env = os.environ.copy()
        full_env.update(self.env)
        
        self.process = await asyncio.create_subprocess_exec(
            self.command,
            *self.args,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=full_env
        )

        # 1. Initialize
        init_res = await self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "clientInfo": {"name": "workhorse", "version": "3.1.0"}
        })
        
        # 2. Initialized Notification
        await self._send_notification("notifications/initialized", {})

        # 3. List Tools
        tools_res = await self._send_request("tools/list", {})
        if tools_res and "tools" in tools_res:
            self.tools = [
                MCPTool(
                    name=t["name"],
                    description=t.get("description", ""),
                    inputSchema=t.get("inputSchema", {}),
                    server_name=self.server_name
                )
                for t in tools_res["tools"]
            ]
        self.is_connected = True

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Executes an MCP tool call on the connected server."""
        if not self.is_connected:
            raise ConnectionError(f"MCP server '{self.server_name}' is not connected.")
        res = await self._send_request("tools/call", {
            "name": tool_name,
            "arguments": arguments
        })
        if res and "content" in res:
            text_blocks = [c.get("text", "") for c in res["content"] if c.get("type") == "text"]
            return "\n".join(text_blocks)
        return json.dumps(res)

    async def _send_request(self, method: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        self._request_id += 1
        req = JSONRPCRequest(id=self._request_id, method=method, params=params)
        payload = req.model_dump_json() + "\n"
        
        if not self.process or not self.process.stdin:
            return None
        self.process.stdin.write(payload.encode("utf-8"))
        await self.process.stdin.drain()

        if not self.process.stdout:
            return None
        line = await self.process.stdout.readline()
        if not line:
            return None
        res = json.loads(line.decode("utf-8"))
        return res.get("result")

    async def _send_notification(self, method: str, params: Dict[str, Any]):
        payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": params}) + "\n"
        if self.process and self.process.stdin:
            self.process.stdin.write(payload.encode("utf-8"))
            await self.process.stdin.drain()

    async def disconnect(self):
        if self.process:
            try:
                self.process.terminate()
                await self.process.wait()
            except Exception:
                pass
        self.is_connected = False
