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

### High-Level Data Flow

```
ARXML file ──> parser/arxml_parser.py ──> in-memory model (models/M2/*)
                                                          │
                                            mutate via AUTOSAR singleton
                                                          │
                                   writer/arxml_writer.py <── ARXML file
```

The in-memory model is a bi-directional object graph rooted at the `AUTOSAR` singleton. The parser builds it; the writer serializes it back. Round-trip integrity (parse → write → re-parse → compare) is the contract enforced by the integration tests.

### Module Organization (`src/armodel/`)

- **models/** — AUTOSAR data model classes following the AUTOSAR M2 meta-model
  - `models/M2/MSR/` — meta-model semantic rules (AsamHdo, DataDictionary, Documentation, CalibrationData)
  - `models/M2/AUTOSARTemplates/` — template models grouped by domain (CommonStructure, SWComponentTemplate, SystemTemplate, BswModuleTemplate, ECUCDescriptionTemplate, ECUCParameterDefTemplate, EcuResourceTemplate, GenericStructure, DiagnosticExtract)
  - `models/utils/` — UUID management (`UUIDMgr`)
- **parser/** — ARXML parsing (`arxml_parser.py`, abstract base, Excel/connector parsers, `file_parser.py`)
- **writer/** — ARXML writing (`arxml_writer.py`, abstract base)
- **cli/** — console_scripts entry points (one module per CLI tool)
- **lib/** — shared utilities (`sw_component.py`, `system_signal.py`, `cli_args_parser.py`)
- **data_models/** — standalone models like `sw_connector.py`
- **transformer/** — data transformations (e.g. `admin_data.py`)
- **report/** — Excel report generation (`connector_xls_report.py`, `excel_report.py`)

### M2 Schema Structure

The model is organized per the AUTOSAR M2 meta-model. Every model class ultimately derives from `ARObject` → `Referrable` → `MultilanguageReferrable` → `Identifiable` → `PackageableElement` → `ARElement` → `AtpType` (see `README.md` §1.9 for the full heritage tree). New model classes must be placed under the correct `AUTOSARTemplates` domain package.

### Adding a New Model Class

1. Decide if it is a leaf package (`.py` file, package name = filename) or non-leaf (has subpackages → define in `__init__.py`)
2. Create it under the correct domain in `src/armodel/models/M2/AUTOSARTemplates/`
3. Add a wildcard import in the parent `__init__.py`: `from .my_class import *`
4. Add an import to `src/armodel/models/__init__.py` if it is a top-level name
5. Add a corresponding test under `tests/test_armodel/models/M2/`
6. Run `python scripts/run_tests.py` and `npm run black`

## Code Style

- **Do NOT add comments** unless asked
- Line length: Black is the enforced formatter at **200 chars** (`pyproject.toml` `[tool.black]`) — always run `npm run black`. `coding_rules.md` documents 79 as the PEP 8 ideal and flake8 warns (exit-zero) at 127, but these do NOT block commits. Don't manually wrap lines to 79; let Black handle it. 4-space indent, double quotes
- Classes: `PascalCase`. AUTOSAR methods: `camelCase`. Constants: `UPPER_CASE`
- Setters return `self` (method chaining)
- Type annotations: Python 3.8-compatible — `typing.Optional[T]` / `typing.List[T]`, NEVER `T | None` or `list[...]` (project requires Python >= 3.8, CI runs on 3.8–3.13)
  - NOTE: `CLAUDE.md` and `docs/development/coding_rules.md` incorrectly recommend `str | None` (3.10+ syntax). That guidance is WRONG for this repo — do not follow it. Use `typing` imports.
- Package structure rule: **leaf packages** (no subdirs) define the class in a `.py` file named after the package; **non-leaf packages** (have subdirs) define classes in `__init__.py`

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
