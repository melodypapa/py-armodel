"""
Reader tests for StreamFilterIpv4Address (CP_TPS_SystemTemplate Table 3.89, p.138, R23-11).

Covers the IPV-4-ADDRESS / IPV-4-ADDRESS-MASK children of the STREAM-FILTER-IPV-4-ADDRESS
element shape (AUTOSAR_00052.xsd group STREAM-FILTER-IPV-4-ADDRESS — emitted in live
documents as the DESTINATION-IPV-4-ADDRESS / SOURCE-IPV-4-ADDRESS children of the
SWITCH-STREAM-FILTER-RULE IP/TP rule), the absent-element case and the
empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_ipv4_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterIpv4Address
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DESTINATION-IPV-4-ADDRESS xmlns='{NS}'>{inner}</DESTINATION-IPV-4-ADDRESS>")


class TestReadStreamFilterIpv4Address:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<IPV-4-ADDRESS>192.168.0.1</IPV-4-ADDRESS>" "<IPV-4-ADDRESS-MASK>255.255.0.0</IPV-4-ADDRESS-MASK>")
        ipv4_address = StreamFilterIpv4Address()
        parser.readStreamFilterIpv4Address(element, ipv4_address)

        assert isinstance(ipv4_address.getIpv4Address(), Ip4AddressString)
        assert ipv4_address.getIpv4Address().getValue() == "192.168.0.1"
        assert isinstance(ipv4_address.getIpv4AddressMask(), Ip4AddressString)
        assert ipv4_address.getIpv4AddressMask().getValue() == "255.255.0.0"

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<IPV-4-ADDRESS>10.0.0.1</IPV-4-ADDRESS>")
        ipv4_address = StreamFilterIpv4Address()
        parser.readStreamFilterIpv4Address(element, ipv4_address)

        assert ipv4_address.getIpv4Address().getValue() == "10.0.0.1"
        assert ipv4_address.getIpv4AddressMask() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        ipv4_address = StreamFilterIpv4Address()
        parser.readStreamFilterIpv4Address(element, ipv4_address)

        assert ipv4_address.getIpv4Address() is None
        assert ipv4_address.getIpv4AddressMask() is None
