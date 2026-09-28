"""Parser tests for FlexrayPhysicalChannel (Table 3.34, p.89).

XML element order per XSD group FLEXRAY-PHYSICAL-CHANNEL: CHANNEL-NAME (the only
class-own attribute; frameTriggerings/signalTriggerings etc. belong to the abstract
base PhysicalChannel, Table 3.7). Coverage runs through the PHYSICAL-CHANNELS
dispatch on readCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster, FlexrayPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CHANNEL = (
    "<PHYSICAL-CHANNELS>"
    "<FLEXRAY-PHYSICAL-CHANNEL>"
    "<SHORT-NAME>chan</SHORT-NAME>"
    "<CHANNEL-NAME>CHANNEL-A</CHANNEL-NAME>"
    "</FLEXRAY-PHYSICAL-CHANNEL>"
    "</PHYSICAL-CHANNELS>"
)

BARE_CHANNEL = "<PHYSICAL-CHANNELS>" "<FLEXRAY-PHYSICAL-CHANNEL>" "<SHORT-NAME>chan</SHORT-NAME>" "</FLEXRAY-PHYSICAL-CHANNEL>" "</PHYSICAL-CHANNELS>"


def _read_into_cluster(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = FlexrayCluster(pkg, "Cluster")
    ARXMLParser().readCommunicationClusterPhysicalChannels(root, cluster)
    return cluster


class TestReadFlexrayPhysicalChannel:
    def test_dispatch_creates_flexray_channel_with_short_name(self, parser):
        cluster = _read_into_cluster(BARE_CHANNEL)
        channels = cluster.getPhysicalChannels()
        assert len(channels) == 1
        channel = channels[0]
        assert isinstance(channel, FlexrayPhysicalChannel)
        assert channel.getShortName() == "chan"

    def test_reads_channel_name_with_value(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]

        channel_name = channel.getChannelName()
        assert channel_name is not None
        assert channel_name.getValue() == "CHANNEL-A"

    def test_reads_channel_without_channel_name_to_none(self, parser):
        cluster = _read_into_cluster(BARE_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        assert channel.getChannelName() is None
