#!/usr/bin/env bash
set -euo pipefail

echo "Fetching origin and pruning stale references..."
git fetch -p origin
