from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (
    TDEventBswInternalBehaviorTypeEnum,
)


class TestTDEventBswInternalBehaviorTypeEnum:
    def test_members(self):
        assert TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_ACTIVATED == "BSW-MODULE-ENTITY-ACTIVATED"
        assert TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED == "BSW-MODULE-ENTITY-STARTED"
        assert TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_TERMINATED == "BSW-MODULE-ENTITY-TERMINATED"

    def test_instantiation_and_set_value(self):
        enum = TDEventBswInternalBehaviorTypeEnum()
        assert enum.setValue(TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED) is enum
        assert enum.getValue() == TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED

    def test_validate_enum_value(self):
        enum = TDEventBswInternalBehaviorTypeEnum()
        assert enum.validateEnumValue("bogus") is False
