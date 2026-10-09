"""Reader tests for BusMirrorChannelMappingIp (SystemTemplate TPS Table 6.333, p.706).

readBusMirrorChannelMappingIp calls the base readBusMirrorChannelMapping
and reads TRANSMISSION-DEADLINE last per the XSD group
BUS-MIRROR-CHANNEL-MAPPING-IP (AUTOSAR_00052.xsd).
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMappingIp
from tests.test_armodel.parser._helpers import _snip


class TestBusMirrorChannelMappingIpReader:
    def test_read_full_field_values(self, parser):
        mapping = BusMirrorChannelMappingIp(None, "IpMapping")
        element = _snip(
            """
            <SHORT-NAME>IpMapping</SHORT-NAME>
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
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-IP",
        )

        parser.readBusMirrorChannelMappingIp(element, mapping)

        assert mapping.getShortName() == "IpMapping"
        assert mapping.getMirroringProtocol().getValue() == "VERSION-1"
        assert mapping.getSourceChannel() is not None
        assert mapping.getTargetChannel() is not None
        assert len(mapping.getTargetPduTriggeringRefs()) == 1
        assert mapping.getTransmissionDeadline().getValue() == 0.5

    def test_read_empty(self, parser):
        mapping = BusMirrorChannelMappingIp(None, "IpMapping")
        element = _snip(
            """
            <SHORT-NAME>IpMapping</SHORT-NAME>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-IP",
        )

        parser.readBusMirrorChannelMappingIp(element, mapping)

        assert mapping.getMirroringProtocol() is None
        assert mapping.getSourceChannel() is None
        assert mapping.getTargetChannel() is None
        assert mapping.getTargetPduTriggeringRefs() == []
        assert mapping.getTransmissionDeadline() is None
