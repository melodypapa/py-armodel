from pathlib import Path

import pytest
import yaml
from openpyxl import load_workbook

from armodel.data_models.ecuc import OsApplication, OsOs, OsTask
from armodel.report import OsConfigExporter, OsConfigXlsxExporter, OsConfigYamlExporter


def test_write_yaml_uses_semantic_names(tmp_path: Path):
    os_os = OsOs().setName("Os")
    os_os.addOsApplication(OsApplication().setName("App"))
    os_os.addOsTask(OsTask().setName("Task").setOsTaskPriority(5))
    output = tmp_path / "os.yaml"

    OsConfigYamlExporter().export(os_os, output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert data["OsApplication"][0]["name"] == "App"
    assert data["OsTask"][0]["OsTaskPriority"] == 5


def test_write_yaml_omits_none_and_empty_list_values(tmp_path: Path):
    os_os = OsOs().setName("Os")
    os_os.addOsTask(OsTask().setName("Task").setOsTaskPriority(5))
    output = tmp_path / "os.yaml"

    OsConfigYamlExporter().export(os_os, output)

    task = yaml.safe_load(output.read_text(encoding="utf-8"))["OsTask"][0]
    assert task == {"name": "Task", "OsTaskPriority": 5}


def test_os_config_export_rejects_unsupported_extension(tmp_path: Path):
    with pytest.raises(ValueError, match="Unsupported OS configuration export format"):
        OsConfigExporter().export(OsOs(), tmp_path / "os.json")


def test_write_xlsx_uses_expected_sheets(tmp_path: Path):
    output = tmp_path / "os.xlsx"
    os_os = OsOs().setName("Os")
    os_os.addOsApplication(OsApplication().setName("App"))
    os_os.addOsTask(OsTask().setName("Task"))
    OsConfigXlsxExporter().export(os_os, output)

    workbook = load_workbook(output)
    assert "OsApplication" in workbook.sheetnames
    assert "OsTask" in workbook.sheetnames


def test_write_yaml_without_pyyaml_raises_actionable_error(tmp_path: Path, monkeypatch):
    import builtins

    real_import = builtins.__import__

    def blocked_import(name, *args, **kwargs):
        if name == "yaml":
            raise ImportError("No module named 'yaml'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", blocked_import)
    os_os = OsOs().setName("Os")
    with pytest.raises(ImportError, match="pip install pyyaml"):
        OsConfigYamlExporter().export(os_os, tmp_path / "os.yaml")


def test_write_yaml_represents_relationships_by_name(tmp_path: Path):
    application = OsApplication().setName("App")
    task = OsTask().setName("Task")
    application.addOsAppTaskRef(task)
    task.addOsTaskAccessingApplication(application)
    application.setOsRestartTask(task)
    os_os = OsOs().setName("Os")
    os_os.addOsApplication(application)
    os_os.addOsTask(task)
    output = tmp_path / "os.yaml"

    OsConfigYamlExporter().export(os_os, output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert data["OsApplication"][0]["OsAppTaskRef"] == ["Task"]
    assert data["OsApplication"][0]["OsRestartTask"] == "Task"
    assert data["OsTask"][0]["OsTaskAccessingApplication"] == ["App"]


def test_write_yaml_keeps_flattened_and_reference_fields(tmp_path: Path):
    task = OsTask().setName("Task")
    task.addOsTaskAppModeRef("/Os/Os/OSDEFAULTAPPMODE")
    task.setOsTaskExecutionBudget(0.005)
    task.addOsTaskResourceLockBudget(0.001)
    task.addOsTaskResourceLockResourceRef("/Os/Os/Resource_Init")
    os_os = OsOs().setName("Os")
    os_os.addOsTask(task)

    output = tmp_path / "os.yaml"
    OsConfigYamlExporter().export(os_os, output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    exported = data["OsTask"][0]
    assert exported["OsTaskAppModeRef"] == ["/Os/Os/OSDEFAULTAPPMODE"]
    assert exported["OsTaskExecutionBudget"] == 0.005
    assert exported["OsTaskResourceLockBudget"] == [0.001]
    assert exported["OsTaskResourceLockResourceRef"] == ["/Os/Os/Resource_Init"]


def test_write_xlsx_rows_use_name_identity_and_exact_fields(tmp_path: Path):
    task = OsTask().setName("Task").setOsTaskPriority(5).setOsStacksize(1024)
    task.addOsTaskEventRef("/Os/Os/Event1")
    task.addOsTaskEventRef("/Os/Os/Event2")
    application = OsApplication().setName("App").setOsTrusted(False)
    application.addOsAppTaskRef(task)
    os_os = OsOs().setName("Os")
    os_os.addOsApplication(application)
    os_os.addOsTask(task)
    output = tmp_path / "os.xlsx"

    OsConfigXlsxExporter().export(os_os, output)

    workbook = load_workbook(output)
    task_sheet = workbook["OsTask"]
    headers = [cell.value for cell in task_sheet[1]]
    assert headers[0] == "name"
    assert "OsTaskPriority" in headers
    assert "OsStacksize" in headers
    rows = list(task_sheet.iter_rows(min_row=2, values_only=True))
    assert rows[0][headers.index("name")] == "Task"
    assert rows[0][headers.index("OsTaskPriority")] == 5
    event_cell = task_sheet.cell(row=2, column=headers.index("OsTaskEventRef") + 1)
    assert event_cell.value == "/Os/Os/Event1\n/Os/Os/Event2"
    assert event_cell.alignment.wrap_text is True

    application_sheet = workbook["OsApplication"]
    app_headers = [cell.value for cell in application_sheet[1]]
    app_rows = list(application_sheet.iter_rows(min_row=2, values_only=True))
    assert app_rows[0][app_headers.index("name")] == "App"
    assert app_rows[0][app_headers.index("OsTrusted")] is False
    assert app_rows[0][app_headers.index("OsAppTaskRef")] == "Task"
