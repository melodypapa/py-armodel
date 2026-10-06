from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrameTypeEnum,
)


class TestTDEventFrameTypeEnum:
    def test_members(self):
        assert TDEventFrameTypeEnum.FRAME_QUEUED_FOR_TRANSMISSION == "FRAME-QUEUED-FOR-TRANSMISSION"
        assert TDEventFrameTypeEnum.FRAME_RECEIVED_BY_IF == "FRAME-RECEIVED-BY-IF"
        assert TDEventFrameTypeEnum.FRAME_TRANSMITTED_ON_BUS == "FRAME-TRANSMITTED-ON-BUS"

    def test_instantiation_and_set_value(self):
        enum = TDEventFrameTypeEnum()
        assert enum.setValue(TDEventFrameTypeEnum.FRAME_RECEIVED_BY_IF) is enum
        assert enum.getValue() == TDEventFrameTypeEnum.FRAME_RECEIVED_BY_IF

    def test_validate_enum_value(self):
        enum = TDEventFrameTypeEnum()
        assert enum.validateEnumValue("bogus") is False
