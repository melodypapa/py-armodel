"""
Tests for parsing ARP-PROPS elements (Ipv4ArpProps, Table 3.102, p.146).

Round-trip counterpart: tests/test_armodel/writer/test_ipv4_arp_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4ArpProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadIpv4ArpProps:
    """Test readIpv4ArpProps (Ipv4ArpProps, Table 3.102)."""

    def test_read_all_members(self, parser):
        """Every ARP-PROPS group element populates its model field with its value."""
        props = Ipv4ArpProps()
        element = ET.fromstring(
            f"""<ARP-PROPS xmlns='{NS}'>
                <TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP>3</TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP>
                <TCP-IP-ARP-PACKET-QUEUE-ENABLED>true</TCP-IP-ARP-PACKET-QUEUE-ENABLED>
                <TCP-IP-ARP-REQUEST-TIMEOUT>1.5</TCP-IP-ARP-REQUEST-TIMEOUT>
                <TCP-IP-ARP-TABLE-ENTRY-TIMEOUT>2.5</TCP-IP-ARP-TABLE-ENTRY-TIMEOUT>
            </ARP-PROPS>"""
        )

        parser.readIpv4ArpProps(element, props)

        assert props.getTcpIpArpNumGratuitousArpOnStartup().getValue() == 3
        assert props.getTcpIpArpPacketQueueEnabled().getValue() is True
        assert props.getTcpIpArpRequestTimeout().getValue() == 1.5
        assert props.getTcpIpArpTableEntryTimeout().getValue() == 2.5

    def test_read_arobject_level(self, parser):
        """The ARObject level (checksum S / timestamp T) is populated via readARObject."""
        props = Ipv4ArpProps()
        element = ET.fromstring(
            f"""<ARP-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <TCP-IP-ARP-PACKET-QUEUE-ENABLED>false</TCP-IP-ARP-PACKET-QUEUE-ENABLED>
            </ARP-PROPS>"""
        )

        parser.readIpv4ArpProps(element, props)

        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "123"
        assert props.getTimestamp() is not None
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert props.getTcpIpArpPacketQueueEnabled().getValue() is False

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        props = Ipv4ArpProps()
        element = ET.fromstring(f"""<ARP-PROPS xmlns='{NS}'/>""")

        parser.readIpv4ArpProps(element, props)

        assert props.getTcpIpArpNumGratuitousArpOnStartup() is None
        assert props.getTcpIpArpPacketQueueEnabled() is None
        assert props.getTcpIpArpRequestTimeout() is None
        assert props.getTcpIpArpTableEntryTimeout() is None
