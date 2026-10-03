#!/usr/bin/env bash
# Re-mirror the Veracross API docs and commit any changes.
# Run from the mirror directory (where this script + mirror.py live).
set -euo pipefail
cd "$(dirname "$0")"

command -v python3 >/dev/null || { echo "python3 required" >&2; exit 1; }
python3 -c "import yaml" 2>/dev/null || pip install --quiet pyyaml

# Rebuild the mirror in place.
python3 mirror.py --out . --concurrency 8

# Commit + push only if something changed.
if ! git diff --quiet -- . || ! git diff --cached --quiet -- .; then
  git add -A
  git commit -m "sync: re-mirror Veracross API docs ($(date -u +%F))"
  git push
  echo "updated and pushed"
else
  echo "no changes since last mirror"
fi
