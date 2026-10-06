"""
Writer/reader round-trip tests for Ipv4ArpProps (Table 3.102, p.146).

XML element order per XSD IPV-4-ARP-PROPS group: TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP,
TCP-IP-ARP-PACKET-QUEUE-ENABLED, TCP-IP-ARP-REQUEST-TIMEOUT, TCP-IP-ARP-TABLE-ENTRY-TIMEOUT
(unwrapped direct children of ARP-PROPS).
writeIpv4Props dispatches ARP-PROPS to writeIpv4ArpProps since the Ipv4ArpProps sync
(Table 3.102) — the child is fully serialized, no longer identity-only.
writeIpv4ArpProps calls writeARObject on the ARP-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4ArpProps, Ipv4Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP",
    "TCP-IP-ARP-PACKET-QUEUE-ENABLED",
    "TCP-IP-ARP-REQUEST-TIMEOUT",
    "TCP-IP-ARP-TABLE-ENTRY-TIMEOUT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv4_arp_props():
    props = Ipv4ArpProps()
    props.setTcpIpArpNumGratuitousArpOnStartup(PositiveInteger().setValue(3))
    props.setTcpIpArpPacketQueueEnabled(Boolean().setValue(True))
    props.setTcpIpArpRequestTimeout(TimeValue().setValue(1.5))
    props.setTcpIpArpTableEntryTimeout(TimeValue().setValue(2.5))
    return props


def _write_ipv4_arp_props(props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv4ArpProps(parent, props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv4ArpProps:
    def test_members_in_xsd_order(self):
        parent = _write_ipv4_arp_props(_full_ipv4_arp_props())
        arp_props = parent.find("ARP-PROPS")

        children = [child.tag for child in arp_props]
        assert children == XSD_ORDER

    def test_members_written_with_field_values(self):
        parent = _write_ipv4_arp_props(_full_ipv4_arp_props())
        arp_props = parent.find("ARP-PROPS")

        assert arp_props.find("TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP").text == "3"
        assert arp_props.find("TCP-IP-ARP-PACKET-QUEUE-ENABLED").text == "true"
        assert arp_props.find("TCP-IP-ARP-REQUEST-TIMEOUT").text == "1.5"
        assert arp_props.find("TCP-IP-ARP-TABLE-ENTRY-TIMEOUT").text == "2.5"

    def test_bare_props_emits_no_group_children(self):
        parent = _write_ipv4_arp_props(Ipv4ArpProps())
        arp_props = parent.find("ARP-PROPS")

        assert len(list(arp_props)) == 0

    def test_checksum_emitted(self):
        props = Ipv4ArpProps()
        checksum = String()
        checksum.setValue("456")
        props.setChecksum(checksum)
        parent = _write_ipv4_arp_props(props)

        assert parent.find("ARP-PROPS").attrib.get("S") == "456"


class TestIpv4ArpPropsRoundTrip:
    def test_round_trip_full_through_arp_props(self):
        parent = _write_ipv4_arp_props(_full_ipv4_arp_props())
        reloaded = Ipv4ArpProps()
        ARXMLParser().readIpv4ArpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpArpNumGratuitousArpOnStartup().getValue() == 3
        assert reloaded.getTcpIpArpPacketQueueEnabled().getValue() is True
        assert reloaded.getTcpIpArpRequestTimeout().getValue() == 1.5
        assert reloaded.getTcpIpArpTableEntryTimeout().getValue() == 2.5

    def test_round_trip_empty_through_arp_props(self):
        parent = _write_ipv4_arp_props(Ipv4ArpProps())
        reloaded = Ipv4ArpProps()
        ARXMLParser().readIpv4ArpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpArpNumGratuitousArpOnStartup() is None
        assert reloaded.getTcpIpArpPacketQueueEnabled() is None
        assert reloaded.getTcpIpArpRequestTimeout() is None
        assert reloaded.getTcpIpArpTableEntryTimeout() is None

    def test_round_trip_full_through_ipv4_props_dispatch(self):
        """The upgraded Ipv4Props dispatch fully round-trips the ARP-PROPS child."""
        ipv4_props = Ipv4Props()
        ipv4_props.setArpProps(_full_ipv4_arp_props())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIpv4Props(parent, ipv4_props)

        arp_props_element = parent.find("IPV-4-PROPS/ARP-PROPS")
        xml_text = ET.tostring(parent.find("IPV-4-PROPS"), encoding="unicode")
        namespaced = ET.fromstring(xml_text.replace("IPV-4-PROPS", "IPV-4-PROPS xmlns='%s'" % NS, 1))

        assert arp_props_element.find("TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP").text == "3"

        reloaded = Ipv4Props()
        ARXMLParser().readIpv4Props(namespaced, reloaded)
        reloaded_arp = reloaded.getArpProps()
        assert isinstance(reloaded_arp, Ipv4ArpProps)
        assert reloaded_arp.getTcpIpArpNumGratuitousArpOnStartup().getValue() == 3
        assert reloaded_arp.getTcpIpArpPacketQueueEnabled().getValue() is True
        assert reloaded_arp.getTcpIpArpRequestTimeout().getValue() == 1.5
        assert reloaded_arp.getTcpIpArpTableEntryTimeout().getValue() == 2.5

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv4_props = Ipv4Props()
        ipv4_props.setArpProps(_full_ipv4_arp_props())
        eth_ip_props.setIpv4Props(ipv4_props)

        out_file = str(tmp_path / "ipv4_arp_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded_arp = reloaded_eth_ip_props.getIpv4Props().getArpProps()
        assert isinstance(reloaded_arp, Ipv4ArpProps)
        assert reloaded_arp.getTcpIpArpNumGratuitousArpOnStartup().getValue() == 3
        assert reloaded_arp.getTcpIpArpPacketQueueEnabled().getValue() is True
        assert reloaded_arp.getTcpIpArpRequestTimeout().getValue() == 1.5
        assert reloaded_arp.getTcpIpArpTableEntryTimeout().getValue() == 2.5
