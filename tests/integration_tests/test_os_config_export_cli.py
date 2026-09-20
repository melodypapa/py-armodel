from pathlib import Path

import yaml
from openpyxl import load_workbook

from armodel.cli.os_config_export_cli import main

OS_ECUC_FILE = Path(__file__).parent / "test_files" / "Os_ECUC.arxml"
EXPECTED_YAML_FILE = Path(__file__).parent / "test_files" / "Os_ECUC.yaml"

APPLICATION_FIELDS = {
    "name",
    "OsTrusted",
    "OsAppAlarmRef",
    "OsAppCounterRef",
    "OsAppTaskRef",
    "OsAppStartupHook",
    "OsAppErrorHook",
    "OsAppShutdownHook",
    "ApplicationState",
}


def test_os_config_export_cli_exports_real_os_ecuc_to_xlsx(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.xlsx"
    monkeypatch.setattr("sys.argv", ["os-ecuc-export", str(OS_ECUC_FILE), str(output)])

    main()

    workbook = load_workbook(output)
    assert workbook.sheetnames == ["OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"]
    assert workbook["OsApplication"]["A2"].value == "OsApplication_QM"
    assert workbook["OsTask"]["A2"].value == "Init_Task"
    alarm_headers = [cell.value for cell in workbook["OsAlarm"][1]]
    alarm_names = [row[0] for row in workbook["OsAlarm"].iter_rows(min_row=2, values_only=True)]
    assert alarm_names == ["AlarmSetRteShutdownEvent", "AlarmIncrementRteCounter"]
    assert "OsAlarmCounterRef" in alarm_headers
    assert workbook["OsIsr"]["A2"].value == "CanIsr"
    assert workbook["OsScheduleTable"]["A2"].value == "SystemScheduleTable"
    assert (tmp_path / "os_ecuc_export.log").exists()


def test_os_config_export_cli_exports_real_os_ecuc_to_yaml(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.yaml"
    monkeypatch.setattr("sys.argv", ["os-ecuc-export", str(OS_ECUC_FILE), str(output)])

    main()

    content = output.read_text(encoding="utf-8")
    assert "name: OsApplication_QM" in content
    assert "name: Init_Task" in content
    assert (tmp_path / "os_ecuc_export.log").exists()


def test_os_config_export_cli_matches_complete_yaml_fixture(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.yaml"
    monkeypatch.setattr("sys.argv", ["os-ecuc-export", str(OS_ECUC_FILE), str(output)])

    main()

    generated = yaml.safe_load(output.read_text(encoding="utf-8"))
    expected = yaml.safe_load(EXPECTED_YAML_FILE.read_text(encoding="utf-8"))

    assert generated == expected
    assert set(generated) == {"OsApplication", "OsTask", "OsAlarm", "OsIsr", "OsScheduleTable"}
    assert generated["OsApplication"]
    assert generated["OsTask"]
    assert generated["OsAlarm"]
    assert generated["OsIsr"]
    assert generated["OsScheduleTable"]
    assert all(set(application) == APPLICATION_FIELDS for application in generated["OsApplication"])
    assert all(value is not None and value != [] for task in generated["OsTask"] for value in task.values())
    assert [alarm["name"] for alarm in generated["OsAlarm"]] == ["AlarmSetRteShutdownEvent", "AlarmIncrementRteCounter"]
    assert generated["OsIsr"][0]["name"] == "CanIsr"
    assert generated["OsIsr"][0]["OsIsrCategory"] == "CATEGORY_2"
    assert [point["OsScheduleTblExpPointOffset"] for point in generated["OsScheduleTable"][0]["OsScheduleTableExpiryPoint"]] == [2, 5]


def test_os_config_export_cli_4_4_matches_existing_yaml_fixture(monkeypatch, tmp_path: Path):
    output = tmp_path / "os-4.4.0.yaml"
    input_file = OS_ECUC_FILE.with_name("Os_ECUC_4.4.0.arxml")
    monkeypatch.setattr("sys.argv", ["os-ecuc-export", str(input_file), str(output)])

    main()

    generated = yaml.safe_load(output.read_text(encoding="utf-8"))
    expected = yaml.safe_load(EXPECTED_YAML_FILE.read_text(encoding="utf-8"))

    assert generated["OsApplication"] == expected["OsApplication"]
    assert sorted(generated["OsTask"], key=lambda task: task["name"]) == sorted(expected["OsTask"], key=lambda task: task["name"])
