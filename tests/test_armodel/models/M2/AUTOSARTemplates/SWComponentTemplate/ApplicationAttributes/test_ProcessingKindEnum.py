from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ProcessingKindEnum

CLASS_NOTE = "Kind of processing which has been applied to a data element."


class TestProcessingKindEnum:
    def test_heritage(self):
        assert issubclass(ProcessingKindEnum, AREnum)

    def test_members_and_values(self):
        assert ProcessingKindEnum.FILTERED == "FILTERED"
        assert ProcessingKindEnum.NONE == "NONE"
        assert ProcessingKindEnum.RAW == "RAW"

    def test_literal_set_is_exact(self):
        assert ProcessingKindEnum().getEnumValues() == ("FILTERED", "NONE", "RAW")

    def test_instantiability(self):
        enum = ProcessingKindEnum()
        result = enum.setValue(ProcessingKindEnum.FILTERED)
        assert result is enum
        assert enum.getValue() == ProcessingKindEnum.FILTERED

    def test_class_docstring_verbatim(self):
        assert ProcessingKindEnum.__doc__.strip() == CLASS_NOTE
