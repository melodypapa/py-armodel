import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)

CLASS_NOTE = "Defines whether a Pdu contributes to the triggering of the data transmission if Pdu collection is enabled."


class TestPduCollectionTriggerEnum:
    """Test cases for PduCollectionTriggerEnum (Table 6.41, p.357)."""

    def test_member_presence_and_values(self):
        assert PduCollectionTriggerEnum.ALWAYS == "always"
        assert PduCollectionTriggerEnum.NEVER == "never"
        assert list(PduCollectionTriggerEnum().getEnumValues()) == [
            "always",
            "never",
        ]

    def test_instantiability(self):
        enum = PduCollectionTriggerEnum()
        assert enum == enum.setValue(PduCollectionTriggerEnum.NEVER)
        assert enum.getValue() == "never"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PduCollectionTriggerEnum.__doc__) == CLASS_NOTE
