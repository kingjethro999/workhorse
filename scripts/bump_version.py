#!/usr/bin/env python3
"""
Workhorse Version Bumper & Git Commit Hook Helper.

Bumping Rules:
- On every commit: bump patch (+0.0.1)
- On every x.x.9: bump to x.(x+1).0
- On every x.599.9: bump to (x+1).0.0
"""
import re
import sys
from pathlib import Path

def compute_next_version(ver_str: str) -> str:
    clean = ver_str.strip().lstrip("v")
    parts = clean.split(".")
    if len(parts) != 3:
        raise ValueError(f"Version must be in MAJOR.MINOR.PATCH format, got: {ver_str}")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])

    if patch == 9:
        if minor == 599:
            major += 1
            minor = 0
            patch = 0
        else:
            minor += 1
            patch = 0
    else:
        patch += 1

    return f"{major}.{minor}.{patch}"

def bump_all_files(repo_root: Path) -> tuple[str, str]:
    version_file = repo_root / "version"
    pyproject_file = repo_root / "pyproject.toml"

    if not version_file.exists():
        version_file.write_text("0.0.1\n", encoding="utf-8")
        current_version = "0.0.1"
    else:
        current_version = version_file.read_text(encoding="utf-8").strip()

    next_version = compute_next_version(current_version)

    # 1. Update version file
    version_file.write_text(f"{next_version}\n", encoding="utf-8")

    # 2. Update pyproject.toml
    if pyproject_file.exists():
        content = pyproject_file.read_text(encoding="utf-8")
        new_content = re.sub(
            r'version\s*=\s*"[^"]+"',
            f'version = "{next_version}"',
            content,
            count=1
        )
        pyproject_file.write_text(new_content, encoding="utf-8")

    # 3. Update workhorse/__init__.py if __version__ is defined
    init_file = repo_root / "workhorse" / "__init__.py"
    if init_file.exists():
        init_content = init_file.read_text(encoding="utf-8")
        if "__version__" in init_content:
            new_init = re.sub(
                r'__version__\s*=\s*"[^"]+"',
                f'__version__ = "{next_version}"',
                init_content,
                count=1
            )
            init_file.write_text(new_init, encoding="utf-8")
        else:
            init_file.write_text(f'__version__ = "{next_version}"\n' + init_content, encoding="utf-8")

    return current_version, next_version

if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    old_v, new_v = bump_all_files(root)
    print(f"[Workhorse Version Hook] Bumped version from {old_v} -> {new_v}")
