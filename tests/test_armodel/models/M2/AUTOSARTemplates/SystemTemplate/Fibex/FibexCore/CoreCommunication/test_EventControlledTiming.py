import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    EventControlledTiming,
    TimeRangeType,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = (
    """Specification of a event driven sending behavior. The PDU is sent n (numberOfRepeat + 1) times separated by the repetitionPeriod. If numberOfRepeats = 0, then the Pdu is sent just once."""
)


class TestEventControlledTiming:
    """Test cases for EventControlledTiming (Table 6.66, p.409)."""

    def test_initialization_defaults(self):
        obj = EventControlledTiming()
        assert obj.getNumberOfRepetitions() is None
        assert obj.getRepetitionPeriod() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = EventControlledTiming()
        assert obj.setNumberOfRepetitions(4) is obj
        assert obj.getNumberOfRepetitions() == 4
        obj.setNumberOfRepetitions(None)
        assert obj.getNumberOfRepetitions() == 4
        item = TimeRangeType()
        assert obj.setRepetitionPeriod(item) is obj
        assert obj.getRepetitionPeriod() is item
        obj.setRepetitionPeriod(None)
        assert obj.getRepetitionPeriod() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EventControlledTiming.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = EventControlledTiming()
        assert (
            inspect.cleandoc(obj.getNumberOfRepetitions.__doc__) == "Defines the number of repetitions for the Direct/N-Times transmission mode and the event driven part of Mixed transmission mode."
        )
        assert (
            inspect.cleandoc(obj.setNumberOfRepetitions.__doc__).split("\n")[0]
            == "Defines the number of repetitions for the Direct/N-Times transmission mode and the event driven part of Mixed transmission mode."
        )
        assert (
            inspect.cleandoc(obj.getRepetitionPeriod.__doc__)
            == "The repetitionPeriod specifies the time in seconds that elapses before the pdu can be sent the next time (Minimum repeat gap between two pdus). The repetition Period is optional in case that no repetitions are configured."
        )
        assert (
            inspect.cleandoc(obj.setRepetitionPeriod.__doc__).split("\n")[0]
            == "The repetitionPeriod specifies the time in seconds that elapses before the pdu can be sent the next time (Minimum repeat gap between two pdus). The repetition Period is optional in case that no repetitions are configured."
        )
