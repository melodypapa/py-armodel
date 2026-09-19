# OS Application and Task Collector Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert parsed ECUC OS configuration objects into actual AUTOSAR OS model classes and export them through a new `os-config-export` CLI command as XLSX or YAML.

**Architecture:** Keep the generic ARXML parser responsible for ECUC model construction. Add standalone no-argument OS model classes under `armodel.models.extended.os`, with M2-style getters, setters, and adders but no M2 inheritance or parent field. Add `OsEcucParser` under `armodel.parser` as the dedicated ECUC-to-OS loader; it reads ECUC objects and populates `OsOs`, `OsApplication`, and `OsTask`. Register a new `os-config-export` console script with `--format {xlsx,yaml}`, defaulting to `xlsx`.

**Tech Stack:** Python 3.8-compatible typing and project-style model classes, existing `ARXMLParser` and `AUTOSAR` singleton, `argparse`, `openpyxl`, optional `pyyaml` test dependency.

## Global Constraints

- Python >= 3.8; use `typing.Optional` and `typing.List`, never `T | None` or `list[...]`.
- Use exact AUTOSAR Chapter 10 names for semantic fields and the existing `Identifiable` short-name identity convention.
- Strict mapping: ignore vendor-only fields such as `OsStacksize`.
- `OsEcucParser` reads ECUC model objects first; exporters must not inspect ECUC model internals.
- Store `Os_ECUC.arxml` under `tests/integration_tests/test_files` as the committed OS integration fixture.
- Preserve existing parser behavior and do not modify generic ECUC parser logic unless a concrete adapter gap is proven.
- Use `apply_patch` for manual edits.
- Run `npm run lint` and relevant tests; exclude `build/` from lint.
- Run `npm run black` for changed Python files.

---

### Task 1: Add OS Semantic Model Classes

**Files:**
- Create: `src/armodel/models/extended/__init__.py`
- Create: `src/armodel/models/extended/os/__init__.py`
- Create: `src/armodel/models/extended/os/models.py`
- Create: `tests/test_armodel/models/extended/__init__.py`
- Create: `tests/test_armodel/models/extended/os/__init__.py`
- Create: `tests/test_armodel/models/extended/os/test_models.py`

**Interfaces:**
- Produces standalone `OsApplication`, `OsTask`, and `OsOs` classes with M2-style accessors, no M2 inheritance, no parent field, no-argument constructors, and a `name` identity member.
- `OsApplication.OsAppTaskRef` contains `List[OsTask]`.
- `OsApplication.OsRestartTask` contains `Optional[OsTask]`.
- `OsTask.OsTaskAccessingApplication` contains `List[OsApplication]`.
- `OsOs.OsApplication` and `OsOs.OsTask` contain the top-level semantic object lists.

- [ ] **Step 1: Write failing model-class shape tests**

```python
from armodel.models.extended.os import OsApplication, OsOs, OsTask


def test_os_model_identity_and_standard_fields():
    application = OsApplication()
    task = OsTask()
    application.setName("App")
    task.setName("Task")
    assert application.getName() == "App"
    assert task.getName() == "Task"
    assert hasattr(application, "OsTrusted")
    assert hasattr(task, "OsTaskPriority")
    assert hasattr(task, "OsTaskAppModeRef")
    assert hasattr(task, "OsTaskExecutionBudget")
    assert not hasattr(task, "OsStacksize")


def test_os_relationship_fields_are_initialized_independently():
    application = OsApplication().setName("App")
    task = OsTask().setName("Task")
    first = OsOs().setName("Os")
    second = OsOs().setName("OtherOs")

    first.addOsApplication(application)
    second.addOsApplication(OsApplication().setName("Other"))
    application.addOsAppTaskRef(task)

    assert first.getOsApplications()[0].getOsAppTaskRefs() == [task]
    assert second.getOsApplications()[0].getOsAppTaskRefs() == []
```

- [ ] **Step 2: Run the focused tests and verify they fail**

Run: `uv run pytest tests/test_armodel/models/extended/os/test_models.py -v`

