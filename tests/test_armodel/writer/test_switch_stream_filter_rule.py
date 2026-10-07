"""
Writer tests for SwitchStreamFilterRule (CP_TPS_SystemTemplate Table 3.85, p.136, R23-11).

Checks the IDENTIFIABLE base level (SHORT-NAME emission), the child element shape and
the XSD sequence order (DATA-LINK-LAYER-RULE, IEEE-1722-TP-RULE, IP-TP-RULE per group
SWITCH-STREAM-FILTER-RULE — the element is emitted in live documents as the
STREAM-FILTER-RULE child of the SWITCH-STREAM-IDENTIFICATION), the nested leaf values,
the partial-emission case and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_switch_stream_filter_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
    MacAddressString,
    PositiveInteger,
    PositiveUnlimitedInteger,
)
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
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _mac(value):
    address = MacAddressString()
    address.setValue(value)
    return address


def _ipv4(value):
    ip = Ip4AddressString()
    ip.setValue(value)
    return ip


def _ipv6(value):
    ip = Ip6AddressString()
    ip.setValue(value)
    return ip


def _port(value):
    port = PositiveInteger()
    port.setValue(value)
    return port


def _stream_id(value):
    stream_id = PositiveUnlimitedInteger()
    stream_id.setValue(value)
    return stream_id


def _full_data_link_layer_rule() -> StreamFilterRuleDataLinkLayer:
    rule = StreamFilterRuleDataLinkLayer()
    destination_mac_address = StreamFilterMACAddress()
    destination_mac_address.setMacAddress(_mac("02:00:00:00:00:01"))
    destination_mac_address.setMacAddressMask(_mac("FF:FF:FF:00:00:00"))
    rule.setDestinationMacAddress(destination_mac_address)
    rule.setEtherType(_port("2048"))
    source_mac_address = StreamFilterMACAddress()
    source_mac_address.setMacAddress(_mac("02:00:00:00:00:02"))
    rule.setSourceMacAddress(source_mac_address)
    rule.setVlanId(_port("10"))
    rule.setVlanPriority(_port("5"))
    return rule


def _full_ip_tp_rule() -> StreamFilterRuleIpTp:
    rule = StreamFilterRuleIpTp()
    destination_ipv4_address = StreamFilterIpv4Address()
    destination_ipv4_address.setIpv4Address(_ipv4("192.168.0.1"))
    rule.setDestinationIpv4Address(destination_ipv4_address)
    destination_ipv6_address = StreamFilterIpv6Address()
    destination_ipv6_address.setIpv6Address(_ipv6("2001:0DB8:0000:0000:0000:0000:0000:0001"))
    rule.setDestinationIpv6Address(destination_ipv6_address)
    destination_port_range = StreamFilterPortRange()
    destination_port_range.setMax(_port("65535"))
    destination_port_range.setMin(_port("1024"))
    rule.addDestinationPort(destination_port_range)
    source_ipv4_address = StreamFilterIpv4Address()
    source_ipv4_address.setIpv4Address(_ipv4("10.0.0.1"))
    rule.setSourceIpv4Address(source_ipv4_address)
    source_port_range = StreamFilterPortRange()
    source_port_range.setMin(_port("443"))
    rule.addSourcePort(source_port_range)
    return rule


def _full_rule() -> SwitchStreamFilterRule:
    rule = SwitchStreamFilterRule(MockParent(), "Rule1")
    rule.setDataLinkLayerRule(_full_data_link_layer_rule())
    tp_rule = StreamFilterIEEE1722Tp()
    tp_rule.setStreamId(_stream_id("0x0102030405060708"))
    rule.setIeee1722TpRule(tp_rule)
    rule.setIpTpRule(_full_ip_tp_rule())
    return rule


def _write(rule):
    element = ET.Element("SWITCH-STREAM-FILTER-RULE")
    ARXMLWriter().writeSwitchStreamFilterRule(element, rule)
    return element


class TestWriteSwitchStreamFilterRule:
    def test_write_identifiable_base_level(self):
        element = _write(SwitchStreamFilterRule(MockParent(), "Rule1"))

        assert element.find("SHORT-NAME").text == "Rule1"

    def test_write_all_children_in_xsd_order(self):
        element = _write(_full_rule())

        assert [child.tag for child in element] == ["SHORT-NAME", "DATA-LINK-LAYER-RULE", "IEEE-1722-TP-RULE", "IP-TP-RULE"]

        data_link_layer_rule = element.find("DATA-LINK-LAYER-RULE")
        assert [child.tag for child in data_link_layer_rule] == ["DESTINATION-MAC-ADDRESS", "ETHER-TYPE", "SOURCE-MAC-ADDRESS", "VLAN-ID", "VLAN-PRIORITY"]
        assert data_link_layer_rule.find("DESTINATION-MAC-ADDRESS/MAC-ADDRESS").text == "02:00:00:00:00:01"
        assert data_link_layer_rule.find("DESTINATION-MAC-ADDRESS/MAC-ADDRESS-MASK").text == "FF:FF:FF:00:00:00"
        assert data_link_layer_rule.find("ETHER-TYPE").text == "2048"
        assert data_link_layer_rule.find("SOURCE-MAC-ADDRESS/MAC-ADDRESS").text == "02:00:00:00:00:02"
        assert data_link_layer_rule.find("VLAN-ID").text == "10"
        assert data_link_layer_rule.find("VLAN-PRIORITY").text == "5"

        ieee_1722_tp_rule = element.find("IEEE-1722-TP-RULE")
        assert [child.tag for child in ieee_1722_tp_rule] == ["STREAM-ID"]
        assert ieee_1722_tp_rule.find("STREAM-ID").text == "0x0102030405060708"

        ip_tp_rule = element.find("IP-TP-RULE")
        assert [child.tag for child in ip_tp_rule] == ["DESTINATION-IPV-4-ADDRESS", "DESTINATION-IPV-6-ADDRESS", "DESTINATION-PORTS", "SOURCE-IPV-4-ADDRESS", "SOURCE-PORTS"]
        assert ip_tp_rule.find("DESTINATION-IPV-4-ADDRESS/IPV-4-ADDRESS").text == "192.168.0.1"
        assert ip_tp_rule.find("DESTINATION-IPV-6-ADDRESS/IPV-6-ADDRESS").text == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert ip_tp_rule.find("DESTINATION-PORTS/STREAM-FILTER-PORT-RANGE/MAX").text == "65535"
        assert ip_tp_rule.find("DESTINATION-PORTS/STREAM-FILTER-PORT-RANGE/MIN").text == "1024"
        assert ip_tp_rule.find("SOURCE-IPV-4-ADDRESS/IPV-4-ADDRESS").text == "10.0.0.1"
        assert ip_tp_rule.find("SOURCE-PORTS/STREAM-FILTER-PORT-RANGE/MIN").text == "443"

    def test_write_partial_emission(self):
        rule = SwitchStreamFilterRule(MockParent(), "Rule1")
        tp_rule = StreamFilterIEEE1722Tp()
        tp_rule.setStreamId(_stream_id("0x0102030405060708"))
        rule.setIeee1722TpRule(tp_rule)

        element = _write(rule)

        assert [child.tag for child in element] == ["SHORT-NAME", "IEEE-1722-TP-RULE"]

    def test_write_empty_emits_no_rule_children(self):
        element = _write(SwitchStreamFilterRule(MockParent(), "Rule1"))

        assert [child.tag for child in element] == ["SHORT-NAME"]

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_rule())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = SwitchStreamFilterRule(MockParent(), "Initial")
        ARXMLParser(options={"warning": True}).readSwitchStreamFilterRule(namespaced, recovered)

        assert element.find("SHORT-NAME").text == "Rule1"
        data_link_layer_rule = recovered.getDataLinkLayerRule()
        assert data_link_layer_rule.getDestinationMacAddress().getMacAddress().getValue() == "02:00:00:00:00:01"
        assert data_link_layer_rule.getDestinationMacAddress().getMacAddressMask().getValue() == "FF:FF:FF:00:00:00"
        assert data_link_layer_rule.getEtherType().getValue() == 2048
        assert data_link_layer_rule.getSourceMacAddress().getMacAddress().getValue() == "02:00:00:00:00:02"
        assert data_link_layer_rule.getVlanId().getValue() == 10
        assert data_link_layer_rule.getVlanPriority().getValue() == 5
        assert recovered.getIeee1722TpRule().getStreamId().getValue() == 0x0102030405060708
        ip_tp_rule = recovered.getIpTpRule()
        assert ip_tp_rule.getDestinationIpv4Address().getIpv4Address().getValue() == "192.168.0.1"
        assert ip_tp_rule.getDestinationIpv6Address().getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert ip_tp_rule.getDestinationPorts()[0].getMax().getValue() == 65535
        assert ip_tp_rule.getDestinationPorts()[0].getMin().getValue() == 1024
        assert ip_tp_rule.getSourceIpv4Address().getIpv4Address().getValue() == "10.0.0.1"
        assert ip_tp_rule.getSourcePorts()[0].getMin().getValue() == 443
