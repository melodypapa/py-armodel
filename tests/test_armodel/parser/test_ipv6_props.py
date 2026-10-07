"""
Tests for parsing IPV-6-PROPS elements (Ipv6Props, Table 3.105, p.148).

Round-trip counterpart: tests/test_armodel/writer/test_ipv6_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Ipv6NdpProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Dhcpv6Props, Ipv6FragmentationProps, Ipv6Props
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


class TestReadIpv6Props:
    """Test readIpv6Props (Ipv6Props, Table 3.105)."""

    def test_read_all_members(self, parser):
        """Every IPV-6-PROPS group element populates its model field."""
        ipv6_props = Ipv6Props()
        element = ET.fromstring(
            f"""<IPV-6-PROPS xmlns='{NS}'>
                <DHCP-PROPS/>
                <FRAGMENTATION-PROPS/>
                <NDP-PROPS/>
            </IPV-6-PROPS>"""
        )

        parser.readIpv6Props(element, ipv6_props)

        assert isinstance(ipv6_props.getDhcpProps(), Dhcpv6Props)
        assert isinstance(ipv6_props.getFragmentationProps(), Ipv6FragmentationProps)
        assert isinstance(ipv6_props.getNdpProps(), Ipv6NdpProps)

    def test_read_arobject_levels(self, parser):
        """The ARObject levels (checksum S / timestamp T) are populated via readARObject."""
        ipv6_props = Ipv6Props()
        element = ET.fromstring(
            f"""<IPV-6-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <DHCP-PROPS/>
            </IPV-6-PROPS>"""
        )

        parser.readIpv6Props(element, ipv6_props)

        assert ipv6_props.getChecksum() is not None
        assert ipv6_props.getChecksum().getValue() == "123"
        assert ipv6_props.getTimestamp() is not None
        assert ipv6_props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert isinstance(ipv6_props.getDhcpProps(), Dhcpv6Props)

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        ipv6_props = Ipv6Props()
        element = ET.fromstring(f"""<IPV-6-PROPS xmlns='{NS}'/>""")

        parser.readIpv6Props(element, ipv6_props)

        assert ipv6_props.getDhcpProps() is None
        assert ipv6_props.getFragmentationProps() is None
        assert ipv6_props.getNdpProps() is None
