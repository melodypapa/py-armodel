"""
Writer tests for StreamFilterIpv6Address (CP_TPS_SystemTemplate Table 3.90, p.138, R23-11).

Checks the child element values and the XSD sequence order (IPV-6-ADDRESS,
IPV-6-ADDRESS-MASK per group STREAM-FILTER-IPV-6-ADDRESS — the element is emitted in
live documents as the DESTINATION-IPV-6-ADDRESS / SOURCE-IPV-6-ADDRESS child of the
SWITCH-STREAM-FILTER-RULE IP/TP rule), the partial-emission case and the
write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_ipv6_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip6AddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterIpv6Address
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ipv6(value):
    ip = Ip6AddressString()
    ip.setValue(value)
    return ip


def _full_ipv6_address() -> StreamFilterIpv6Address:
    ipv6_address = StreamFilterIpv6Address()
    ipv6_address.setIpv6Address(_ipv6("2001:0DB8:0000:0000:0000:0000:0000:0001"))
    ipv6_address.setIpv6AddressMask(_ipv6("FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"))
    return ipv6_address


def _write(ipv6_address):
    element = ET.Element("DESTINATION-IPV-6-ADDRESS")
    ARXMLWriter().writeStreamFilterIpv6Address(element, ipv6_address)
    return element


class TestWriteStreamFilterIpv6Address:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_ipv6_address())

        assert [child.tag for child in element] == ["IPV-6-ADDRESS", "IPV-6-ADDRESS-MASK"]
        assert element.find("IPV-6-ADDRESS").text == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert element.find("IPV-6-ADDRESS-MASK").text == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"

    def test_write_partial_omits_absent_elements(self):
        ipv6_address = StreamFilterIpv6Address()
        ipv6_address.setIpv6AddressMask(_ipv6("FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"))

        element = _write(ipv6_address)

        assert [child.tag for child in element] == ["IPV-6-ADDRESS-MASK"]
        assert element.find("IPV-6-ADDRESS-MASK").text == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterIpv6Address())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_ipv6_address())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterIpv6Address()
        ARXMLParser(options={"warning": True}).readStreamFilterIpv6Address(namespaced, recovered)

        assert isinstance(recovered.getIpv6Address(), Ip6AddressString)
        assert recovered.getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert isinstance(recovered.getIpv6AddressMask(), Ip6AddressString)
        assert recovered.getIpv6AddressMask().getValue() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"
