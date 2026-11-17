#!/usr/bin/env bash
# =============================================================================
# Workhorse Tri-Alias Global Installer (workhorse, workhouse, wh)
# =============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)"
LOCAL_BIN="$HOME/.local/bin"

if [ ! -f "$SCRIPT_DIR/workhorse.py" ]; then
    INSTALL_TARGET="$HOME/.workhorse"
    echo "[*] Resolving latest Workhorse release from GitHub..."
    LATEST_TAG=$(curl -sSL -H "Accept: application/vnd.github+json" https://api.github.com/repos/kingjethro999/workhorse/releases/latest 2>/dev/null | grep -o '"tag_name": *"[^"]*"' | head -n 1 | cut -d'"' -f4)
    if [ -z "$LATEST_TAG" ]; then
        LATEST_TAG="main"
    fi
    echo "[*] Installing Workhorse release ($LATEST_TAG) into $INSTALL_TARGET..."
    if [ -d "$INSTALL_TARGET/.git" ]; then
        (cd "$INSTALL_TARGET" && git fetch --tags 2>/dev/null && git checkout "$LATEST_TAG" 2>/dev/null || git checkout main)
    else
        git clone --depth 1 --branch "$LATEST_TAG" https://github.com/kingjethro999/workhorse.git "$INSTALL_TARGET" 2>/dev/null || \
        git clone https://github.com/kingjethro999/workhorse.git "$INSTALL_TARGET"
    fi
    SCRIPT_DIR="$INSTALL_TARGET"
fi

echo "=== Installing Workhorse Workstation (Tri-Alias: workhorse, workhouse, wh) ==="

# 1. Setup isolated virtualenv if needed
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo "[*] Creating virtual environment at $SCRIPT_DIR/.venv..."
    python3 -m venv "$SCRIPT_DIR/.venv"
fi

echo "[*] Upgrading pip and installing dependencies..."
"$SCRIPT_DIR/.venv/bin/pip" install --upgrade pip
"$SCRIPT_DIR/.venv/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"
"$SCRIPT_DIR/.venv/bin/pip" install -e "$SCRIPT_DIR"

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

# 5. Check PATH and inform user
echo ""
if [[ ":$PATH:" != *":$LOCAL_BIN:"* ]]; then
    echo "[!] Notice: $LOCAL_BIN is not currently in your \$PATH."
    echo "    Add this to your ~/.bashrc or ~/.zshrc:"
    echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
fi

echo "[SUCCESS] Workhorse installed successfully!"
echo "          Executable from ANY directory via: workhorse, workhouse, or wh"
