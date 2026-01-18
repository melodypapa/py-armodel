# Test Runner

Run the project test suite with comprehensive reporting and validation.

## Actions

When the user runs `/test`, perform the following:

### 1. Run Tests
- Execute the test runner script: `python scripts/run_tests.py --all`
- Or run specific test suites based on $ARGUMENTS:
  - `--unit`: Run only unit tests
  - `--integration`: Run only integration tests
  - `<test_file>`: Run specific test file

### 2. Check Coverage
- Review the coverage report output
- Verify coverage meets the ≥95% threshold
- Report any files with coverage below 100%

### 3. Report Results
- Display test execution summary
- Show total tests run, passed/failed
- Highlight any failures or errors
- Show coverage percentage

### 4. Troubleshooting
If tests fail:
- Identify which tests failed
- Show error messages
- Offer to investigate the failing tests
- Suggest fixes based on error output

## Usage Examples

```
/test
/test --unit
/test --integration
/test tests/models/test_autosar_models.py
/test --unit --verbose
```

## Quality Gates

The project requires:
- ✅ All tests pass
- ✅ Coverage ≥95%
- ✅ No unexpected errors or warnings