Expected: FAIL because `armodel.models.extended.os` and the model classes do not yet exist.

- [ ] **Step 3: Implement project-style model classes**

Implement `models.py` with standalone classes, no M2 inheritance, no parent field, and no-argument constructors. Use mutable members, `getXxx`/`setXxx` accessors, `addXxx` methods for repeated members, and chainable setters. Use Python 3.8-compatible annotations. The identity member is `name`, exposed by `getName()` and `setName()`. Include these exact fields:

```python
class OsApplication:
    name: str
    OsTrusted: Optional[bool]
    OsTrustedApplicationDelayTimingViolationCall: Optional[bool]
    OsTrustedApplicationWithProtection: Optional[bool]
    OsAppAlarmRef: List[str]
    OsAppCounterRef: List[str]
    OsAppEcucPartitionRef: Optional[str]
    OsAppIsrRef: List[str]
    OsAppScheduleTableRef: List[str]
    OsAppTaskRef: List[OsTask]
    OsMemoryMappingCodeLocationRef: Optional[str]
    OsRestartTask: Optional[OsTask]
    OsAppStartupHook: Optional[bool]
    OsAppErrorHook: Optional[bool]
    OsAppShutdownHook: Optional[bool]
    OsTrustedFunctionName: List[str]
    ApplicationState: str
```

```python
class OsTask:
    name: str
    OsTaskActivation: Optional[int]
    OsTaskPeriod: Optional[float]
    OsTaskPriority: Optional[int]
    OsTaskSchedule: Optional[str]
    OsMemoryMappingCodeLocationRef: Optional[str]
    OsTaskAccessingApplication: List[OsApplication]
    OsTaskEventRef: List[str]
    OsTaskResourceRef: List[str]
    OsTaskAppModeRef: List[str]
    OsTaskAllInterruptLockBudget: Optional[float]
    OsTaskExecutionBudget: Optional[float]
    OsTaskOsInterruptLockBudget: Optional[float]
    OsTaskTimeFrame: Optional[float]
    OsTaskResourceLockBudget: List[float]
    OsTaskResourceLockResourceRef: List[str]
```

Use `ApplicationState = "APPLICATION_ACCESSIBLE"` by default. Do not include separate `OsTaskAutostart`, `OsTaskTimingProtection`, or `OsTaskResourceLock` classes.

- [ ] **Step 4: Run the focused tests and verify they pass**

Run: `uv run pytest tests/test_armodel/models/extended/os/test_models.py -v`

Expected: PASS.

- [ ] **Step 5: Commit the datamodel task**

```bash
git add src/armodel/models/extended tests/test_armodel/models/extended
git commit -m "feat: add AUTOSAR OS semantic model classes"
```

### Task 2: Convert ECUC Objects to OS Model Classes

**Files:**
- Create: `src/armodel/parser/os_ecuc_parser.py`
- Modify: `src/armodel/parser/__init__.py`
- Create: `tests/test_armodel/models/extended/os/test_converter.py`

**Interfaces:**
- Produces `OsEcucParser.load(path, document=None) -> OsOs` and `OsEcucParser.parseEcuc(document) -> OsOs`.
- `load(path)` sets the AR release to `R23-11`, invokes the existing `ARXMLParser` to construct ECUC model objects, and delegates to `parseEcuc`.
- `parseEcuc(document)` consumes ECUC model objects and populates standalone OS model objects.
- `OsOs.from_file(path)` and `OsOs.from_ecuc(document)` are optional convenience delegates to `OsEcucParser`; the parser class is the primary loader API.

- [ ] **Step 1: Write a failing conversion test using the demo file**

