import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    CyclicTiming,
    EventControlledTiming,
    TransmissionModeTiming,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """If the COM Transmission Mode is false the timing is aggregated by the TransmissionModeTiming element in the role of transmissionModeFalseTiming. If the COM Transmission Mode is true the timing is aggregated by the TransmissionModeTiming element in the role of transmissionModeTrueTiming. COM supports the following Transmission Modes: • Periodic (Cyclic Timing) • Direct /n-times (EventControlledTiming) • Mixed (Cyclic and EventControlledTiming are assigned)"""


class TestTransmissionModeTiming:
    """Test cases for TransmissionModeTiming (Table 6.62, p.394)."""

    def test_initialization_defaults(self):
        obj = TransmissionModeTiming()
        assert obj.getCyclicTiming() is None
        assert obj.getEventControlledTiming() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = TransmissionModeTiming()
        item = CyclicTiming()
        assert obj.setCyclicTiming(item) is obj
        assert obj.getCyclicTiming() is item
        obj.setCyclicTiming(None)
        assert obj.getCyclicTiming() is item
        item = EventControlledTiming()
        assert obj.setEventControlledTiming(item) is obj
        assert obj.getEventControlledTiming() is item
        obj.setEventControlledTiming(None)
        assert obj.getEventControlledTiming() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TransmissionModeTiming.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TransmissionModeTiming()
        assert inspect.cleandoc(obj.getCyclicTiming.__doc__) == "Periodic Transmission Mode."
        assert inspect.cleandoc(obj.setCyclicTiming.__doc__).split("\n")[0] == "Periodic Transmission Mode."
        assert inspect.cleandoc(obj.getEventControlledTiming.__doc__) == "Direct Transmission Mode."
        assert inspect.cleandoc(obj.setEventControlledTiming.__doc__).split("\n")[0] == "Direct Transmission Mode."
