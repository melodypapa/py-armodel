from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrameTypeEnum,
)


class TestTDEventFrameTypeEnum:
    def test_members(self):
        assert TDEventFrameTypeEnum.FRAME_QUEUED_FOR_TRANSMISSION == "frameQueuedForTransmission"
        assert TDEventFrameTypeEnum.FRAME_RECEIVED_BY_IF == "frameReceivedByIf"
        assert TDEventFrameTypeEnum.FRAME_TRANSMITTED_ON_BUS == "frameTransmittedOnBus"

    def test_instantiation_and_set_value(self):
        enum = TDEventFrameTypeEnum()
        assert enum.setValue("frameReceivedByIf") is enum
        assert enum.getValue() == "frameReceivedByIf"

    def test_validate_enum_value(self):
        enum = TDEventFrameTypeEnum()
        assert enum.validateEnumValue("bogus") is False
