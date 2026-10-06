from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModeDeclarationTypeEnum,
)


class TestTDEventBswModeDeclarationTypeEnum:
    def test_members(self):
        assert TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_REQUESTED == "MODE-DECLARATION-REQUESTED"
        assert TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_COMPLETED == "MODE-DECLARATION-SWITCH-COMPLETED"
        assert TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED == "MODE-DECLARATION-SWITCH-INITIATED"

    def test_instantiation_and_set_value(self):
        enum = TDEventBswModeDeclarationTypeEnum()
        assert enum.setValue("MODE-DECLARATION-SWITCH-COMPLETED") is enum
        assert enum.getValue() == "MODE-DECLARATION-SWITCH-COMPLETED"

    def test_validate_enum_value(self):
        enum = TDEventBswModeDeclarationTypeEnum()
        assert enum.validateEnumValue("bogus") is False
