from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventIPduTypeEnum,
)


class TestTDEventIPduTypeEnum:
    def test_members(self):
        assert TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM == "iPduReceivedByCom"
        assert TDEventIPduTypeEnum.IPDU_SENT_TO_IF == "iPduSentToIf"

    def test_instantiation_and_set_value(self):
        enum = TDEventIPduTypeEnum()
        assert enum.setValue("iPduReceivedByCom") is enum
        assert enum.getValue() == "iPduReceivedByCom"

    def test_validate_enum_value(self):
        enum = TDEventIPduTypeEnum()
        assert enum.validateEnumValue("bogus") is False
