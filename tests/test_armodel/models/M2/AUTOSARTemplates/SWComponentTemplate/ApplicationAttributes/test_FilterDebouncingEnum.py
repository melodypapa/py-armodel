from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import FilterDebouncingEnum

CLASS_NOTE = "This enumeration defines possible values for the filter debouncing strategy."


class TestFilterDebouncingEnum:
    def test_heritage(self):
        assert issubclass(FilterDebouncingEnum, AREnum)

    def test_members_and_values(self):
        assert FilterDebouncingEnum.DEBOUNCE_DATA == "DEBOUNCE-DATA"
        assert FilterDebouncingEnum.RAW_DATA == "RAW-DATA"
        assert FilterDebouncingEnum.WAIT_TIME_DATE == "WAIT-TIME-DATE"

    def test_literal_set_is_exact(self):
        assert FilterDebouncingEnum().getEnumValues() == ("DEBOUNCE-DATA", "RAW-DATA", "WAIT-TIME-DATE")

    def test_instantiability(self):
        enum = FilterDebouncingEnum()
        result = enum.setValue(FilterDebouncingEnum.RAW_DATA)
        assert result is enum
        assert enum.getValue() == FilterDebouncingEnum.RAW_DATA

    def test_class_docstring_verbatim(self):
        assert FilterDebouncingEnum.__doc__.strip() == CLASS_NOTE
