#!/usr/bin/env python3
"""
Workhorse Terminal UI Application Entrypoint.
Provides WorkhorseApp and standalone TUI / CLI launcher.
"""
import sys
import os
from pathlib import Path

_root_dir = str(Path(__file__).resolve().parent)
_venv_python = os.path.join(_root_dir, ".venv", "bin", "python")

# If invoked directly and NOT already in a virtualenv, re-exec into isolated .venv
if __name__ == "__main__":
    _in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    if not _in_venv and os.path.exists(_venv_python):
        os.execv(_venv_python, [_venv_python] + sys.argv)

if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from workhorse.tui.app import WorkhorseApp

def main():
    if len(sys.argv) > 1 and not (len(sys.argv) == 2 and sys.argv[1] in ("-t", "--tui")):
        from workhorse.cli import run_cli
        run_cli()
    else:
        app = WorkhorseApp()
        app.run()

if __name__ == "__main__":
    main()
