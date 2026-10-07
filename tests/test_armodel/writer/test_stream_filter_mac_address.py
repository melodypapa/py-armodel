"""
Writer tests for StreamFilterMACAddress (CP_TPS_SystemTemplate Table 3.87, p.137, R23-11).

Checks the child element values and the XSD sequence order (MAC-ADDRESS,
MAC-ADDRESS-MASK per group STREAM-FILTER-MAC-ADDRESS — the element is emitted in
live documents as the DESTINATION-MAC-ADDRESS / SOURCE-MAC-ADDRESS child of the
SWITCH-STREAM-FILTER-RULE data-link-layer rule), the partial-emission case and the
write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_mac_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterMACAddress
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _mac(value):
    m = MacAddressString()
    m.setValue(value)
    return m


def _full_mac_address() -> StreamFilterMACAddress:
    mac_address = StreamFilterMACAddress()
    mac_address.setMacAddress(_mac("FF:FF:FF:FF:FF:FF"))
    mac_address.setMacAddressMask(_mac("FF:00:00:00:00:00"))
    return mac_address


def _write(mac_address):
    element = ET.Element("DESTINATION-MAC-ADDRESS")
    ARXMLWriter().writeStreamFilterMACAddress(element, mac_address)
    return element


class TestWriteStreamFilterMACAddress:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_mac_address())

        assert [child.tag for child in element] == ["MAC-ADDRESS", "MAC-ADDRESS-MASK"]
        assert element.find("MAC-ADDRESS").text == "FF:FF:FF:FF:FF:FF"
        assert element.find("MAC-ADDRESS-MASK").text == "FF:00:00:00:00:00"

    def test_write_partial_omits_absent_elements(self):
        mac_address = StreamFilterMACAddress()
        mac_address.setMacAddressMask(_mac("FF:FF:00:00:00:00"))

        element = _write(mac_address)

        assert [child.tag for child in element] == ["MAC-ADDRESS-MASK"]
        assert element.find("MAC-ADDRESS-MASK").text == "FF:FF:00:00:00:00"

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterMACAddress())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_mac_address())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterMACAddress()
        ARXMLParser(options={"warning": True}).readStreamFilterMACAddress(namespaced, recovered)

        assert isinstance(recovered.getMacAddress(), MacAddressString)
        assert recovered.getMacAddress().getValue() == "FF:FF:FF:FF:FF:FF"
        assert isinstance(recovered.getMacAddressMask(), MacAddressString)
        assert recovered.getMacAddressMask().getValue() == "FF:00:00:00:00:00"
