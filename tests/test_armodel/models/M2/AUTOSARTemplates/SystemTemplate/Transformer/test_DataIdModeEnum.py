from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataIdModeEnum


class TestDataIdModeEnum:
    """
    Model tests for DataIdModeEnum (AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 7.24).
    """

    def test_initialization(self):
        enum = DataIdModeEnum()
        assert enum is not None
        assert isinstance(enum, AREnum)

    def test_literal_values(self):
        enum = DataIdModeEnum()
        assert DataIdModeEnum.ALL_16_BIT == "all16Bit"
        assert DataIdModeEnum.ALTERNATING_8_BIT == "alternating8Bit"
        assert DataIdModeEnum.LOWER_12_BIT == "lower12Bit"
        assert DataIdModeEnum.LOWER_8_BIT == "lower8Bit"
        assert list(enum.getEnumValues()) == ["all16Bit", "alternating8Bit", "lower12Bit", "lower8Bit"]

    def test_set_value_round_trip(self):
        enum = DataIdModeEnum()
        assert enum == enum.setValue(None)
        assert enum.getValue() == ""
        assert enum == enum.setValue(DataIdModeEnum.ALL_16_BIT)
        assert enum.getValue() == DataIdModeEnum.ALL_16_BIT

    def test_validate_enum_value(self):
        enum = DataIdModeEnum()
        assert enum.validateEnumValue("all16Bit") is True
        assert enum.validateEnumValue("alternating8Bit") is True
        assert enum.validateEnumValue("lower12Bit") is True
        assert enum.validateEnumValue("lower8Bit") is True
        assert enum.validateEnumValue("notADataIdMode") is False
