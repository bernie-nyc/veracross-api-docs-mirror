#!/usr/bin/env bash
# Bootstrap the Veracross API docs mirror's GitHub Wiki.
#
# GitHub creates a repo's backing wiki git repository (*.wiki.git) lazily —
# the FIRST wiki page must be saved via the logged-in web UI. After that,
# this script pushes all 484 mirrored pages.
#
# One-time manual step (must be done in a browser logged in as bernie-nyc):
#   1. Open  https://github.com/bernie-nyc/veracross-api-docs-mirror/wiki
#   2. Click "Create a page" (top right), save a placeholder titled "Home"
#      (any content; it will be overwritten).
#
# Then, from a machine with `gh`/git credentialed for bernie-nyc:
#   bash wiki_bootstrap.sh
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="bernie-nyc/veracross-api-docs-mirror"
TARBALL="$DIR/wiki-source.tar.gz"

[ -f "$TARBALL" ] || { echo "ERROR: missing $TARBALL"; exit 1; }

# 1) verify the backing wiki repo is now pushable
if ! git ls-remote "https://github.com/$REPO.wiki.git" >/dev/null 2>&1; then
  echo "ERROR: the wiki git repo is not materialized yet."
  echo "Do the one-time web step first: create a 'Home' page at"
  echo "  https://github.com/$REPO/wiki"
  exit 1
fi
echo "✓ wiki git repo is live"

# 2) clone the (now-existing) wiki repo.
#    IMPORTANT: GitHub renders the wiki from its DEFAULT branch, which is `master`
#    (NOT `gh-pages`). Pushing to gh-pages leaves the wiki showing only the
#    placeholder Home page. So we force-push to master.
rm -rf /tmp/wiki_push
git clone -q "https://github.com/$REPO.wiki.git" /tmp/wiki_push
cd /tmp/wiki_push
git checkout -q -B master origin/master 2>/dev/null || git checkout -q -B master

# 3) replace ALL contents with the mirrored pages
find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
tar -xf "$TARBALL" -C .

# 4) commit + force-push to the wiki's default branch (master)
git add -A
git -c user.email="bernie-nyc@users.noreply.github.com" -c user.name="bernie-nyc" \
  commit -qm "Mirror Veracross API docs left menu as wiki pages (484, flat links)"
git push -f origin master
echo "✓ pushed to master. Wiki live at https://github.com/$REPO/wiki"
