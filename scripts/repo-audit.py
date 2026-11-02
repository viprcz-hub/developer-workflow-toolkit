#!/usr/bin/env python3
"""
Simple repository hygiene auditor.
Checks for:
1. Dirty working tree or uncommitted changes.
2. Stash stack size.
3. Untracked large files (> 5MB).
"""

import os
import subprocess
import sys

def run_cmd(cmd):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return res.stdout.strip()

def main():
    print("--- Repository Hygiene Audit ---")
    
    # Check if git repo
    is_git = run_cmd(["git", "rev-parse", "--is-inside-work-tree"])
    if is_git != "true":
        print("Error: Current directory is not a git repository.")
        sys.exit(1)

    # 1. Dirty check
    status = run_cmd(["git", "status", "--porcelain"])
    if status:
        lines = status.splitlines()
        print(f"[!] Warning: Working tree has {len(lines)} uncommitted changes.")
    else:
        print("[+] Working tree is clean.")

    # 2. Stash check
    stash_list = run_cmd(["git", "stash", "list"])
    if stash_list:
        stash_count = len(stash_list.splitlines())
        print(f"[!] Stash stack contains {stash_count} entries.")
    else:
        print("[+] No stashes found.")

    # 3. Check large files in working tree
    large_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in dirs:
            dirs.remove(".git")
        for f in files:
            path = os.path.join(root, f)
            try:
                sz = os.path.getsize(path)
                if sz > 5 * 1024 * 1024:
                    large_files.append((path, sz / (1024 * 1024)))
            except OSError:
                pass

    if large_files:
        print(f"[!] Warning: Found {len(large_files)} files larger than 5MB:")
        for p, mb in large_files:
            print(f"    - {p}: {mb:.2f} MB")
    else:
        print("[+] No oversized files (>5MB) detected.")

    print("Audit finished.")

if __name__ == "__main__":
    main()