```python
from pathlib import Path

from armodel.models.extended.os import OsOs


def test_from_file_converts_demo_os_configuration():
    result = OsEcucParser().load(Path("tests/integration_tests/test_files/Os_ECUC.arxml"))

    assert [item.getName() for item in result.getOsApplications()] == ["OsApplication_QM"]
    assert [item.getName() for item in result.getOsTasks()] == [
        "Init_Task",
        "Rte_Time_Task",
        "Rte_Event_Task",
        "SchMDiagStateTask_20ms",
    ]
    application = result.getOsApplications()[0]
    assert [item.getName() for item in application.getOsAppTaskRefs()] == [
        "Init_Task",
        "Rte_Time_Task",
        "Rte_Event_Task",
        "SchMDiagStateTask_20ms",
    ]
    assert application.OsTrusted is False
```

- [ ] **Step 2: Run the demo test and verify it fails**

Run: `uv run pytest tests/test_armodel/models/extended/os/test_converter.py::test_from_file_converts_demo_os_configuration -v`

Expected: FAIL because the conversion API is not implemented.

- [ ] **Step 3: Add ECUC traversal helpers in the converter**

Implement helpers that:

1. Locate `MODULE-CONFIGURATION` elements whose definition path ends in `/Os`.
2. Enumerate legacy `CONTAINER` values under the module.
3. Read each container's `SHORT-NAME` and `DEFINITION-REF`.
4. Index containers by normalized ECUC value path, using the module package path plus the container short name.
5. Read scalar `PARAMETER-VALUES` by the final component of each parameter definition path.
6. Read repeated `REFERENCE-VALUES` in source order.
7. Recursively locate nested `SUB-CONTAINERS` by definition short name.

Keep the helper output internal to `src/armodel/parser/os_ecuc_parser.py`; it must return typed values and normalized reference strings, not ECUC objects exposed to callers.

- [ ] **Step 4: Implement task-first conversion**

For each container with definition short name `OsTask`, create one no-argument `OsTask()` and populate `name` through `setName()` plus the standard fields through project-style setters:

```python
task.setOsTaskActivation(read_int("OsTaskActivation"))
task.setOsTaskPeriod(read_float("OsTaskPeriod"))
task.setOsTaskPriority(read_int("OsTaskPriority"))
task.setOsTaskSchedule(read_enum("OsTaskSchedule"))
task.setOsMemoryMappingCodeLocationRef(read_reference("OsMemoryMappingCodeLocationRef"))
for value in read_references("OsTaskEventRef"):
    task.addOsTaskEventRef(value)
for value in read_references("OsTaskResourceRef"):
    task.addOsTaskResourceRef(value)
for value in nested_references("OsTaskAutostart", "OsTaskAppModeRef"):
    task.addOsTaskAppModeRef(value)
task.setOsTaskAllInterruptLockBudget(nested_float("OsTaskTimingProtection", "OsTaskAllInterruptLockBudget"))
task.setOsTaskExecutionBudget(nested_float("OsTaskTimingProtection", "OsTaskExecutionBudget"))
task.setOsTaskOsInterruptLockBudget(nested_float("OsTaskTimingProtection", "OsTaskOsInterruptLockBudget"))
task.setOsTaskTimeFrame(nested_float("OsTaskTimingProtection", "OsTaskTimeFrame"))
for value in nested_floats("OsTaskTimingProtection", "OsTaskResourceLock", "OsTaskResourceLockBudget"):
    task.addOsTaskResourceLockBudget(value)
for value in nested_references("OsTaskTimingProtection", "OsTaskResourceLock", "OsTaskResourceLockResourceRef"):
    task.addOsTaskResourceLockResourceRef(value)
```

Ignore `OsStacksize` and any other non-standard parameter.

- [ ] **Step 5: Implement application conversion and relationship resolution**

Create every `OsApplication`, populate its Chapter 10 fields, then resolve `OsAppTaskRef` and `OsRestartTask` to the existing task instances. Resolve each task's `OsTaskAccessingApplication` to existing application instances. Deduplicate object references while preserving first-seen order.

Raise a specific conversion error for a standard reference whose target cannot be found. Do not infer relationships from short-name prefixes or substrings.

- [ ] **Step 6: Run converter tests and add missing-value/reference tests**

Add tests for absent optional fields, repeated references, ignored `OsStacksize`, malformed scalar values, and unresolved standard references.

