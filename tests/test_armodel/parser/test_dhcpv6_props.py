"""
Tests for parsing DHCP-PROPS elements (Dhcpv6Props, Table 3.107, p.149).

The instance element is <DHCP-PROPS> (XSD type AR:DHCPV-6-PROPS;
DHCPV-6-PROPS group contents) — the type name is the XSD group/complexType
name only, the instance tag under IPV-6-PROPS stays DHCP-PROPS.
Round-trip counterpart: tests/test_armodel/writer/test_dhcpv6_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Dhcpv6Props
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


class TestReadDhcpv6Props:
    """Test readDhcpv6Props (Dhcpv6Props, Table 3.107)."""

    def test_read_all_members(self, parser):
        """Every DHCPV-6-PROPS group element populates its model field with its value."""
        props = Dhcpv6Props()
        element = ET.fromstring(
            f"""<DHCP-PROPS xmlns='{NS}'>
                <TCP-IP-DHCP-V-6-CNF-DELAY-MAX>100.0</TCP-IP-DHCP-V-6-CNF-DELAY-MAX>
                <TCP-IP-DHCP-V-6-CNF-DELAY-MIN>1.0</TCP-IP-DHCP-V-6-CNF-DELAY-MIN>
                <TCP-IP-DHCP-V-6-INF-DELAY-MAX>110.0</TCP-IP-DHCP-V-6-INF-DELAY-MAX>
                <TCP-IP-DHCP-V-6-INF-DELAY-MIN>2.0</TCP-IP-DHCP-V-6-INF-DELAY-MIN>
                <TCP-IP-DHCP-V-6-SOL-DELAY-MAX>120.0</TCP-IP-DHCP-V-6-SOL-DELAY-MAX>
                <TCP-IP-DHCP-V-6-SOL-DELAY-MIN>3.0</TCP-IP-DHCP-V-6-SOL-DELAY-MIN>
            </DHCP-PROPS>"""
        )

        parser.readDhcpv6Props(element, props)

        assert props.getTcpIpDhcpV6CnfDelayMax().getValue() == 100.0
        assert props.getTcpIpDhcpV6CnfDelayMin().getValue() == 1.0
        assert props.getTcpIpDhcpV6InfDelayMax().getValue() == 110.0
        assert props.getTcpIpDhcpV6InfDelayMin().getValue() == 2.0
        assert props.getTcpIpDhcpV6SolDelayMax().getValue() == 120.0
        assert props.getTcpIpDhcpV6SolDelayMin().getValue() == 3.0

    def test_read_arobject_level(self, parser):
        """The ARObject level (checksum S / timestamp T) is populated via readARObject."""
        props = Dhcpv6Props()
        element = ET.fromstring(
            f"""<DHCP-PROPS xmlns='{NS}' S='456' T='2023-01-01T00:00:00Z'>
                <TCP-IP-DHCP-V-6-CNF-DELAY-MIN>1.0</TCP-IP-DHCP-V-6-CNF-DELAY-MIN>
            </DHCP-PROPS>"""
        )

        parser.readDhcpv6Props(element, props)

        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "456"
        assert props.getTimestamp() is not None
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert props.getTcpIpDhcpV6CnfDelayMin().getValue() == 1.0

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        props = Dhcpv6Props()
        element = ET.fromstring(f"""<DHCP-PROPS xmlns='{NS}'/>""")

        parser.readDhcpv6Props(element, props)

        assert props.getTcpIpDhcpV6CnfDelayMax() is None
        assert props.getTcpIpDhcpV6CnfDelayMin() is None
        assert props.getTcpIpDhcpV6InfDelayMax() is None
        assert props.getTcpIpDhcpV6InfDelayMin() is None
        assert props.getTcpIpDhcpV6SolDelayMax() is None
        assert props.getTcpIpDhcpV6SolDelayMin() is None
