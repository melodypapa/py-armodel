import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PncGatewayTypeEnum,
)

CLASS_NOTE = "Defines the PncGateway roles."


class TestPncGatewayTypeEnum:
    """Test cases for PncGatewayTypeEnum (Table 3.5, p.55)."""

    def test_member_presence_and_values(self):
        assert PncGatewayTypeEnum.ACTIVE == "ACTIVE"
        assert PncGatewayTypeEnum.NONE == "NONE"
        assert PncGatewayTypeEnum.PASSIVE == "PASSIVE"
        assert list(PncGatewayTypeEnum().getEnumValues()) == ["ACTIVE", "NONE", "PASSIVE"]

    def test_instantiability(self):
        enum = PncGatewayTypeEnum()
        assert enum == enum.setValue(PncGatewayTypeEnum.PASSIVE)
        assert enum.getValue() == "PASSIVE"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PncGatewayTypeEnum.__doc__) == CLASS_NOTE
