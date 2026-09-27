import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    TimeRangeType,
    TimeRangeTypeTolerance,
    TimeValue,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """The timeRange can be specified with the value attribute. Optionally a tolerance can be defined."""


class TestTimeRangeType:
    """Test cases for TimeRangeType (Table 6.67, p.413)."""

    def test_initialization_defaults(self):
        obj = TimeRangeType()
        assert obj.getTolerance() is None
        assert obj.getValue() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = TimeRangeType()
        item = TimeRangeTypeTolerance()
        assert obj.setTolerance(item) is obj
        assert obj.getTolerance() is item
        obj.setTolerance(None)
        assert obj.getTolerance() is item
        item = TimeValue()
        assert obj.setValue(item) is obj
        assert obj.getValue() is item
        obj.setValue(None)
        assert obj.getValue() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeRangeType.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TimeRangeType()
        assert inspect.cleandoc(obj.getTolerance.__doc__) == "Optional specification of a tolerance."
        assert inspect.cleandoc(obj.setTolerance.__doc__).split("\n")[0] == "Optional specification of a tolerance."
        assert inspect.cleandoc(obj.getValue.__doc__) == "Average value of a date (in seconds)"
        assert inspect.cleandoc(obj.setValue.__doc__).split("\n")[0] == "Average value of a date (in seconds)"
