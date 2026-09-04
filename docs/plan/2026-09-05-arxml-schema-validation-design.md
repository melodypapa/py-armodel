# ARXML Schema Validation (XSD) Design

Date: 2026-09-05
Status: Approved design, not yet implemented

## Goal

Validate ARXML files against the official AUTOSAR XSD schemas **before** parsing.
Mismatches are reported as warnings; parsing continues regardless.

## Decisions (from brainstorming)

| Question | Decision |
|----------|----------|
| Where does validation run? | Both: opt-in inside `ARXMLParser.load()` **and** a standalone `arxml-validate` CLI |
| Which XSD? | The file's own `xsi:schemaLocation` attribute, mapped through `release_xsd_mappings` to a bundled schema |
| On mismatch | Warn & continue (never raise) |
| Default state | Opt-in (`options["schema_validation"] = False` by default) |
| Error volume | First N errors (default 20) + summary line |
| XSD files in install package | **Copied** into the package as resources (repo-root `autosar/*/xsd` remains untouched as document reference) |

## Architecture

### New module: `src/armodel/lib/schema_validator.py`

```python
validator = ARXMLSchemaValidator(options={"max_reported_errors": 20})
valid = validator.validate("file.arxml")   # True / False / None (skipped)
```

Resolution flow (`validate()`):

1. Parse the file with `lxml.etree` (first lxml usage in `src/`; lxml is already a
   runtime dependency) and read the root's `xsi:schemaLocation` — the last token is
   the XSD filename (e.g. `AUTOSAR_00050.xsd`).
2. Reverse-lookup that filename in `release_xsd_mappings`
   (`src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py:151`)
   to get the release, then resolve to the bundled
   `src/armodel/resource/autosar/<release>/xsd/<filename>`.
3. If no bundled XSD exists for that release, warn
   ("no bundled schema, validation skipped") and return `None`.
4. Build `lxml.etree.XMLSchema` once per XSD file (module-level cache) and run
   `schema.validate()`.

Reporting on mismatch: each error logged with `logger.warning` in the codebase's
existing colorama style, formatted `<file>:<line>:<col>: <lxml message>`, capped at
the first N plus a summary line (`"N total schema errors (showing first 20)"`).
Returns `False`. Never raises.

### Parser integration

- `AbstractARXMLParser` gains `options["schema_validation"] = False` (opt-in).
- When enabled, `ARXMLParser.load()` calls the validator **first**, then proceeds
  regardless of the result (warn & continue).

## Standalone CLI

New module `src/armodel/cli/arxml_validate_cli.py`, following the
`arxml_format_cli.py` template.

```
arxml-validate [-v] [--max-errors N] INPUT [INPUT ...]
```

- Multiple input files; always validates; no opt-in flag needed.
- Per-file summary line: `VALID`, `INVALID (37 errors)`, or
  `SKIPPED (no schema for AUTOSAR_00050.xsd)`; final tally at the end.
- Registered in `pyproject.toml`:
  `arxml-validate = "armodel.cli.arxml_validate_cli:main"`.

Exit codes:

| Code | Meaning |
|------|---------|
| 0 | all files valid (or all skipped) |
| 1 | at least one file has schema errors |
| 2 | usage / file-not-found error |

Scope guard (YAGNI): no `--xsd` override, no directory recursion, no writer-side
validation in v1.

## Packaging

The XSD files ship inside the wheel as package resources. The repo-root
`autosar/<release>/xsd/` files are the **document reference** and remain untouched;
the validation code uses its own **copy** under `src/armodel/resource/` (one
additional copy, deliberately — do not move the originals, do not delete them).

```
src/armodel/resource/autosar/R23-11/xsd/AUTOSAR_00052.xsd
src/armodel/resource/autosar/R4.4.0/xsd/AUTOSAR_00046.xsd (+ xml.xsd)
src/armodel/resource/autosar/R4.3.1/xsd/AUTOSAR_00044.xsd
```

- `pyproject.toml`:

```toml
[tool.setuptools.package-data]
armodel = ["resource/autosar/*/xsd/*.xsd*"]
```

- Runtime resolution: `os.path.join(os.path.dirname(armodel.__file__), "resource",
  "autosar", release, "xsd")` — Python 3.8-safe; works installed and in-checkout
  (`zip-safe = false` is already set).
- Wheel size grows ~22 MB (9.2 + 6.7 + 6.2). Accepted for offline validation.
- The 737 MB of pdf/markdown specs under repo-root `autosar/` stay out of the wheel.

## Error handling (all warn & skip, never raise)

| Situation | Behavior |
|-----------|----------|
| Malformed XML | warn `malformed XML: <msg>`, return `None` |
| No `xsi:schemaLocation` on root | warn `no schemaLocation declared`, return `None` |
| XSD filename not in `release_xsd_mappings` | warn `unknown schema '<name>'`, return `None` |
| No bundled XSD for the release | warn `no bundled schema for <release>`, return `None` |
| Bundled XSD fails to load | warn, return `None` (defensive) |
| Namespace mismatch file vs schema | lxml reports it as a normal schema error; no special handling |

## Testing

`tests/test_armodel/lib/test_schema_validator.py` (mirrors source layout):

- Unit: resolution logic (mapped → bundled path, unknown schema, missing
  schemaLocation), schema cache reuse, cap-at-N truncation + summary, return values
  `True`/`False`/`None`, malformed XML.
- Integration: validate the 19 R4.3.1 (`AUTOSAR_00044.xsd`) custom test files —
  expect `True`; one deliberately broken fixture expects `False` with warnings.
- CLI: exit codes 0/1.

## Open items

- Coverage is limited to the 3 bundled releases (R4.3.1, R4.4.0, R23-11). More XSDs
  (e.g. `AUTOSAR_00050.xsd` for R21-11, which 23 integration test files target) can
  be added later by dropping files into `src/armodel/resource/autosar/<release>/xsd/`
  — zero code change thanks to `release_xsd_mappings`.
- The two XSD locations (repo reference vs package copy) must be kept in sync
  manually when schemas are updated.
