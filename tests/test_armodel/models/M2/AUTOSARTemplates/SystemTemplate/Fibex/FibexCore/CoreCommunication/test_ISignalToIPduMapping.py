import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
    RefType,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalToIPduMapping,
    TransferPropertyEnum,
)

CLASS_NOTE = "An ISignalToIPduMapping describes the mapping of ISignals to ISignalIPdus and defines the position of the ISignal within an ISignalIPdu."
CLASS_CONSTRAINTS = (
    "[constr_5322] Value range of ISignalToIPduMapping.startPosition: The value of ISignalToIPduMapping.startPosition shall be in the range of 0..4294967295 Bits.",
    "[constr_5323] Value range of ISignalToIPduMapping.updateIndicationBitPosition: The value of ISignalToIPduMapping.updateIndicationBitPosition shall be in the range of 0..4294967295 Bits.",
    "[constr_3514] No two ISignalToIPduMappings shall reference the identical ISignal: No two ISignalToIPduMappings shall reference the identical ISignal in the role iSignal in the scope of one System.",
)
NOTES = {
    "iSignalRef": (
        "Reference to a ISignal that is mapped into the ISignal IPdu. Each ISignal contained in the ISignalGroup shall be mapped "
        "into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an "
        "ISignalToIPduMapping are mutually exclusive."
    ),
    "iSignalGroupRef": (
        "Reference to an ISignalGroup that is mapped into the SignalIPdu. If an ISignalToIPduMapping for an ISignal Group is "
        "defined, only the UpdateIndicationBitPosition and the transferProperty is relevant. The startPosition and the "
        "packingByteOrder shall be ignored. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own "
        "ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive."
    ),
    "packingByteOrder": (
        "This parameter defines the order of the bytes of the signal and the packing into the SignalIPdu. The byte ordering "
        '"Little Endian" (MostSignificantByteLast), "Big Endian" (MostSignificantByteFirst) and "Opaque" can be selected. For '
        "opaque data endianness conversion shall be configured to Opaque. The value of this attribute impacts the absolute "
        "position of the signal into the SignalIPdu (see the startPosition attribute description). For an ISignalGroup the "
        "packingByteOrder is irrelevant and shall be ignored."
    ),
    "startPosition": (
        "This parameter is necessary to describe the bitposition of a signal within an SignalIPdu. It denotes the least "
        'significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see '
        'the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the '
        'bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most '
        "significant bit in byte 0 is bit 7. Please note that the way the bytes will be actually sent on the bus does not "
        "impact this representation: they will always be seen by the software as a byte array. If a mapping for the "
        "ISignalGroup is defined, this attribute is irrelevant and shall be ignored."
    ),
    "transferProperty": ("Defines how the referenced ISignal contributes to the send triggering of the ISignalIPdu."),
    "updateIndicationBitPosition": (
        "The UpdateIndicationBit indicates to the receivers that the signal (or the signal group) was updated by the sender. "
        "Length is always one bit. The UpdateIndicationBitPosition attribute describes the position of the update bit within "
        "the SignalIPdu. For Signals of a ISignalGroup this attribute is irrelevant and shall be ignored. Note that the exact "
        "bit position of the updateIndicationBit Position is linked to the value of the attribute packingByte Order because the "
        "method of finding the bit position is different for the values mostSignificantByteFirst and most SignificantByteLast. "
        "This means that if the value of packingByteOrder is changed while the value of update IndicationBitPosition remains "
        "unchanged the exact bit position of updateIndicationBitPosition within the enclosing ISignalIPdu still undergoes a "
        'change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big '
        'Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit '
        'counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with '
        "bit 0 (least significant bit). The most significant bit in byte 0 is bit 7."
    ),
}


