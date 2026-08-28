from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventOperationTypeEnum,
)


class TestTDEventOperationTypeEnum:
    def test_members(self):
        assert TDEventOperationTypeEnum.OPERATION_CALLED == "operationCalled"
        assert TDEventOperationTypeEnum.OPERATION_CALL_RECEIVED == "operationCallReceived"
        assert TDEventOperationTypeEnum.OPERATION_CALL_RESPONSE_RECEIVED == "operationCallResponseReceived"
        assert TDEventOperationTypeEnum.OPERATION_CALL_RESPONSE_SENT == "operationCallResponseSent"

    def test_instantiation_and_set_value(self):
        enum = TDEventOperationTypeEnum()
        assert enum.setValue("operationCalled") is enum
        assert enum.getValue() == "operationCalled"

    def test_validate_enum_value(self):
        enum = TDEventOperationTypeEnum()
        assert enum.validateEnumValue("bogus") is False
