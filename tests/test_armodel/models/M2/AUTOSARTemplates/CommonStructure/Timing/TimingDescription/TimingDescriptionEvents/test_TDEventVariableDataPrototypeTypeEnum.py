from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventVariableDataPrototypeTypeEnum,
)


class TestTDEventVariableDataPrototypeTypeEnum:
    def test_members(self):
        assert TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_RECEIVED == "variableDataPrototypeReceived"
        assert TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_SENT == "variableDataPrototypeSent"

    def test_instantiation_and_set_value(self):
        enum = TDEventVariableDataPrototypeTypeEnum()
        assert enum.setValue("variableDataPrototypeReceived") is enum
        assert enum.getValue() == "variableDataPrototypeReceived"

    def test_validate_enum_value(self):
        enum = TDEventVariableDataPrototypeTypeEnum()
        assert enum.validateEnumValue("bogus") is False
