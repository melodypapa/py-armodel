from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (
    TDEventSwcInternalBehaviorTypeEnum,
)


class TestTDEventSwcInternalBehaviorTypeEnum:
    def test_members(self):
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_ACTIVATED == "runnableEntityActivated"
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_STARTED == "runnableEntityStarted"
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_TERMINATED == "runnableEntityTerminated"
        assert TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_VARIABLE_ACCESS == "runnableEntityVariableAccess"

    def test_instantiation_and_set_value(self):
        enum = TDEventSwcInternalBehaviorTypeEnum()
        assert enum.setValue("runnableEntityActivated") is enum
        assert enum.getValue() == "runnableEntityActivated"

    def test_validate_enum_value(self):
        enum = TDEventSwcInternalBehaviorTypeEnum()
        assert enum.validateEnumValue("bogus") is False
