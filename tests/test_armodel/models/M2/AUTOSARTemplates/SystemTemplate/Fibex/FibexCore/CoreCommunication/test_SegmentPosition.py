import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SegmentPosition,
)

CLASS_NOTE = (
    "The StaticPart and the DynamicPart can be separated in multiple segments within the multiplexed PDU. "
    "The ISignalIPdus are copied bit by bit into the MultiplexedIPdu. If the space of the first segment is 5 bits large "
    "than the first 5 bits of the ISignalIPdu are copied into this first segment and so on."
)
BYTE_ORDER_NOTE = (
    "This attribute defines the order of the bytes of the segment and the packing into the MultiplexedIPdu. "
    "Please consider that [constr_3247] and [constr_3224] are restricting the usage of this attribute."
)
LENGTH_NOTE = "Data Length of the segment in bits."
POSITION_NOTE = (
    "Segments bit position relatively to the beginning of a multiplexed IPdu. Note that the absolute position of the segment "
    "in the MultiplexedIPdu is determined by the definition of the segmentByteOrder attribute of the SegmentPosition. "
    "If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. "
    "If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. "
    'In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". '
    "The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7."
)


class TestSegmentPosition:
    """Test cases for SegmentPosition (Table 6.77, p.412)."""

    def test_initialization_defaults(self):
        position = SegmentPosition()
        assert position.getSegmentByteOrder() is None
        assert position.getSegmentLength() is None
        assert position.getSegmentPosition() is None

    def test_get_set_round_trip_and_none_noop(self):
        position = SegmentPosition()
        assert position.setSegmentLength(8) is position
        assert position.getSegmentLength() == 8
        position.setSegmentLength(None)
        assert position.getSegmentLength() == 8

        assert position.setSegmentPosition(3) is position
        assert position.getSegmentPosition() == 3
        position.setSegmentPosition(None)
        assert position.getSegmentPosition() == 3

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SegmentPosition.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        position = SegmentPosition()
        assert inspect.cleandoc(position.getSegmentByteOrder.__doc__) == BYTE_ORDER_NOTE
        assert inspect.cleandoc(position.setSegmentByteOrder.__doc__).split("\n")[0] == BYTE_ORDER_NOTE
        assert inspect.cleandoc(position.getSegmentLength.__doc__) == LENGTH_NOTE
        assert inspect.cleandoc(position.setSegmentLength.__doc__).split("\n")[0] == LENGTH_NOTE
        assert inspect.cleandoc(position.getSegmentPosition.__doc__) == POSITION_NOTE
        assert inspect.cleandoc(position.setSegmentPosition.__doc__).split("\n")[0] == POSITION_NOTE
