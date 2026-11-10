# developer-workflow-toolkit

> Practical automation scripts, Git utilities, and productivity recipes for modern engineering environments.

## Overview
A curated set of lightweight, single-purpose workflow tools designed to keep local repositories clean, verify repo hygiene, and streamline daily engineering routines without heavyweight dependencies.

## Included Tools
- **Git Merged Branch Cleaner (`scripts/git-cleanup.sh`)**: Prunes merged local branches and removes stale remote references.
- **Repository Hygiene Auditor (`scripts/repo-audit.py`)**: Checks for uncommitted changes, oversized files (>5MB), and untracked artifacts.

## Usage
```bash
# Clean merged local branches
bash scripts/git-cleanup.sh

# Run repository hygiene check
python3 scripts/repo-audit.py
```

## License
MIT