Run: `uv run pytest tests/test_armodel/models/extended/os/test_converter.py -v`

Expected: PASS.

- [ ] **Step 7: Run the full OS test package**

Run: `uv run pytest tests/test_armodel/models/extended/os -v`

Expected: PASS.

- [ ] **Step 8: Commit the converter task**

```bash
git add src/armodel/parser/os_ecuc_parser.py src/armodel/parser/__init__.py tests/test_armodel/models/extended/os/test_converter.py
git commit -m "feat: convert ECUC OS objects to semantic model classes"
```

### Task 3: Add YAML and XLSX Exporters

**Files:**
- Create: `src/armodel/models/extended/os/exporters.py`
- Create: `tests/test_armodel/models/extended/os/test_exporters.py`
- Modify: `pyproject.toml:29-46`

**Interfaces:**
- Consumes only `OsOs` model objects.
- Produces `write_yaml(os_os: OsOs, output_path: Path) -> None` and `write_xlsx(os_os: OsOs, output_path: Path) -> None`.

- [ ] **Step 1: Write failing exporter tests**

```python
from pathlib import Path

import yaml
from openpyxl import load_workbook

from armodel.models.extended.os import OsApplication, OsOs, OsTask
from armodel.models.extended.os.exporters import write_xlsx, write_yaml


def test_write_yaml_uses_semantic_names(tmp_path: Path):
    os_os = OsOs().setName("Os")
    os_os.addOsApplication(OsApplication().setName("App"))
    os_os.addOsTask(OsTask().setName("Task").setOsTaskPriority(5))
    output = tmp_path / "os.yaml"

    write_yaml(os_os, output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert data["OsApplication"][0]["name"] == "App"
    assert data["OsTask"][0]["OsTaskPriority"] == 5


def test_write_xlsx_uses_expected_sheets(tmp_path: Path):
    output = tmp_path / "os.xlsx"
    os_os = OsOs().setName("Os")
    os_os.addOsApplication(OsApplication().setName("App"))
    os_os.addOsTask(OsTask().setName("Task"))
    write_xlsx(os_os, output)

    workbook = load_workbook(output)
    assert "OsApplication" in workbook.sheetnames
    assert "OsTask" in workbook.sheetnames
```

- [ ] **Step 2: Run exporter tests and verify they fail**

Run: `uv run pytest tests/test_armodel/models/extended/os/test_exporters.py -v`

Expected: FAIL because exporter functions are not implemented.

- [ ] **Step 3: Implement recursive model serialization for YAML**

Use explicit serializer helpers over the project-style model getters, or a shared model-to-dictionary helper limited to the new OS classes. Serialize exact field names. Convert object relationships to `getName()` values to avoid recursive object graphs. Keep reference strings unchanged. Use `yaml.safe_dump(..., sort_keys=False)` and add `pyyaml` only to the existing pytest optional dependency if it is needed by runtime tests rather than runtime package imports.

- [ ] **Step 4: Implement XLSX worksheets**

Use `openpyxl` and the existing `ExcelReporter` conventions. Create worksheets `OsApplication` and `OsTask`; write exact field names in row 1 and one row per object. Serialize lists as stable delimiter-joined values and object relationships as `name` delimiter-joined values. Do not create separate nested-object worksheets because those fields are flattened into `OsTask`.

- [ ] **Step 5: Run exporter tests and verify they pass**

Run: `uv run pytest tests/test_armodel/models/extended/os/test_exporters.py -v`

Expected: PASS.

- [ ] **Step 6: Commit the exporter task**

```bash
git add src/armodel/models/extended/os/exporters.py tests/test_armodel/models/extended/os/test_exporters.py pyproject.toml
git commit -m "feat: export semantic OS configuration"
```

### Task 4: Add the `os-config-export` CLI

**Files:**
- Create: `src/armodel/cli/os_config_export_cli.py`
- Create: `tests/test_armodel/cli/test_os_config_export_cli.py`
- Modify: `pyproject.toml:36-46`

