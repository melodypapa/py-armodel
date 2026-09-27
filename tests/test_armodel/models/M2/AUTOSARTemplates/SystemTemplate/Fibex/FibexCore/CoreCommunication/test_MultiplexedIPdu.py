import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ByteOrderEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DynamicPart,
    MultiplexedIPdu,
    StaticPart,
    TriggerMode,
)

CLASS_NOTE = (
    "A MultiplexedPdu (i.e. NOT a COM I-PDU) contains a DynamicPart, an optional StaticPart and a selector Field. "
    "In case of multiplexing this IPdu is routed between the Pdu Multiplexer and the Interface Layer. A multiplexer "
    "is used to define variable parts within an IPdu that may carry different signals. The receivers of such a IPdu "
    "can determine which signalPdus are transmitted by evaluating the selector field, which carries a unique selector "
    "code for each sub-part. Tags: atp.recommendedPackage=Pdus"
)
NOTES = {
    "dynamicPart": (
        "According to the value of the selector field some parts of the IPdu have a different layout. In a complete "
        "System Description a MultiplexedIPdu shall contain a Dynamic Part. The following use cases support the "
        "multiplicity to be 0..1: • If a MultiplexedIPdu is received by a Pdu Gateway and is not delivered to the IPduM "
        "but routed directly to a bus interface then the content of the MulitplexedIPdu doesn't need to be described in "
        "the System Extract/ Ecu Extract. • If a MultiplexedIPdu is received by an ECU which is only interested in the "
        "static part of the MultiplexedIPdu then the dynamicPart does not need to be described in the System "
        "Extract/Ecu Extract. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; "
        "atpVariation Tags: atp.Splitkey=dynamicPart, dynamicPart.variation Point.shortLabel "
        "vh.latestBindingTime=postBuild"
    ),
    "selectorFieldByteOrder": (
        "This attribute defines the order of the bytes of the selector Field and the packing into the MultiplexedIPdu. "
        "Please consider that [constr_3247] and [constr_3223] are restricting the usage of this attribute. In a complete "
        "System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not "
        "delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't "
        "need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1."
    ),
    "selectorFieldLength": (
        "The size in bits of the selector field shall be configurable in a range of 1-16 bits. In a complete System "
        "Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered "
        "to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be "
        "described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1."
    ),
    "selectorFieldStartPosition": (
        "This parameter is necessary to describe the position of the selector field within the IPdu. Note that the "
        "absolute position of the selectorField in the MultiplexedIPdu is determined by the definition of the "
        "selectorFieldByteOrder attribute of the Multiplexed Pdu. If Big Endian is specified, the start position "
        "indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start "
        "position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is "
        'always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 '
        "(least significant bit). The most significant bit in byte 0 is bit 7. In a complete System Description this "
        "attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but "
        "routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the "
        "System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1."
    ),
    "staticPart": (
        "The static part of the multiplexed IPdu is the same regardless of the selector field. The static part is "
        "optional. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=staticPart, staticPart.variationPoint.short Label vh.latestBindingTime=postBuild"
    ),
    "triggerMode": (
        "IPduM can be configured to send a transmission request for the new multiplexed IPdu to the PDU-Router because "
        "of the trigger conditions/ modes that are described in the TriggerMode enumeration. In a complete System "
        "Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered "
        "to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be "
        "described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1."
    ),
    "unusedBitPattern": (
        "AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPdu with this bit-pattern. This attribute is "
        "mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu. In a complete "
        "System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not "
        "delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't "
        "need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1."
    ),
}


class TestMultiplexedIPdu:
    """Test cases for MultiplexedIPdu (Table 6.72, p.410)."""

    def test_initialization_defaults(self):
        ipdu = MultiplexedIPdu(None, "Ipdu")
        assert ipdu.getDynamicPart() is None
        assert ipdu.getSelectorFieldByteOrder() is None
        assert ipdu.getSelectorFieldLength() is None
        assert ipdu.getSelectorFieldStartPosition() is None
        assert ipdu.getStaticPart() is None
        assert ipdu.getTriggerMode() is None
        assert ipdu.getUnusedBitPattern() is None

    def test_get_set_round_trip_and_none_noop(self):
        ipdu = MultiplexedIPdu(None, "Ipdu")

        dynamic_part = DynamicPart()
        assert ipdu.setDynamicPart(dynamic_part) is ipdu
        assert ipdu.getDynamicPart() is dynamic_part
        ipdu.setDynamicPart(None)
        assert ipdu.getDynamicPart() is dynamic_part

        static_part = StaticPart()
        assert ipdu.setStaticPart(static_part) is ipdu
        assert ipdu.getStaticPart() is static_part

        byte_order = ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST)
        assert ipdu.setSelectorFieldByteOrder(byte_order) is ipdu
        assert ipdu.getSelectorFieldByteOrder() is byte_order

        assert ipdu.setSelectorFieldLength(4) is ipdu
        assert ipdu.getSelectorFieldLength() == 4

        assert ipdu.setSelectorFieldStartPosition(8) is ipdu
        assert ipdu.getSelectorFieldStartPosition() == 8

        trigger_mode = TriggerMode().setValue(TriggerMode.STATIC_PART_TRIGGER)
        assert ipdu.setTriggerMode(trigger_mode) is ipdu
        assert ipdu.getTriggerMode() is trigger_mode

        assert ipdu.setUnusedBitPattern(0xFF) is ipdu
        assert ipdu.getUnusedBitPattern() == 0xFF

    def test_class_docstring_note(self):
        assert inspect.cleandoc(MultiplexedIPdu.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        ipdu = MultiplexedIPdu(None, "Ipdu")
        for attr in (
            "dynamicPart",
            "selectorFieldByteOrder",
            "selectorFieldLength",
            "selectorFieldStartPosition",
            "staticPart",
            "triggerMode",
            "unusedBitPattern",
        ):
            getter = getattr(ipdu, "get" + attr[0].upper() + attr[1:])
            setter = getattr(ipdu, "set" + attr[0].upper() + attr[1:])
            assert inspect.cleandoc(getter.__doc__) == NOTES[attr], attr
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == NOTES[attr], attr
