import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPdu,
    J1939DcmIPdu,
    Pdu,
)

CLASS_NOTE = "Represents the IPdus handled by J1939Dcm. Tags: atp.recommendedPackage=Pdus"
CLASS_CONSTRAINTS = ("[constr_3096] Allowed values for diagnosticMessageType: The allowed values of diagnosticMessageType range from 1..57.",)
NOTES = {
    "diagnosticMessageType": "This attribute is used to identify the actual DMx message, e.g 1 means DM01, etc.",
}


class TestJ1939DcmIPdu:
    """Test cases for J1939DcmIPdu (Table 6.24, p.344)."""

    def test_inheritance(self):
        assert issubclass(J1939DcmIPdu, IPdu)
        assert issubclass(J1939DcmIPdu, Pdu)

    def test_concrete_instantiation(self):
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")
        assert pdu.getShortName() == "J1939DcmIPdu1"

    def test_initialization_defaults(self):
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")
        assert pdu.getDiagnosticMessageType() is None
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getContainedIPduProps() is None

    def test_get_set_diagnostic_message_type(self):
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")

        value = PositiveInteger().setValue("1")
        assert pdu.setDiagnosticMessageType(value) is pdu
        assert pdu.getDiagnosticMessageType() is value
        assert pdu.getDiagnosticMessageType().getValue() == 1
        pdu.setDiagnosticMessageType(None)
        assert pdu.getDiagnosticMessageType() is value

    def test_annotation_pins(self):
        getter_hints = typing.get_type_hints(J1939DcmIPdu.getDiagnosticMessageType)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(J1939DcmIPdu.setDiagnosticMessageType)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is J1939DcmIPdu

    def test_class_docstring_note(self):
        assert inspect.cleandoc(J1939DcmIPdu.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")
        getter = getattr(pdu, "getDiagnosticMessageType")
        setter = getattr(pdu, "setDiagnosticMessageType")
        assert inspect.cleandoc(getter.__doc__) == NOTES["diagnosticMessageType"]
        assert inspect.cleandoc(setter.__doc__).split("\n")[0] == NOTES["diagnosticMessageType"]

    def test_init_has_no_docstring(self):
        assert J1939DcmIPdu.__init__.__doc__ is None
