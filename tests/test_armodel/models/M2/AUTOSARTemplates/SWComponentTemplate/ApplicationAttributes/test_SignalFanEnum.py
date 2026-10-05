from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import SignalFanEnum

CLASS_NOTE = "Signal Fan inside the Composition Component Type."


class TestSignalFanEnum:
    def test_heritage(self):
        assert issubclass(SignalFanEnum, AREnum)

    def test_members_and_values(self):
        assert SignalFanEnum.NFOLD == "nfold"
        assert SignalFanEnum.SINGLE == "single"

    def test_literal_set_is_exact(self):
        assert SignalFanEnum().getEnumValues() == ("nfold", "single")

    def test_instantiability(self):
        enum = SignalFanEnum()
        result = enum.setValue(SignalFanEnum.SINGLE)
        assert result is enum
        assert enum.getValue() == "single"

    def test_class_docstring_verbatim(self):
        assert SignalFanEnum.__doc__.strip() == CLASS_NOTE
