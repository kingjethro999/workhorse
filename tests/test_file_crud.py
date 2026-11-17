"""
Unit tests for Active Repository File CRUD and Chunking Engine.
"""
import tempfile
import shutil
from pathlib import Path
from workhorse.tools.file_crud import WorkspaceManager

def test_workspace_file_operations():
    tmp_dir = tempfile.mkdtemp()
    try:
        wm = WorkspaceManager(tmp_dir)

        # 1. Write file
        wm.write_file("test.txt", "line1\nline2\nline3\n")
        assert (Path(tmp_dir) / "test.txt").exists()

        # 2. Read file
        content = wm.read_file("test.txt")
        assert "line1\nline2\nline3\n" == content

        # 3. Read chunks
        chunks = wm.read_file_chunks("test.txt", chunk_size_lines=2)
        assert len(chunks) == 2
        assert chunks[0]["start_line"] == 1
        assert chunks[0]["end_line"] == 2
        assert chunks[1]["start_line"] == 3

        # 4. Overwrite file and check backup creation
        wm.write_file("test.txt", "updated content")
        assert (Path(tmp_dir) / ".workhorse_backups").exists()
        backups = list((Path(tmp_dir) / ".workhorse_backups").glob("*.bak"))
        assert len(backups) == 1

        # 5. List dir
        items = wm.list_dir(".")
        assert any(item["name"] == "test.txt" for item in items)

        # 6. Delete file
        wm.delete_path("test.txt")
        assert not (Path(tmp_dir) / "test.txt").exists()

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

def test_syntax_validation():
    tmp_dir = tempfile.mkdtemp()
    try:
        wm = WorkspaceManager(tmp_dir)
        valid_py = "def foo():\n    return 42\n"
        is_val, err = wm.validate_syntax("code.py", valid_py)
        assert is_val is True
        assert err is None

        invalid_py = "def foo( return 42"
        is_val, err = wm.validate_syntax("bad.py", invalid_py)
        assert is_val is False
        assert "SyntaxError" in err
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
