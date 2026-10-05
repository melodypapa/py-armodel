from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import MappingDirectionEnum

SPEC_NOTE = "Specifies the conversion direction for which the mapping is applicable."


class TestMappingDirectionEnum:
    def test_members_and_values(self):
        assert MappingDirectionEnum.BIDIRECTIONAL == "bidirectional"
        assert MappingDirectionEnum.FIRST_TO_SECOND == "firstToSecond"
        assert MappingDirectionEnum.SECOND_TO_FIRST == "secondToFirst"

    def test_literal_set_is_exact(self):
        assert MappingDirectionEnum().getEnumValues() == ("bidirectional", "firstToSecond", "secondToFirst")

    def test_instantiability(self):
        enum = MappingDirectionEnum()
        result = enum.setValue(MappingDirectionEnum.FIRST_TO_SECOND)
        assert result is enum
        assert enum.getValue() == "firstToSecond"

    def test_class_docstring_verbatim(self):
        assert MappingDirectionEnum.__doc__.strip() == SPEC_NOTE
