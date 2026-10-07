"""
Tests for parsing AUTO-IP-PROPS elements (Ipv4AutoIpProps, Table 3.103, p.147).

Round-trip counterpart: tests/test_armodel/writer/test_ipv4_auto_ip_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4AutoIpProps
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


class TestReadIpv4AutoIpProps:
    """Test readIpv4AutoIpProps (Ipv4AutoIpProps, Table 3.103)."""

    def test_read_all_members(self, parser):
        """Every AUTO-IP-PROPS group element populates its model field with its value."""
        props = Ipv4AutoIpProps()
        element = ET.fromstring(
            f"""<AUTO-IP-PROPS xmlns='{NS}'>
                <TCP-IP-AUTO-IP-INIT-TIMEOUT>3.0</TCP-IP-AUTO-IP-INIT-TIMEOUT>
            </AUTO-IP-PROPS>"""
        )

        parser.readIpv4AutoIpProps(element, props)

        assert props.getTcpIpAutoIpInitTimeout().getValue() == 3.0

    def test_read_arobject_level(self, parser):
        """The ARObject level (checksum S / timestamp T) is populated via readARObject."""
        props = Ipv4AutoIpProps()
        element = ET.fromstring(
            f"""<AUTO-IP-PROPS xmlns='{NS}' S='123' T='2023-01-01T00:00:00Z'>
                <TCP-IP-AUTO-IP-INIT-TIMEOUT>1.5</TCP-IP-AUTO-IP-INIT-TIMEOUT>
            </AUTO-IP-PROPS>"""
        )

        parser.readIpv4AutoIpProps(element, props)

        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "123"
        assert props.getTimestamp() is not None
        assert props.getTimestamp().getValue() == "2023-01-01T00:00:00Z"
        assert props.getTcpIpAutoIpInitTimeout().getValue() == 1.5

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        props = Ipv4AutoIpProps()
        element = ET.fromstring(f"""<AUTO-IP-PROPS xmlns='{NS}'/>""")

        parser.readIpv4AutoIpProps(element, props)

        assert props.getTcpIpAutoIpInitTimeout() is None
