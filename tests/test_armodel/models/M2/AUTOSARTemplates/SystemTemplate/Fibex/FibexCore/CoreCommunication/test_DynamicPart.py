import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DynamicPart,
    DynamicPartAlternative,
    MultiplexedPart,
    VariationPointCapable,
)

CLASS_NOTE = "Dynamic part of a multiplexed I-Pdu. Reserved space which is used to transport varying SignalIPdus " "at the same position, controlled by the corresponding selectorFieldCode."
MEMBER_NOTE = "Com IPdu alternatives that are transmitted in the Dynamic Part of the MultiplexedIPdu."


class TestDynamicPart:
    """Test cases for DynamicPart (Table 6.74, p.410)."""

    def test_inheritance(self):
        assert issubclass(DynamicPart, MultiplexedPart)
        assert issubclass(DynamicPart, VariationPointCapable)

    def test_dynamic_part_alternatives_default_empty(self):
        part = DynamicPart()
        assert part.getDynamicPartAlternatives() == []
        assert part.getSegmentPositions() == []

    def test_add_dynamic_part_alternative_appends_and_chains(self):
        part = DynamicPart()
        alternative = DynamicPartAlternative()
        assert part.addDynamicPartAlternative(alternative) is part
        assert part.getDynamicPartAlternatives() == [alternative]

    def test_add_dynamic_part_alternative_none_noop(self):
        part = DynamicPart()
        part.addDynamicPartAlternative(None)
        assert part.getDynamicPartAlternatives() == []

    def test_class_docstring_note(self):
        assert inspect.cleandoc(DynamicPart.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        part = DynamicPart()
        assert inspect.cleandoc(part.getDynamicPartAlternatives.__doc__) == MEMBER_NOTE
        assert inspect.cleandoc(part.addDynamicPartAlternative.__doc__).split("\n")[0] == MEMBER_NOTE