**Interfaces:**
- Console script: `os-config-export = armodel.cli.os_config_export_cli:main`.
- Command: `os-config-export INPUT OUTPUT [--format {xlsx,yaml}]`.
- Default format: `xlsx`.

- [ ] **Step 1: Write failing CLI tests**

```python
from pathlib import Path

from openpyxl import load_workbook

from armodel.cli.os_config_export_cli import main


def test_cli_defaults_to_xlsx(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.xlsx"
    monkeypatch.setattr("sys.argv", ["os-config-export", "tests/integration_tests/test_files/Os_ECUC.arxml", str(output)])

    main()

    assert output.exists()
    assert "OsTask" in load_workbook(output).sheetnames


def test_cli_supports_yaml(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.yaml"
    monkeypatch.setattr("sys.argv", ["os-config-export", "tests/integration_tests/test_files/Os_ECUC.arxml", str(output), "--format", "yaml"])

    main()

    assert output.exists()
```

- [ ] **Step 2: Run CLI tests and verify they fail**

Run: `uv run pytest tests/test_armodel/cli/test_os_config_export_cli.py -v`

Expected: FAIL because the module and console entry point are not implemented.

- [ ] **Step 3: Implement argument parsing and dispatch**

Use `argparse` with positional `INPUT` and `OUTPUT`, and `--format` choices `xlsx` and `yaml`, default `xlsx`. Call `OsOs.from_file(args.INPUT)`, then dispatch to `write_xlsx` or `write_yaml`. Convert expected input/conversion/output exceptions into `parser.error(...)` or a non-zero `SystemExit`; successful conversion returns normally.

- [ ] **Step 4: Register the console script**

Add exactly:

```toml
os-config-export = "armodel.cli.os_config_export_cli:main"
```

- [ ] **Step 5: Run CLI tests and verify they pass**

Run: `uv run pytest tests/test_armodel/cli/test_os_config_export_cli.py -v`

Expected: PASS.

- [ ] **Step 6: Verify the installed command metadata**

Run: `uv run python -m pip install -e .` then `uv run os-config-export --help`.

Expected: help output includes `--format {xlsx,yaml}` and identifies `xlsx` as the default behavior in the usage/help text.

- [ ] **Step 7: Commit the CLI task**

```bash
git add src/armodel/cli/os_config_export_cli.py tests/test_armodel/cli/test_os_config_export_cli.py pyproject.toml
git commit -m "feat: add OS configuration export CLI"
```

### Task 5: Documentation and Quality Verification

**Files:**
- Modify: `docs/superpowers/specs/2026-09-19-os-application-task-collector-design.md` only if implementation details require a clarified contract.

- [ ] **Step 1: Run the complete focused test suite**

Run: `uv run pytest tests/test_armodel/models/extended/os tests/test_armodel/cli/test_os_config_export_cli.py -v`

Expected: PASS.

- [ ] **Step 2: Run the demo CLI for both formats**

Run: `uv run os-config-export tests/integration_tests/test_files/Os_ECUC.arxml build/os_config.xlsx`

Run: `uv run os-config-export tests/integration_tests/test_files/Os_ECUC.arxml build/os_config.yaml --format yaml`

Expected: both files are created; the XLSX contains `OsApplication` and `OsTask` sheets; YAML contains the same semantic objects and exact field names.

- [ ] **Step 3: Run formatting and lint**

Run: `npm run black`

Run: `npm run lint`

Expected: both commands complete successfully. Do not auto-sort imports in the existing model/parser files.

- [ ] **Step 4: Run the repository test command**

Run: `uv run python scripts/run_tests.py --no-coverage`

Expected: all applicable existing tests pass.

- [ ] **Step 5: Inspect the final diff and status**

Run: `git diff --check` and `git status --short`.

Expected: no whitespace errors; only intended implementation, test, dependency, and documentation files are modified. Do not alter unrelated user files such as `data/AUTOSAR_CP_SWS_OS.pdf` or `data/usage.md`.
