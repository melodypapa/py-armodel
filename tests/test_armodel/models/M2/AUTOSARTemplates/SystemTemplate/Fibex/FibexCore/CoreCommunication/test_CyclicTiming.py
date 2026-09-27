import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    CyclicTiming,
    TimeRangeType,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """Specification of a cyclic sending behavior."""


class TestCyclicTiming:
    """Test cases for CyclicTiming (Table 6.65, p.408)."""

    def test_initialization_defaults(self):
        obj = CyclicTiming()
        assert obj.getTimeOffset() is None
        assert obj.getTimePeriod() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = CyclicTiming()
        item = TimeRangeType()
        assert obj.setTimeOffset(item) is obj
        assert obj.getTimeOffset() is item
        obj.setTimeOffset(None)
        assert obj.getTimeOffset() is item
        item = TimeRangeType()
        assert obj.setTimePeriod(item) is obj
        assert obj.getTimePeriod() is item
        obj.setTimePeriod(None)
        assert obj.getTimePeriod() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CyclicTiming.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = CyclicTiming()
        assert (
            inspect.cleandoc(obj.getTimeOffset.__doc__)
            == "This attribute specifies the time until first transmission of this I-PDU. This attribute defines the time between Com_ IpduGroupStart and the first transmission of the cyclic part of this transmission request for this I-PDU."
        )
        assert (
            inspect.cleandoc(obj.setTimeOffset.__doc__).split("\n")[0]
            == "This attribute specifies the time until first transmission of this I-PDU. This attribute defines the time between Com_ IpduGroupStart and the first transmission of the cyclic part of this transmission request for this I-PDU."
        )
        assert inspect.cleandoc(obj.getTimePeriod.__doc__) == "Period of the repetition of cyclic transmissions."
        assert inspect.cleandoc(obj.setTimePeriod.__doc__).split("\n")[0] == "Period of the repetition of cyclic transmissions."
