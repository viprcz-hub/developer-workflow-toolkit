#!/usr/bin/env python3
import subprocess, sys

def main():
    print("Checking repository hygiene...")
    res = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    if res.stdout.strip():
        print("Working tree is dirty.")
    else:
        print("Working tree is clean.")

if __name__ == "__main__":
    main()
