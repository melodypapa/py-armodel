from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventISignalTypeEnum,
)


class TestTDEventISignalTypeEnum:
    def test_members(self):
        assert TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE == "I-SIGNAL-AVAILABLE-FOR-RTE"
        assert TDEventISignalTypeEnum.ISIGNAL_SENT_TO_COM == "I-SIGNAL-SENT-TO-COM"

    def test_instantiation_and_set_value(self):
        enum = TDEventISignalTypeEnum()
        assert enum.setValue(TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE) is enum
        assert enum.getValue() == TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE

    def test_validate_enum_value(self):
        enum = TDEventISignalTypeEnum()
        assert enum.validateEnumValue("bogus") is False
