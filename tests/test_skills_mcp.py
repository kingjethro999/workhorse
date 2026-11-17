"""
Unit tests for Cross-Agent Skills and MCP Protocol models.
"""
import tempfile
import shutil
from pathlib import Path
from workhorse.skills.models import Skill, SkillMetadata
from workhorse.skills.registry import SkillRegistry
from workhorse.mcp.protocol import JSONRPCRequest, JSONRPCResponse, MCPTool

def test_skill_frontmatter_parsing():
    tmp = tempfile.mkdtemp()
    try:
        skill_file = Path(tmp) / "SKILL.md"
        skill_file.write_text("""---
name: test-skill
description: A test skill for validation.
triggers:
  - test
  - validate
---
# Test Skill Instructions
Do something useful.
""")
        skill = Skill.parse_from_file(skill_file, origin="workspace")
        assert skill is not None
        assert skill.metadata.name == "test-skill"
        assert "validate" in skill.metadata.triggers
        assert "Test Skill Instructions" in skill.instructions
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def test_mcp_protocol_models():
    req = JSONRPCRequest(id=1, method="tools/list", params={})
    raw_json = req.model_dump_json()
    assert '"jsonrpc":"2.0"' in raw_json
    assert '"method":"tools/list"' in raw_json

    resp = JSONRPCResponse(id=1, result={"tools": []})
    assert resp.result == {"tools": []}

    tool = MCPTool(name="read_file", description="reads a file", inputSchema={}, server_name="filesystem")
    assert tool.name == "read_file"
