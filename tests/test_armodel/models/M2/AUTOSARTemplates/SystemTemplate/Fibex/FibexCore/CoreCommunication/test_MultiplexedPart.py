import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    MultiplexedPart,
    SegmentPosition,
)

CLASS_NOTE = "The StaticPart and the DynamicPart have common properties. " "Both can be separated in multiple segments within the multiplexed PDU."
MEMBER_NOTE = (
    "The StaticPart and the DynamicPart can be separated in multiple segments within the multiplexed PDU. " "Therefore the StaticPart and the DynamicPart can contain multiple SegmentPositions."
)


class ConcretePart(MultiplexedPart):
    pass


class TestMultiplexedPart:
    """Test cases for MultiplexedPart (Table 6.76, p.411)."""

    def test_abstract(self):
        with pytest.raises(TypeError):
            MultiplexedPart()

    def test_segment_positions_default_empty(self):
        part = ConcretePart()
        assert part.getSegmentPositions() == []

    def test_add_segment_position_appends_and_chains(self):
        part = ConcretePart()
        position = SegmentPosition()
        assert part.addSegmentPosition(position) is part
        assert part.getSegmentPositions() == [position]

    def test_add_segment_position_none_noop(self):
        part = ConcretePart()
        part.addSegmentPosition(None)
        assert part.getSegmentPositions() == []

    def test_class_docstring_note(self):
        assert inspect.cleandoc(MultiplexedPart.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        part = ConcretePart()
        assert inspect.cleandoc(part.getSegmentPositions.__doc__) == MEMBER_NOTE
        assert inspect.cleandoc(part.addSegmentPosition.__doc__).split("\n")[0] == MEMBER_NOTE
