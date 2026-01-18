# Quality Check

Run all quality checks (linting, type checking, testing) to ensure code meets project standards.

## Quality Checks

When the user runs `/quality`, run the following checks in order:

### 1. Linting with Ruff
```bash
ruff check src/ tests/
```
- Expected: All checks pass with no errors or warnings
- If failures: Show linting errors and offer to fix

### 2. Type Checking with Mypy
```bash
mypy src/autosar_pdf2txt/
```
- Expected: Success: no issues found in 9 source files
- If failures: Show type errors and suggest fixes

### 3. Testing with Coverage
```bash
python scripts/run_tests.py --unit
```
- Expected: All tests pass (126 tests) with ≥95% coverage
- If failures: Identify failing tests and help debug

### 4. Report Summary
Display a summary table:
```
Check        Status    Details
──────────────────────────────────
Ruff         ✅ Pass    No errors
Mypy         ✅ Pass    No issues
Pytest       ✅ Pass    126/126 tests, 97% coverage
```

## Quality Gates

All of the following must pass before committing:
1. ✅ Ruff linting: No errors
2. ✅ Mypy type checking: No issues
3. ✅ Pytest: All tests pass
4. ✅ Coverage: ≥95%

## Arguments

Use `$ARGUMENTS` for specific checks:
- `--lint-only`: Run only linting
- `--type-only`: Run only type checking
- `--test-only`: Run only tests
- `--fix`: Auto-fix linting issues with `ruff check --fix`

## Usage Examples

```
/quality
/quality --fix
/quality --test-only
```

## References

See `docs/development/coding_rules.md` for complete coding standards.
