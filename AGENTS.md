# Agent Guidelines for py-armodel

## Build, Lint, Test Commands

**Tests (recommended):** `python scripts/run_tests.py` — colored output, summary, auto-installs pyyaml
- `--unit` / `--integration` / `--no-coverage` / `--verbose` (coverage is ON by default; there is no `--coverage` flag)
- Subset with `python scripts/run_tests.py -k "datatypes"` or `pytest -k "not integration"` (`-k` is a positional passthrough)
- Integration tests: round-trip parse → write → re-parse → compare (29 ARXML files)
- Custom test dirs via `tests/integration_tests/config.yaml`

**Lint:** `npm run flake8` — syntax checks only (E9, F63, F7, F82)
- CI also runs: `--max-complexity=10 --max-line-length=127` (warnings, exit-zero)
- **Exclude `build/`** from lint (generated code)
- **Black formatter:** `npm run black` — formats code with 200 character line length
- **Black check:** `npm run black-check` — checks code formatting without modifying files

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
- Line length: `coding_rules.md` says 79, but Black formats to 200 (`pyproject.toml` `[tool.black]`) — run `npm run black`; flake8 only warns at 127 (exit-zero). 4-space indent, double quotes
- Classes: `PascalCase`. AUTOSAR methods: `camelCase`. Constants: `UPPER_CASE`
- Setters return `self` (method chaining)
- Type annotations: Python 3.8-compatible — `typing.Optional[T]` / `typing.List[T]`, NEVER `T | None` or `list[...]` (project requires Python >= 3.8)

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
- `docs/development/class_check_rules.md` — 12 rules for aligning model classes with the AUTOSAR PDF spec (method parity checklists, spec-based docstrings, `Optional`/`List` hints, setter chaining). Recent work = aligning model classes to these rules.
