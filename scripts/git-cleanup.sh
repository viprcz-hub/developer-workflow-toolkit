#!/usr/bin/env bash
set -euo pipefail

echo "=== Git Branch Cleanup ==="
echo "Fetching origin and pruning deleted remote references..."
git fetch -p origin

MAIN_BRANCH="main"
if ! git show-ref --verify --quiet refs/heads/main; then
  if git show-ref --verify --quiet refs/heads/master; then
    MAIN_BRANCH="master"
  fi
fi

echo "Active default branch: ${MAIN_BRANCH}"

MERGED_BRANCHES=$(git branch --merged "${MAIN_BRANCH}" | grep -Ev "(\*|${MAIN_BRANCH}|master|develop|dev)" || true)

if [ -z "${MERGED_BRANCHES}" ]; then
  echo "No stale merged branches found to delete."
else
  echo "Found merged branches:"
  echo "${MERGED_BRANCHES}"
  echo "Deleting..."
  echo "${MERGED_BRANCHES}" | xargs -n 1 git branch -d
  echo "Cleanup complete."
fi
