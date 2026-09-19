# OS Application and Task Collector Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert parsed ECUC OS configuration objects into actual AUTOSAR OS model classes and export them through a new `os-config-export` CLI command as XLSX or YAML.

**Architecture:** Keep the generic ARXML parser responsible for ECUC model construction. Add standalone no-argument OS model classes under `armodel.data_models.os` (the repo's existing home for standalone models, e.g. `sw_connector.py`), with M2-style getters, setters, and adders but no M2 inheritance or parent field. Add `OsEcucParser` under `armodel.parser` as the dedicated ECUC-to-OS loader; it reads ECUC objects and populates `OsOs`, `OsApplication`, and `OsTask`. Register a new `os-config-export` console script with `--format {xlsx,yaml}`, defaulting to `xlsx`, following the existing CLI house pattern (verbose/warning flags, logging setup, INPUT/OUTPUT positionals).

**Tech Stack:** Python 3.8-compatible typing and project-style model classes, existing `ARXMLParser` and `AUTOSAR` singleton, `argparse`, `openpyxl`, lazy-imported `pyyaml` (already present via the `pytest` extra; never a hard runtime import).

## Global Constraints

- Python >= 3.8; use `typing.Optional` and `typing.List`, never `T | None` or `list[...]`.
- Use exact AUTOSAR Chapter 10 names for semantic fields and the existing `Identifiable` short-name identity convention, exposed as `name` with `getName()`/`setName()` (accepted deviation from the M2 `shortName` accessor — see the design spec, "Accepted Deviations").
- Semantic field names keep the verbatim PascalCase ECUC parameter names (e.g. `OsTaskPriority`); this is a recorded, accepted deviation from the repo's camelCase model-field convention.
- Strict mapping: collect every standard Chapter 10 parameter (including `OsStacksize`, which IS a standard `OsTask` parameter in SWS OS); ignore only genuinely vendor-specific parameters.
- `OsEcucParser` reads ECUC model objects first; exporters must not inspect ECUC model internals.
- Store `Os_ECUC.arxml` under `tests/integration_tests/test_files` as the committed OS integration fixture. It is created by Task 0. Because `tests/integration_tests/config.yaml` scans `test_files/` by default, committing it extends the integration round-trip corpus — Task 0 verifies the suite still passes with the file present.
- Preserve existing parser behavior and do not modify generic ECUC parser logic unless a concrete adapter gap is proven.
- Use `apply_patch` for manual edits.
- Run `npm run lint` and relevant tests; exclude `build/` from lint.
- Run `npm run black` for changed Python files.
- Do NOT re-sort imports in `src/armodel/models/**`, `parser/arxml_parser.py`, or `writer/arxml_writer.py` (per `pyproject.toml` per-file-ignores); new files outside those ignore rules (e.g. `src/armodel/parser/os_ecuc_parser.py`, `src/armodel/report/os_export.py`) must be ruff I001-clean.

---

### Task 0: Create the OS ECUC Integration Fixture

**Files:**
- Create: `tests/integration_tests/test_files/Os_ECUC.arxml`

**Interfaces:**
- A single legacy-form ECUC ARXML file containing one `ECUC-MODULE-CONFIGURATION` (definition path ends in `/Os`) with one root `OsOs` container holding exactly one `OsApplication` container (`OsApplication_QM`) and four `OsTask` containers (`Init_Task`, `Rte_Time_Task`, `Rte_Event_Task`, `SchMDiagStateTask_20ms`).
- Application task membership expressed via `OsAppTaskRef` reference values; task access expressed via `OsTaskAccessingApplication` reference values.
- Task containers carry standard parameters (`OsTaskActivation`, `OsTaskPeriod`, `OsTaskPriority`, `OsTaskSchedule`, `OsStacksize`), nested `OsTaskAutostart` (`OsTaskAppModeRef`), `OsTaskTimingProtection` (`OsTaskAllInterruptLockBudget`, `OsTaskExecutionBudget`, `OsTaskOsInterruptLockBudget`, `OsTaskTimeFrame`), and `OsTaskResourceLock` (`OsTaskResourceLockBudget`, `OsTaskResourceLockResourceRef`) sub-containers, plus one deliberately vendor-specific parameter (e.g. `OsVendorSpecificParam`) that the strict converter must ignore.
- Reference `VALUE-REF` paths use the normalized form `/Os/<OsOs container short name>/<task short name>` so the converter's path index resolves them.

- [ ] **Step 1: Author `Os_ECUC.arxml`**

Use the legacy ECUC element names (`MODULE-CONFIGURATION`, `CONTAINERS`, `CONTAINER`, `PARAMETER-VALUES`, `REFERENCE-VALUES`, `SUB-CONTAINERS`) under the standard `AUTOSAR` / `AR-PACKAGES` / `AR-PACKAGE` envelope with the `http://autosar.org/schema/r4.0` namespace. The task names, application name, and membership asserted by later tasks MUST match this file exactly; author them together.

- [ ] **Step 2: Verify the generic parser accepts it**

Run: `uv run python -c "from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR; from armodel.parser import ARXMLParser; doc = AUTOSAR.getInstance(); doc.clear(); doc.setARRelease('R23-11'); ARXMLParser().load('tests/integration_tests/test_files/Os_ECUC.arxml', doc); print('ok')"`

Expected: prints `ok` without exceptions.

- [ ] **Step 3: Verify the integration round-trip still passes with the fixture committed**

Run: `uv run python scripts/run_tests.py --integration --no-coverage`

Expected: PASS. The new file joins the scanned corpus (`test_files/` is a default directory in `tests/integration_tests/config.yaml`); it must round-trip parse → write → re-parse losslessly. If (and only if) a genuine generic-parser ECUC gap makes lossless round-tripping impossible, add the file to `exclude_patterns` in `tests/integration_tests/config.yaml` with a comment naming the gap, and record it as a deviation — do not weaken the generic parser in this plan.

- [ ] **Step 4: Commit the fixture**

```bash
git add tests/integration_tests/test_files/Os_ECUC.arxml
git commit -m "test: add OS ECUC integration fixture"
```

### Task 1: Add OS Semantic Model Classes

**Files:**
- Create: `src/armodel/data_models/os/__init__.py`
- Create: `src/armodel/data_models/os/models.py`
- Create: `tests/test_armodel/data_models/os/__init__.py`
- Create: `tests/test_armodel/data_models/os/test_models.py`

**Interfaces:**
- Produces standalone `OsApplication`, `OsTask`, and `OsOs` classes with M2-style accessors, no M2 inheritance, no parent field, no-argument constructors, and a `name` identity member.
- `OsApplication.OsAppTaskRef` contains `List[OsTask]`.
- `OsApplication.OsRestartTask` contains `Optional[OsTask]`.
- `OsTask.OsTaskAccessingApplication` contains `List[OsApplication]`.
- `OsOs.OsApplication` and `OsOs.OsTask` contain the top-level semantic object lists.

- [ ] **Step 1: Write failing model-class shape tests**

```python
from armodel.data_models.os import OsApplication, OsOs, OsTask


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
    assert hasattr(task, "OsStacksize")


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

Run: `uv run pytest tests/test_armodel/data_models/os/test_models.py -v`

Expected: FAIL because `armodel.data_models.os` and the model classes do not yet exist.

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
    OsStacksize: Optional[int]
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

`OsStacksize` is a standard SWS OS `OsTask` parameter and is collected like any other Chapter 10 field. Use `ApplicationState = "APPLICATION_ACCESSIBLE"` by default. Do not include separate `OsTaskAutostart`, `OsTaskTimingProtection`, or `OsTaskResourceLock` classes.

- [ ] **Step 4: Run the focused tests and verify they pass**

Run: `uv run pytest tests/test_armodel/data_models/os/test_models.py -v`

Expected: PASS.

- [ ] **Step 5: Verify the model test-parity script is still green**

Run: `uv run python scripts/check_model_test_parity.py`

Expected: OK. (`src/armodel/data_models` is outside the parity scan root `src/armodel/models`, so the new package introduces no file-presence or class-coverage requirements; the check confirms nothing existing regressed.)

- [ ] **Step 6: Commit the datamodel task**

```bash
git add src/armodel/data_models/os tests/test_armodel/data_models/os
git commit -m "feat: add AUTOSAR OS semantic model classes"
```

### Task 2: Convert ECUC Objects to OS Model Classes

**Files:**
- Create: `src/armodel/parser/os_ecuc_parser.py`
- Modify: `src/armodel/parser/__init__.py`
- Create: `tests/test_armodel/data_models/os/test_converter.py`

**Interfaces:**
- Produces `OsEcucParser.load(path, document=None, warning=False) -> OsOs` and `OsEcucParser.parseEcuc(document, warning=False) -> OsOs`.
- `load(path)` sets the AR release to `R23-11`, invokes the existing `ARXMLParser` to construct ECUC model objects, and delegates to `parseEcuc`.
- `warning=True` downgrades unresolved standard references from conversion errors to logged warnings (the CLI `-w/--warning` flag feeds this), matching the `-w` convention of the existing CLIs.
- `parseEcuc(document)` consumes ECUC model objects and populates standalone OS model objects.
- `OsOs.from_file(path)` and `OsOs.from_ecuc(document)` are optional convenience delegates to `OsEcucParser`; the parser class is the primary loader API.

- [ ] **Step 1: Write a failing conversion test using the demo file**

```python
from pathlib import Path

from armodel.data_models.os import OsOs
from armodel.parser import OsEcucParser


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

Run: `uv run pytest tests/test_armodel/data_models/os/test_converter.py::test_from_file_converts_demo_os_configuration -v`

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
task.setOsStacksize(read_int("OsStacksize"))
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

Ignore genuinely vendor-specific parameters (the fixture's `OsVendorSpecificParam`) and any other non-standard parameter; `OsStacksize` is standard and collected.

- [ ] **Step 5: Implement application conversion and relationship resolution**

Create every `OsApplication`, populate its Chapter 10 fields, then resolve `OsAppTaskRef` and `OsRestartTask` to the existing task instances. Resolve each task's `OsTaskAccessingApplication` to existing application instances. Deduplicate object references while preserving first-seen order.

Raise a specific conversion error for a standard reference whose target cannot be found (downgraded to a logged warning when `warning=True`). Do not infer relationships from short-name prefixes or substrings.

- [ ] **Step 6: Run converter tests and add missing-value/reference tests**

Add tests for absent optional fields, repeated references, the ignored vendor parameter, `OsStacksize` collection, malformed scalar values, and unresolved standard references (both error and `warning=True` modes).

Run: `uv run pytest tests/test_armodel/data_models/os/test_converter.py -v`

Expected: PASS.

- [ ] **Step 7: Run the full OS test package**

Run: `uv run pytest tests/test_armodel/data_models/os -v`

Expected: PASS.

- [ ] **Step 8: Commit the converter task**

```bash
git add src/armodel/parser/os_ecuc_parser.py src/armodel/parser/__init__.py tests/test_armodel/data_models/os/test_converter.py
git commit -m "feat: convert ECUC OS objects to semantic model classes"
```

### Task 3: Add YAML and XLSX Exporters

**Files:**
- Create: `src/armodel/report/os_export.py`
- Modify: `src/armodel/report/__init__.py`
- Create: `tests/test_armodel/report/__init__.py`
- Create: `tests/test_armodel/report/test_os_export.py`

**Interfaces:**
- Consumes only `OsOs` model objects.
- Produces `write_yaml(os_os: OsOs, output_path: Path) -> None` and `write_xlsx(os_os: OsOs, output_path: Path) -> None`.
- The exporters live under `armodel.report` (the repo's home for report/export writers, e.g. `ExcelReporter`, `ConnectorXlsReport`), not under `models`, and are exported through the package `__init__.py` exactly like `ConnectorXlsReport` (`from armodel.report import write_xlsx, write_yaml`).
- `pyyaml` is imported lazily inside `write_yaml`; when the module is missing, raise `ImportError` with the message `pyyaml is required for YAML export: pip install pyyaml`. Do not add pyyaml to the runtime dependencies or touch `pyproject.toml` (it is already in the `pytest` extra for tests).

- [ ] **Step 1: Write failing exporter tests**

```python
from pathlib import Path

import pytest
import yaml
from openpyxl import load_workbook

from armodel.data_models.os import OsApplication, OsOs, OsTask
from armodel.report import write_xlsx, write_yaml


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


def test_write_yaml_without_pyyaml_raises_actionable_error(tmp_path: Path, monkeypatch):
    import builtins

    from armodel.report import write_yaml

    real_import = builtins.__import__

    def blocked_import(name, *args, **kwargs):
        if name == "yaml":
            raise ImportError("No module named 'yaml'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", blocked_import)
    os_os = OsOs().setName("Os")
    with pytest.raises(ImportError, match="pip install pyyaml"):
        write_yaml(os_os, tmp_path / "os.yaml")
```

- [ ] **Step 2: Run exporter tests and verify they fail**

Run: `uv run pytest tests/test_armodel/report/test_os_export.py -v`

Expected: FAIL because exporter functions are not implemented.

- [ ] **Step 3: Implement recursive model serialization for YAML**

Use explicit serializer helpers over the project-style model getters, or a shared model-to-dictionary helper limited to the new OS classes. Serialize exact field names. Convert object relationships to `getName()` values to avoid recursive object graphs. Keep reference strings unchanged. Use `yaml.safe_dump(..., sort_keys=False)` with the lazy `pyyaml` import described in the interfaces.

Then export the module through the package exactly like `ConnectorXlsReport`: in `src/armodel/report/__init__.py` add `from armodel.report.os_export import write_xlsx, write_yaml` and extend `__all__` accordingly.

- [ ] **Step 4: Implement XLSX worksheets**

Use `openpyxl` and the existing `ExcelReporter` conventions. Create worksheets `OsApplication` and `OsTask`; write exact field names in row 1 and one row per object. Serialize lists as stable delimiter-joined values and object relationships as `name` delimiter-joined values. Do not create separate nested-object worksheets because those fields are flattened into `OsTask`.

- [ ] **Step 5: Run exporter tests and verify they pass**

Run: `uv run pytest tests/test_armodel/report/test_os_export.py -v`

Expected: PASS.

- [ ] **Step 6: Commit the exporter task**

```bash
git add src/armodel/report tests/test_armodel/report
git commit -m "feat: export semantic OS configuration"
```

### Task 4: Add the `os-config-export` CLI (house pattern)

**Files:**
- Create: `src/armodel/cli/os_config_export_cli.py`
- Create: `tests/test_armodel/cli/test_os_config_export_cli.py`
- Modify: `pyproject.toml` `[project.scripts]`

**Interfaces:**
- Console script: `os-config-export = armodel.cli.os_config_export_cli:main`.
- Command: `os-config-export [-v/--verbose] [-w/--warning] INPUT... OUTPUT [--format {xlsx,yaml}]`, default format `xlsx`.
- Follow the existing CLI house pattern exactly (see `connector2xlsx_cli.py` / `file_list_cli.py`): stdlib imports first, then `from armodel import __version__` with the version banner in `ap.description`, then package-level imports (`from armodel.parser import ...`, `from armodel.report import ...` — no deep-module report imports); argparse with `-v/--verbose` and `-w/--warning` store-true flags, positional `INPUT` (`nargs="+"`) and `OUTPUT`, the shared `[%(levelname)s] : %(message)s` logging format with a stderr `StreamHandler` plus a `FileHandler` writing `os_config_export.log` next to `OUTPUT` (removed first if it exists), file handler at DEBUG, stdout at INFO (DEBUG when `--verbose`), the work inside `try/except` that re-raises, and the `if __name__ == "__main__": main()` guard.
- `-w/--warning` is forwarded to `OsEcucParser.load(..., warning=True)` so unresolved standard references become logged warnings instead of conversion errors.

- [ ] **Step 1: Write failing CLI tests**

```python
import logging
from pathlib import Path

from openpyxl import load_workbook

from armodel.cli.os_config_export_cli import main


def test_cli_defaults_to_xlsx(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.xlsx"
    monkeypatch.setattr("sys.argv", ["os-config-export", "tests/integration_tests/test_files/Os_ECUC.arxml", str(output)])

    main()

    assert output.exists()
    assert "OsTask" in load_workbook(output).sheetnames
    assert (tmp_path / "os_config_export.log").exists()


def test_cli_supports_yaml(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.yaml"
    monkeypatch.setattr("sys.argv", ["os-config-export", "tests/integration_tests/test_files/Os_ECUC.arxml", str(output), "--format", "yaml"])

    main()

    assert output.exists()


def test_cli_warning_flag_downgrades_unresolved_references(monkeypatch, tmp_path: Path, caplog):
    output = tmp_path / "os.xlsx"
    monkeypatch.setattr("sys.argv", ["os-config-export", "-w", "tests/integration_tests/test_files/Os_ECUC.arxml", str(output)])

    main()

    assert output.exists()
```

(The warning-flag test requires a fixture variant with a dangling standard reference; author it as an in-memory ECUC document via `parseEcuc`, or extend the fixture only if the demo file itself must stay minimal. Keep the demo file assertable and put the dangling-reference case in the converter tests of Task 2 instead if simpler.)

- [ ] **Step 2: Run CLI tests and verify they fail**

Run: `uv run pytest tests/test_armodel/cli/test_os_config_export_cli.py -v`

Expected: FAIL because the module and console entry point are not implemented.

- [ ] **Step 3: Implement the CLI following the house pattern**

The module structure mirrors the other CLI tools (`file_list_cli.py`, `connector2xlsx_cli.py`): stdlib imports first, `from armodel import __version__` for the description banner, package-level imports (`from armodel.parser import ...`, `from armodel.report import ...` — no deep-module report imports), a single `main()`, the shared logging block, `try/except` re-raise, and the `__main__` guard:

```python
import argparse
import logging
import os.path
import sys

from armodel import __version__
from armodel.parser import OsEcucParser
from armodel.report import write_xlsx, write_yaml


def main():
    version = __version__

    ap = argparse.ArgumentParser()
    ap.description = "Export the semantic OS configuration (OsApplication, OsTask) from an ECUC ARXML file. <%s>" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("-w", "--warning", required=False, help="Skip unresolved reference errors and report them as warning messages", action="store_true")
    ap.add_argument("INPUT", help="The path of the ECUC OS configuration ARXML", nargs="+")
    ap.add_argument("OUTPUT", help="The path of the output file (xlsx or yaml)")
    ap.add_argument("--format", required=False, choices=["xlsx", "yaml"], default="xlsx", help="Export format (default: xlsx)")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter("[%(levelname)s] : %(message)s")

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, "os_config_export.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)

    else:
        stdout_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        os_os = OsEcucParser().load(args.INPUT[0], warning=args.warning)
        if args.format == "yaml":
            write_yaml(os_os, args.OUTPUT)
        else:
            write_xlsx(os_os, args.OUTPUT)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Register the console script**

Add to `[project.scripts]` in `pyproject.toml`:

```toml
os-config-export = "armodel.cli.os_config_export_cli:main"
```

- [ ] **Step 5: Run CLI tests and verify they pass**

Run: `uv run pytest tests/test_armodel/cli/test_os_config_export_cli.py -v`

Expected: PASS.

- [ ] **Step 6: Verify the installed command metadata**

Run: `uv run python -m pip install -e .` then `uv run os-config-export --help`.

Expected: help output includes `-v/--verbose`, `-w/--warning`, `--format {xlsx,yaml}` with xlsx shown as the default, and the positional `INPUT ... OUTPUT` usage — consistent with the other armodel CLI tools.

- [ ] **Step 7: Commit the CLI task**

```bash
git add src/armodel/cli/os_config_export_cli.py tests/test_armodel/cli/test_os_config_export_cli.py pyproject.toml
git commit -m "feat: add OS configuration export CLI"
```

### Task 5: Documentation and Quality Verification

**Files:**
- Modify: `docs/superpowers/specs/2026-09-19-os-application-task-collector-design.md` only if implementation details require a clarified contract.

- [ ] **Step 1: Run the complete focused test suite**

Run: `uv run pytest tests/test_armodel/data_models/os tests/test_armodel/report/test_os_export.py tests/test_armodel/cli/test_os_config_export_cli.py -v`

Expected: PASS.

- [ ] **Step 2: Run the demo CLI for both formats**

Run: `uv run os-config-export tests/integration_tests/test_files/Os_ECUC.arxml build/os_config.xlsx`

Run: `uv run os-config-export tests/integration_tests/test_files/Os_ECUC.arxml build/os_config.yaml --format yaml`

Expected: both files are created; the XLSX contains `OsApplication` and `OsTask` sheets; YAML contains the same semantic objects and exact field names; `os_config_export.log` is written next to each output.

- [ ] **Step 3: Run formatting and lint**

Run: `npm run black`

Run: `npm run lint`

Expected: both commands complete successfully. Do not auto-sort imports in the existing model/parser files.

- [ ] **Step 4: Run the repository test command**

Run: `uv run python scripts/check_model_test_parity.py`

Run: `uv run python scripts/run_tests.py --no-coverage`

Expected: parity script reports OK; all applicable existing tests pass — including the integration round-trip corpus with the new `Os_ECUC.arxml` fixture from Task 0.

- [ ] **Step 5: Inspect the final diff and status**

Run: `git diff --check` and `git status --short`.

Expected: no whitespace errors; only intended implementation, test, dependency, fixture, and documentation files are modified. Do not alter unrelated user files such as `data/AUTOSAR_CP_SWS_OS.pdf` or `data/usage.md`.
