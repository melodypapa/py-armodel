import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecuredPduHeaderEnum,
)

CLASS_NOTE = "Defines the header which will be inserted into the SecuredIPdu."


class TestSecuredPduHeaderEnum:
    """Test cases for SecuredPduHeaderEnum (Table 6.43, p.369)."""

    def test_member_presence_and_values(self):
        assert SecuredPduHeaderEnum.NO_HEADER == "NO-HEADER"
        assert SecuredPduHeaderEnum.SECURED_PDU_HEADER08_BIT == "SECURED-PDU-HEADER-08-BIT"
        assert SecuredPduHeaderEnum.SECURED_PDU_HEADER16_BIT == "SECURED-PDU-HEADER-16-BIT"
        assert SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT == "SECURED-PDU-HEADER-32-BIT"
        assert list(SecuredPduHeaderEnum().getEnumValues()) == [
            SecuredPduHeaderEnum.NO_HEADER,
            SecuredPduHeaderEnum.SECURED_PDU_HEADER08_BIT,
            SecuredPduHeaderEnum.SECURED_PDU_HEADER16_BIT,
            SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT,
        ]

    def test_instantiability(self):
        enum = SecuredPduHeaderEnum()
        assert enum == enum.setValue(SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT)
        assert enum.getValue() == SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecuredPduHeaderEnum.__doc__) == CLASS_NOTE
