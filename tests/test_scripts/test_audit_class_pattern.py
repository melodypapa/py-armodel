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
        assert any(lvl == "WARN" and code == "PATTERN" and "Rule 0028" in msg for lvl, code, msg in report.rows)

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

    def test_silent_for_numeric_ar_type_class_in_base_map(self):
        node = _class_node("class Numerical(ARType):\n" '    """docstring\n' "\n" "    Tags: xml.xsd.pattern=[0-9]+\n" '    """\n' "\n" "    def __init__(self):\n" "        super().__init__()\n")
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")

    def test_warns_when_pattern_attr_is_none(self):
        node = _class_node(
            "class Foo(ARLiteral):\n"
            '    """docstring\n'
            "\n"
            "    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n"
            '    """\n'
            "\n"
            "    PATTERN = None\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")

    def test_silent_when_attr_declared_as_ann_assign(self):
        node = _class_node(
            "class Foo(ARLiteral):\n"
            '    """docstring\n'
            "\n"
            "    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n"
            '    """\n'
            "\n"
            '    PATTERN: Optional[str] = r"[A-Z][a-zA-Z0-9_]*"\n'
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")

    def test_warns_when_bare_annotation_without_value(self):
        node = _class_node(
            "class Foo(ARLiteral):\n"
            '    """docstring\n'
            "\n"
            "    Tags: xml.xsd.pattern=[A-Z][a-zA-Z0-9_]*\n"
            '    """\n'
            "\n"
            "    PATTERN: str\n"
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")

    def test_limit_is_exempt(self):
        node = _class_node(
            "class Limit(ARLiteral):\n"
            '    """docstring\n'
            "\n"
            "    Tags: xml.xsd.pattern=INF|-INF|NaN\n"
            '    """\n'
            "\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
        )
        report = Report()
        check_pattern(report, node)
        assert not any("Rule 0028" in msg for lvl, _code, msg in report.rows if lvl == "WARN")
