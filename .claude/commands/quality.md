# Quality Check

Run all quality checks (linting, type checking, testing) to ensure code meets project standards.

## Quality Checks

When the user runs `/quality`, run the following checks in order:

### 1. Linting with Flake8
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```
- Expected: All checks pass with no E9, F63, F7, F82 errors
- If failures: Show linting errors and offer to fix

### 2. Linting V2 Models with Ruff
```bash
ruff check src/armodel/models_v2/
```
- Expected: No critical ruff errors (warnings acceptable)
- Warnings: Line length violations from long V2 imports are acceptable
- If failures: Show ruff errors and offer to fix

### 3. Type Checking V2 Models with MyPy
```bash
mypy src/armodel/models_v2/
```
- Expected: No critical type errors (warnings acceptable)
- Warnings: Missing type hints acceptable for gradual adoption
- If failures: Show mypy errors and offer to fix

### 4. Install Package
```bash
pip install -e .
```
- Expected: Package installs successfully

### 5. Testing with Pytest
```bash
pytest
```
- Expected: All tests pass
- If failures: Identify failing tests and help debug

### 6. Report Summary
Display a summary table:
```
Check        Status    Details
──────────────────────────────────
Flake8       ✅ Pass    No E9,F63,F7,F82 errors
Ruff (V2)    ✅ Pass    No critical errors in models_v2
MyPy (V2)    ✅ Pass    No critical type errors in models_v2
Pytest       ✅ Pass    All tests passed
```

## Quality Gates

All of the following must pass before committing:
1. ✅ Flake8 linting: No E9, F63, F7, F82 errors
2. ✅ Ruff (V2): No critical errors in models_v2 (warnings acceptable)
3. ✅ MyPy (V2): No critical type errors in models_v2 (warnings acceptable)
4. ✅ Pytest: All tests pass

## Arguments

Use `$ARGUMENTS` for specific checks:
- `--lint-only`: Run only linting
- `--test-only`: Run only tests

## Usage Examples

```
/quality
/quality --test-only
```

## References

See `.github/workflows/python-package.yml` for CI/CD configuration with ruff and mypy.

See `pyproject.toml` for ruff and mypy configuration settings.
