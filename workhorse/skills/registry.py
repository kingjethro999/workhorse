"""
Cross-Agent Skills Harvester and In-Memory Registry.
Scans Claude, Antigravity, Cursor, and local directories.
"""
import os
from pathlib import Path
from typing import Dict, List, Optional
from workhorse.skills.models import Skill, SkillMetadata

class SkillRegistry:
    _instance = None

    def __init__(self):
        self.skills: Dict[str, Skill] = {}
        self.scan_all()

    @classmethod
    def get(cls) -> "SkillRegistry":
        if cls._instance is None:
            cls._instance = SkillRegistry()
        return cls._instance

    def scan_all(self, workspace_path: Optional[str] = None):
        """Scans all standard cross-agent directories for SKILL.md files."""
        home = Path.home()
        search_roots = [
            # Claude Code & Desktop
            (home / ".claude" / "skills", "claude"),
            (home / ".config" / "claude" / "skills", "claude"),
            # Antigravity & Gemini CLI
            (home / ".gemini" / "antigravity" / "skills", "antigravity"),
            (home / ".gemini" / "antigravity" / "builtin" / "skills", "antigravity"),
            (home / ".gemini" / "config" / "plugins", "antigravity"),
            # Cursor & Codex
            (home / ".cursor" / "skills", "cursor"),
            (home / ".codex" / "skills", "codex"),
            # Workhorse Global
            (home / ".local" / "share" / "workhorse" / "skills", "workhorse"),
            (home / ".config" / "workhorse" / "skills", "workhorse"),
        ]

        if workspace_path:
            w_path = Path(workspace_path)
            search_roots.extend([
                (w_path / ".workhorse" / "skills", "workspace"),
                (w_path / ".agent" / "skills", "workspace"),
                (w_path / ".claude" / "skills", "workspace"),
                (w_path / ".cursor" / "skills", "workspace"),
            ])

        for root_path, origin in search_roots:
            if not root_path.exists():
                continue
            for skill_file in root_path.glob("**/SKILL.md"):
                s = Skill.parse_from_file(skill_file, origin=origin)
                if s:
                    self.skills[s.metadata.name.lower()] = s

    def find_matching_skill(self, prompt: str) -> Optional[Skill]:
        """Matches user prompt against skill descriptions and triggers."""
        lowered = prompt.lower()
        if "/skill:" in lowered:
            parts = lowered.split("/skill:")[1].split()
            if parts:
                target_name = parts[0].strip()
                if target_name in self.skills:
                    return self.skills[target_name]

        for skill in self.skills.values():
            for trigger in skill.metadata.triggers:
                if trigger.lower() in lowered:
                    return skill

        return None

    def list_skills(self) -> List[SkillMetadata]:
        return [s.metadata for s in self.skills.values()]
