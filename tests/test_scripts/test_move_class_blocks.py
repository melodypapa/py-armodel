import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent.parent / "scripts" / "move_class_blocks.py"


def run_mover(source, target, *classes):
    return subprocess.run([sys.executable, str(SCRIPT), str(source), str(target), *classes], capture_output=True, text=True)


def test_moves_class_with_leading_comments(tmp_path):
    src = tmp_path / "src.py"
    src.write_text("import x\n\n\n# checklist for A\nclass A:\n    pass\n\n\n# checklist for B\nclass B:\n    pass\n")
    tgt = tmp_path / "tgt.py"
    tgt.write_text("class Z:\n    pass\n")

    result = run_mover(src, tgt, "A")

    assert result.returncode == 0, result.stderr
    assert "class A" not in src.read_text()
    assert "# checklist for A" not in src.read_text()
    assert "# checklist for B" in src.read_text()
    assert "class B" in src.read_text()
    assert "class A:" in tgt.read_text()
    assert "# checklist for A" in tgt.read_text()
    assert "class Z:" in tgt.read_text()


def test_missing_class_fails_with_message(tmp_path):
    src = tmp_path / "src.py"
    src.write_text("class A:\n    pass\n")
    tgt = tmp_path / "tgt.py"
    tgt.write_text("")

    result = run_mover(src, tgt, "Nope")

    assert result.returncode != 0
    assert "Nope" in result.stderr
    assert "class A" in src.read_text()
