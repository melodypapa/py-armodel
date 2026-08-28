from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventModeDeclarationTypeEnum,
)


class TestTDEventModeDeclarationTypeEnum:
    def test_members(self):
        assert TDEventModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_COMPLETED == "modeDeclarationSwitchCompleted"
        assert TDEventModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED == "modeDeclarationSwitchInitiated"

    def test_instantiation_and_set_value(self):
        enum = TDEventModeDeclarationTypeEnum()
        assert enum.setValue("modeDeclarationSwitchCompleted") is enum
        assert enum.getValue() == "modeDeclarationSwitchCompleted"

    def test_validate_enum_value(self):
        enum = TDEventModeDeclarationTypeEnum()
        assert enum.validateEnumValue("bogus") is False
