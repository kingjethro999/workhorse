"""
JSON-RPC 2.0 Models for Model Context Protocol (MCP).
"""
from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel

class JSONRPCRequest(BaseModel):
    jsonrpc: str = "2.0"
    id: Union[int, str]
    method: str
    params: Optional[Dict[str, Any]] = None

class JSONRPCResponse(BaseModel):
    jsonrpc: str = "2.0"
    id: Union[int, str]
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None

class MCPTool(BaseModel):
    name: str
    description: str
    inputSchema: Dict[str, Any]
    server_name: str
