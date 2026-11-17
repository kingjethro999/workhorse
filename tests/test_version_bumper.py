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
