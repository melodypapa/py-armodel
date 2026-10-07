"""
Reader tests for SwitchStreamFilterRule (CP_TPS_SystemTemplate Table 3.85, p.136, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME round-trip) and the DATA-LINK-LAYER-RULE /
IEEE-1722-TP-RULE / IP-TP-RULE children of the SWITCH-STREAM-FILTER-RULE element shape
(AUTOSAR_00052.xsd group SWITCH-STREAM-FILTER-RULE — emitted in live documents as the
STREAM-FILTER-RULE child of the SWITCH-STREAM-IDENTIFICATION), the nested leaf values
(MAC address/mask, EtherType, VLAN id/priority, STREAM-ID, Ipv4/Ipv6 addresses and port
ranges), the absent-element case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_switch_stream_filter_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIEEE1722Tp,
    StreamFilterIpv4Address,
    StreamFilterIpv6Address,
    StreamFilterMACAddress,
    StreamFilterPortRange,
    StreamFilterRuleDataLinkLayer,
    StreamFilterRuleIpTp,
    SwitchStreamFilterRule,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<SWITCH-STREAM-FILTER-RULE xmlns='{NS}'>{inner}</SWITCH-STREAM-FILTER-RULE>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<SWITCH-STREAM-FILTER-RULE xmlns='{NS}' {attrs}>{inner}</SWITCH-STREAM-FILTER-RULE>")


def _full_inner() -> str:
    return (
        "<SHORT-NAME>Rule1</SHORT-NAME>"
        "<DATA-LINK-LAYER-RULE S='1'>"
        "<DESTINATION-MAC-ADDRESS><MAC-ADDRESS>02:00:00:00:00:01</MAC-ADDRESS><MAC-ADDRESS-MASK>FF:FF:FF:00:00:00</MAC-ADDRESS-MASK></DESTINATION-MAC-ADDRESS>"
        "<ETHER-TYPE>2048</ETHER-TYPE>"
        "<SOURCE-MAC-ADDRESS><MAC-ADDRESS>02:00:00:00:00:02</MAC-ADDRESS></SOURCE-MAC-ADDRESS>"
        "<VLAN-ID>10</VLAN-ID>"
        "<VLAN-PRIORITY>5</VLAN-PRIORITY>"
        "</DATA-LINK-LAYER-RULE>"
        "<IEEE-1722-TP-RULE S='2'><STREAM-ID>0x0102030405060708</STREAM-ID></IEEE-1722-TP-RULE>"
        "<IP-TP-RULE S='3'>"
        "<DESTINATION-IPV-4-ADDRESS><IPV-4-ADDRESS>192.168.0.1</IPV-4-ADDRESS></DESTINATION-IPV-4-ADDRESS>"
        "<DESTINATION-IPV-6-ADDRESS><IPV-6-ADDRESS>2001:0DB8:0000:0000:0000:0000:0000:0001</IPV-6-ADDRESS></DESTINATION-IPV-6-ADDRESS>"
        "<DESTINATION-PORTS><STREAM-FILTER-PORT-RANGE><MAX>65535</MAX><MIN>1024</MIN></STREAM-FILTER-PORT-RANGE></DESTINATION-PORTS>"
        "<SOURCE-IPV-4-ADDRESS><IPV-4-ADDRESS>10.0.0.1</IPV-4-ADDRESS></SOURCE-IPV-4-ADDRESS>"
        "<SOURCE-PORTS><STREAM-FILTER-PORT-RANGE><MIN>443</MIN></STREAM-FILTER-PORT-RANGE></SOURCE-PORTS>"
        "</IP-TP-RULE>"
    )


class TestReadStreamSwitchStreamFilterRule:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs("UUID='5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1'", "")
        rule = SwitchStreamFilterRule(MockParent(), "Initial")
        parser.readSwitchStreamFilterRule(element, rule)

        assert rule.getUuid().getValue() == "5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1"
        assert rule.getDataLinkLayerRule() is None
        assert rule.getIeee1722TpRule() is None
        assert rule.getIpTpRule() is None

    def test_read_data_link_layer_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        rule = SwitchStreamFilterRule(MockParent(), "Initial")
        parser.readSwitchStreamFilterRule(element, rule)

        data_link_layer_rule = rule.getDataLinkLayerRule()
        assert isinstance(data_link_layer_rule, StreamFilterRuleDataLinkLayer)
        assert isinstance(data_link_layer_rule.getDestinationMacAddress(), StreamFilterMACAddress)
        assert data_link_layer_rule.getDestinationMacAddress().getMacAddress().getValue() == "02:00:00:00:00:01"
        assert data_link_layer_rule.getDestinationMacAddress().getMacAddressMask().getValue() == "FF:FF:FF:00:00:00"
        assert data_link_layer_rule.getEtherType().getValue() == 2048
        assert isinstance(data_link_layer_rule.getSourceMacAddress(), StreamFilterMACAddress)
        assert data_link_layer_rule.getSourceMacAddress().getMacAddress().getValue() == "02:00:00:00:00:02"
        assert data_link_layer_rule.getVlanId().getValue() == 10
        assert data_link_layer_rule.getVlanPriority().getValue() == 5

    def test_read_ieee_1722_tp_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        rule = SwitchStreamFilterRule(MockParent(), "Initial")
        parser.readSwitchStreamFilterRule(element, rule)

        ieee_1722_tp_rule = rule.getIeee1722TpRule()
        assert isinstance(ieee_1722_tp_rule, StreamFilterIEEE1722Tp)
        assert ieee_1722_tp_rule.getStreamId().getValue() == 0x0102030405060708

    def test_read_ip_tp_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        rule = SwitchStreamFilterRule(MockParent(), "Initial")
        parser.readSwitchStreamFilterRule(element, rule)

        ip_tp_rule = rule.getIpTpRule()
        assert isinstance(ip_tp_rule, StreamFilterRuleIpTp)
        assert isinstance(ip_tp_rule.getDestinationIpv4Address(), StreamFilterIpv4Address)
        assert ip_tp_rule.getDestinationIpv4Address().getIpv4Address().getValue() == "192.168.0.1"
        assert isinstance(ip_tp_rule.getDestinationIpv6Address(), StreamFilterIpv6Address)
        assert ip_tp_rule.getDestinationIpv6Address().getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        destination_ports = ip_tp_rule.getDestinationPorts()
        assert len(destination_ports) == 1
        assert all(isinstance(port, StreamFilterPortRange) for port in destination_ports)
        assert destination_ports[0].getMax().getValue() == 65535
        assert destination_ports[0].getMin().getValue() == 1024
        assert isinstance(ip_tp_rule.getSourceIpv4Address(), StreamFilterIpv4Address)
        assert ip_tp_rule.getSourceIpv4Address().getIpv4Address().getValue() == "10.0.0.1"
        source_ports = ip_tp_rule.getSourcePorts()
        assert len(source_ports) == 1
        assert source_ports[0].getMin().getValue() == 443

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        rule = SwitchStreamFilterRule(MockParent(), "Initial")
        parser.readSwitchStreamFilterRule(element, rule)

        assert rule.getDataLinkLayerRule() is None
        assert rule.getIeee1722TpRule() is None
        assert rule.getIpTpRule() is None
