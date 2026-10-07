"""
Reader tests for StreamFilterIpv6Address (CP_TPS_SystemTemplate Table 3.90, p.138, R23-11).

Covers the IPV-6-ADDRESS / IPV-6-ADDRESS-MASK children of the STREAM-FILTER-IPV-6-ADDRESS
element shape (AUTOSAR_00052.xsd group STREAM-FILTER-IPV-6-ADDRESS — emitted in live
documents as the DESTINATION-IPV-6-ADDRESS / SOURCE-IPV-6-ADDRESS children of the
SWITCH-STREAM-FILTER-RULE IP/TP rule), the absent-element case and the
empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_ipv6_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip6AddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterIpv6Address
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DESTINATION-IPV-6-ADDRESS xmlns='{NS}'>{inner}</DESTINATION-IPV-6-ADDRESS>")


class TestReadStreamFilterIpv6Address:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<IPV-6-ADDRESS>2001:0DB8:0000:0000:0000:0000:0000:0001</IPV-6-ADDRESS>" "<IPV-6-ADDRESS-MASK>FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00</IPV-6-ADDRESS-MASK>")
        ipv6_address = StreamFilterIpv6Address()
        parser.readStreamFilterIpv6Address(element, ipv6_address)

        assert isinstance(ipv6_address.getIpv6Address(), Ip6AddressString)
        assert ipv6_address.getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert isinstance(ipv6_address.getIpv6AddressMask(), Ip6AddressString)
        assert ipv6_address.getIpv6AddressMask().getValue() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<IPV-6-ADDRESS>FE80:0000:0000:0000:0000:0000:0000:0001</IPV-6-ADDRESS>")
        ipv6_address = StreamFilterIpv6Address()
        parser.readStreamFilterIpv6Address(element, ipv6_address)

        assert ipv6_address.getIpv6Address().getValue() == "FE80:0000:0000:0000:0000:0000:0000:0001"
        assert ipv6_address.getIpv6AddressMask() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        ipv6_address = StreamFilterIpv6Address()
        parser.readStreamFilterIpv6Address(element, ipv6_address)

        assert ipv6_address.getIpv6Address() is None
        assert ipv6_address.getIpv6AddressMask() is None
