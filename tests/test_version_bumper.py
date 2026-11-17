"""
Unit tests for the Workhorse Version Bumper algorithm.
"""
import pytest
from scripts.bump_version import compute_next_version

def test_standard_patch_bump():
    assert compute_next_version("0.0.1") == "0.0.2"
    assert compute_next_version("0.0.7") == "0.0.8"
    assert compute_next_version("0.0.8") == "0.0.9"

def test_minor_roll_on_patch_9():
    # on every x.x.9, bump to x.1.0 (or x.(minor+1).0)
    assert compute_next_version("0.0.9") == "0.1.0"
    assert compute_next_version("0.1.9") == "0.2.0"
    assert compute_next_version("1.42.9") == "1.43.0"

def test_major_roll_on_minor_599_patch_9():
    # on every x.599.9, bump to 1.x.x (or (x+1).0.0)
    assert compute_next_version("0.599.9") == "1.0.0"
    assert compute_next_version("1.599.9") == "2.0.0"
    assert compute_next_version("2.599.9") == "3.0.0"

def test_leading_v_handling():
    assert compute_next_version("v0.0.1") == "0.0.2"
    assert compute_next_version("v0.0.9") == "0.1.0"
    assert compute_next_version("v0.599.9") == "1.0.0"

def test_invalid_format_raises():
    with pytest.raises(ValueError):
        compute_next_version("1.0")
    with pytest.raises(ValueError):
        compute_next_version("invalid")

def test_bump_all_files_integration(tmp_path):
    from scripts.bump_version import bump_all_files
    # Setup test workspace
    (tmp_path / "version").write_text("0.0.9\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "test"\nversion = "0.0.9"\n', encoding="utf-8")
    
    pkg_dir = tmp_path / "workhorse"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").write_text('__version__ = "0.0.9"\n', encoding="utf-8")

    web_dir = tmp_path / "web"
    web_dir.mkdir()
    (web_dir / "package.json").write_text('{"name": "web", "version": "0.0.9"}\n', encoding="utf-8")

    old_v, new_v = bump_all_files(tmp_path)
    assert old_v == "0.0.9"
    assert new_v == "0.1.0"

    assert (tmp_path / "version").read_text(encoding="utf-8").strip() == "0.1.0"
    assert 'version = "0.1.0"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    assert '__version__ = "0.1.0"' in (pkg_dir / "__init__.py").read_text(encoding="utf-8")
    assert '"version": "0.1.0"' in (web_dir / "package.json").read_text(encoding="utf-8")
