#!/usr/bin/env python3
"""
mirror.py — Reliably mirror the Veracross API documentation
(hosted on Stoplight Elements at https://api-docs.veracross.com/)
into a local directory tree of verbatim Markdown + valid OpenAPI 3.0 YAML,
ready to be pushed to a GitHub repo.

How it works
------------
The Stoplight Elements site is a JavaScript single-page app; the raw content
is not in the HTML. It is served from a small public JSON API on the same
host. This script:

  1. Fetches the homepage and reads the numeric workspace ID embedded in
     `window.__OVERMIND_MUTATIONS` (a plain script tag), then base64url-encodes
     it into the "wk:<id>" ID the API expects.
  2. GETs /api/v1/workspaces/<id>/nodes?limit=<big> -> the full node index
     (articles, http_operations, models, http_services) for every project.
  3. For each node it GETs /api/v1/projects/<proj>/nodes/<node> which returns
     the node's `data`:
        - articles   -> verbatim Markdown
        - services   -> spec scaffolding (info/tags/servers/securitySchemes)
        - operations -> a single OpenAPI operation (path/method/params/req/resp)
        - models     -> a JSON schema component
  4. Markdown is written out verbatim to <out>/docs/...
  5. Operations + models are grouped by their source spec file and assembled
     into a valid, renderable OpenAPI 3.0 document written to <out>/reference/...

Only stdlib + PyYAML are used. All network calls are plain GETs with retries.

Usage:
    python3 mirror.py --out ./veracross-api-docs-mirror
    python3 mirror.py --out ./mirror --concurrency 8 --limit 5000
"""

import argparse
import base64
import concurrent.futures as cf
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

try:
    import yaml  # PyYAML
except ImportError:
    yaml = None

BASE_DEFAULT = "https://api-docs.veracross.com"
UA = "Mozilla/5.0 (compatible; astinus-mirror/1.0)"
VERSION_HEADER = "Stoplight-Elements-Version: 4.31.0"

# Stoplight-internal keys that must be stripped from emitted OpenAPI.
STRIP_KEYS = {"id", "x-stoplight", "$schema", "style", "explicitProperties",
              "encodings", "extensions"}


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def http_get(url, retries=4, timeout=60, headers=None):
    """GET a URL, returning bytes. Exponential backoff on 429/5xx/timeouts."""
    hdrs = {"User-Agent": UA, "Accept": "application/json", "Stoplight-Elements-Version": "4.31.0"}
    if headers:
        hdrs.update(headers)
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.status
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(1.5 * (2 ** attempt))
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
            time.sleep(1.2 * (2 ** attempt))
    raise RuntimeError(f"GET failed after {retries} tries: {url} ({last!r})")


def http_get_json(url, **kw):
    b, _ = http_get(url, **kw)
    return json.loads(b)


# --------------------------------------------------------------------------- #
# Workspace discovery
# --------------------------------------------------------------------------- #
def discover_workspace(base):
    """Read the numeric workspace id from the homepage's embedded state."""
    html, _ = http_get(base + "/")
    text = html.decode("utf-8", "replace")
    m = re.search(r"window\.__OVERMIND_MUTATIONS\s*=\s*", text)
    if not m:
        raise RuntimeError("could not find __OVERMIND_MUTATIONS in homepage")
    dec = json.JSONDecoder()
    muts, _ = dec.raw_decode(text[m.end():])
    num_id = None
    slug = None
    for mu in muts:
        path = mu.get("path", "")
        args = mu.get("args", [])
        if path == "workspaces.currentWorkspace" and args and isinstance(args[0], dict):
            num_id = args[0].get("id")
            slug = args[0].get("slug")
        if path == "router.workspaceSlug" and args:
            slug = slug or args[0]
    if not num_id:
        raise RuntimeError("could not find numeric workspace id")
    encoded = base64.urlsafe_b64encode(f"wk:{num_id}".encode()).rstrip(b"=").decode()
    return encoded, num_id, slug


