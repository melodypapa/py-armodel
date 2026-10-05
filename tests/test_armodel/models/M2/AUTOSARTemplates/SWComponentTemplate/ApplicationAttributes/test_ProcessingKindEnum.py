from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ProcessingKindEnum

CLASS_NOTE = "Kind of processing which has been applied to a data element."


class TestProcessingKindEnum:
    def test_heritage(self):
        assert issubclass(ProcessingKindEnum, AREnum)

    def test_members_and_values(self):
        assert ProcessingKindEnum.FILTERED == "filtered"
        assert ProcessingKindEnum.NONE == "none"
        assert ProcessingKindEnum.RAW == "raw"

    def test_literal_set_is_exact(self):
        assert ProcessingKindEnum().getEnumValues() == ("filtered", "none", "raw")

    def test_instantiability(self):
        enum = ProcessingKindEnum()
        result = enum.setValue(ProcessingKindEnum.FILTERED)
        assert result is enum
        assert enum.getValue() == "filtered"

    def test_class_docstring_verbatim(self):
        assert ProcessingKindEnum.__doc__.strip() == CLASS_NOTE
