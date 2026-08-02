# Agent Guidelines for py-armodel

## Build, Lint, Test Commands

**Tests (recommended):** `python scripts/run_tests.py` — colored output, summary, auto-installs pyyaml
- `--unit` / `--integration` / `--coverage` / `--verbose`
- Subset with `-k "datatypes"` or `pytest -k "not integration"`
- Integration tests: round-trip parse → write → re-parse → compare (29 ARXML files)
- Custom test dirs via `tests/integration_tests/config.yaml`

**Lint:** `npm run flake8` — syntax checks only (E9, F63, F7, F82)
- CI also runs: `--max-complexity=10 --max-line-length=127` (warnings, exit-zero)
- **Exclude `build/`** from lint (generated code)

**Build:** `python -m build` (requires `pip install build`)
**Dev install:** `pip install -e .`

## Critical: AUTOSAR Version MUST Be Set

```python
AUTOSAR.setARRelease('R23-11')  # REQUIRED before parse or write
document = AUTOSAR.getInstance()
document.clear()  # or AUTOSAR.new()
parser.load('file.arxml', document)
writer.save('output.arxml', document)
```

## Architecture

- Source: `src/armodel/` (src layout). Tests: `tests/test_armodel/` mirrors source structure
- `AUTOSAR` singleton: `getInstance()` / `new()` to reset
- Model classes use wildcard exports in `__init__.py` — when adding a class, add `from .my_class import *` to parent `__init__.py`
- Use `ABC` from `abc` module (not `ABCMeta`)
- Current version: 1.9.3, Python >= 3.8 (CI tests 3.8–3.13)
- Dependencies: `colorama`, `openpyxl`, `lxml` (runtime)

## Code Style

- **Do NOT add comments** unless asked
- Max line length: 79 (CI warns at 127). 4-space indent, double quotes
- Classes: `PascalCase`. AUTOSAR methods: `camelCase`. Constants: `UPPER_CASE`
- Setters return `self` (method chaining)
- Type annotations: Python 3.10+ union syntax (`str | None` not `Optional[str]`)

## Parser & Model Gotchas

```python
parser = ARXMLParser(options={"warning": True})  # warnings instead of exceptions
```

- `findXXX()` returns `None` if not found (no exceptions)
- Same short names can coexist across *different* types
- Duplicate UUID checking is enabled
- Boolean values in XML: no spaces (`true` not ` true `)
- Float scientific notation is handled (`1.23e-5`)
- Bi-directional parent-child references — use `addElement()` to maintain them

## CLI Tools (console_scripts)

`arxml-dump`, `arxml-format`, `armodel-component`, `connector2xlsx`, `connector-update`, `armodel-system-signal`, `armodel-memory-section`, `armodel-file-list`, `armodel-uuid-checker`, `format-xml`

## Pytest Markers (defined in pytest.ini)

`integration`, `slow`, `datatypes`, `components`, `bsw`, `system`, `blueprint`, `lifecycle`

## Slash Commands (for Claude Code)

`.claude/commands/` — `/test`, `/quality`, `/gh-workflow`, `/merge-pr`, `/req`

## Key References

- `CLAUDE.md` — comprehensive project guidance (this file is the condensed agent reference)
- `docs/development/coding_rules.md` — detailed coding standards
