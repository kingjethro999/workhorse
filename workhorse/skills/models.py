"""
Data models and frontmatter parser for Cross-Agent Skills.
"""
from pathlib import Path
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
import re

class SkillMetadata(BaseModel):
    name: str
    description: str
    triggers: List[str] = Field(default_factory=list)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    mcp_dependencies: List[str] = Field(default_factory=list)
    path: Path
    origin: str  # "claude", "antigravity", "cursor", "workhorse", "workspace"

class Skill:
    def __init__(self, metadata: SkillMetadata, instructions: str, script_dir: Optional[Path] = None):
        self.metadata = metadata
        self.instructions = instructions
        self.script_dir = script_dir

    @classmethod
    def parse_from_file(cls, skill_file: Path, origin: str = "custom") -> Optional["Skill"]:
        try:
            content = skill_file.read_text(encoding="utf-8", errors="replace")
            # Parse YAML Frontmatter
            frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
            if not frontmatter_match:
                name = skill_file.parent.name if skill_file.name == "SKILL.md" else skill_file.stem
                meta = SkillMetadata(
                    name=name,
                    description=f"Skill loaded from {origin}",
                    path=skill_file,
                    origin=origin
                )
                return cls(metadata=meta, instructions=content)

            fm_raw, instructions = frontmatter_match.groups()
            import yaml
            data = yaml.safe_load(fm_raw) or {}
            
            meta = SkillMetadata(
                name=data.get("name", skill_file.parent.name),
                description=data.get("description", "No description provided."),
                triggers=data.get("triggers", []),
                parameters=data.get("parameters", {}),
                mcp_dependencies=data.get("mcp_dependencies", []),
                path=skill_file,
                origin=origin
            )
            script_path = skill_file.parent / "scripts"
            return cls(
                metadata=meta,
                instructions=instructions.strip(),
                script_dir=script_path if script_path.is_dir() else None
            )
        except Exception:
            return None
