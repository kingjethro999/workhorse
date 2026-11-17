"""
Active Repository File CRUD & Chunking Engine.
Operates directly on the active working repository without sandboxing restrictions.
"""
import os
import shutil
import time
import ast
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

class WorkspaceManager:
    def __init__(self, root_dir: Optional[str] = None):
        self.root = Path(root_dir or os.getcwd()).resolve()
        self.backup_dir = self.root / ".workhorse_backups"

    def list_dir(self, rel_path: str = ".") -> List[Dict[str, Any]]:
        target = (self.root / rel_path).resolve()
        if not target.is_dir():
            raise NotADirectoryError(f"Not a directory: {rel_path}")
        results = []
        for item in sorted(target.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
            if item.name.startswith((".git", ".venv", "__pycache__", ".workhorse_backups", "node_modules")):
                continue
            results.append({
                "name": item.name,
                "is_dir": item.is_dir(),
                "size": item.stat().st_size if item.is_file() else 0,
                "path": str(item.relative_to(self.root))
            })
        return results

    def read_file(self, rel_path: str, max_lines: int = 1000) -> str:
        target = (self.root / rel_path).resolve()
        if not target.is_file():
            raise FileNotFoundError(f"File not found: {rel_path}")
        with open(target, "r", encoding="utf-8", errors="replace") as f:
            lines = [f.readline() for _ in range(max_lines)]
        return "".join(lines)

    def read_file_chunks(self, rel_path: str, chunk_size_lines: int = 200) -> List[Dict[str, Any]]:
        target = (self.root / rel_path).resolve()
        if not target.is_file():
            raise FileNotFoundError(f"File not found: {rel_path}")
        with open(target, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        total = len(lines)
        chunks = []
        for i in range(0, total, chunk_size_lines):
            slice_lines = lines[i:i + chunk_size_lines]
            chunks.append({
                "chunk_index": len(chunks) + 1,
                "total_chunks": (total + chunk_size_lines - 1) // chunk_size_lines,
                "start_line": i + 1,
                "end_line": min(i + chunk_size_lines, total),
                "content": "".join(slice_lines)
            })
        return chunks

    def validate_syntax(self, rel_path: str, content: str) -> Tuple[bool, Optional[str]]:
        """Pre-validates syntax before file write."""
        ext = Path(rel_path).suffix.lower()
        if ext == ".py":
            try:
                ast.parse(content)
            except SyntaxError as e:
                return False, f"Python SyntaxError at line {e.lineno}: {e.msg}"
        elif ext == ".json":
            try:
                json.loads(content)
            except json.JSONDecodeError as e:
                return False, f"JSONDecodeError at line {e.lineno}: {e.msg}"
        return True, None

    def write_file(self, rel_path: str, content: str, overwrite: bool = True, validate: bool = False) -> bool:
        target = (self.root / rel_path).resolve()
        if target.exists() and not overwrite:
            raise FileExistsError(f"File exists: {rel_path}")

        if validate:
            is_valid, err = self.validate_syntax(rel_path, content)
            if not is_valid:
                raise ValueError(f"Syntax validation failed for {rel_path}: {err}")

        if target.exists():
            self._backup(target)

        target.parent.mkdir(parents=True, exist_ok=True)
        tmp = target.with_suffix(f".tmp_{int(time.time())}_wh")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(content)
        tmp.replace(target)
        return True

    def delete_path(self, rel_path: str) -> bool:
        target = (self.root / rel_path).resolve()
        if not target.exists():
            raise FileNotFoundError(f"Path not found: {rel_path}")
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
        return True

    def get_repo_summary(self, max_files: int = 15) -> str:
        tree = []
        high_signals = ["README.md", "pyproject.toml", "package.json", "Cargo.toml", "go.mod", "Makefile", "requirements.txt"]
        file_previews = []

        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if not d.startswith((".git", ".venv", "node_modules", "__pycache__", ".workhorse"))]
            rel_dir = os.path.relpath(root, self.root)
            for f in files:
                rel_f = os.path.join(rel_dir, f) if rel_dir != "." else f
                tree.append(rel_f)
                if f in high_signals and len(file_previews) < max_files:
                    try:
                        content = self.read_file(rel_f, max_lines=80)
                        file_previews.append(f"--- File: {rel_f} ---\n{content}")
                    except Exception:
                        pass

        summary = f"Total Files Discovered: {len(tree)}\nKey File Listing:\n" + "\n".join(f"- {p}" for p in tree[:30])
        if file_previews:
            summary += "\n\nKey File Contents:\n" + "\n\n".join(file_previews)
        return summary

    def _backup(self, target: Path) -> None:
        try:
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            timestamp = int(time.time())
            bak = self.backup_dir / f"{target.name}.{timestamp}.bak"
            shutil.copy2(target, bak)
        except Exception:
            pass
