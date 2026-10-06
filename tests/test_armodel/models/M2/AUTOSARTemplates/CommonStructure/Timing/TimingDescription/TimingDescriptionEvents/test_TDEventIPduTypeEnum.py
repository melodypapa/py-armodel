from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventIPduTypeEnum,
)


class TestTDEventIPduTypeEnum:
    def test_members(self):
        assert TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM == "I-PDU-RECEIVED-BY-COM"
        assert TDEventIPduTypeEnum.IPDU_SENT_TO_IF == "I-PDU-SENT-TO-IF"

    def test_instantiation_and_set_value(self):
        enum = TDEventIPduTypeEnum()
        assert enum.setValue(TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM) is enum
        assert enum.getValue() == TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM

    def test_validate_enum_value(self):
        enum = TDEventIPduTypeEnum()
        assert enum.validateEnumValue("bogus") is False
