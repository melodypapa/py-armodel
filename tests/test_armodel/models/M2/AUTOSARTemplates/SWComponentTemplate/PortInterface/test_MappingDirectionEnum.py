from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import MappingDirectionEnum

SPEC_NOTE = "Specifies the conversion direction for which the mapping is applicable."


class TestMappingDirectionEnum:
    def test_members_and_values(self):
        assert MappingDirectionEnum.BIDIRECTIONAL == "BIDIRECTIONAL"
        assert MappingDirectionEnum.FIRST_TO_SECOND == "FIRST-TO-SECOND"
        assert MappingDirectionEnum.SECOND_TO_FIRST == "SECOND-TO-FIRST"

    def test_literal_set_is_exact(self):
        assert MappingDirectionEnum().getEnumValues() == ("BIDIRECTIONAL", "FIRST-TO-SECOND", "SECOND-TO-FIRST")

    def test_instantiability(self):
        enum = MappingDirectionEnum()
        result = enum.setValue(MappingDirectionEnum.FIRST_TO_SECOND)
        assert result is enum
        assert enum.getValue() == MappingDirectionEnum.FIRST_TO_SECOND

    def test_class_docstring_verbatim(self):
        assert MappingDirectionEnum.__doc__.strip() == SPEC_NOTE
