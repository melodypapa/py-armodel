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
        assert DataIdModeEnum.ALL_16_BIT == "ALL-16-BIT"
        assert DataIdModeEnum.ALTERNATING_8_BIT == "ALTERNATING-8-BIT"
        assert DataIdModeEnum.LOWER_12_BIT == "LOWER-12-BIT"
        assert DataIdModeEnum.LOWER_8_BIT == "LOWER-8-BIT"
        assert list(enum.getEnumValues()) == ["ALL-16-BIT", "ALTERNATING-8-BIT", "LOWER-12-BIT", "LOWER-8-BIT"]

    def test_set_value_round_trip(self):
        enum = DataIdModeEnum()
        assert enum == enum.setValue(None)
        assert enum.getValue() == ""
        assert enum == enum.setValue(DataIdModeEnum.ALL_16_BIT)
        assert enum.getValue() == DataIdModeEnum.ALL_16_BIT

    def test_validate_enum_value(self):
        enum = DataIdModeEnum()
        assert enum.validateEnumValue("ALL-16-BIT") is True
        assert enum.validateEnumValue("ALTERNATING-8-BIT") is True
        assert enum.validateEnumValue("LOWER-12-BIT") is True
        assert enum.validateEnumValue("LOWER-8-BIT") is True
        assert enum.validateEnumValue("notADataIdMode") is False
