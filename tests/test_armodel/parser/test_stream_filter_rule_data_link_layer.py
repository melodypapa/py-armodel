"""
Reader tests for StreamFilterRuleDataLinkLayer (CP_TPS_SystemTemplate Table 3.86, p.137, R23-11).

Covers the DESTINATION-MAC-ADDRESS / ETHER-TYPE / SOURCE-MAC-ADDRESS / VLAN-ID /
VLAN-PRIORITY children of the STREAM-FILTER-RULE-DATA-LINK-LAYER element shape
(AUTOSAR_00052.xsd group STREAM-FILTER-RULE-DATA-LINK-LAYER — emitted in live
documents as the DATA-LINK-LAYER-RULE child of the SWITCH-STREAM-FILTER-RULE
element), the nested StreamFilterMACAddress dispatch, the absent-element case
and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_rule_data_link_layer.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterMACAddress, StreamFilterRuleDataLinkLayer
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<STREAM-FILTER-RULE-DATA-LINK-LAYER xmlns='{NS}'>{inner}</STREAM-FILTER-RULE-DATA-LINK-LAYER>")


class TestReadStreamFilterRuleDataLinkLayer:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<DESTINATION-MAC-ADDRESS><MAC-ADDRESS>02:00:00:00:00:01</MAC-ADDRESS><MAC-ADDRESS-MASK>FF:FF:FF:FF:FF:FF</MAC-ADDRESS-MASK></DESTINATION-MAC-ADDRESS>"
            "<ETHER-TYPE>2048</ETHER-TYPE>"
            "<SOURCE-MAC-ADDRESS><MAC-ADDRESS>02:00:00:00:00:02</MAC-ADDRESS></SOURCE-MAC-ADDRESS>"
            "<VLAN-ID>10</VLAN-ID>"
            "<VLAN-PRIORITY>5</VLAN-PRIORITY>"
        )
        rule = StreamFilterRuleDataLinkLayer()
        parser.readStreamFilterRuleDataLinkLayer(element, rule)

        assert isinstance(rule.getDestinationMacAddress(), StreamFilterMACAddress)
        assert rule.getDestinationMacAddress().getMacAddress().getValue() == "02:00:00:00:00:01"
        assert rule.getDestinationMacAddress().getMacAddressMask().getValue() == "FF:FF:FF:FF:FF:FF"
        assert isinstance(rule.getEtherType(), PositiveInteger)
        assert rule.getEtherType().getValue() == 2048
        assert isinstance(rule.getSourceMacAddress(), StreamFilterMACAddress)
        assert rule.getSourceMacAddress().getMacAddress().getValue() == "02:00:00:00:00:02"
        assert rule.getSourceMacAddress().getMacAddressMask() is None
        assert isinstance(rule.getVlanId(), PositiveInteger)
        assert rule.getVlanId().getValue() == 10
        assert isinstance(rule.getVlanPriority(), PositiveInteger)
        assert rule.getVlanPriority().getValue() == 5

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<ETHER-TYPE>2048</ETHER-TYPE>" "<VLAN-ID>10</VLAN-ID>")
        rule = StreamFilterRuleDataLinkLayer()
        parser.readStreamFilterRuleDataLinkLayer(element, rule)

        assert rule.getDestinationMacAddress() is None
        assert rule.getEtherType().getValue() == 2048
        assert rule.getSourceMacAddress() is None
        assert rule.getVlanId().getValue() == 10
        assert rule.getVlanPriority() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        rule = StreamFilterRuleDataLinkLayer()
        parser.readStreamFilterRuleDataLinkLayer(element, rule)

        assert rule.getDestinationMacAddress() is None
        assert rule.getEtherType() is None
        assert rule.getSourceMacAddress() is None
        assert rule.getVlanId() is None
        assert rule.getVlanPriority() is None
