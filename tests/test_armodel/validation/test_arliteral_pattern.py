import logging

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.validation import PrimitivePatternError, warning_mode


class _DummyLiteral(ARLiteral):
    PATTERN = r"[A-Z][a-zA-Z0-9_]*"


class _UnconstrainedLiteral(ARLiteral):
    pass


class TestCheckValue:
    def test_valid_value_accepted(self):
        literal = _DummyLiteral()
        literal.value = "Valid_Name2"
        assert literal.value == "Valid_Name2"

    def test_invalid_value_raises_by_default(self):
        with pytest.raises(PrimitivePatternError) as exc_info:
            _DummyLiteral().value = "9bad"
        assert exc_info.value.class_name == "_DummyLiteral"
        assert exc_info.value.value == "9bad"
        assert exc_info.value.pattern == r"[A-Z][a-zA-Z0-9_]*"

    def test_warning_mode_logs_and_keeps_value(self, caplog):
        literal = _DummyLiteral()
        with warning_mode(True, "test.arxml"), caplog.at_level(logging.WARNING, logger="armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes"):
            literal.value = "9bad"
        assert literal.value == "9bad"
        assert any("9bad" in record.message and "test.arxml" in record.message for record in caplog.records)

    def test_none_pattern_passthrough(self):
        literal = _UnconstrainedLiteral()
        literal.value = "anything ! goes"
        assert literal.value == "anything ! goes"

    def test_empty_string_passthrough(self):
        literal = _DummyLiteral()
        literal.value = ""
        assert literal.value == ""

    def test_nonempty_string_not_a_str_type_still_rejected(self):
        with pytest.raises(ValueError) as exc_info:
            _DummyLiteral().value = 123
        assert "Unsupported Type" in str(exc_info.value)

    def test_set_value_flows_through_check(self):
        literal = _DummyLiteral()
        with pytest.raises(PrimitivePatternError):
            literal.setValue("bad")
        literal.setValue("Good")
        assert literal.getValue() == "Good"

    def test_pattern_cache_reuse(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import _PATTERN_CACHE

        _DummyLiteral().value = "A"
        assert r"[A-Z][a-zA-Z0-9_]*" in _PATTERN_CACHE
