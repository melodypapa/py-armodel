import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
    Integer,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PduToFrameMapping

CLASS_NOTE = "A PduToFrameMapping defines the composition of Pdus in each frame."
NOTES = {
    "packingByteOrder": "This attribute defines the order of the bytes of the Pdu and the packing into the Frame. Please consider that [constr_3246] and [constr_3222] are restricting the usage of this attribute.",
    "pduRef": "Reference to a I-Pdu, N-Pdu or NmPdu that is transmitted in the Frame.",
    "startPosition": "This attribute describes the bitposition of a Pdu within a Frame. Please note that the absolute position of the Pdu in the Frame is determined by the definition of the packingByte Order attribute. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the Frame. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the Frame. The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. The Pdus are byte aligned in a Frame and only the values 0, 8, 16, 24,... (for little endian) and 7, 15, 23, ... (for big endian) are allowed.",
    "updateIndicationBitPosition": 'Indication to the receivers that the corresponding Pdu was updated by the sender. This attribute describes the position of the update bit in the frame that aggregates this PDUToFrameMapping. Length is always one bit. Note that the exact bit position of the updateIndicationBit Position is linked to the value of the attribute packingByte Order because the method of finding the bit position is different for the values mostSignificantByteFirst and most SignificantByteLast. This means that if the value of packingByteOrder is changed while the value of update IndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing Frame still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian"',
}


class TestPduToFrameMapping:
    """Test cases for PduToFrameMapping (Table 6.29, p.347)."""

    def test_inheritance(self):
        assert issubclass(PduToFrameMapping, Identifiable)
        assert issubclass(PduToFrameMapping, VariationPointCapable)

    def test_concrete_instantiation(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")
        assert mapping.getShortName() == "PduToFrameMapping1"

    def test_initialization_defaults(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")
        assert mapping.getPackingByteOrder() is None
        assert mapping.getPduRef() is None
        assert mapping.getStartPosition() is None
        assert mapping.getUpdateIndicationBitPosition() is None
        assert mapping.getVariationPoint() is None

    def test_get_set_packing_byte_order(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")

        value = ByteOrderEnum()
        value.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)
        assert mapping.setPackingByteOrder(value) is mapping
        assert mapping.getPackingByteOrder() is value
        assert mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
        mapping.setPackingByteOrder(None)
        assert mapping.getPackingByteOrder() is value

    def test_get_set_pdu_ref(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")

        value = RefType()
        value.setValue("/pdus/NmPdu1")
        value.setDest("NM-PDU")
        assert mapping.setPduRef(value) is mapping
        assert mapping.getPduRef() is value
        assert mapping.getPduRef().getValue() == "/pdus/NmPdu1"
        assert mapping.getPduRef().getDest() == "NM-PDU"
        mapping.setPduRef(None)
        assert mapping.getPduRef() is value

    def test_get_set_start_position(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")

        value = Integer().setValue("8")
        assert mapping.setStartPosition(value) is mapping
        assert mapping.getStartPosition() is value
        assert mapping.getStartPosition().getValue() == 8
        mapping.setStartPosition(None)
        assert mapping.getStartPosition() is value

    def test_get_set_update_indication_bit_position(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")

        value = Integer().setValue("7")
        assert mapping.setUpdateIndicationBitPosition(value) is mapping
        assert mapping.getUpdateIndicationBitPosition() is value
        assert mapping.getUpdateIndicationBitPosition().getValue() == 7
        mapping.setUpdateIndicationBitPosition(None)
        assert mapping.getUpdateIndicationBitPosition() is value

    def test_annotation_pins(self):
        pairs = [
            ("getPackingByteOrder", "setPackingByteOrder", ByteOrderEnum),
            ("getPduRef", "setPduRef", RefType),
            ("getStartPosition", "setStartPosition", Integer),
            ("getUpdateIndicationBitPosition", "setUpdateIndicationBitPosition", Integer),
        ]
        for getter_name, setter_name, member_type in pairs:
            getter_hints = typing.get_type_hints(getattr(PduToFrameMapping, getter_name))
            assert getter_hints.get("return") == typing.Optional[member_type], getter_name
            setter_hints = typing.get_type_hints(getattr(PduToFrameMapping, setter_name))
            assert setter_hints.get("value") == typing.Optional[member_type], setter_name
            assert setter_hints.get("return") is PduToFrameMapping, setter_name

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PduToFrameMapping.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        mapping = PduToFrameMapping(None, "PduToFrameMapping1")
        for attr, note in NOTES.items():
            getter = getattr(mapping, "get%s%s" % (attr[0].upper(), attr[1:]))
            setter = getattr(mapping, "set%s%s" % (attr[0].upper(), attr[1:]))
            assert inspect.cleandoc(getter.__doc__) == note, attr
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == note, attr
            assert "A None value is a no-op and does not overwrite an existing %s." % attr in inspect.cleandoc(setter.__doc__), attr

    def test_init_has_no_docstring(self):
        assert PduToFrameMapping.__init__.__doc__ is None
