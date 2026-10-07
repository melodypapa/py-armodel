"""
Tests for parsing FRAGMENTATION-PROPS elements (Ipv6FragmentationProps, Table 3.106, p.148).

The instance element is <FRAGMENTATION-PROPS> (XSD type AR:IPV-6-FRAGMENTATION-PROPS;
IPV-6-FRAGMENTATION-PROPS group contents) — the type name is the XSD group/complexType
name only, the instance tag under IPV-6-PROPS stays FRAGMENTATION-PROPS.
Round-trip counterpart: tests/test_armodel/writer/test_ipv6_fragmentation_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6FragmentationProps
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


class TestReadIpv6FragmentationProps:
    """Test readIpv6FragmentationProps (Ipv6FragmentationProps, Table 3.106)."""

    def test_read_all_members(self, parser):
        """Every FRAGMENTATION-PROPS group element populates its model field with its value."""
        props = Ipv6FragmentationProps()
        element = ET.fromstring(
            f"""<FRAGMENTATION-PROPS xmlns='{NS}'>
                <TCP-IP-IP-REASSEMBLY-BUFFER-COUNT>4</TCP-IP-IP-REASSEMBLY-BUFFER-COUNT>
                <TCP-IP-IP-REASSEMBLY-BUFFER-SIZE>1500</TCP-IP-IP-REASSEMBLY-BUFFER-SIZE>
                <TCP-IP-IP-REASSEMBLY-SEGMENT-COUNT>2</TCP-IP-IP-REASSEMBLY-SEGMENT-COUNT>
                <TCP-IP-IP-REASSEMBLY-TIMEOUT>1.0</TCP-IP-IP-REASSEMBLY-TIMEOUT>
                <TCP-IP-IP-TX-FRAGMENT-BUFFER-COUNT>5</TCP-IP-IP-TX-FRAGMENT-BUFFER-COUNT>
                <TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE>1500</TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE>
            </FRAGMENTATION-PROPS>"""
        )

        parser.readIpv6FragmentationProps(element, props)

        assert props.getTcpIpIpReassemblyBufferCount().getValue() == 4
        assert props.getTcpIpIpReassemblyBufferSize().getValue() == 1500
        assert props.getTcpIpIpReassemblySegmentCount().getValue() == 2
        assert props.getTcpIpIpReassemblyTimeout().getValue() == 1.0
        assert props.getTcpIpIpTxFragmentBufferCount().getValue() == 5
        assert props.getTcpIpIpTxFragmentBufferSize().getValue() == 1500

    def test_read_arobject_level(self, parser):
        """The ARObject level (checksum S / timestamp T) is populated via readARObject."""
        props = Ipv6FragmentationProps()
        element = ET.fromstring(
            f"""<FRAGMENTATION-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <TCP-IP-IP-REASSEMBLY-BUFFER-COUNT>4</TCP-IP-IP-REASSEMBLY-BUFFER-COUNT>
            </FRAGMENTATION-PROPS>"""
        )

        parser.readIpv6FragmentationProps(element, props)

        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "123"
        assert props.getTimestamp() is not None
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert props.getTcpIpIpReassemblyBufferCount().getValue() == 4

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        props = Ipv6FragmentationProps()
        element = ET.fromstring(f"""<FRAGMENTATION-PROPS xmlns='{NS}'/>""")

        parser.readIpv6FragmentationProps(element, props)

        assert props.getTcpIpIpReassemblyBufferCount() is None
        assert props.getTcpIpIpReassemblyBufferSize() is None
        assert props.getTcpIpIpReassemblySegmentCount() is None
        assert props.getTcpIpIpReassemblyTimeout() is None
        assert props.getTcpIpIpTxFragmentBufferCount() is None
        assert props.getTcpIpIpTxFragmentBufferSize() is None
