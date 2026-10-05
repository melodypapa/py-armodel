from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import PulseTestEnum

CLASS_NOTE = "This element indicates to the connected Actuator Software component whether the data-element " "can be used to generate pulse test sequences using the IoHwAbstraction layer"


class TestPulseTestEnum:
    def test_heritage(self):
        assert issubclass(PulseTestEnum, AREnum)

    def test_members_and_values(self):
        assert PulseTestEnum.DISABLE == "disable"
        assert PulseTestEnum.ENABLE == "enable"

    def test_literal_set_is_exact(self):
        assert PulseTestEnum().getEnumValues() == ("disable", "enable")

    def test_instantiability(self):
        enum = PulseTestEnum()
        result = enum.setValue(PulseTestEnum.ENABLE)
        assert result is enum
        assert enum.getValue() == "enable"

    def test_class_docstring_verbatim(self):
        assert PulseTestEnum.__doc__.strip() == CLASS_NOTE
