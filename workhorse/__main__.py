"""
Direct invocation module for `python -m workhorse`.
"""
import sys
import os
from pathlib import Path

_root_dir = str(Path(__file__).resolve().parent.parent)
_venv_python = os.path.join(_root_dir, ".venv", "bin", "python")

if __name__ == "__main__":
    _in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    if not _in_venv and os.path.exists(_venv_python):
        os.execv(_venv_python, [_venv_python] + sys.argv)

if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from workhorse.cli import run_cli

if __name__ == "__main__":
    run_cli()
