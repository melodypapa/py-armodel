# Integration Test Baseline Design

**Date**: 2025-01-24
**Author**: Design Discussion
**Status**: Approved

## Overview

Create integration tests for the ARXML parser and writer to establish a safety baseline before refactoring. The tests will validate that the parser and writer work correctly together through round-trip testing: parse → write → re-parse → compare.

## Problem Statement

Before refactoring the ARXML parser and writer, we need a comprehensive test suite that validates:
- The parser correctly reads ARXML files
- The writer correctly produces valid ARXML
- Round-trip operations preserve data integrity
- Changes during refactoring don't break existing functionality

Current unit tests use small XML fragments and don't validate the full parse-write cycle.

## Goals

1. **Round-trip validation**: Ensure data integrity through full parse-write-reparse cycle
2. **Full model equality**: Deep comparison of original and re-parsed models
3. **Comprehensive coverage**: Test all 29 ARXML files in `test_files/`
4. **Extensibility**: Support additional ARXML files from external directories
5. **Auto-detection**: Automatically detect AUTOSAR version from each file

## Architecture

### Test Structure

```
tests/integration_tests/
├── __init__.py                 # Package marker
├── conftest.py                 # Pytest fixtures
├── config.yaml                 # Additional directory configuration
├── test_roundtrip.py           # Main round-trip test class
└── README.md                   # Documentation
```

### Core Components

1. **`conftest.py`** - Pytest fixtures:
   - `test_files_dir()`: Returns path to `test_files/`
   - `arxml_files()`: Yields all ARXML file paths (default + additional)
   - `autosar_reset()`: Resets AUTOSAR singleton between tests
   - `temp_file()`: Creates temporary file paths for write operations

2. **`test_roundtrip.py`** - Main test class:
   - `TestRoundTrip`: Parameterized test class
   - `test_roundtrip_all_files(arxml_file_path)`: Main test method

3. **`config.yaml`** - Configuration:
   - Additional directories to scan for `.arxml` files
   - Category labels for selective testing
   - Exclude patterns for unwanted files

## Implementation Details

### Version Detection

Extract AUTOSAR version from XML schema location in `<AUTOSAR>` element:

```python
# Example mapping
XSD_TO_VERSION = {
    "AUTOSAR_4-3-0.xsd": "4.3.0",
    "AUTOSAR_00046.xsd": "R23-11",
    "AUTOSAR_00049.xsd": "R24-11",
}
```

Fallback to default version (e.g., "R23-11") if detection fails.

### Deep Equality Comparison

Recursive comparison function since model objects lack `__eq__`:

```python
def assert_models_equal(original, reparsed, path=""):
    """Recursively compare AUTOSAR models"""
    # Compare types
    # Compare attributes (short_name, UUID, etc.)
    # Compare child collections recursively
    # Skip parent references (implementation detail)
```

### Test Execution Flow

For each ARXML file:
1. Reset AUTOSAR singleton: `AUTOSAR.new()`
2. Detect version from file → `AUTOSAR.setARRelease(version)`
3. Parse original file → `original_doc`
4. Write to temp file → `temp_path`
5. Reset singleton and re-parse temp file → `reparsed_doc`
6. Compare: `assert_models_equal(original_doc, reparsed_doc)`

### Error Handling

- **Parse failures**: Mark as `xfail`, skip round-trip
- **Write failures**: Fail test with error details
- **Re-parse failures**: Fail test (writer produced invalid ARXML)
- **Comparison failures**: Report exact divergence path with expected vs actual values

### Configuration

`config.yaml` format:

```yaml
# Additional directories to scan for ARXML files
additional_directories:
  - path: "/path/to/project/arxml"
    category: "production"
    description: "Real production ARXML files"
    recursive: true  # Scan subdirectories

  - path: "../external_files"
    category: "stress-test"
    description: "External test files"
    recursive: false  # Only top-level .arxml files

# Optional: Exclude specific files or patterns
exclude_patterns:
  - "*/temp/*.arxml"
  - "*/backup/*.arxml"
  - "*_test_backup.arxml"
```

### File Discovery

1. Always include all 29 files from `test_files/` directory
2. Load `config.yaml` and scan additional directories
3. Respect `recursive` flag for subdirectory scanning
4. Apply `exclude_patterns` to filter unwanted files
5. Mark files with `category` for selective testing

### Known Issues Tracking

Track files with known parsing/round-trip issues:

```python
KNOWN_ISSUES = {
    "SomeFile.arxml": {
        "reason": "Unsupported element XYZ",
        "issue_url": "https://github.com/.../issues/123"
    }
}
```

Marked as `xfail` with appropriate messages.

## Test Categorization

ARXML files categorized by type for selective testing:

- **datatypes**: AUTOSAR_Datatypes.arxml, *_DataType*.arxml
- **components**: SoftwareComponents.arxml, *SwComponentTypes*.arxml
- **bsw**: BswM_Bswmd.arxml, BswMMode.arxml
- **system**: CanSystem.arxml
- **blueprint**: *_Blueprint.arxml
- **lifecycle**: *_LifeCycle_*.arxml, *_Standard.arxml
- **production**: Additional files from config (category: "production")
- **stress-test**: Large/complex files from config (category: "stress-test")

### Usage Examples

```bash
# Run all tests
pytest tests/integration_tests/

# Run only default test_files
pytest tests/integration_tests/ -k "not additional"

# Run only datatypes category
pytest tests/integration_tests/ -k "datatypes"

# Run only production files from additional directories
pytest tests/integration_tests/ -k "production"

# Run only stress-test category
pytest tests/integration_tests/ -k "stress-test"

# Verbose mode
pytest -v tests/integration_tests/test_roundtrip.py
```

## Pytest Markers

- `@pytest.mark.integration`: Mark as integration tests
- `@pytest.mark.slow`: Mark for skipping in quick runs
- Category markers: `@pytest.mark.datatypes`, `@pytest.mark.production`, etc.

## Performance Considerations

Running all tests may be slow. Support:
- Quick runs: `pytest -m "not slow"`
- Per-category testing for faster feedback
- Parallel execution with pytest-xdist (future enhancement)

## CI/CD Integration

Integration tests run in GitHub Actions:
- Separate job from unit tests
- Not blocking for quick PR checks
- Full suite runs before merge
- Results reported in PR comments

## Documentation

### README.md Contents

- Purpose of integration tests
- How to run tests
- How to add new test files via config.yaml
- How to interpret failures
- Troubleshooting common issues

### Code Documentation

- Module docstring: Explain round-trip approach
- Class docstring: Test purpose and methodology
- Method docstrings: Detailed explanation of comparison logic

## Success Criteria

1. All 29 default ARXML files pass round-trip tests
2. Additional directory scanning works correctly
3. Test failures provide clear, actionable error messages
4. Tests complete in reasonable time (< 5 minutes for full suite)
5. Baseline established before refactoring begins
6. Tests catch intentional regressions when validated

## Future Enhancements

- Parallel test execution with pytest-xdist
- Performance benchmarking (parse time, file size tracking)
- HTML coverage report for parsed elements
- Diff output for failed comparisons (side-by-side)
- Integration with refactoring progress tracking

## References

- AUTOSAR standard: https://www.autosar.org/
- pytest documentation: https://docs.pytest.org/
- Project ARXML parser refactoring design: `docs/plans/2025-01-24-arxml-parser-refactoring-design.md`
