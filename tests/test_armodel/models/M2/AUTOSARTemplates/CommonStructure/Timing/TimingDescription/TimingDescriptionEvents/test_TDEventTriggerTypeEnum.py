from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventTriggerTypeEnum,
)


class TestTDEventTriggerTypeEnum:
    def test_members(self):
        assert TDEventTriggerTypeEnum.TRIGGER_ACTIVATED == "TRIGGER-ACTIVATED"
        assert TDEventTriggerTypeEnum.TRIGGER_RELEASED == "TRIGGER-RELEASED"

    def test_instantiation_and_set_value(self):
        enum = TDEventTriggerTypeEnum()
        assert enum.setValue(TDEventTriggerTypeEnum.TRIGGER_RELEASED) is enum
        assert enum.getValue() == TDEventTriggerTypeEnum.TRIGGER_RELEASED

    def test_validate_enum_value(self):
        enum = TDEventTriggerTypeEnum()
        assert enum.validateEnumValue("bogus") is False
