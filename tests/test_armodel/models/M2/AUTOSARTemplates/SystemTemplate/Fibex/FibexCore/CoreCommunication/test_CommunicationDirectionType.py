import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
)

CLASS_NOTE = "Describes the communication direction."


class TestCommunicationDirectionType:
    """Test cases for CommunicationDirectionType (Table 6.33, p.351)."""

    def test_member_presence_and_values(self):
        assert CommunicationDirectionType.IN == "in"
        assert CommunicationDirectionType.OUT == "out"
        assert list(CommunicationDirectionType().getEnumValues()) == ["in", "out"]

    def test_instantiability(self):
        enum = CommunicationDirectionType()
        assert enum == enum.setValue(CommunicationDirectionType.OUT)
        assert enum.getValue() == "out"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CommunicationDirectionType.__doc__) == CLASS_NOTE
