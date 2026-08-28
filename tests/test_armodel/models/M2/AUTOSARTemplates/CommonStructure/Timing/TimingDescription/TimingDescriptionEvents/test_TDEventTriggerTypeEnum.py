from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventTriggerTypeEnum,
)


class TestTDEventTriggerTypeEnum:
    def test_members(self):
        assert TDEventTriggerTypeEnum.TRIGGER_ACTIVATED == "triggerActivated"
        assert TDEventTriggerTypeEnum.TRIGGER_RELEASED == "triggerReleased"

    def test_instantiation_and_set_value(self):
        enum = TDEventTriggerTypeEnum()
        assert enum.setValue("triggerReleased") is enum
        assert enum.getValue() == "triggerReleased"

    def test_validate_enum_value(self):
        enum = TDEventTriggerTypeEnum()
        assert enum.validateEnumValue("bogus") is False
