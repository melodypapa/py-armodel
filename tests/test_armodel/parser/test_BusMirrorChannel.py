"""Reader tests for BusMirrorChannel (SystemTemplate TPS Table 6.327, p.698).

getBusMirrorChannel populates the model via setBusMirrorNetworkId /
setChannelRef, with the CHANNELS wrapper (PHYSICAL-CHANNEL-REF-CONDITIONAL)
last per the XSD group BUS-MIRROR-CHANNEL (AUTOSAR_00052.xsd). The helper is
exercised through its real call path, readBusMirrorChannelMapping's
SOURCE-CHANNEL / TARGET-CHANNEL branches.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMapping
from tests.test_armodel.parser._helpers import _snip


class _ConcreteMapping(BusMirrorChannelMapping):
    pass


class TestBusMirrorChannelReader:
    def test_read_full_field_values(self, parser):
        mapping = _ConcreteMapping(None, "Mapping")
        element = _snip(
            """
            <SHORT-NAME>Mapping</SHORT-NAME>
            <SOURCE-CHANNEL S="1234">
                <BUS-MIRROR-NETWORK-ID>1</BUS-MIRROR-NETWORK-ID>
                <CHANNELS>
                    <PHYSICAL-CHANNEL-REF-CONDITIONAL>
                        <PHYSICAL-CHANNEL-REF DEST="CAN-PHYSICAL-CHANNEL">/BusMirror/CanPhysicalChannel</PHYSICAL-CHANNEL-REF>
                    </PHYSICAL-CHANNEL-REF-CONDITIONAL>
                </CHANNELS>
            </SOURCE-CHANNEL>
            <TARGET-CHANNEL>
                <BUS-MIRROR-NETWORK-ID>2</BUS-MIRROR-NETWORK-ID>
            </TARGET-CHANNEL>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-CAN",
        )

        parser.readBusMirrorChannelMapping(element, mapping)

        source_channel = mapping.getSourceChannel()
        assert source_channel is not None
        assert source_channel.getChecksum().getValue() == "1234"
        assert source_channel.getBusMirrorNetworkId().getValue() == 1
        assert source_channel.getChannelRef().getValue() == "/BusMirror/CanPhysicalChannel"
        assert source_channel.getChannelRef().getDest() == "CAN-PHYSICAL-CHANNEL"

        target_channel = mapping.getTargetChannel()
        assert target_channel is not None
        assert target_channel.getBusMirrorNetworkId().getValue() == 2
        assert target_channel.getChannelRef() is None

    def test_read_empty(self, parser):
        mapping = _ConcreteMapping(None, "Mapping")
        element = _snip(
            """
            <SHORT-NAME>Mapping</SHORT-NAME>
            <SOURCE-CHANNEL/>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-CAN",
        )

        parser.readBusMirrorChannelMapping(element, mapping)

        source_channel = mapping.getSourceChannel()
        assert source_channel is not None
        assert source_channel.getBusMirrorNetworkId() is None
        assert source_channel.getChannelRef() is None
