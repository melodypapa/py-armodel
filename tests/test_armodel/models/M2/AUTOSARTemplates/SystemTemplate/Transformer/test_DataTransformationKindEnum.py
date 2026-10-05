from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataTransformationKindEnum

SPEC_NOTE = "This enumeration contributes to the definition of the scope of the DataTransformation."


class TestDataTransformationKindEnum:
    def test_members_and_values(self):
        assert DataTransformationKindEnum.ASYMMETRIC_FROM_BYTE_ARRAY == "asymmetricFromByteArray"
        assert DataTransformationKindEnum.ASYMMETRIC_TO_BYTE_ARRAY == "asymmetricToByteArray"
        assert DataTransformationKindEnum.SYMMETRIC == "symmetric"

    def test_literal_set_is_exact(self):
        assert DataTransformationKindEnum().getEnumValues() == ("asymmetricFromByteArray", "asymmetricToByteArray", "symmetric")

    def test_instantiability(self):
        enum = DataTransformationKindEnum()
        result = enum.setValue(DataTransformationKindEnum.SYMMETRIC)
        assert result is enum
        assert enum.getValue() == "symmetric"

    def test_class_docstring_verbatim(self):
        assert DataTransformationKindEnum.__doc__.strip() == SPEC_NOTE
