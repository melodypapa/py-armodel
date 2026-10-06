"""
Tests for parsing IPV-4-PROPS elements (Ipv4Props, Table 3.101, p.146).

Round-trip counterpart: tests/test_armodel/writer/test_ipv4_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Ipv4FragmentationProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4ArpProps, Ipv4AutoIpProps, Ipv4Props
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


class TestReadIpv4Props:
    """Test readIpv4Props (Ipv4Props, Table 3.101)."""

    def test_read_all_members(self, parser):
        """Every IPV-4-PROPS group element populates its model field."""
        ipv4_props = Ipv4Props()
        element = ET.fromstring(
            f"""<IPV-4-PROPS xmlns='{NS}'>
                <ARP-PROPS/>
                <AUTO-IP-PROPS/>
                <FRAGMENTATION-PROPS/>
            </IPV-4-PROPS>"""
        )

        parser.readIpv4Props(element, ipv4_props)

        assert isinstance(ipv4_props.getArpProps(), Ipv4ArpProps)
        assert isinstance(ipv4_props.getAutoIpProps(), Ipv4AutoIpProps)
        assert isinstance(ipv4_props.getFragmentationProps(), Ipv4FragmentationProps)

    def test_read_arobject_levels(self, parser):
        """The ARObject levels (checksum S / timestamp T) are populated via readARObject."""
        ipv4_props = Ipv4Props()
        element = ET.fromstring(
            f"""<IPV-4-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <ARP-PROPS/>
            </IPV-4-PROPS>"""
        )

        parser.readIpv4Props(element, ipv4_props)

        assert ipv4_props.getChecksum() is not None
        assert ipv4_props.getChecksum().getValue() == "123"
        assert ipv4_props.getTimestamp() is not None
        assert ipv4_props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert isinstance(ipv4_props.getArpProps(), Ipv4ArpProps)

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        ipv4_props = Ipv4Props()
        element = ET.fromstring(f"""<IPV-4-PROPS xmlns='{NS}'/>""")

        parser.readIpv4Props(element, ipv4_props)

        assert ipv4_props.getArpProps() is None
        assert ipv4_props.getAutoIpProps() is None
        assert ipv4_props.getFragmentationProps() is None
