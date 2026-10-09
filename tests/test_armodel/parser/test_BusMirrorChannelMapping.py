"""Reader tests for BusMirrorChannelMapping (SystemTemplate TPS Table 6.325, p.697).

readBusMirrorChannelMapping populates the model via setMirroringProtocol /
setSourceChannel / setTargetChannel / addTargetPduTriggeringRef, with the
TARGET-PDU-TRIGGERINGS wrapper list last per the XSD group
BUS-MIRROR-CHANNEL-MAPPING (AUTOSAR_00052.xsd).
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMapping, MirroringProtocolEnum
from tests.test_armodel.parser._helpers import _snip


class _ConcreteMapping(BusMirrorChannelMapping):
    pass


class TestBusMirrorChannelMappingReader:
    def test_read_full_field_values(self, parser):
        mapping = _ConcreteMapping(None, "Mapping")
        element = _snip(
            """
            <SHORT-NAME>Mapping</SHORT-NAME>
            <MIRRORING-PROTOCOL>VERSION-1</MIRRORING-PROTOCOL>
            <SOURCE-CHANNEL S="1234">
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
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-CAN",
        )

        parser.readBusMirrorChannelMapping(element, mapping)

        protocol = mapping.getMirroringProtocol()
        assert isinstance(protocol, MirroringProtocolEnum)
        assert protocol.getValue() == "VERSION-1"
        source_channel = mapping.getSourceChannel()
        assert source_channel is not None
        assert source_channel.getChecksum().getValue() == "1234"
        assert mapping.getTargetChannel() is not None
        refs = mapping.getTargetPduTriggeringRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Fibex/PduTriggering"
        assert refs[0].getDest() == "PDU-TRIGGERING"

    def test_read_empty(self, parser):
        mapping = _ConcreteMapping(None, "Mapping")
        element = _snip(
            """
            <SHORT-NAME>Mapping</SHORT-NAME>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-CAN",
        )

        parser.readBusMirrorChannelMapping(element, mapping)

        assert mapping.getMirroringProtocol() is None
        assert mapping.getSourceChannel() is None
        assert mapping.getTargetChannel() is None
        assert mapping.getTargetPduTriggeringRefs() == []
