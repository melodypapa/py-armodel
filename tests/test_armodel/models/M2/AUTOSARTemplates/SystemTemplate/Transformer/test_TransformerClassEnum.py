from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformerClassEnum


class TestTransformerClassEnum:
    """
    Model tests for TransformerClassEnum (AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.90).
    """

    def test_initialization(self):
        enum = TransformerClassEnum()
        assert enum is not None
        assert isinstance(enum, AREnum)

    def test_literal_values(self):
        enum = TransformerClassEnum()
        assert TransformerClassEnum.CUSTOM == "CUSTOM"
        assert TransformerClassEnum.SAFETY == "SAFETY"
        assert TransformerClassEnum.SECURITY == "SECURITY"
        assert TransformerClassEnum.SERIALIZER == "SERIALIZER"
        assert list(enum.getEnumValues()) == ["CUSTOM", "SAFETY", "SECURITY", "SERIALIZER"]

    def test_set_value_round_trip(self):
        enum = TransformerClassEnum()
        assert enum == enum.setValue(None)
        assert enum.getValue() == ""
        assert enum == enum.setValue(TransformerClassEnum.CUSTOM)
        assert enum.getValue() == TransformerClassEnum.CUSTOM
        assert enum == enum.setValue(TransformerClassEnum.SERIALIZER)
        assert enum.getValue() == TransformerClassEnum.SERIALIZER

    def test_validate_enum_value(self):
        enum = TransformerClassEnum()
        assert enum.validateEnumValue("CUSTOM") is True
        assert enum.validateEnumValue("SAFETY") is True
        assert enum.validateEnumValue("SECURITY") is True
        assert enum.validateEnumValue("SERIALIZER") is True
        assert enum.validateEnumValue("notATransformerClass") is False
