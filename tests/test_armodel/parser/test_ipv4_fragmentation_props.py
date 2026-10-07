"""
Tests for parsing FRAGMENTATION-PROPS elements (Ipv4FragmentationProps, Table 3.104, p.147).

The instance element is <FRAGMENTATION-PROPS> (XSD type AR:IPV-4-FRAGMENTATION-PROPS;
IPV-4-FRAGMENTATION-PROPS group contents).
Round-trip counterpart: tests/test_armodel/writer/test_ipv4_fragmentation_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4FragmentationProps
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


class TestReadIpv4FragmentationProps:
    """Test readIpv4FragmentationProps (Ipv4FragmentationProps, Table 3.104)."""

    def test_read_all_members(self, parser):
        """Every FRAGMENTATION-PROPS group element populates its model field with its value."""
        props = Ipv4FragmentationProps()
        element = ET.fromstring(
            f"""<FRAGMENTATION-PROPS xmlns='{NS}'>
                <TCP-IP-IP-FRAGMENTATION-RX-ENABLED>true</TCP-IP-IP-FRAGMENTATION-RX-ENABLED>
                <TCP-IP-IP-NUM-FRAGMENTS>8</TCP-IP-IP-NUM-FRAGMENTS>
                <TCP-IP-IP-NUM-REASS-DGRAMS>4</TCP-IP-IP-NUM-REASS-DGRAMS>
                <TCP-IP-IP-REASS-TIMEOUT>15.0</TCP-IP-IP-REASS-TIMEOUT>
            </FRAGMENTATION-PROPS>"""
        )

        parser.readIpv4FragmentationProps(element, props)

        assert props.getTcpIpIpFragmentationRxEnabled().getValue() is True
        assert props.getTcpIpIpNumFragments().getValue() == 8
        assert props.getTcpIpIpNumReassDgrams().getValue() == 4
        assert props.getTcpIpIpReassTimeout().getValue() == 15.0

    def test_read_arobject_level(self, parser):
        """The ARObject level (checksum S / timestamp T) is populated via readARObject."""
        props = Ipv4FragmentationProps()
        element = ET.fromstring(
            f"""<FRAGMENTATION-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <TCP-IP-IP-NUM-FRAGMENTS>8</TCP-IP-IP-NUM-FRAGMENTS>
            </FRAGMENTATION-PROPS>"""
        )

        parser.readIpv4FragmentationProps(element, props)

        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "123"
        assert props.getTimestamp() is not None
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert props.getTcpIpIpNumFragments().getValue() == 8

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        props = Ipv4FragmentationProps()
        element = ET.fromstring(f"""<FRAGMENTATION-PROPS xmlns='{NS}'/>""")

        parser.readIpv4FragmentationProps(element, props)

        assert props.getTcpIpIpFragmentationRxEnabled() is None
        assert props.getTcpIpIpNumFragments() is None
        assert props.getTcpIpIpNumReassDgrams() is None
        assert props.getTcpIpIpReassTimeout() is None
