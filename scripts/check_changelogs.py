#!/usr/bin/env python3
"""
check_changelogs.py — gate for the GitHub Actions sync workflow.

Before re-mirroring, this checks the three Veracross changelog endpoints
(Authorization-API, Data-API, Files-API — the "full" changelog documents).
Veracross appends an entry to a changelog whenever the corresponding API
changes, so a diff in any of the three is the signal that a re-mirror is
worthwhile. If none of them have new content, the workflow skips the sync.

Exit codes:
  0  check completed (look at the `changed` output: true = sync, false = skip)
  1  check failed (network / unexpected — fail the workflow, don't silently skip)

Env:
  VERACROSS_DOCS_BASE  base URL of the docs site (default: api-docs.veracross.com)
  MIRROR_DIR           local dir holding the mirror (default: . = repo root)
  GITHUB_OUTPUT        set by Actions; we append `changed=true|false`
"""

import base64
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

BASE = os.environ.get("VERACROSS_DOCS_BASE", "https://api-docs.veracross.com")
OUT_DIR = os.environ.get("MIRROR_DIR", ".")
UA = "Mozilla/5.0 (compatible; astinus-mirror/1.0; GH-Actions)"

# The three changelog documents that gate the sync. These are the uris of the
# changelog articles inside the Stoplight workspace (see mirror_manifest.json).
CHANGELOG_URIS = [
    "docs/changelogs/Authorization-API.full.md",
    "docs/changelogs/Data-API.full.md",
    "docs/changelogs/Files-API.full.md",
]

MAX_ATTEMPTS = 4


def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def with_retries(fn, label):
    last = None
    for i in range(MAX_ATTEMPTS):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 - we retry everything here
            last = e
            time.sleep(2 * (2 ** i))
    raise RuntimeError(f"{label} failed after {MAX_ATTEMPTS} attempts: {last!r}")


def discover_workspace():
    """Numeric workspace id -> encoded 'wk:' id (same trick as mirror.py)."""
    html = with_retries(lambda: http_get(BASE + "/"), "fetch homepage").decode("utf-8", "replace")
    m = re.search(r"window\.__OVERMIND_MUTATIONS\s*=\s*", html)
    if not m:
        raise RuntimeError("__OVERMIND_MUTATIONS not found in homepage")
    muts = json.JSONDecoder().raw_decode(html[m.end():])[0]
    for mu in muts:
        if mu.get("path") == "workspaces.currentWorkspace" and mu.get("args"):
            wid = mu["args"][0].get("id")
            if wid:
                return base64.urlsafe_b64encode(f"wk:{wid}".encode()).rstrip(b"=").decode()
    raise RuntimeError("could not find numeric workspace id")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def main():
    ws = with_retries(discover_workspace, "workspace discovery")
    idx_raw = with_retries(
        lambda: http_get(f"{BASE}/api/v1/workspaces/{ws}/nodes?limit=5000"),
        "fetch node index",
    )
    nodes = json.loads(idx_raw)
    by_uri = {n.get("uri", "").lstrip("/"): n for n in nodes}

    print(f"Checking 3 changelog endpoints against the local mirror in {OUT_DIR!r} ...")
    changed = False
    for uri in CHANGELOG_URIS:
        node = by_uri.get(uri)
        if node is None:
            print(f"  [CHANGED/missing] {uri}: node no longer in the index")
            changed = True
            continue
        node_raw = with_retries(
            lambda n=node: http_get(f"{BASE}/api/v1/projects/{n['project_id']}/nodes/{n['id']}"),
            f"fetch node for {uri}",
        )
        remote = (json.loads(node_raw).get("data") or "").encode("utf-8")
        local_path = os.path.join(OUT_DIR, uri)
        if not os.path.exists(local_path):
            print(f"  [CHANGED/absent]  {uri}: not mirrored locally yet")
            changed = True
            continue
        with open(local_path, "rb") as f:
            local = f.read()
        same = sha256(remote) == sha256(local)
        tag = "unchanged" if same else "CHANGED"
        print(f"  [{tag:13s}] {uri}  remote={sha256(remote)[:12]} local={sha256(local)[:12]}")
        if not same:
            changed = True

    print(f"result: {'CHANGED -> run the sync' if changed else 'no new content -> skip'}")

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001
        print(f"check FAILED: {e!r}", file=sys.stderr)
        sys.exit(1)
