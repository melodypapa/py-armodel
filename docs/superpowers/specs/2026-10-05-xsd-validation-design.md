# XSD Validation for ARXML Parse and Write — Design

- **Date:** 2026-10-05
- **Status:** Approved; **amended during planning/execution** — §3-§5 below carry `AMENDED` notes
  describing the as-built behavior where it differs from the original text. The authoritative
  implementation record is `docs/superpowers/plans/2026-10-05-xsd-validation.md` (header notes 1-10).
- **Scope:** Pre-parse XSD validation in `ARXMLParser.load()` and pre-save validation in `ARXMLWriter.save()`, backed by bundled AUTOSAR schemas.

## 1. Problem

`ARXMLParser.load()` currently reads files with `xml.etree.ElementTree` and performs no schema
validation — only a root-tag check. Structurally invalid ARXML is discovered late (or not at all)
during model construction, producing warnings far from the root cause. Users need files validated
against the official AUTOSAR XSD for their release **before** any parsing or writing happens.

## 2. Decisions (from brainstorming)

| Question | Decision |
|---|---|
| Schema source | Bundle official AUTOSAR XSDs inside the package (`armodel/validation/schemas/`) |
| Failure handling | Respect the existing parser convention: `options={"warning": True}` logs and continues; default raises |
| Schema selection | Auto-select by detected release; explicit path/release override the detection |
| Coverage | Both sides: parse-time gate **and** save-time gate |

## 3. New package `src/armodel/validation/`

### `validator.py`

- `ValidationError` dataclass: `line: int`, `column: int`, `message: str`, `domain: str`.
  Validation never raises; it returns structured errors and the caller decides what to do.
- `ARXMLValidator`:
  - `__init__(self, xsd_path: Optional[str] = None, release: Optional[str] = None)` —
    explicit path wins over explicit release; both `None` triggers auto-detection from the document.
  - `validate_string(xml: str) -> List[ValidationError]` — parse with lxml, validate, return **all**
    errors (not just the first).
  - `validate_tree(root) -> List[ValidationError]` — same, for an already-built lxml tree.
  - Schema compilation is lazy and cached per release at module level (compilation takes seconds;
    the test suite round-trips hundreds of files).
- Implementation uses `lxml.etree.XMLSchema` — lxml is already a dependency; **no new dependencies**.

> **AMENDED (as built):** the API is **class-based**. `ARXMLValidator` owns all state as class
> attributes (schema registry, compile caches, lock) and exposes: `validate_bytes(data)` /
> `validate_string(xml)` (instance), and classmethods `detect_schema_path(data)`,
> `detect_schema_info(data)` (path + document namespace), `get_schema(xsd_path)`,
> `get_schema_target_namespace(xsd_path)`, `register_schema_file(filename, path)`, and the
> `for_document(data)` factory (returns None when no bundled schema matches the document's
> `xsi:schemaLocation` filename OR the document namespace differs from the schema's
> targetNamespace). There is no `validate_tree`; no module-level functions.

### `schemas/`

- Package data: `R19-11/`, `R20-11/`, `R21-11/`, `R22-11/`, `R23-11/` — the releases the test corpus
  uses; adding more is a drop-in of a new directory.
- Each directory holds the official release XSD set with its includes/imports intact.
- Registered via package-data in `pyproject.toml`.
- `README.md` in the package records provenance (which autosar.org release tarball each set came from).

> **AMENDED (as built):** bundled set is **R23-11, R4.4.0, R4.3.1, R3.2.3** — the four releases the
> repo already vendors under `autosar/<release>/xsd/` (byte-copies, hash-sync-tested). The W3C
> `xml.xsd` exists as a SINGLE shared copy at `schemas/xml.xsd`, resolved by the validator's
> directory-then-`SCHEMA_DIR`-fallback resolver.

## 4. Release auto-detection

The `AUTOSAR` root element's `xsi:schemaLocation` (e.g. `.../AUTOSAR_M2-MOD.xsd`) is matched against
bundled release directories; `ADMIN-DATA` schema info is the fallback. If no schema can be resolved:
a notice is produced ("no schema for detected release X") and — with `warning=True` — processing
continues **unvalidated**; otherwise it raises like any other validation failure.

> **AMENDED (as built):** detection uses **only** `xsi:schemaLocation` (the `ADMIN-DATA` fallback
> was dropped — no AUTOSAR tool writes resolvable schema info there). An **unresolvable schema or a
> namespace mismatch logs a warning and processing continues UNVALIDATED in every mode** — this is
> not an error, because the writer's default `AUTOSAR_4-0-3.xsd` and legacy R3 documents
> (`http://autosar.org`) have no compatible bundled schema, and raising would break legitimate
> existing usage.

## 5. Parser integration (`ARXMLParser.load`)

Validation is a **pre-parse gate inside the same `load()` call** — not interleaved with model
building, not a separate API:

1. Read file bytes.
2. Validate bytes against the XSD (no model construction has happened yet).
3. Invalid:
   - `options={"warning": True}` → each error logged via `self.logger.warning`; parsing proceeds.
   - default → raise `ARXMLParseError` (new exception on the parser's existing error base) with all
     violations formatted; no half-built `AUTOSAR` document is left behind.
4. Valid → existing `ET.parse` → model-building code runs unchanged.

`options={"validate": False}` disables validation entirely — the escape hatch for legacy/imperfect
files. **Validation is ON by default** whenever a schema can be resolved.

> **AMENDED (as built):** failures are reported **one `logger.error` line per violation, then a
> single `ValueError`** ("failed schema validation with N error(s) (first: line …, col …: …)") that
> aborts the load — no new exception class, matching the repo's `ValueError` convention. With
> `warning: True`, each violation is logged via `logger.warning` and parsing continues.

## 6. Writer integration (`ARXMLWriter.save`)

`save()` serializes to an in-memory string as today, validates the string, then writes to disk only
if valid (in `warning=True` mode: logs and writes anyway). Same `validate: False` escape hatch.
This catches model states that would produce invalid ARXML before they reach disk.

## 7. Testing

- Unit tests under `tests/test_armodel/validation/`: release detection, schema caching, error list
  contents, `validate: False` escape hatch, warning-mode logging behavior.
- One malformed fixture (e.g. bad element ordering) asserted to fail validation.
- The existing integration corpus asserted to pass under the R23-11 schema — this doubles as an
  audit of how spec-clean the integration files are; failures examined individually before deciding
  whether to fix files or annotate.
- No network access; validation is deterministic.

## 8. Out of scope (YAGNI)

Schematron / semantic validation, emitting XSDs, a CLI subcommand, on-demand schema download.
