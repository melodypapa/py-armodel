import sys

from scripts.run_tests import run_command


def test_run_command_decodes_utf8_subprocess_output():
    success, output = run_command(
        [sys.executable, "-c", "import sys; sys.stdout.buffer.write('✓'.encode('utf-8'))"],
        "UTF-8 subprocess output",
    )

    assert success is True
    assert output.strip() == "✓"