class TestISignalToIPduMapping:
    """Test cases for ISignalToIPduMapping (Table 6.14, p.326)."""

    def test_inheritance(self):
        assert issubclass(ISignalToIPduMapping, Identifiable)
        assert issubclass(ISignalToIPduMapping, VariationPointCapable)

    def test_initialization_defaults(self):
        mapping = ISignalToIPduMapping(None, "Mapping")
        assert mapping.getISignalRef() is None
        assert mapping.getISignalGroupRef() is None
        assert mapping.getPackingByteOrder() is None
        assert mapping.getStartPosition() is None
        assert mapping.getTransferProperty() is None
        assert mapping.getUpdateIndicationBitPosition() is None
        assert mapping.getVariationPoint() is None

    def test_get_set_i_signal_ref(self):
        mapping = ISignalToIPduMapping(None, "Mapping")

        ref = RefType()
        ref.value = "/ISignals/ISignal1"
        assert mapping.setISignalRef(ref) is mapping
        assert mapping.getISignalRef() is ref
        mapping.setISignalRef(None)
        assert mapping.getISignalRef() is ref

    def test_get_set_i_signal_group_ref(self):
        mapping = ISignalToIPduMapping(None, "Mapping")

        ref = RefType()
        ref.value = "/ISignalGroups/ISignalGroup1"
        assert mapping.setISignalGroupRef(ref) is mapping
        assert mapping.getISignalGroupRef() is ref
        mapping.setISignalGroupRef(None)
        assert mapping.getISignalGroupRef() is ref

    def test_get_set_packing_byte_order(self):
        mapping = ISignalToIPduMapping(None, "Mapping")

        byte_order = ByteOrderEnum()
        byte_order.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST)
        assert mapping.setPackingByteOrder(byte_order) is mapping
        assert mapping.getPackingByteOrder() is byte_order
        mapping.setPackingByteOrder(None)
        assert mapping.getPackingByteOrder() is byte_order

    def test_get_set_start_position(self):
        mapping = ISignalToIPduMapping(None, "Mapping")

        position = UnlimitedInteger()
        position.setValue("8")
        assert mapping.setStartPosition(position) is mapping
        assert mapping.getStartPosition() is position
        assert mapping.getStartPosition().getValue() == 8
        mapping.setStartPosition(None)
        assert mapping.getStartPosition() is position

    def test_get_set_transfer_property(self):
        mapping = ISignalToIPduMapping(None, "Mapping")

        prop = TransferPropertyEnum()
        prop.setValue(TransferPropertyEnum.TRIGGERED)
        assert mapping.setTransferProperty(prop) is mapping
        assert mapping.getTransferProperty() is prop
        mapping.setTransferProperty(None)
        assert mapping.getTransferProperty() is prop

    def test_get_set_update_indication_bit_position(self):
        mapping = ISignalToIPduMapping(None, "Mapping")

        position = UnlimitedInteger()
        position.setValue("3")
        assert mapping.setUpdateIndicationBitPosition(position) is mapping
        assert mapping.getUpdateIndicationBitPosition() is position
        assert mapping.getUpdateIndicationBitPosition().getValue() == 3
        mapping.setUpdateIndicationBitPosition(None)
        assert mapping.getUpdateIndicationBitPosition() is position

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalToIPduMapping.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        mapping = ISignalToIPduMapping(None, "Mapping")
        pairs = (
            ("getISignalRef", "setISignalRef", "iSignalRef"),
            ("getISignalGroupRef", "setISignalGroupRef", "iSignalGroupRef"),
            ("getPackingByteOrder", "setPackingByteOrder", "packingByteOrder"),
            ("getStartPosition", "setStartPosition", "startPosition"),
            ("getTransferProperty", "setTransferProperty", "transferProperty"),
            ("getUpdateIndicationBitPosition", "setUpdateIndicationBitPosition", "updateIndicationBitPosition"),
        )
        for getter_name, mutator_name, key in pairs:
            getter = getattr(mapping, getter_name)
            mutator = getattr(mapping, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert ISignalToIPduMapping.__init__.__doc__ is None
