import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduCollectionSemanticsEnum,
)

CLASS_NOTE = "Defines the collection semantics for ContainedIPdus."


class TestContainedIPduCollectionSemanticsEnum:
    """Test cases for ContainedIPduCollectionSemanticsEnum (Table 6.40, p.357)."""

    def test_member_presence_and_values(self):
        assert ContainedIPduCollectionSemanticsEnum.LAST_IS_BEST == "lastIsBest"
        assert ContainedIPduCollectionSemanticsEnum.QUEUED == "queued"
        assert list(ContainedIPduCollectionSemanticsEnum().getEnumValues()) == [
            "lastIsBest",
            "queued",
        ]

    def test_instantiability(self):
        enum = ContainedIPduCollectionSemanticsEnum()
        assert enum == enum.setValue(ContainedIPduCollectionSemanticsEnum.QUEUED)
        assert enum.getValue() == "queued"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ContainedIPduCollectionSemanticsEnum.__doc__) == CLASS_NOTE
