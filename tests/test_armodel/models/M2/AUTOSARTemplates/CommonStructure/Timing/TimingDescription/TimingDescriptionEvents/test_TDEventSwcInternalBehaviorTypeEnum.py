from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (
    TDEventSwcInternalBehaviorTypeEnum,
)


class TestTDEventSwcInternalBehaviorTypeEnum:
    def test_members(self):
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_ACTIVATED == "RUNNABLE-ENTITY-ACTIVATED"
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_STARTED == "RUNNABLE-ENTITY-STARTED"
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_TERMINATED == "RUNNABLE-ENTITY-TERMINATED"
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_VARIABLE_ACCESS == "RUNNABLE-ENTITY-VARIABLE-ACCESS"

    def test_instantiation_and_set_value(self):
        enum = TDEventSwcInternalBehaviorTypeEnum()
        assert enum.setValue(TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_ACTIVATED) is enum
        assert enum.getValue() == TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_ACTIVATED

    def test_validate_enum_value(self):
        enum = TDEventSwcInternalBehaviorTypeEnum()
        assert enum.validateEnumValue("bogus") is False
