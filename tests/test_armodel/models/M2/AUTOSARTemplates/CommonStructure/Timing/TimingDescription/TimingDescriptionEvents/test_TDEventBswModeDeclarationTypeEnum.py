from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModeDeclarationTypeEnum,
)


class TestTDEventBswModeDeclarationTypeEnum:
    def test_members(self):
        assert TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_REQUESTED == "modeDeclarationRequested"
        assert TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_COMPLETED == "modeDeclarationSwitchCompleted"
        assert TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED == "modeDeclarationSwitchInitiated"

    def test_instantiation_and_set_value(self):
        enum = TDEventBswModeDeclarationTypeEnum()
        assert enum.setValue("modeDeclarationSwitchCompleted") is enum
        assert enum.getValue() == "modeDeclarationSwitchCompleted"

    def test_validate_enum_value(self):
        enum = TDEventBswModeDeclarationTypeEnum()
        assert enum.validateEnumValue("bogus") is False
