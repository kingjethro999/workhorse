"""
Cross-Agent MCP Discovery Engine.
Reads configs from Claude Desktop, Claude Code, Cursor, and Antigravity.
"""
import os
import json
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any
from workhorse.mcp.client import StdioMCPClient

class MCPRegistry:
    _instance = None

    def __init__(self):
        self.clients: Dict[str, StdioMCPClient] = {}
        self.discover_servers()

    @classmethod
    def get(cls) -> "MCPRegistry":
        if cls._instance is None:
            cls._instance = MCPRegistry()
        return cls._instance

    def discover_servers(self, workspace_path: Optional[str] = None):
        """Scans for external MCP config files."""
        home = Path.home()
        config_files = [
            # Claude Desktop
            home / ".config" / "Claude" / "claude_desktop_config.json",
            # Claude Code
            home / ".claude" / "mcp.json",
            # Cursor
            home / ".cursor" / "mcp.json",
            # Workhorse Global
            home / ".config" / "workhorse" / "mcp.json",
        ]

        if workspace_path:
            config_files.append(Path(workspace_path) / ".cursor" / "mcp.json")
            config_files.append(Path(workspace_path) / ".workhorse" / "mcp.json")

        for cfg_path in config_files:
            if not cfg_path.is_file():
                continue
            try:
                data = json.loads(cfg_path.read_text(encoding="utf-8"))
                servers = data.get("mcpServers", {})
                for s_name, s_conf in servers.items():
                    if s_name not in self.clients and "command" in s_conf:
                        self.clients[s_name] = StdioMCPClient(
                            server_name=s_name,
                            command=s_conf["command"],
                            args=s_conf.get("args", []),
                            env=s_conf.get("env", {})
                        )
            except Exception:
                continue

    async def initialize_all(self):
        for client in self.clients.values():
            if not client.is_connected:
                try:
                    await asyncio.wait_for(client.connect(), timeout=5.0)
                except Exception:
                    pass

    def get_all_tools(self) -> List[Any]:
        all_tools = []
        for client in self.clients.values():
            if client.is_connected:
                all_tools.extend(client.tools)
        return all_tools
