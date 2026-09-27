import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    DataFilter,
    TransmissionModeCondition,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """Possibility to attach a condition to each signal within an I-PDU. If at least one condition evaluates to true, TRANSMISSION MODE True shall be used for this I-Pdu. In all other cases, the TRANSMISSION MODE FALSE shall be used."""


class TestTransmissionModeCondition:
    """Test cases for TransmissionModeCondition (Table 6.60, p.393)."""

    def test_initialization_defaults(self):
        obj = TransmissionModeCondition()
        assert obj.getDataFilter() is None
        assert obj.getISignalInIPduRef() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = TransmissionModeCondition()
        item = DataFilter()
        assert obj.setDataFilter(item) is obj
        assert obj.getDataFilter() is item
        obj.setDataFilter(None)
        assert obj.getDataFilter() is item
        item = _ref()
        assert obj.setISignalInIPduRef(item) is obj
        assert obj.getISignalInIPduRef() is item
        obj.setISignalInIPduRef(None)
        assert obj.getISignalInIPduRef() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TransmissionModeCondition.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TransmissionModeCondition()
        assert inspect.cleandoc(obj.getDataFilter.__doc__) == "Possibilities to define conditions"
        assert inspect.cleandoc(obj.setDataFilter.__doc__).split("\n")[0] == "Possibilities to define conditions"
        assert inspect.cleandoc(obj.getISignalInIPduRef.__doc__) == "Reference to a signal to which a condition is attached."
        assert inspect.cleandoc(obj.setISignalInIPduRef.__doc__).split("\n")[0] == "Reference to a signal to which a condition is attached."
