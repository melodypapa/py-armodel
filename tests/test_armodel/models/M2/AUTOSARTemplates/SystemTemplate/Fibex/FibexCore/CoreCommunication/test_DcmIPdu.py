import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagPduType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DcmIPdu,
    IPdu,
    Pdu,
)

CLASS_NOTE = "Represents the IPdus handled by Dcm. Tags: atp.recommendedPackage=Pdus"
CLASS_CONSTRAINTS = ("[constr_9194] Existence of DcmIPdu.diagPduType: For each DcmIPdu, the attribute diagPduType shall exist at the time when the System Description is complete.",)
NOTES = {
    "diagPduType": "Attribute is used to distinguish a request from a response.",
}


class TestDcmIPdu:
    """Test cases for DcmIPdu (Table 6.22, p.343)."""

    def test_inheritance(self):
        assert issubclass(DcmIPdu, IPdu)
        assert issubclass(DcmIPdu, Pdu)

    def test_concrete_instantiation(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        assert pdu.getShortName() == "DcmIPdu1"

    def test_initialization_defaults(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        assert pdu.getDiagPduType() is None
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getContainedIPduProps() is None

    def test_get_set_diag_pdu_type(self):
        pdu = DcmIPdu(None, "DcmIPdu1")

        value = DiagPduType().setValue(DiagPduType.DIAG_REQUEST)
        assert pdu.setDiagPduType(value) is pdu
        assert pdu.getDiagPduType() is value
        assert pdu.getDiagPduType().getValue() == DiagPduType.DIAG_REQUEST
        pdu.setDiagPduType(None)
        assert pdu.getDiagPduType() is value

    def test_annotation_pins(self):
        getter_hints = typing.get_type_hints(DcmIPdu.getDiagPduType)
        assert getter_hints.get("return") == typing.Optional[DiagPduType]
        setter_hints = typing.get_type_hints(DcmIPdu.setDiagPduType)
        assert setter_hints.get("value") == typing.Optional[DiagPduType]
        assert setter_hints.get("return") is DcmIPdu

    def test_class_docstring_note(self):
        assert inspect.cleandoc(DcmIPdu.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        pdu = DcmIPdu(None, "DcmIPdu1")
        getter = getattr(pdu, "getDiagPduType")
        setter = getattr(pdu, "setDiagPduType")
        assert inspect.cleandoc(getter.__doc__) == NOTES["diagPduType"]
        assert inspect.cleandoc(setter.__doc__).split("\n")[0] == NOTES["diagPduType"]

    def test_init_has_no_docstring(self):
        assert DcmIPdu.__init__.__doc__ is None
