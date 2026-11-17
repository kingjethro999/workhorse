#!/usr/bin/env bash
# =============================================================================
# Workhorse Tri-Alias Global Installer (workhorse, workhouse, wh)
# =============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_BIN="$HOME/.local/bin"

echo "=== Installing Workhorse Workstation (Tri-Alias: workhorse, workhouse, wh) ==="

# 1. Setup isolated virtualenv if needed
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo "[*] Creating virtual environment at $SCRIPT_DIR/.venv..."
    python3 -m venv "$SCRIPT_DIR/.venv"
fi

echo "[*] Upgrading pip and installing dependencies..."
"$SCRIPT_DIR/.venv/bin/pip" install --upgrade pip
"$SCRIPT_DIR/.venv/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"

# 2. Setup global wrapper in ~/.local/bin
mkdir -p "$LOCAL_BIN"
LAUNCHER="$LOCAL_BIN/workhorse"

echo "[*] Writing global launcher to $LAUNCHER..."
cat << EOF > "$LAUNCHER"
#!/usr/bin/env bash
INSTALL_DIR="$SCRIPT_DIR"
export WORKHORSE_INVOCATION_CWD="\$(pwd)"
export WORKHORSE_INSTALL_DIR="\$INSTALL_DIR"
exec "\$INSTALL_DIR/.venv/bin/python" "\$INSTALL_DIR/workhorse.py" "\$@"
EOF

chmod +x "$LAUNCHER"
chmod +x "$SCRIPT_DIR/workhorse.py"
chmod +x "$SCRIPT_DIR/app.py"

# 3. Create symlinks for workhouse and wh
echo "[*] Creating aliases 'workhouse' and 'wh'..."
ln -sf "$LAUNCHER" "$LOCAL_BIN/workhouse"
ln -sf "$LAUNCHER" "$LOCAL_BIN/wh"

# 4. Install Git Commit Hook if in a git repo
if [ -d "$SCRIPT_DIR/.git" ]; then
    echo "[*] Installing version bumper git pre-commit hook..."
    mkdir -p "$SCRIPT_DIR/.git/hooks"
    cp "$SCRIPT_DIR/scripts/git-hooks/pre-commit" "$SCRIPT_DIR/.git/hooks/pre-commit"
    chmod +x "$SCRIPT_DIR/.git/hooks/pre-commit"
fi

# 5. Check PATH configuration
if [[ ":$PATH:" != *":$LOCAL_BIN:"* ]]; then
    echo "[!] Notice: $LOCAL_BIN is not in your current PATH."
    if ! grep -q '\.local/bin' "$HOME/.bashrc" 2>/dev/null; then
        echo "[*] Adding export PATH=\"\$HOME/.local/bin:\$PATH\" to ~/.bashrc..."
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    fi
fi

echo "============================================================"
echo "  [SUCCESS] Installed: 'workhorse', 'workhouse', and 'wh'    "
echo "  Call 'wh' or 'workhouse' in ANY directory to launch TUI!  "
echo "============================================================"
