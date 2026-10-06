from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventModeDeclarationTypeEnum,
)


class TestTDEventModeDeclarationTypeEnum:
    def test_members(self):
        assert TDEventModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_COMPLETED == "MODE-DECLARATION-SWITCH-COMPLETED"
        assert TDEventModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED == "MODE-DECLARATION-SWITCH-INITIATED"

    def test_instantiation_and_set_value(self):
        enum = TDEventModeDeclarationTypeEnum()
        assert enum.setValue("MODE-DECLARATION-SWITCH-COMPLETED") is enum
        assert enum.getValue() == "MODE-DECLARATION-SWITCH-COMPLETED"

    def test_validate_enum_value(self):
        enum = TDEventModeDeclarationTypeEnum()
        assert enum.validateEnumValue("bogus") is False
