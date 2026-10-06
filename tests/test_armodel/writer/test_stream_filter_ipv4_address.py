"""
Writer tests for StreamFilterIpv4Address (CP_TPS_SystemTemplate Table 3.89, p.138, R23-11).

Checks the child element values and the XSD sequence order (IPV-4-ADDRESS,
IPV-4-ADDRESS-MASK per group STREAM-FILTER-IPV-4-ADDRESS — the element is emitted in
live documents as the DESTINATION-IPV-4-ADDRESS / SOURCE-IPV-4-ADDRESS child of the
SWITCH-STREAM-FILTER-RULE IP/TP rule), the partial-emission case and the
write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_ipv4_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterIpv4Address
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ipv4(value):
    ip = Ip4AddressString()
    ip.setValue(value)
    return ip


def _full_ipv4_address() -> StreamFilterIpv4Address:
    ipv4_address = StreamFilterIpv4Address()
    ipv4_address.setIpv4Address(_ipv4("192.168.0.1"))
    ipv4_address.setIpv4AddressMask(_ipv4("255.255.0.0"))
    return ipv4_address


def _write(ipv4_address):
    element = ET.Element("DESTINATION-IPV-4-ADDRESS")
    ARXMLWriter().writeStreamFilterIpv4Address(element, ipv4_address)
    return element


class TestWriteStreamFilterIpv4Address:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_ipv4_address())

        assert [child.tag for child in element] == ["IPV-4-ADDRESS", "IPV-4-ADDRESS-MASK"]
        assert element.find("IPV-4-ADDRESS").text == "192.168.0.1"
        assert element.find("IPV-4-ADDRESS-MASK").text == "255.255.0.0"

    def test_write_partial_omits_absent_elements(self):
        ipv4_address = StreamFilterIpv4Address()
        ipv4_address.setIpv4AddressMask(_ipv4("255.255.255.0"))

        element = _write(ipv4_address)

        assert [child.tag for child in element] == ["IPV-4-ADDRESS-MASK"]
        assert element.find("IPV-4-ADDRESS-MASK").text == "255.255.255.0"

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterIpv4Address())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_ipv4_address())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterIpv4Address()
        ARXMLParser(options={"warning": True}).readStreamFilterIpv4Address(namespaced, recovered)

        assert isinstance(recovered.getIpv4Address(), Ip4AddressString)
        assert recovered.getIpv4Address().getValue() == "192.168.0.1"
        assert isinstance(recovered.getIpv4AddressMask(), Ip4AddressString)
        assert recovered.getIpv4AddressMask().getValue() == "255.255.0.0"
