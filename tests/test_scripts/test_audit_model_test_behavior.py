"""Tests for the model/test behavioral audit helpers."""

import ast
import importlib.util
from pathlib import Path

SCRIPT_PATH = Path(__file__).parents[2] / "scripts" / "audit_model_test_behavior.py"
SPEC = importlib.util.spec_from_file_location("audit_model_test_behavior", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

audit_class = MODULE.audit_class
normalized_methods = MODULE.normalized_methods


def test_normalized_methods_matches_project_test_naming():
    node = ast.parse("class TestFoo:\n    def test_get_value(self):\n        pass\n").body[0]

    assert normalized_methods(node) == {"getvalue"}


def test_audit_reports_missing_method_and_enum_checks():
    source = ast.parse(
        """
class ExampleEnum(AREnum):
    def __init__(self):
        super().__init__((self.FIRST,))

    FIRST = "FIRST"

    def getValue(self):
        return self.value
"""
    ).body[0]
    test = ast.parse(
        """
class TestExampleEnum:
    def test_initialization(self):
        ExampleEnum()
"""
    ).body[0]

    report = audit_class(source, [(None, test, "ExampleEnum")])
    codes = {issue["code"] for issue in report["issues"]}

    assert "HEURISTIC_METHOD_TOKEN_GAP" in codes
    assert "HEURISTIC_ENUM_API_GAP" in codes
    assert "HEURISTIC_INVALID_ENUM_GAP" in codes
