"""Reader tests for BusMirrorChannelMappingUserDefined (SystemTemplate TPS Table 6.334, p.707).

readBusMirrorChannelMappingUserDefined calls the base readBusMirrorChannelMapping
and reads TRANSMISSION-DEADLINE last per the XSD group
BUS-MIRROR-CHANNEL-MAPPING-USER-DEFINED (AUTOSAR_00052.xsd).
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMappingUserDefined
from tests.test_armodel.parser._helpers import _snip


class TestBusMirrorChannelMappingUserDefinedReader:
    def test_read_full_field_values(self, parser):
        mapping = BusMirrorChannelMappingUserDefined(None, "UserDefinedMapping")
        element = _snip(
            """
            <SHORT-NAME>UserDefinedMapping</SHORT-NAME>
            <MIRRORING-PROTOCOL>VERSION-1</MIRRORING-PROTOCOL>
            <SOURCE-CHANNEL>
                <BUS-MIRROR-NETWORK-ID>1</BUS-MIRROR-NETWORK-ID>
            </SOURCE-CHANNEL>
            <TARGET-CHANNEL>
                <BUS-MIRROR-NETWORK-ID>2</BUS-MIRROR-NETWORK-ID>
            </TARGET-CHANNEL>
            <TARGET-PDU-TRIGGERINGS>
                <PDU-TRIGGERING-REF-CONDITIONAL>
                    <PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/PduTriggering</PDU-TRIGGERING-REF>
                </PDU-TRIGGERING-REF-CONDITIONAL>
            </TARGET-PDU-TRIGGERINGS>
            <TRANSMISSION-DEADLINE>0.5</TRANSMISSION-DEADLINE>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-USER-DEFINED",
        )

        parser.readBusMirrorChannelMappingUserDefined(element, mapping)

        assert mapping.getShortName() == "UserDefinedMapping"
        assert mapping.getMirroringProtocol().getValue() == "VERSION-1"
        assert mapping.getSourceChannel() is not None
        assert mapping.getTargetChannel() is not None
        assert len(mapping.getTargetPduTriggeringRefs()) == 1
        assert mapping.getTransmissionDeadline().getValue() == 0.5

    def test_read_empty(self, parser):
        mapping = BusMirrorChannelMappingUserDefined(None, "UserDefinedMapping")
        element = _snip(
            """
            <SHORT-NAME>UserDefinedMapping</SHORT-NAME>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-USER-DEFINED",
        )

        parser.readBusMirrorChannelMappingUserDefined(element, mapping)

        assert mapping.getMirroringProtocol() is None
        assert mapping.getSourceChannel() is None
        assert mapping.getTargetChannel() is None
        assert mapping.getTargetPduTriggeringRefs() == []
        assert mapping.getTransmissionDeadline() is None
