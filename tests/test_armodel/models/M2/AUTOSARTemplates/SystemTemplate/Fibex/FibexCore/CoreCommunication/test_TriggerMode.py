import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    TriggerMode,
)

CLASS_NOTE = "IPduM can be configured to send a transmission request for the new multiplexed I-PDU to the PDU-Router because of conditions/ modes."


class TestTriggerMode:
    """Test cases for TriggerMode (Table 6.71, p.408)."""

    def test_member_presence_and_values(self):
        assert TriggerMode.DYNAMIC_PART_TRIGGER == "DYNAMIC-PART-TRIGGER"
        assert TriggerMode.NONE == "NONE"
        assert TriggerMode.STATIC_OR_DYNAMIC_PART_TRIGGER == "STATIC-OR-DYNAMIC-PART-TRIGGER"
        assert TriggerMode.STATIC_PART_TRIGGER == "STATIC-PART-TRIGGER"
        assert list(TriggerMode().getEnumValues()) == [
            TriggerMode.DYNAMIC_PART_TRIGGER,
            "NONE",
            TriggerMode.STATIC_OR_DYNAMIC_PART_TRIGGER,
            TriggerMode.STATIC_PART_TRIGGER,
        ]

    def test_instantiability(self):
        enum = TriggerMode()
        assert enum == enum.setValue(TriggerMode.STATIC_PART_TRIGGER)
        assert enum.getValue() == TriggerMode.STATIC_PART_TRIGGER

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TriggerMode.__doc__) == CLASS_NOTE
