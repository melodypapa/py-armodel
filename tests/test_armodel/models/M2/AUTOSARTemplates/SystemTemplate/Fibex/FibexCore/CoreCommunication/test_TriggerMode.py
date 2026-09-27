import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    TriggerMode,
)

CLASS_NOTE = "IPduM can be configured to send a transmission request for the new multiplexed I-PDU to the PDU-Router because of conditions/ modes."


class TestTriggerMode:
    """Test cases for TriggerMode (Table 6.71, p.408)."""

    def test_member_presence_and_values(self):
        assert TriggerMode.DYNAMIC_PART_TRIGGER == "dynamicPartTrigger"
        assert TriggerMode.NONE == "none"
        assert TriggerMode.STATIC_OR_DYNAMIC_PART_TRIGGER == "staticOrDynamicPartTrigger"
        assert TriggerMode.STATIC_PART_TRIGGER == "staticPartTrigger"
        assert list(TriggerMode().getEnumValues()) == [
            "dynamicPartTrigger",
            "none",
            "staticOrDynamicPartTrigger",
            "staticPartTrigger",
        ]

    def test_instantiability(self):
        enum = TriggerMode()
        assert enum == enum.setValue(TriggerMode.STATIC_PART_TRIGGER)
        assert enum.getValue() == "staticPartTrigger"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TriggerMode.__doc__) == CLASS_NOTE
