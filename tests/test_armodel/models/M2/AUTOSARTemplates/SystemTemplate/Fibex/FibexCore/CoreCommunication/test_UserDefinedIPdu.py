import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    UserDefinedIPdu,
)

CLASS_NOTE = (
    "UserDefinedIPdu allows to describe PDU-based communication over Complex Drivers. If a new BSW module is added "
    "above the PduR (e.g. a Diagnostic Service ) then this IPdu element shall be used to describe the communication. "
    "Tags: atp.recommendedPackage=Pdus"
)
CDD_TYPE_NOTE = "This attribute defines the CDD that transmits or receives the UserDefinedPdu. If several CDDs are defined this " "attribute is used to distinguish between them."


class TestUserDefinedIPdu:
    """Test cases for UserDefinedIPdu (Table 6.28, p.346)."""

    def test_initialization_defaults(self):
        ipdu = UserDefinedIPdu(None, "Ipdu")
        assert ipdu.getCddType() is None

    def test_get_set_round_trip_and_none_noop(self):
        ipdu = UserDefinedIPdu(None, "Ipdu")
        assert ipdu.setCddType("myCdd") is ipdu
        assert ipdu.getCddType() == "myCdd"
        ipdu.setCddType(None)
        assert ipdu.getCddType() == "myCdd"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedIPdu.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        ipdu = UserDefinedIPdu(None, "Ipdu")
        assert inspect.cleandoc(ipdu.getCddType.__doc__) == CDD_TYPE_NOTE
        assert inspect.cleandoc(ipdu.setCddType.__doc__).split("\n")[0] == CDD_TYPE_NOTE
