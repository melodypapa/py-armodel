"""Tests for the sync-autosar-class audit `check_pattern` check (Rule 0028)."""

import ast
import importlib.util
from pathlib import Path

SCRIPT_PATH = Path(__file__).parents[2] / ".agents" / "skills" / "sync-autosar-class" / "audit_class.py"
SPEC = importlib.util.spec_from_file_location("audit_class", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

Report = MODULE.Report
check_pattern = MODULE.check_pattern


def _class_node(source):
    return ast.parse(source).body[0]


class TestCheckPattern:
    def test_warns_when_docstring_has_pattern_but_no_attr(self):
        node = _class_node(
            "class Foo(ARLiteral):\n" '    """docstring\n' "\n" "    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n" '    """\n' "\n" "    def __init__(self):\n" "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert report.failed is False
        assert any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")

    def test_silent_when_attr_declared(self):
        node = _class_node(
            "class Foo(ARLiteral):\n"
            '    """docstring\n'
            "\n"
            "    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n"
            '    """\n'
            "\n"
            '    PATTERN = r"[A-Z][a-zA-Z0-9_]*"\n'
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")

    def test_silent_when_no_pattern_tag(self):
        node = _class_node(
            "class Foo(ARLiteral):\n" '    """docstring\n' "\n" "    Tags: xml.xsd.customType=NMTOKEN-STRING\n" '    """\n' "\n" "    def __init__(self):\n" "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")
