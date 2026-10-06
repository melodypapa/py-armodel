from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventOperationTypeEnum,
)


class TestTDEventOperationTypeEnum:
    def test_members(self):
        assert TDEventOperationTypeEnum.OPERATION_CALLED == "OPERATION-CALLED"
        assert TDEventOperationTypeEnum.OPERATION_CALL_RECEIVED == "OPERATION-CALL-RECEIVED"
        assert TDEventOperationTypeEnum.OPERATION_CALL_RESPONSE_RECEIVED == "OPERATION-CALL-RESPONSE-RECEIVED"
        assert TDEventOperationTypeEnum.OPERATION_CALL_RESPONSE_SENT == "OPERATION-CALL-RESPONSE-SENT"

    def test_instantiation_and_set_value(self):
        enum = TDEventOperationTypeEnum()
        assert enum.setValue(TDEventOperationTypeEnum.OPERATION_CALLED) is enum
        assert enum.getValue() == TDEventOperationTypeEnum.OPERATION_CALLED

    def test_validate_enum_value(self):
        enum = TDEventOperationTypeEnum()
        assert enum.validateEnumValue("bogus") is False
