#!/usr/bin/env python3
"""
render_wiki_op.py — render a single OpenAPI operation into the exact
Veracross-wiki markdown page format.

Reverse-engineered byte-for-byte from the committed wiki pages (verified by
regenerating unchanged operations from the pre-update spec and diffing).

Rules encoded (from the committed pages):
  * Page = nav line + ">" + breadcrumb + "---" + H1(summary) + "## METHOD path"
           + summary + [operation description] + [param tables] +
           [request body] + responses + footer.
  * Parameters (query, path) render with PLAIN types (no max / read-only).
  * Header parameters are DERIVED (not in the spec):
        collection GET -> X-Page-Number, X-Page-Size, X-API-Value-Lists, X-API-Revision
        non-coll. GET  -> X-API-Value-Lists, X-API-Revision
        write ops      -> X-API-Revision
  * Schemas (request body + response content) render with full types
    (max N, read-only) and get <details> blocks for top-level object
    ("nested object fields") and array<object> ("array item fields") fields.
  * Request-body content type line is bold:  **Content type:** `...`
    Response content type line is not bold:  Content type: `...`
  * Response block: "**CODE** — desc" + 2 blank; header lines; 1 blank;
    "Content type:" + 2 blank; schema. 204 (no content) ends at the header.
  * Exactly one blank line separates response blocks; footer after the last.

Usage:
  python3 render_wiki_op.py <spec.yaml> <METHOD> <path> <section>  > out.md
"""
import sys, yaml

NAV = ("> [Home](Home) · [Concepts](General-Principles) · "
       "[Guides](Making-a-Data-API-Request) · [Diagrams](OAuth-SSO-Login-Flow) · "
       "[Changelog](Data-API-Changelog) · [Data API](Data-API) · "
       "[Authorization API](Authorization-API) · [Files API](Files-API)")
SOURCE = "https://api-docs.veracross.com/"
FOOTER_OP = (f"*Auto-mirrored from [{SOURCE}]({SOURCE}). "
             "Raw OpenAPI spec: [repo](https://github.com/bernie-nyc/veracross-api-docs-mirror).*")


# ---------------------------------------------------------------- type cells
def _array_base(schema):
    items = schema.get("items", {})
    it = items.get("type") if isinstance(items, dict) else None
    if it in ("object", None):
        return "array<object>"
    return f"array<{it}>"


def type_str(schema):
    """Full type cell for schema fields: base + max + read-only."""
    if not isinstance(schema, dict):
        return "object"
    t = schema.get("type")
    if t == "array":
        extras = []
        if schema.get("readOnly"):
            extras.append("<small>read-only</small>")
        base = _array_base(schema)
        return base + (" " + " ".join(extras) if extras else "")
    base = t or "object"
    extras = []
    if schema.get("maxLength") is not None:
        extras.append(f"<small>max {schema['maxLength']}</small>")
    if schema.get("readOnly"):
        extras.append("<small>read-only</small>")
    return base + (" " + " ".join(extras) if extras else "")


def param_type(schema):
    """Plain type cell for parameters (no max / read-only)."""
    if not isinstance(schema, dict):
        return "object"
    t = schema.get("type")
    if t == "array":
        return _array_base(schema)
    return t or "object"


def desc_str(d):
    """Description cell: blank-line breaks -> two spaces, single -> one."""
    if not d:
        return ""
    return str(d).replace("\r\n", "\n").replace("\n\n", "  ").replace("\n", " ")


# ------------------------------------------------------------------ tables
def param_table(params):
    rows = []
    for p in params:
        req = "yes" if p.get("required") else ""
        rows.append(f"| `{p.get('name','')}` | {param_type(p.get('schema',{}))} | {req} | {desc_str(p.get('description'))} |")
    return ("| Name | Type | Required | Description |\n|---|---|---|---|\n" + "\n".join(rows)) if rows else ""


def _field_table(schema):
    req_set = set(schema.get("required") or [])
    props = schema.get("properties") or {}
    rows = []
    for name, s in props.items():
        req = "yes" if name in req_set else ""
        rows.append(f"| `{name}` | {type_str(s)} | {req} | {desc_str((s or {}).get('description'))} |")
    # fields listed in `required` but absent from `properties` (spec quirk):
    # render with a default type, as the original mirror did.
    listed = set(props)
    for name in (schema.get("required") or []):
        if name not in listed:
            rows.append(f"| `{name}` | integer | yes |  |")
    return "| Field | Type | Required | Description |\n|---|---|---|---|\n" + "\n".join(rows)


