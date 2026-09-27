import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecuredPduHeaderEnum,
)

CLASS_NOTE = "Defines the header which will be inserted into the SecuredIPdu."


class TestSecuredPduHeaderEnum:
    """Test cases for SecuredPduHeaderEnum (Table 6.43, p.369)."""

    def test_member_presence_and_values(self):
        assert SecuredPduHeaderEnum.NO_HEADER == "noHeader"
        assert SecuredPduHeaderEnum.SECURED_PDU_HEADER08_BIT == "securedPduHeader08Bit"
        assert SecuredPduHeaderEnum.SECURED_PDU_HEADER16_BIT == "securedPduHeader16Bit"
        assert SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT == "securedPduHeader32Bit"
        assert list(SecuredPduHeaderEnum().getEnumValues()) == [
            "noHeader",
            "securedPduHeader08Bit",
            "securedPduHeader16Bit",
            "securedPduHeader32Bit",
        ]

    def test_instantiability(self):
        enum = SecuredPduHeaderEnum()
        assert enum == enum.setValue(SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT)
        assert enum.getValue() == "securedPduHeader32Bit"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecuredPduHeaderEnum.__doc__) == CLASS_NOTE
