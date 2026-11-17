"""
Universal MCP Subsystem.
"""
from workhorse.mcp.protocol import JSONRPCRequest, JSONRPCResponse, MCPTool
from workhorse.mcp.client import StdioMCPClient
from workhorse.mcp.registry import MCPRegistry

__all__ = ["JSONRPCRequest", "JSONRPCResponse", "MCPTool", "StdioMCPClient", "MCPRegistry"]
