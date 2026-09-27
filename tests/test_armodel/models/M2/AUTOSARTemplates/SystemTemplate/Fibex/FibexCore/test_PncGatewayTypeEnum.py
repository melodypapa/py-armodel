import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PncGatewayTypeEnum,
)

CLASS_NOTE = "Defines the PncGateway roles."


class TestPncGatewayTypeEnum:
    """Test cases for PncGatewayTypeEnum (Table 3.5, p.55)."""

    def test_member_presence_and_values(self):
        assert PncGatewayTypeEnum.ACTIVE == "active"
        assert PncGatewayTypeEnum.NONE == "none"
        assert PncGatewayTypeEnum.PASSIVE == "passive"
        assert list(PncGatewayTypeEnum().getEnumValues()) == ["active", "none", "passive"]

    def test_instantiability(self):
        enum = PncGatewayTypeEnum()
        assert enum == enum.setValue(PncGatewayTypeEnum.PASSIVE)
        assert enum.getValue() == "passive"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PncGatewayTypeEnum.__doc__) == CLASS_NOTE
