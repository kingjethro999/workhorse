"""
Safe Command Execution Helper.
"""
import subprocess

def run_bash(cmd: str, timeout: int = 30) -> dict:
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return {"stdout": p.stdout[:5000], "stderr": p.stderr[:5000], "code": p.returncode}
    except Exception as e:
        return {"stdout": "", "stderr": str(e), "code": -1}
