from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrameEthernetTypeEnum,
)


class TestTDEventFrameEthernetTypeEnum:
    def test_members(self):
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION == "frameEthernetQueuedForTransmission"
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_BY_IF == "frameEthernetReceivedByIf"
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_ON_BUS == "frameEthernetReceivedOnBus"
        assert TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_SENT_ON_BUS == "frameEthernetSentOnBus"

    def test_instantiation_and_set_value(self):
        enum = TDEventFrameEthernetTypeEnum()
        assert enum.setValue("frameEthernetReceivedByIf") is enum
        assert enum.getValue() == "frameEthernetReceivedByIf"

    def test_validate_enum_value(self):
        enum = TDEventFrameEthernetTypeEnum()
        assert enum.validateEnumValue("bogus") is False
