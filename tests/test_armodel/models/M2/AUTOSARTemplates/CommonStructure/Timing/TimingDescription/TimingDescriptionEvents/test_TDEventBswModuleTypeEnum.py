from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModuleTypeEnum,
)


class TestTDEventBswModuleTypeEnum:
    def test_members(self):
        assert TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED == "bswMEntryCalled"
        assert TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALL_RETURNED == "bswMEntryCallReturned"

    def test_instantiation_and_set_value(self):
        enum = TDEventBswModuleTypeEnum()
        assert enum.setValue("bswMEntryCalled") is enum
        assert enum.getValue() == "bswMEntryCalled"

    def test_validate_enum_value(self):
        enum = TDEventBswModuleTypeEnum()
        assert enum.validateEnumValue("bogus") is False
