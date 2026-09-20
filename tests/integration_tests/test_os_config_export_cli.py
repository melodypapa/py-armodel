from pathlib import Path

from openpyxl import load_workbook

from armodel.cli.os_config_export_cli import main

OS_ECUC_FILE = Path(__file__).parent / "test_files" / "Os_ECUC.arxml"


def test_os_config_export_cli_exports_real_os_ecuc_to_xlsx(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.xlsx"
    monkeypatch.setattr("sys.argv", ["os-config-export", str(OS_ECUC_FILE), str(output)])

    main()

    workbook = load_workbook(output)
    assert workbook.sheetnames == ["OsApplication", "OsTask"]
    assert workbook["OsApplication"]["A2"].value == "OsApplication_QM"
    assert workbook["OsTask"]["A2"].value == "Init_Task"
    assert (tmp_path / "os_config_export.log").exists()


def test_os_config_export_cli_exports_real_os_ecuc_to_yaml(monkeypatch, tmp_path: Path):
    output = tmp_path / "os.yaml"
    monkeypatch.setattr("sys.argv", ["os-config-export", str(OS_ECUC_FILE), str(output), "--format", "yaml"])

    main()

    content = output.read_text(encoding="utf-8")
    assert "name: OsApplication_QM" in content
    assert "name: Init_Task" in content
    assert (tmp_path / "os_config_export.log").exists()
