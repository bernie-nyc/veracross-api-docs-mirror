# Veracross API Documentation — Mirror

A mirror of the Veracross API technical documentation, originally hosted on
[Stoplight Elements](https://api-docs.veracross.com/).

> **Not official.** This is an independent mirror for reference/convenience.
> The content is © Veracross, Inc. This repo mirrors what is publicly served
> by their docs API and is not affiliated with or endorsed by Veracross.

## What's in here

| Path | Contents |
|------|----------|
| `docs/` | All **26** Markdown articles (concepts, guides, changelogs, support) — mirrored **verbatim** from the source. |
| `reference/` | **5** OpenAPI 3.0 specifications, reconstructed into valid YAML: `Data-API`, `Files-API`, `Authorization-API`, `OneRoster-Rostering`, `OneRoster-Gradebook`. |
| `mirror_manifest.json` | Machine-readable manifest of every mirrored file, its source URL, and the source's commit/workspace metadata. |

The `reference/` specs were **reconstructed** from Stoplight's decomposed
node data (service scaffolding + per-operation + per-schema nodes) into
standard, renderable OpenAPI 3.0. They are not the original YAML files
(Stoplight does not expose those to anonymous clients), but they carry the
full operation set — paths, methods, parameters, request bodies, responses,
schemas, tags, servers, and security.

| Spec | Paths | Operations |
|------|-------|-----------|
| `reference/Data-API.yaml` | 303 | 440 |
| `reference/OneRoster-Rostering.yaml` | 56 | 56 |
| `reference/Files-API.yaml` | 6 | 9 |
| `reference/Authorization-API.yaml` | 7 | 7 |
| `reference/OneRoster-Gradebook.yaml` | 14 | 23 |

## How the mirror is built

`../mirror.py` (kept alongside this repo's tooling) pulls everything from
Stoplight's public JSON API on the same host — no browser, no auth:

1. Reads the numeric workspace id from the homepage's embedded
   `window.__OVERMIND_MUTATIONS` and base64url-encodes it to the `wk:<id>`
   id the API expects.
2. `GET /api/v1/workspaces/<id>/nodes?limit=5000` → the full node index.
3. `GET /api/v1/projects/<proj>/nodes/<node>` per node → the node's `data`.
4. Writes articles verbatim; assembles the OpenAPI specs.

## Re-mirroring (keeping it current)

```bash
pip install pyyaml
python3 mirror.py --out veracross-api-docs-mirror --concurrency 8
git add -A
git commit -m "sync: re-mirror Veracross API docs $(date -u +%F)"
git push
```

The script is idempotent and overwrites changed files. Point it at a
different Stoplight-hosted site with `--base <url>`.

To keep it fresh automatically, run that block on a schedule (e.g. a cron
job or GitHub Actions workflow). See `update.sh`.

## License / provenance

See `mirror_manifest.json` for the exact source URL and node metadata of
every file. Content © Veracross, Inc.; mirrored in good faith for reference.
