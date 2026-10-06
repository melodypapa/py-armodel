from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrameEthernetTypeEnum,
)


class TestTDEventFrameEthernetTypeEnum:
    def test_members(self):
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION == "FRAME-ETHERNET-QUEUED-FOR-TRANSMISSION"
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_BY_IF == "FRAME-ETHERNET-RECEIVED-BY-IF"
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_ON_BUS == "FRAME-ETHERNET-RECEIVED-ON-BUS"
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_SENT_ON_BUS == "FRAME-ETHERNET-SENT-ON-BUS"

    def test_instantiation_and_set_value(self):
        enum = TDEventFrameEthernetTypeEnum()
        assert enum.setValue(TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_BY_IF) is enum
        assert enum.getValue() == TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_BY_IF

    def test_validate_enum_value(self):
        enum = TDEventFrameEthernetTypeEnum()
        assert enum.validateEnumValue("bogus") is False
