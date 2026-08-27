from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (
    TDEventBswInternalBehaviorTypeEnum,
)


class TestTDEventBswInternalBehaviorTypeEnum:
    def test_members(self):
        assert TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_ACTIVATED == "bswModuleEntityActivated"
        assert TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED == "bswModuleEntityStarted"
        assert TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_TERMINATED == "bswModuleEntityTerminated"

    def test_instantiation_and_set_value(self):
        enum = TDEventBswInternalBehaviorTypeEnum()
        assert enum.setValue("bswModuleEntityStarted") is enum
        assert enum.getValue() == "bswModuleEntityStarted"

    def test_validate_enum_value(self):
        enum = TDEventBswInternalBehaviorTypeEnum()
        assert enum.validateEnumValue("bogus") is False
