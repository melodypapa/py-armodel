# Integration Tests

Round-trip integration tests for py-armodel ARXML parser and writer.

## Purpose

These integration tests validate the parser and writer work correctly together through round-trip testing:

1. **Parse** ARXML file → AUTOSAR model
2. **Write** AUTOSAR model → ARXML file
3. **Re-parse** written ARXML file → AUTOSAR model
4. **Compare** original and re-parsed models for full equality

This establishes a safety baseline before refactoring the parser and writer.

## Running the Tests

### Using the Test Runner Script (Recommended)

The `scripts/run_tests.py` script provides a convenient way to run tests with colored output and summaries:

```bash
# Run all tests (unit + integration)
python scripts/run_tests.py

# Run only unit tests
python scripts/run_tests.py --unit

# Run only integration tests
python scripts/run_tests.py --integration

# Run with coverage reports
python scripts/run_tests.py --coverage

# Verbose output
python scripts/run_tests.py --verbose

# Pass additional pytest arguments
python scripts/run_tests.py -k "test_parser"
```

### Run All Tests

```bash
# Run all integration tests
pytest tests/integration_tests/

# Verbose output
pytest -v tests/integration_tests/

# Very verbose with print output
pytest -vv -s tests/integration_tests/
```

### Run Specific Categories

```bash
# Run only default test_files/ (29 files)
pytest tests/integration_tests/ -k "default"

# Run only datatypes-related tests
pytest tests/integration_tests/ -k "datatypes"

# Run only production files (from config.yaml)
pytest tests/integration_tests/ -k "production"

# Run only stress-test files
pytest tests/integration_tests/ -k "stress-test"

# Run only tests from additional directories (not test_files/)
pytest tests/integration_tests/ -k "additional"
```

### Quick Runs (Skip Slow Tests)

```bash
# Skip integration tests entirely
pytest -m "not integration"

# Skip slow tests
pytest -m "not slow"
```

## Adding New Test Files

### Adding Individual Files

1. Place ARXML files in `test_files/` directory at project root
2. They will be automatically discovered and tested

### Adding Entire Directories

Edit `config.yaml` to add directories:

```yaml
additional_directories:
  - path: "/path/to/your/project/arxml"
    category: "production"
    description: "Real production ARXML files"
    recursive: true  # Scan subdirectories

  - path: "../external_test_files"
    category: "stress-test"
    description: "Large/complex files"
    recursive: false  # Only top-level files
```

### Excluding Files

Use `exclude_patterns` in `config.yaml`:

```yaml
exclude_patterns:
  - "*/temp/*.arxml"
  - "*/backup/*.arxml"
  - "*_draft.arxml"
```

## Interpreting Failures

### Parse Failures

If a file fails to parse initially:

```
FAILED: Failed to parse SomeFile.arxml: ParseError: ...
```

This indicates the parser cannot handle the file. Check:
- File is valid ARXML
- AUTOSAR version is supported
- Required elements are implemented in the parser

### Write Failures

If writing fails:

```
FAILED: Failed to write SomeFile.arxml to /tmp/...: WriteError: ...
```

This indicates the writer cannot serialize the model. Check:
- Model is complete and valid
- Writer supports all elements in the model

### Re-parse Failures

If re-parsing the written file fails:

```
FAILED: Failed to re-parse written file /tmp/...: ParseError: ...
```

**This is critical** - it means the writer produced invalid ARXML.
The temporary file path is preserved for manual inspection.

### Comparison Failures

If models don't match after round-trip:

```
FAILED: Round-trip mismatch for SomeFile.arxml:
Value mismatch at RoundTrip(SomeFile.arxml).AR-PACKAGES[0].SHORT-NAME:
  Expected: OriginalPackage
  Got: ModifiedPackage
Temporary file preserved at: /tmp/...
```

This indicates data loss or corruption during round-trip.
The path shows exactly where the models differ.

## Troubleshooting

### Import Errors

If you see import errors:

```bash
# Install in editable mode
pip install -e .
```

### AUTOSAR Singleton Issues

If tests fail due to AUTOSAR singleton state:

```bash
# Run tests with isolation (no parallel execution)
pytest tests/integration_tests/ -p no:xdist
```

### Timeout Issues

For large files causing timeouts:

```bash
# Increase timeout (if using pytest-timeout)
pytest tests/integration_tests/ --timeout=300
```

### Temporary File Cleanup

Temporary files should be cleaned up automatically. If they persist:

```bash
# Manually clean temp directory
rm -rf /tmp/pytest-of-*/
```

## File Categorization

ARXML files are automatically categorized by filename patterns:

- **datatypes**: `*DataType*.arxml`, `AUTOSAR_Datatypes.arxml`
- **components**: `*SwComponentTypes*.arxml`, `SoftwareComponents.arxml`
- **bsw**: `BswM*.arxml`
- **system**: `CanSystem.arxml`, `*System.arxml`
- **blueprint**: `*_Blueprint.arxml`
- **lifecycle**: `*_LifeCycle_*.arxml`, `*_Standard.arxml`
- **default**: Files from `test_files/` directory
- **additional**: Files from config.yaml directories
- **production**: Config-specified production files
- **stress-test**: Config-specified stress-test files

## Known Issues

Files with known parsing/round-trip issues are tracked in `test_roundtrip.py`:

```python
KNOWN_ISSUES = {
    "SomeFile.arxml": {
        "reason": "Unsupported element XYZ",
        "issue_url": "https://github.com/melodypapa/py-armodel/issues/123"
    }
}
```

These tests are marked as `xfail` (expected to fail) and won't cause the test suite to fail.

## CI/CD Integration

These tests run in GitHub Actions:
- Separate job from unit tests
- Runs on every pull request
- Full suite runs before merge
- Results reported in PR comments

To run locally before pushing:

```bash
# Quick check (unit tests only)
pytest tests/test_armodel/

# Full check (unit + integration)
pytest tests/
```

## Performance

Typical run times:
- Single file: ~1-5 seconds
- 29 default files: ~30-60 seconds
- With additional files: Varies by file count and size

For faster iteration during development:
1. Run specific categories: `pytest -k "datatypes"`
2. Skip slow tests: `pytest -m "not slow"`
3. Run only default files: `pytest -k "default"`

## Further Reading

- Design document: `docs/plans/2025-01-24-integration-test-baseline-design.md`
- pytest documentation: https://docs.pytest.org/
- Project README: https://github.com/melodypapa/py-armodel
