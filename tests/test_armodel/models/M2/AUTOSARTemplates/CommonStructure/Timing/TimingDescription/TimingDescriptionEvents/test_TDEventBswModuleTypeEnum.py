from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModuleTypeEnum,
)


class TestTDEventBswModuleTypeEnum:
    def test_members(self):
        assert TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED == "BSW-M-ENTRY-CALLED"
        assert TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALL_RETURNED == "BSW-M-ENTRY-CALL-RETURNED"

    def test_instantiation_and_set_value(self):
        enum = TDEventBswModuleTypeEnum()
        assert enum.setValue(TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED) is enum
        assert enum.getValue() == TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED

    def test_validate_enum_value(self):
        enum = TDEventBswModuleTypeEnum()
        assert enum.validateEnumValue("bogus") is False
