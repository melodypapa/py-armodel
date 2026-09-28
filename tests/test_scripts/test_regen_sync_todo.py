import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).parents[2] / "scripts" / "regen_sync_todo.py"
SPEC = importlib.util.spec_from_file_location("regen_sync_todo", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_parse_group_rows_rejects_a_class_queued_in_different_groups(tmp_path, monkeypatch):
    (tmp_path / "Group1.md").write_text("- [x] `SharedClass` — sync record\n", encoding="utf-8")
    (tmp_path / "Group2.md").write_text("- [ ] `SharedClass` — duplicate sync record\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "SYNC", tmp_path)
    monkeypatch.setattr(MODULE, "GROUPS", ["Group1", "Group2"])

    with pytest.raises(ValueError, match=r"SharedClass.*Group1\.md:1.*Group2\.md:1"):
        MODULE.parse_group_rows({}, {})


def test_parse_group_rows_rejects_repeated_class_rows_within_one_group(tmp_path, monkeypatch):
    (tmp_path / "Group1.md").write_text("- [x] `SharedClass` — first row\n- [ ] `SharedClass` — second row\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "SYNC", tmp_path)
    monkeypatch.setattr(MODULE, "GROUPS", ["Group1"])

    with pytest.raises(ValueError, match=r"SharedClass.*Group1\.md:1.*Group1\.md:2"):
        MODULE.parse_group_rows({}, {})


def test_resolve_row_normalizes_commit_id_to_git_abbreviation_length():
    full_commit = subprocess.run(["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
    expected = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", "--short=10", f"{full_commit}^{{commit}}"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    row = MODULE.resolve_row(
        "Group1",
        "SharedClass",
        "x",
        f"- [x] `SharedClass` — commit: {full_commit}",
        "",
        {"SharedClass"},
        {},
        {},
        {"SharedClass": {"Group1"}},
    )

    assert row["commit"] == expected
    assert len(row["commit"]) >= 10


def test_main_uses_utf8_for_all_sync_file_reads_and_writes(tmp_path, monkeypatch):
    source = tmp_path / "src"
    source.mkdir()
    (source / "example.py").write_text("# non-ASCII — source\n", encoding="utf-8")
    (tmp_path / "Group1.md").write_text("- [x] `SharedClass` — sync record\n", encoding="utf-8")
    (tmp_path / "SyncTodoIndex.md").write_text("existing — index\n", encoding="utf-8")
    (tmp_path / "sync-report.md").write_text("existing — report\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "SYNC", tmp_path)
    monkeypatch.setattr(MODULE, "SRC", source)
    monkeypatch.setattr(MODULE, "GROUPS", ["Group1"])
    monkeypatch.setattr(sys, "argv", [str(SCRIPT_PATH), "--write"])
    original_open = Path.open

    def require_utf8(path, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
        assert encoding == "utf-8", f"{path} opened without explicit UTF-8 encoding"
        return original_open(path, mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline)

    monkeypatch.setattr(Path, "open", require_utf8)

    assert MODULE.main() == 0
    assert "`SharedClass`" in (tmp_path / "SyncTodoIndex.md").read_text(encoding="utf-8")
    assert "`SharedClass`" in (tmp_path / "sync-report.md").read_text(encoding="utf-8")


def test_main_reports_cross_group_duplicate_before_writing_reports(tmp_path, monkeypatch, capsys):
    (tmp_path / "src").mkdir()
    (tmp_path / "Group1.md").write_text("- [x] `SharedClass` — sync record\n", encoding="utf-8")
    (tmp_path / "Group2.md").write_text("- [ ] `SharedClass` — duplicate sync record\n", encoding="utf-8")
    index = tmp_path / "SyncTodoIndex.md"
    report = tmp_path / "sync-report.md"
    index.write_text("existing index\n", encoding="utf-8")
    report.write_text("existing report\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "SYNC", tmp_path)
    monkeypatch.setattr(MODULE, "SRC", tmp_path / "src")
    monkeypatch.setattr(MODULE, "GROUPS", ["Group1", "Group2"])
    monkeypatch.setattr(sys, "argv", [str(SCRIPT_PATH), "--write"])

    result = MODULE.main()

    assert result == 1
    assert "SharedClass" in capsys.readouterr().err
    assert index.read_text() == "existing index\n"
    assert report.read_text() == "existing report\n"
