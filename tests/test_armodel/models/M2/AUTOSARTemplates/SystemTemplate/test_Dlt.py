import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import DltDefaultTraceStateEnum


class TestDltDefaultTraceStateEnum:
    """Tests for DltDefaultTraceStateEnum (R23-11 SystemTemplate, Table 6.337, p.723)."""

    def test_instantiation(self):
        enum = DltDefaultTraceStateEnum()
        assert isinstance(enum, AREnum)
        assert enum.getValue() == ""

    def test_members(self):
        enum = DltDefaultTraceStateEnum()
        values = enum.getEnumValues()
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED == "DefaultTraceStateDisabled"
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED == "DefaultTraceStateEnabled"
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED in values
        assert DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED in values
        assert len(values) == 2

    def test_enum_values_displayed_order(self):
        enum = DltDefaultTraceStateEnum()
        assert enum.getEnumValues() == (
            DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED,
            DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED,
        )

    def test_class_docstring_note(self):
        assert inspect.cleandoc(DltDefaultTraceStateEnum.__doc__) == "This enumeration defines the supported values for the Dlt default trace state."

    def test_set_value_round_trip(self):
        enum = DltDefaultTraceStateEnum()
        assert enum == enum.setValue(DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED)
        assert enum.getValue() == "DefaultTraceStateEnabled"
