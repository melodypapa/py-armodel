import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainerIPduTriggerEnum,
)

CLASS_NOTE = "Defines when the transmission of the ContainerIPdu shall be requested."


class TestContainerIPduTriggerEnum:
    """Test cases for ContainerIPduTriggerEnum (Table 6.36, p.354)."""

    def test_member_presence_and_values(self):
        assert ContainerIPduTriggerEnum.DEFAULT_TRIGGER == "DEFAULT-TRIGGER"
        assert ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER == "FIRST-CONTAINED-TRIGGER"
        assert list(ContainerIPduTriggerEnum().getEnumValues()) == [
            ContainerIPduTriggerEnum.DEFAULT_TRIGGER,
            ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER,
        ]

    def test_instantiability(self):
        enum = ContainerIPduTriggerEnum()
        assert enum == enum.setValue(ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER)
        assert enum.getValue() == ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ContainerIPduTriggerEnum.__doc__) == CLASS_NOTE
