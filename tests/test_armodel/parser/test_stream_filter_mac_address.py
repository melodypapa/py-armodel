"""
Reader tests for StreamFilterMACAddress (CP_TPS_SystemTemplate Table 3.87, p.137, R23-11).

Covers the MAC-ADDRESS / MAC-ADDRESS-MASK children of the STREAM-FILTER-MAC-ADDRESS
element shape (AUTOSAR_00052.xsd group STREAM-FILTER-MAC-ADDRESS — emitted in live
documents as the DESTINATION-MAC-ADDRESS / SOURCE-MAC-ADDRESS children of the
SWITCH-STREAM-FILTER-RULE data-link-layer rule), the absent-element case and the
empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_mac_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterMACAddress
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DESTINATION-MAC-ADDRESS xmlns='{NS}'>{inner}</DESTINATION-MAC-ADDRESS>")


class TestReadStreamFilterMACAddress:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<MAC-ADDRESS>FF:FF:FF:FF:FF:FF</MAC-ADDRESS>" "<MAC-ADDRESS-MASK>FF:00:00:00:00:00</MAC-ADDRESS-MASK>")
        mac_address = StreamFilterMACAddress()
        parser.readStreamFilterMACAddress(element, mac_address)

        assert isinstance(mac_address.getMacAddress(), MacAddressString)
        assert mac_address.getMacAddress().getValue() == "FF:FF:FF:FF:FF:FF"
        assert isinstance(mac_address.getMacAddressMask(), MacAddressString)
        assert mac_address.getMacAddressMask().getValue() == "FF:00:00:00:00:00"

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<MAC-ADDRESS>AA:BB:CC:DD:EE:FF</MAC-ADDRESS>")
        mac_address = StreamFilterMACAddress()
        parser.readStreamFilterMACAddress(element, mac_address)

        assert mac_address.getMacAddress().getValue() == "AA:BB:CC:DD:EE:FF"
        assert mac_address.getMacAddressMask() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        mac_address = StreamFilterMACAddress()
        parser.readStreamFilterMACAddress(element, mac_address)

        assert mac_address.getMacAddress() is None
        assert mac_address.getMacAddressMask() is None
