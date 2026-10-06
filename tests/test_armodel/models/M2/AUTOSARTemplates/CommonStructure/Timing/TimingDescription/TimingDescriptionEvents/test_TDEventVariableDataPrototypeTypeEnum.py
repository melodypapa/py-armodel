from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventVariableDataPrototypeTypeEnum,
)


class TestTDEventVariableDataPrototypeTypeEnum:
    def test_members(self):
        assert TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_RECEIVED == "VARIABLE-DATA-PROTOTYPE-RECEIVED"
        assert TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_SENT == "VARIABLE-DATA-PROTOTYPE-SENT"

    def test_instantiation_and_set_value(self):
        enum = TDEventVariableDataPrototypeTypeEnum()
        assert enum.setValue(TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_RECEIVED) is enum
        assert enum.getValue() == TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_RECEIVED

    def test_validate_enum_value(self):
        enum = TDEventVariableDataPrototypeTypeEnum()
        assert enum.validateEnumValue("bogus") is False
