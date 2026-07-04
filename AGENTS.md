# Agent Guidelines for py-armodel

## Build, Lint, Test Commands

**Run tests:**
- `python scripts/run_tests.py` - Recommended (colored output, summary)
- `python scripts/run_tests.py --unit` - Unit tests only
- `python scripts/run_tests.py --integration` - Integration tests only
- `python scripts/run_tests.py --coverage` - With coverage reports
- `pytest tests/test_armodel/parser/test_arxml_parser.py` - Specific file
- `pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method` - Specific method
- Or npm shortcuts: `npm run pytest`, `npm run pytest-cov`

**Lint:**
- `npm run flake8` - Syntax checks only (E9, F63, F7, F82)
- CI also runs: `flake8 . --exit-zero --max-complexity=10 --max-line-length=127` (warnings)
- **Exclude build/ from lint** - Contains generated code

**Build:**
- `python -m build` - Full distribution
- `python -m build --sdist` - Source only
- `python -m build --wheel` - Wheel only

## Critical: AUTOSAR Version MUST Be Set

```python
AUTOSAR.setARRelease('R23-11')  # REQUIRED before parse or write
document = AUTOSAR.getInstance()
document.clear()  # or AUTOSAR.new()
parser.load('file.arxml', document)
writer.save('output.arxml', document)
```

## Architecture Quirks

- Source: `src/armodel/`, Tests: `tests/` (mirrors structure)
- `AUTOSAR` singleton: Use `getInstance()` / `new()` to reset
- Model classes use wildcard exports in `__init__.py`
- Abstract base classes use `ABC` from `abc` module (not `ABCMeta`)

## Testing Gotchas

- Integration tests require `pyyaml` (auto-installed by test runner)
- Integration tests use `AUTOSAR.getInstance().new()` to reset singleton between tests
- Custom ARXML files can be added via `tests/integration_tests/config.yaml`
- Integration tests run round-trip validation: parse → write → re-parse → compare

## Code Style

- Max line length: 79 (CI warns at 127)
- Classes: `PascalCase`, Methods: `camelCase` (AUTOSAR standard), Constants: `UPPER_CASE`
- **Do NOT add comments** unless asked
- Method chaining: setters return `self`

## Parser Options

```python
ARXMLParser(options={"warning": True})  # Warnings instead of exceptions
```

## Finding Elements

```python
# findXXX() returns None if not found (no exceptions)
component = autosar.findAtomicSwComponentType('MyComponent')
if component is not None:
    behavior = autosar.getBehavior(component)
```

## Important Constraints

- Python >= 3.8 required (CI tests 3.8-3.13)
- Duplicate UUID checking is enabled
- Same short names can coexist across different types
- Boolean values in XML should not contain spaces
- Float scientific notation is properly handled
