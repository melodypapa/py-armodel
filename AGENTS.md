# Agent Guidelines for py-armodel

## Environment (uv)

The repo is uv-managed — `uv.lock` and a uv-managed `.venv` (Python 3.11) exist.
- `uv sync --extra pytest` — install test deps (plain `pip install -e .` does NOT install pytest)
- `uv run pytest ...` or `uv run python scripts/run_tests.py` — run inside `.venv` without activating (or `source .venv/bin/activate` first); do not commit `.venv` changes
- Extras in `pyproject.toml`: `pytest` (pytest, pytest-cov, pyyaml) and `lint` (ruff, black)

## Build, Lint, Test Commands

**Tests (recommended):** `python scripts/run_tests.py` — colored output, summary, coverage ON by default
- Flags: `--unit` / `--integration` / `--no-coverage` / `--verbose`. There is NO `--coverage` flag despite `README.md` showing one; use `--no-coverage` to disable coverage
- Extra args pass through to pytest: `python scripts/run_tests.py -k "datatypes"`
- Directly: unit `pytest tests/test_armodel/`, integration `pytest tests/integration_tests/ -s`
- Integration tests = round-trip parse → write → re-parse → compare over `tests/integration_tests/test_files/*.arxml`; add custom dirs via `tests/integration_tests/config.yaml`
- CI runs plain `pytest` over all of `tests/` — the full suite must pass

**Lint:** `npm run lint` — runs flake8 syntax checks (E9, F63, F7, F82) **and** ruff (`ruff check src tests scripts`, E/F/W/I rules per `[tool.ruff]` in pyproject.toml). Always use this; do not run flake8 alone
- **Do NOT re-sort imports in `src/armodel/models/**`, `src/armodel/parser/arxml_parser.py`, `src/armodel/writer/arxml_writer.py`** — ruff's I001 (and E402 in parser/writer) is intentionally disabled in `[tool.ruff.lint.per-file-ignores]` because import order avoids circular imports; auto-fixing triggers ImportError at package load
- **Exclude `build/`** from lint (generated code)
- CI also runs flake8 `--exit-zero --max-complexity=10 --max-line-length=127` (warnings, non-blocking)

**Format:** `npm run black` — Black formatter at **200 char** line length (`[tool.black]` in pyproject.toml); `npm run black-check` to check only

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
- Data flow: `parser/arxml_parser.py` builds the in-memory model (`models/M2/*`) → mutate via the AUTOSAR singleton → `writer/arxml_writer.py` serializes it back. Round-trip integrity is the contract enforced by the integration tests
- Model classes are exported via wildcard imports (`from .my_class import *`) in parent `__init__.py` files — a new class MUST be added there or it won't be importable from `armodel.models`
- Heritage: every model class derives from `ARObject` → `Referrable` → `MultilanguageReferrable` → `Identifiable` → `PackageableElement` → `ARElement` (full tree: `README.md` §1.9)
- Domains: `models/M2/MSR/` (AsamHdo, DataDictionary, Documentation, CalibrationData), `models/M2/AUTOSARTemplates/` (CommonStructure, SWComponentTemplate, SystemTemplate, BswModuleTemplate, ECUC*, GenericStructure, DiagnosticExtract), `models/utils/` (UUIDMgr); plus `parser/`, `writer/`, `cli/`, `lib/`, `data_models/`, `transformer/`, `report/`

### Adding a New Model Class

1. **Leaf package** (no subdirs) → define the class in a `.py` file named after the package; **non-leaf** (has subdirs) → define in `__init__.py`
2. Place it under the correct domain in `src/armodel/models/M2/AUTOSARTemplates/`
3. Add `from .my_class import *` to the parent `__init__.py`; add to `src/armodel/models/__init__.py` if top-level
4. Add a test under `tests/test_armodel/models/M2/`; run `python scripts/run_tests.py` and `npm run black`
- For spec-alignment work use the repo skill `sync-autosar-class` (trigger: "sync <ClassName>"; rules in `.claude/skills/sync-autosar-class/rules.md`, AUTOSAR PDF spec tables are the source of truth)

## Code Style

- **Do NOT add comments** unless asked
- Black at 200 chars is the enforced format — don't hand-wrap to 79/127; flake8 line-length/complexity warnings are exit-zero and non-blocking
- Classes `PascalCase`, AUTOSAR methods `camelCase`, constants `UPPER_CASE`; setters return `self` (method chaining)
- Use `ABC` from `abc` as the base class (as `ARObject` does), not `ABCMeta`
- Type annotations MUST be Python 3.8-compatible: `typing.Optional[T]` / `typing.List[T]`, NEVER `T | None` or `list[T]` (requires-python >= 3.8, CI tests 3.8–3.13)
  - NOTE: `CLAUDE.md` and `docs/development/coding_rules.md` recommend 3.10+ union syntax — that guidance is WRONG for this repo; use `typing` imports

## Parser & Model Gotchas

```python
parser = ARXMLParser(options={"warning": True})  # warnings instead of exceptions
```

- `findXXX()` returns `None` if not found (no exception)
- Same short name can coexist across *different* types
- Duplicate UUID checking is enabled
- Booleans written without spaces (`true`); float scientific notation handled (`1.23e-5`)
- Parent-child references are bi-directional — maintain them with `addElement()`

## CLI Tools (console_scripts)

`arxml-dump`, `arxml-format`, `format-xml`, `armodel-component`, `connector2xlsx`, `connector-update`, `armodel-system-signal`, `armodel-memory-section`, `armodel-file-list`, `armodel-uuid-checker`, `os-ecuc-export` — one module per tool in `src/armodel/cli/`

## Pytest Markers (pytest.ini)

`integration`, `slow`, `datatypes`, `components`, `bsw`, `system`, `blueprint`, `lifecycle`

## Slash Commands (Claude Code)

`.claude/commands/` — `/test`, `/quality`, `/gh-workflow`, `/merge-pr`, `/req`

## Key References

- `CLAUDE.md` — comprehensive project guidance (verify against config; see the 3.10-syntax caveat above)
- `docs/development/` — `coding_rules.md`, `parser_writer_conventions.md`, `model_test_parity.md`
- Version lives in `src/armodel/__init__.py` (`__version__`), pulled into the wheel via setuptools dynamic attr — bump there, not in pyproject.toml
