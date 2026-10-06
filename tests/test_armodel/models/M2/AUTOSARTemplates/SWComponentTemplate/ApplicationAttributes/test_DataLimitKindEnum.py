from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import DataLimitKindEnum

CLASS_NOTE = "Indicates whether the data element carries a minimum or maximum value, thereby limiting the current range of another value."


class TestDataLimitKindEnum:
    def test_heritage(self):
        assert issubclass(DataLimitKindEnum, AREnum)

    def test_members_and_values(self):
        assert DataLimitKindEnum.MAX == "MAX"
        assert DataLimitKindEnum.MIN == "MIN"
        assert DataLimitKindEnum.NONE == "NONE"

    def test_literal_set_is_exact(self):
        assert DataLimitKindEnum().getEnumValues() == ("MAX", "MIN", "NONE")

    def test_instantiability(self):
        enum = DataLimitKindEnum()
        result = enum.setValue(DataLimitKindEnum.MAX)
        assert result is enum
        assert enum.getValue() == DataLimitKindEnum.MAX

    def test_class_docstring_verbatim(self):
        assert DataLimitKindEnum.__doc__.strip() == CLASS_NOTE
