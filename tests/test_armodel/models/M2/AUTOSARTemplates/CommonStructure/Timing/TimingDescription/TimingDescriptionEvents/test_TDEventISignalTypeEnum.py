from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventISignalTypeEnum,
)


class TestTDEventISignalTypeEnum:
    def test_members(self):
        assert TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE == "iSignalAvailableForRte"
        assert TDEventISignalTypeEnum.ISIGNAL_SENT_TO_COM == "iSignalSentToCom"

    def test_instantiation_and_set_value(self):
        enum = TDEventISignalTypeEnum()
        assert enum.setValue("iSignalAvailableForRte") is enum
        assert enum.getValue() == "iSignalAvailableForRte"

    def test_validate_enum_value(self):
        enum = TDEventISignalTypeEnum()
        assert enum.validateEnumValue("bogus") is False
