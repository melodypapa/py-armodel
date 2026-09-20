from pathlib import Path

import pytest

from armodel.cli.os_config_export_cli import main


def test_cli_rejects_output_equal_to_input(monkeypatch, tmp_path: Path):
    input_file = tmp_path / "input.arxml"
    input_file.write_text("dummy")
    monkeypatch.setattr("sys.argv", ["os-config-export", str(input_file), str(input_file)])

    with pytest.raises(ValueError, match="must not overwrite the input file"):
        main()