# --------------------------------------------------------------------------- #
# Node index
# --------------------------------------------------------------------------- #
def fetch_all_nodes(base, ws_encoded, limit):
    nodes = []
    offset = 0
    while True:
        url = f"{base}/api/v1/workspaces/{ws_encoded}/nodes?limit={limit}&offset={offset}"
        batch = http_get_json(url)
        if not batch:
            break
        nodes.extend(batch)
        if len(batch) < limit:
            break
        offset += len(batch)
        time.sleep(0.05)
    # de-dupe by (project_id, id)
    seen = set()
    uniq = []
    for n in nodes:
        k = (n.get("project_id"), n.get("id"))
        if k in seen:
            continue
        seen.add(k)
        uniq.append(n)
    return uniq


def fetch_node(base, node):
    url = f"{base}/api/v1/projects/{node['project_id']}/nodes/{node['id']}"
    d = http_get_json(url)
    return node, d


# --------------------------------------------------------------------------- #
# OpenAPI assembly
# --------------------------------------------------------------------------- #
def clean(obj):
    """Recursively strip Stoplight-internal keys from a JSON structure."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in STRIP_KEYS:
                continue
            out[k] = clean(v)
        return out
    if isinstance(obj, list):
        return [clean(x) for x in obj]
    return obj


def param_to_oas(p, where):
    """Stoplight parameter object -> OpenAPI parameter object."""
    out = {
        "name": p.get("name"),
        "in": where,
    }
    if p.get("description"):
        out["description"] = p["description"]
    if where == "path" or p.get("required"):
        out["required"] = True
    schema = clean(p.get("schema", {}))
    if schema:
        out["schema"] = schema
    if p.get("deprecated"):
        out["deprecated"] = True
    return out


def request_to_parameters(opdata):
    req = opdata.get("request", {}) or {}
    params = []
    for where in ("path", "query", "header", "cookie"):
        for p in req.get(where, []) or []:
            params.append(param_to_oas(p, where))
    return params


def request_to_body(opdata):
    req = opdata.get("request", {}) or {}
    body = req.get("body")
    if not body:
        return None
    out = {}
    for c in body.get("contents", []) or []:
        mt = c.get("mediaType", "application/json")
        entry = {}
        if c.get("schema"):
            entry["schema"] = clean(c["schema"])
        if c.get("examples"):
            entry["examples"] = clean(c["examples"])
        out[mt] = entry
    if body.get("required"):
        return {"required": True, "content": out}
    return {"content": out}


def response_to_oas(r):
    code = r.get("code", "default")
    out = {}
    if r.get("description"):
        out["description"] = r["description"]
    else:
        out["description"] = ""
    if r.get("headers"):
        headers = {}
        for h in r["headers"]:
            entry = {}
            if h.get("description"):
                entry["description"] = h["description"]
            if h.get("schema"):
                entry["schema"] = clean(h["schema"])
            if h.get("required"):
                entry["required"] = True
            headers[h.get("name", "header")] = entry
        if headers:
            out["headers"] = headers
    if r.get("contents"):
        content = {}
        for c in r["contents"]:
            mt = c.get("mediaType", "application/json")
            entry = {}
            if c.get("schema"):
                entry["schema"] = clean(c["schema"])
            if c.get("examples"):
                entry["examples"] = clean(c["examples"])
            content[mt] = entry
        if content:
            out["content"] = content
    return code, out


def security_to_oas(security):
    """Node security [[{key, flows, ...}]] -> OpenAPI [[{key: [scopes]}]]."""
    if not security:
        return None
    reqs = []
    for group in security:
        req = {}
        for scheme in group:
            key = scheme.get("key")
            scopes = []
            flows = scheme.get("flows", {}) or {}
            for flow_name, flow in flows.items():
                sc = (flow or {}).get("scopes", {}) or {}
                scopes.extend(sc.keys())
            req[key] = scopes
        reqs.append(req)
    return reqs


def build_operation(opdata):
    op = {}
    tags = [t.get("name") for t in (opdata.get("tags") or []) if t.get("name")]
    if tags:
        op["tags"] = tags
    if opdata.get("summary"):
        op["summary"] = opdata["summary"]
    if opdata.get("description"):
        op["description"] = opdata["description"]
    if opdata.get("iid"):
        op["operationId"] = opdata["iid"]
    if opdata.get("deprecated"):
        op["deprecated"] = True

    params = request_to_parameters(opdata)
    if params:
        op["parameters"] = params

    body = request_to_body(opdata)
    if body:
        op["requestBody"] = body

    responses = {}
    for r in opdata.get("responses", []) or []:
        code, rbody = response_to_oas(r)
        # de-dupe codes (e.g. multiple 4XX)
        responses.setdefault(code, rbody)
    if responses:
        op["responses"] = responses

    sec = security_to_oas(opdata.get("security"))
    if sec:
        op["security"] = sec

    return op


def build_spec(spec_file, service_data, ops, models):
    """Assemble a full OpenAPI 3.0 document from scaffolding + ops + models."""
    sd = json.loads(service_data) if isinstance(service_data, str) else service_data

    doc = {"openapi": "3.0.0"}

    info = {"title": sd.get("name", spec_file), "version": sd.get("version", "1.0.0")}
    if sd.get("description"):
        info["description"] = sd["description"]
    if sd.get("contact"):
        info["contact"] = clean(sd["contact"])
    doc["info"] = info

    servers = []
    for s in sd.get("servers", []) or []:
        e = {"url": s.get("url", "")}
        if s.get("description"):
            e["description"] = s["description"]
        elif s.get("name"):
            e["description"] = s["name"]
        servers.append(e)
    if servers:
        doc["servers"] = servers

    tags = []
    seen_tags = set()
    for t in sd.get("tags", []) or []:
        nm = t.get("name")
        if nm and nm not in seen_tags:
            seen_tags.add(nm)
            e = {"name": nm}
            if t.get("description"):
                e["description"] = t["description"]
            tags.append(e)
    if tags:
        doc["tags"] = tags

    paths = {}
    for od in ops:
        method = (od.get("method") or "").lower()
        path = od.get("path", "")
        if not method or not path:
            continue
        paths.setdefault(path, {})[method] = build_operation(od)

    doc["paths"] = paths

    components = {}
    # security schemes from scaffolding
    ss = sd.get("securitySchemes")
    if ss:
        schemes = {}
        if isinstance(ss, list):
            for s in ss:
                key = s.get("key")
                if not key:
                    continue
                sch = {"type": s.get("type", "http")}
                if s.get("flows"):
                    sch["flows"] = clean(s["flows"])
                if s.get("description"):
                    sch["description"] = s["description"]
                schemes[key] = sch
        elif isinstance(ss, dict):
            schemes = clean(ss)
        if schemes:
            components["securitySchemes"] = schemes

    # models -> components.schemas
    schemas = {}
    for name, mj in models.items():
        if isinstance(mj, str):
            mj = json.loads(mj)
        schemas[name] = clean(mj)
    if schemas:
        components["schemas"] = schemas

    if components:
        doc["components"] = components

    return doc


def dump_yaml(doc):
    if yaml is None:
        raise RuntimeError("PyYAML not installed (pip install pyyaml)")
    return yaml.safe_dump(doc, sort_keys=False, allow_unicode=True,
                          default_flow_style=False, width=1000)


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Mirror Veracross API docs (Stoplight)")
    ap.add_argument("--base", default=BASE_DEFAULT)
    ap.add_argument("--out", default="./veracross-api-docs-mirror")
    ap.add_argument("--limit", type=int, default=5000)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--no-articles", action="store_true")
    ap.add_argument("--no-specs", action="store_true")
    ap.add_argument("--workspace-id", default=None, help="precomputed encoded wk id")
    args = ap.parse_args()

    base = args.base.rstrip("/")
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)

    print(f"[*] base = {base}")
    ws_encoded, ws_num, ws_slug = (None, None, None)
    if args.workspace_id:
        ws_encoded = args.workspace_id
        print(f"[*] using provided workspace id {ws_encoded}")
    else:
        print("[*] discovering workspace id ...")
        ws_encoded, ws_num, ws_slug = discover_workspace(base)
        print(f"[*] workspace slug={ws_slug} numeric_id={ws_num} encoded={ws_encoded}")

    print("[*] fetching node index ...")
    nodes = fetch_all_nodes(base, ws_encoded, args.limit)
    print(f"[*] {len(nodes)} nodes total")

    by_type = {}
    for n in nodes:
        by_type.setdefault(n["type"], []).append(n)
    for t, lst in sorted(by_type.items()):
        print(f"    {t}: {len(lst)}")

    # ---- fetch every node's data (parallel) -------------------------------- #
    print("[*] fetching node contents ...")
    fetched = {}
    errors = []
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = {ex.submit(fetch_node, base, n): n for n in nodes}
        done = 0
        for fut in cf.as_completed(futs):
            n = futs[fut]
            done += 1
            try:
                node, data = fut.result()
                fetched[(node["project_id"], node["id"])] = data
            except Exception as e:
                errors.append((n.get("id"), n.get("uri"), repr(e)))
            if done % 50 == 0:
                print(f"    {done}/{len(nodes)} fetched")
    print(f"[*] fetched {len(fetched)} nodes, {len(errors)} errors")
    if errors:
        for e in errors[:10]:
            print("    ERR", e)

    manifest = {
        "source": base,
        "workspace_slug": ws_slug,
        "workspace_id": ws_num,
        "node_count": len(nodes),
        "fetched": len(fetched),
        "errors": [list(e) for e in errors],
        "articles": [],
        "specs": [],
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    # ---- articles ---------------------------------------------------------- #
    if not args.no_articles:
        print("[*] writing articles ...")
        art_count = 0
        for n in by_type.get("article", []):
            data = fetched.get((n["project_id"], n["id"]))
            if not data or not data.get("data"):
                continue
            rel = n["uri"].lstrip("/")
            dest = os.path.join(out, rel)
            os.makedirs(os.path.dirname(dest) or out, exist_ok=True)
            with open(dest, "w", encoding="utf-8") as f:
                f.write(data["data"])
            art_count += 1
            manifest["articles"].append({
                "path": rel, "title": n.get("title"),
                "source": f"{base}/api/v1/projects/{n['project_id']}/nodes/{n['id']}",
            })
        print(f"    wrote {art_count} articles")

    # ---- specs ------------------------------------------------------------- #
    if not args.no_specs:
        print("[*] assembling OpenAPI specs ...")
        # group ops/models by source spec file (from uri)
        def spec_of(uri):
            return uri.split("/paths")[0].split("/components")[0].lstrip("/")

        specs = {}
        for n in by_type.get("http_service", []):
            specs[n["uri"].lstrip("/")] = {"service": n, "ops": [], "models": {}}
        for n in by_type.get("http_operation", []):
            s = spec_of(n["uri"])
            if s in specs:
                specs[s]["ops"].append(n)
        for n in by_type.get("model", []):
            s = spec_of(n["uri"])
            if s in specs:
                name = n["uri"].split("/components/schemas/")[-1]
                specs[s]["models"][name] = n

        for spec_file, grp in specs.items():
            svc_data = fetched.get((grp["service"]["project_id"], grp["service"]["id"]))
            if not svc_data or not svc_data.get("data"):
                print(f"    !! missing service data for {spec_file}")
                continue
            op_datas = []
            missing = 0
            for on in grp["ops"]:
                d = fetched.get((on["project_id"], on["id"]))
                if d and d.get("data"):
                    op_datas.append(json.loads(d["data"]) if isinstance(d["data"], str) else d["data"])
                else:
                    missing += 1
            model_datas = {}
            for name, mn in grp["models"].items():
                d = fetched.get((mn["project_id"], mn["id"]))
                if d and d.get("data"):
                    model_datas[name] = d["data"]
            try:
                doc = build_spec(spec_file, svc_data["data"], op_datas, model_datas)
                dest = os.path.join(out, spec_file)
                os.makedirs(os.path.dirname(dest) or out, exist_ok=True)
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(dump_yaml(doc))
                npaths = len(doc.get("paths", {}))
                print(f"    {spec_file}: {len(op_datas)} ops "
                      f"({missing} missing), {len(model_datas)} models -> {npaths} paths")
                manifest["specs"].append({
                    "path": spec_file, "operations": len(op_datas),
                    "missing_ops": missing, "models": len(model_datas),
                    "paths": npaths,
                })
            except Exception as e:
                print(f"    !! failed to build {spec_file}: {e!r}")

    # ---- manifest ---------------------------------------------------------- #
    with open(os.path.join(out, "mirror_manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[=] done. mirror written to {out}")
    print(f"[=] articles: {len(manifest['articles'])}  specs: {len(manifest['specs'])}")
    if errors:
        print(f"[!] {len(errors)} fetch errors (see mirror_manifest.json)")


if __name__ == "__main__":
    main()
