import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionSemanticsEnum,
)

CLASS_NOTE = """Defines the collection semantics for the PDU collection feature."""


class TestPduCollectionSemanticsEnum:
    """Test cases for PduCollectionSemanticsEnum (Table 6.165, p.490)."""

    def test_member_presence_and_values(self):
        assert PduCollectionSemanticsEnum.LAST_IS_BEST == "LAST-IS-BEST"
        assert PduCollectionSemanticsEnum.QUEUED == "QUEUED"
        assert list(PduCollectionSemanticsEnum().getEnumValues()) == ["LAST-IS-BEST", "QUEUED"]

    def test_instantiability(self):
        enum = PduCollectionSemanticsEnum()
        assert enum == enum.setValue(PduCollectionSemanticsEnum.LAST_IS_BEST)
        assert enum.getValue() == "LAST-IS-BEST"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PduCollectionSemanticsEnum.__doc__) == CLASS_NOTE
