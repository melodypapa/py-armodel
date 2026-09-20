# Os ECUC YAML Integration Test

## Goal

Add integration coverage for exporting the current `Os_ECUC.arxml` fixture to YAML and ensure the complete generated semantic configuration remains stable.

## Design

- Add `tests/integration_tests/test_files/Os_ECUC.yaml` as the checked-in golden output for the current ARXML fixture.
- Add one integration test to `tests/integration_tests/test_os_config_export_cli.py`.
- Invoke the CLI with `--format yaml` and a temporary output path.
- Load both YAML files with `yaml.safe_load` and compare their complete mappings.
- Assert that both `OsApplication` and `OsTask` sections contain records.
- Assert that every application and task record contains all fields emitted by the exporter.
- Keep production code, the ARXML fixture, and existing smoke coverage unchanged.

## Verification

Run the focused integration test, then the repository lint and test commands if dependencies permit.
