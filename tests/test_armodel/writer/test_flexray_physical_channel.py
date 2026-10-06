"""Writer round-trip tests for FlexrayPhysicalChannel (Table 3.34, p.89).

XML element order per XSD group FLEXRAY-PHYSICAL-CHANNEL: CHANNEL-NAME (the only
class-own attribute; frameTriggerings/signalTriggerings etc. belong to the abstract
base PhysicalChannel, Table 3.7). Coverage runs through the PHYSICAL-CHANNELS
dispatch on writeCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster, FlexrayPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import FlexrayChannelName
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["CHANNEL-NAME"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_cluster_with_channel():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = FlexrayCluster(pkg, "Cluster")
    channel = cluster.createFlexrayPhysicalChannel("chan")
    channel.setChannelName(FlexrayChannelName().setValue(FlexrayChannelName.CHANNEL_A))
    return cluster


def _write_cluster(cluster):
    parent = ET.Element("FLEXRAY-CLUSTER")
    ARXMLWriter().writeCommunicationClusterPhysicalChannels(parent, cluster)
    return parent


class TestWriteFlexrayPhysicalChannel:
    def test_write_all_fields_in_xsd_order(self):
        parent = _write_cluster(_new_cluster_with_channel())
        channel_tag = parent.find("PHYSICAL-CHANNELS/FLEXRAY-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        tags = [child.tag for child in channel_tag]
        assert tags == ["SHORT-NAME"] + XSD_ORDER

    def test_write_field_values(self):
        parent = _write_cluster(_new_cluster_with_channel())
        channel_tag = parent.find("PHYSICAL-CHANNELS/FLEXRAY-PHYSICAL-CHANNEL")
        assert channel_tag.find("CHANNEL-NAME").text == "CHANNEL-A"

    def test_write_channel_without_flexray_fields_omits_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        cluster = FlexrayCluster(pkg, "Cluster")
        cluster.createFlexrayPhysicalChannel("chan")
        parent = _write_cluster(cluster)
        channel_tag = parent.find("PHYSICAL-CHANNELS/FLEXRAY-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        tags = [child.tag for child in channel_tag]
        for flexray_tag in XSD_ORDER:
            assert flexray_tag not in tags

    def test_round_trip_preserves_all_values(self):
        cluster = _new_cluster_with_channel()
        parent = _write_cluster(cluster)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parsed_cluster = FlexrayCluster(parsed_pkg, "Cluster")
        ARXMLParser().readCommunicationClusterPhysicalChannels(root[0], parsed_cluster)

        channel = parsed_cluster.getPhysicalChannels()[0]
        assert isinstance(channel, FlexrayPhysicalChannel)
        assert channel.getShortName() == "chan"
        assert channel.getChannelName() is not None
        assert channel.getChannelName().getValue() == FlexrayChannelName.CHANNEL_A
