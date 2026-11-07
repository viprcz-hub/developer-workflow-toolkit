#!/usr/bin/env bash
set -euo pipefail

echo "Fetching origin and pruning stale references..."
git fetch -p origin

MAIN_BRANCH="main"
if ! git show-ref --verify --quiet refs/heads/main; then
  if git show-ref --verify --quiet refs/heads/master; then
    MAIN_BRANCH="master"
  fi
fi

MERGED=$(git branch --merged "${MAIN_BRANCH}" | grep -Ev "(\*|${MAIN_BRANCH}|master|develop|dev)" || true)
if [ -n "${MERGED}" ]; then
  echo "${MERGED}" | xargs -n 1 git branch -d
fi
