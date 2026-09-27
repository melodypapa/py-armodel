import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    UserDefinedPdu,
)

CLASS_NOTE = (
    "UserDefinedPdu allows to describe PDU-based communication over Complex Drivers. If a new BSW module is added "
    "above the BusIf (e.g. a new Nm module) then this Pdu element shall be used to describe the communication. "
    "Tags: atp.recommendedPackage=Pdus"
)
CDD_TYPE_NOTE = "This attribute defines the CDD that transmits or receives the UserDefinedIPdu. If several CDDs are defined this " "attribute is used to distinguish between them."


class TestUserDefinedPdu:
    """Test cases for UserDefinedPdu (Table 6.27, p.345)."""

    def test_initialization_defaults(self):
        pdu = UserDefinedPdu(None, "Pdu")
        assert pdu.getCddType() is None

    def test_get_set_round_trip_and_none_noop(self):
        pdu = UserDefinedPdu(None, "Pdu")
        assert pdu.setCddType("myCdd") is pdu
        assert pdu.getCddType() == "myCdd"
        pdu.setCddType(None)
        assert pdu.getCddType() == "myCdd"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedPdu.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        pdu = UserDefinedPdu(None, "Pdu")
        assert inspect.cleandoc(pdu.getCddType.__doc__) == CDD_TYPE_NOTE
        assert inspect.cleandoc(pdu.setCddType.__doc__).split("\n")[0] == CDD_TYPE_NOTE