def _details(name, obj_schema, kind):
    return (f"<details><summary><code>{name}</code> — {kind}</summary>\n\n"
            f"{_field_table(obj_schema)}\n\n</details>")


def render_schema(schema):
    """Top-level table + <details> for top-level object / array<object> fields."""
    if not isinstance(schema, dict) or not schema:
        return ""
    parts = [_field_table(schema)]
    for name, s in (schema.get("properties") or {}).items():
        if not isinstance(s, dict):
            continue
        t = s.get("type")
        if t == "object":
            parts.append(_details(name, s, "nested object fields"))
        elif t == "array":
            items = s.get("items", {})
            if isinstance(items, dict) and items.get("type") == "object":
                parts.append(_details(name, items, "array item fields"))
    return "\n\n".join(parts)


# ------------------------------------------------------- derived headers
def _is_collection(op):
    for code in ("200", "201"):
        r = op.get("responses", {}).get(code)
        if not r:
            continue
        for _ct, media in (r.get("content") or {}).items():
            sch = media.get("schema")
            if isinstance(sch, dict):
                data = (sch.get("properties") or {}).get("data")
                if isinstance(data, dict) and data.get("type") == "array":
                    return True
    return False


def derived_headers(section, method, op):
    if section == "Authorization API":
        # Authorization API pages use Content-Type / Authorization headers.
        # (Not regenerated in the current task; best-effort.)
        return [{"name": "Content-Type", "schema": {"type": "string"}, "required": True,
                 "description": "Needs to be `application/x-www-form-urlencoded`"}]
    headers = []
    if _is_collection(op):
        headers.append({"name": "X-Page-Number", "schema": {"type": "integer"}, "required": False, "description": "Page number"})
        headers.append({"name": "X-Page-Size", "schema": {"type": "integer"}, "required": False, "description": "Number of records per page (for collection endpoints)"})
    if method == "get":
        headers.append({"name": "X-API-Value-Lists", "schema": {"type": "string"}, "required": False, "description": "Include Value Lists in response"})
    headers.append({"name": "X-API-Revision", "schema": {"type": "string"}, "required": False, "description": "API Revision"})
    return headers


# ------------------------------------------------------------- main render
def render_operation(spec, method, path, section):
    op = spec["paths"][path][method]
    summary = op.get("summary", "")
    tag = (op.get("tags") or [None])[0] or ""

    header = (f"{NAV}\n>\n> {section} / {tag} / {summary} · [source site]({SOURCE})"
              f"\n\n---\n\n\n")
    core = f"# {summary}\n\n\n## {method.upper()} `{path}`\n\n\n{summary}\n\n\n"

    # operation description (if present), CRLF-normalised
    desc = op.get("description")
    if desc:
        core += desc.replace("\r\n", "\n").rstrip("\n") + "\n\n\n"

    # parameters: query, path (from spec), then derived header params
    params = op.get("parameters", [])
    for loc, label in (("query", "Query parameters:"), ("path", "Path parameters:")):
        grp = [p for p in params if p.get("in") == loc]
        if grp:
            core += f"**{label}**\n\n{param_table(grp)}\n\n\n"
    hdrs = derived_headers(section, method, op)
    if hdrs:
        core += f"**Header parameters:**\n\n{param_table(hdrs)}\n\n\n"

    # request body
    rb = op.get("requestBody")
    if rb:
        core += "### Request body\n\n\n"
        for ct, media in (rb.get("content") or {}).items():
            core += f"**Content type:** `{ct}`\n\n\n"
            core += render_schema(media.get("schema", {}))
        core += "\n\n"

    # responses
    core += "### Responses\n\n\n"
    blocks = []
    for code, r in (op.get("responses") or {}).items():
        rdesc = (r.get("description") or "").strip()
        block = f"**{code}** — {rdesc}\n\n\n"
        for hn, hv in (r.get("headers") or {}).items():
            block += f"- `{hn}`: {desc_str((hv or {}).get('description'))}\n"
        content = r.get("content") or {}
        if content:
            block += "\n"
            for ct, media in content.items():
                block += f"Content type: `{ct}`\n\n\n"
                block += render_schema(media.get("schema", {}))
        blocks.append(block)
    core += "\n\n".join(blocks)

    footer = "\n\n---\n\n" + FOOTER_OP + "\n"
    return header + core + footer


if __name__ == "__main__":
    specfile, method, path, section = sys.argv[1:5]
    spec = yaml.safe_load(open(specfile))
    sys.stdout.write(render_operation(spec, method, path, section))
