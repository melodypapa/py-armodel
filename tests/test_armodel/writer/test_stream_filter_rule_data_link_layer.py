"""
Writer tests for StreamFilterRuleDataLinkLayer (CP_TPS_SystemTemplate Table 3.86, p.137, R23-11).

Checks the child element values and the XSD sequence order (DESTINATION-MAC-ADDRESS,
ETHER-TYPE, SOURCE-MAC-ADDRESS, VLAN-ID, VLAN-PRIORITY per group
STREAM-FILTER-RULE-DATA-LINK-LAYER — the element is emitted in live documents as the
DATA-LINK-LAYER-RULE child of the SWITCH-STREAM-FILTER-RULE element), the nested
StreamFilterMACAddress dispatch, the partial-emission case and the write→parse
round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_rule_data_link_layer.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterMACAddress, StreamFilterRuleDataLinkLayer
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


def _mac_address(address, mask):
    mac_address = StreamFilterMACAddress()
    mac_address.setMacAddress(_mac(address))
    if mask is not None:
        mac_address.setMacAddressMask(_mac(mask))
    return mac_address


def _full_rule() -> StreamFilterRuleDataLinkLayer:
    rule = StreamFilterRuleDataLinkLayer()
    rule.setDestinationMacAddress(_mac_address("02:00:00:00:00:01", "FF:FF:FF:FF:FF:FF"))
    rule.setEtherType(PositiveInteger().setValue("2048"))
    rule.setSourceMacAddress(_mac_address("02:00:00:00:00:02", None))
    rule.setVlanId(PositiveInteger().setValue("10"))
    rule.setVlanPriority(PositiveInteger().setValue("5"))
    return rule


def _write(rule):
    element = ET.Element("STREAM-FILTER-RULE-DATA-LINK-LAYER")
    ARXMLWriter().writeStreamFilterRuleDataLinkLayer(element, rule)
    return element


class TestWriteStreamFilterRuleDataLinkLayer:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_rule())

        assert [child.tag for child in element] == ["DESTINATION-MAC-ADDRESS", "ETHER-TYPE", "SOURCE-MAC-ADDRESS", "VLAN-ID", "VLAN-PRIORITY"]
        assert element.find("DESTINATION-MAC-ADDRESS/MAC-ADDRESS").text == "02:00:00:00:00:01"
        assert element.find("DESTINATION-MAC-ADDRESS/MAC-ADDRESS-MASK").text == "FF:FF:FF:FF:FF:FF"
        assert element.find("ETHER-TYPE").text == "2048"
        assert element.find("SOURCE-MAC-ADDRESS/MAC-ADDRESS").text == "02:00:00:00:00:02"
        assert element.find("VLAN-ID").text == "10"
        assert element.find("VLAN-PRIORITY").text == "5"

    def test_write_partial_omits_absent_elements(self):
        rule = StreamFilterRuleDataLinkLayer()
        rule.setEtherType(PositiveInteger().setValue("2048"))
        rule.setVlanPriority(PositiveInteger().setValue("5"))

        element = _write(rule)

        assert [child.tag for child in element] == ["ETHER-TYPE", "VLAN-PRIORITY"]

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterRuleDataLinkLayer())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_rule())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterRuleDataLinkLayer()
        ARXMLParser(options={"warning": True}).readStreamFilterRuleDataLinkLayer(namespaced, recovered)

        assert isinstance(recovered.getDestinationMacAddress(), StreamFilterMACAddress)
        assert recovered.getDestinationMacAddress().getMacAddress().getValue() == "02:00:00:00:00:01"
        assert recovered.getDestinationMacAddress().getMacAddressMask().getValue() == "FF:FF:FF:FF:FF:FF"
        assert isinstance(recovered.getEtherType(), PositiveInteger)
        assert recovered.getEtherType().getValue() == 2048
        assert isinstance(recovered.getSourceMacAddress(), StreamFilterMACAddress)
        assert recovered.getSourceMacAddress().getMacAddress().getValue() == "02:00:00:00:00:02"
        assert recovered.getSourceMacAddress().getMacAddressMask() is None
        assert isinstance(recovered.getVlanId(), PositiveInteger)
        assert recovered.getVlanId().getValue() == 10
        assert isinstance(recovered.getVlanPriority(), PositiveInteger)
        assert recovered.getVlanPriority().getValue() == 5
