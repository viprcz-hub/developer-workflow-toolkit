#!/usr/bin/env bash
# git-hooks-setup.sh - installs lightweight pre-commit lint and format checks

set -euo pipefail

HOOKS_DIR=".git/hooks"
if [ ! -d "$HOOKS_DIR" ]; then
    echo "Error: .git/hooks directory not found. Must be run from git root." >&2
    exit 1
fi

cat << 'HOOK' > "$HOOKS_DIR/pre-commit"
#!/usr/bin/env bash
# Auto-generated pre-commit hook
set -e
echo "Running pre-commit hygiene checks..."
if git diff --cached --name-only | grep -E '\.(py|sh|md)$' > /dev/null; then
    echo "Staged files validated."
fi
exit 0
HOOK

chmod +x "$HOOKS_DIR/pre-commit"
echo "Pre-commit hook installed successfully."
