"""
Writer tests for StreamFilterRuleIpTp (CP_TPS_SystemTemplate Table 3.88, p.138, R23-11).

Checks the child element shape and the XSD sequence order (DESTINATION-IPV-4-ADDRESS,
DESTINATION-IPV-6-ADDRESS, DESTINATION-PORTS, SOURCE-IPV-4-ADDRESS, SOURCE-IPV-6-ADDRESS,
SOURCE-PORTS per group STREAM-FILTER-RULE-IP-TP — the element is emitted in live documents
as the IP-TP-RULE child of the SWITCH-STREAM-FILTER-RULE element), the nested DESTINATION-PORTS / SOURCE-PORTS
STREAM-FILTER-PORT-RANGE children (full MAX/MIN emission via writeStreamFilterPortRange),
the partial-emission case and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_rule_ip_tp.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString, Ip6AddressString, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIpv4Address,
    StreamFilterIpv6Address,
    StreamFilterPortRange,
    StreamFilterRuleIpTp,
)
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


def _ipv6(value):
    ip = Ip6AddressString()
    ip.setValue(value)
    return ip


def _port(value):
    port = PositiveInteger()
    port.setValue(value)
    return port


def _full_rule() -> StreamFilterRuleIpTp:
    rule = StreamFilterRuleIpTp()
    destination_ipv4_address = StreamFilterIpv4Address()
    destination_ipv4_address.setIpv4Address(_ipv4("192.168.0.1"))
    destination_ipv4_address.setIpv4AddressMask(_ipv4("255.255.0.0"))
    rule.setDestinationIpv4Address(destination_ipv4_address)
    destination_ipv6_address = StreamFilterIpv6Address()
    destination_ipv6_address.setIpv6Address(_ipv6("2001:0DB8:0000:0000:0000:0000:0000:0001"))
    destination_ipv6_address.setIpv6AddressMask(_ipv6("FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"))
    rule.setDestinationIpv6Address(destination_ipv6_address)
    destination_port_range = StreamFilterPortRange()
    destination_port_range.setMax(_port("65535"))
    destination_port_range.setMin(_port("1024"))
    rule.addDestinationPort(destination_port_range)
    second_destination_port_range = StreamFilterPortRange()
    second_destination_port_range.setMin(_port("443"))
    rule.addDestinationPort(second_destination_port_range)
    source_ipv4_address = StreamFilterIpv4Address()
    source_ipv4_address.setIpv4Address(_ipv4("10.0.0.1"))
    rule.setSourceIpv4Address(source_ipv4_address)
    source_ipv6_address = StreamFilterIpv6Address()
    source_ipv6_address.setIpv6Address(_ipv6("FE80:0000:0000:0000:0000:0000:0000:0001"))
    rule.setSourceIpv6Address(source_ipv6_address)
    source_port_range = StreamFilterPortRange()
    source_port_range.setMax(_port("8080"))
    rule.addSourcePort(source_port_range)
    return rule


def _write(rule):
    element = ET.Element("STREAM-FILTER-RULE-IP-TP")
    ARXMLWriter().writeStreamFilterRuleIpTp(element, rule)
    return element


class TestWriteStreamFilterRuleIpTp:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_rule())

        assert [child.tag for child in element] == [
            "DESTINATION-IPV-4-ADDRESS",
            "DESTINATION-IPV-6-ADDRESS",
            "DESTINATION-PORTS",
            "SOURCE-IPV-4-ADDRESS",
            "SOURCE-IPV-6-ADDRESS",
            "SOURCE-PORTS",
        ]
        assert isinstance(element.find("DESTINATION-IPV-4-ADDRESS"), ET.Element)
        assert element.find("DESTINATION-IPV-4-ADDRESS/IPV-4-ADDRESS").text == "192.168.0.1"
        assert element.find("DESTINATION-IPV-4-ADDRESS/IPV-4-ADDRESS-MASK").text == "255.255.0.0"
        assert isinstance(element.find("DESTINATION-IPV-6-ADDRESS"), ET.Element)
        assert element.find("DESTINATION-IPV-6-ADDRESS/IPV-6-ADDRESS").text == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert element.find("DESTINATION-IPV-6-ADDRESS/IPV-6-ADDRESS-MASK").text == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"
        assert [child.tag for child in element.find("DESTINATION-PORTS")] == ["STREAM-FILTER-PORT-RANGE", "STREAM-FILTER-PORT-RANGE"]
        assert element.find("DESTINATION-PORTS/STREAM-FILTER-PORT-RANGE[MAX]").find("MAX").text == "65535"
        assert element.find("DESTINATION-PORTS/STREAM-FILTER-PORT-RANGE[MAX]").find("MIN").text == "1024"
        second_destination_port_range = element.findall("DESTINATION-PORTS/STREAM-FILTER-PORT-RANGE")[1]
        assert [child.tag for child in second_destination_port_range] == ["MIN"]
        assert second_destination_port_range.find("MIN").text == "443"
        assert isinstance(element.find("SOURCE-IPV-4-ADDRESS"), ET.Element)
        assert element.find("SOURCE-IPV-4-ADDRESS/IPV-4-ADDRESS").text == "10.0.0.1"
        assert element.find("SOURCE-IPV-4-ADDRESS/IPV-4-ADDRESS-MASK") is None
        assert isinstance(element.find("SOURCE-IPV-6-ADDRESS"), ET.Element)
        assert element.find("SOURCE-IPV-6-ADDRESS/IPV-6-ADDRESS").text == "FE80:0000:0000:0000:0000:0000:0000:0001"
        assert element.find("SOURCE-IPV-6-ADDRESS/IPV-6-ADDRESS-MASK") is None
        assert [child.tag for child in element.find("SOURCE-PORTS")] == ["STREAM-FILTER-PORT-RANGE"]
        assert element.find("SOURCE-PORTS/STREAM-FILTER-PORT-RANGE").find("MAX").text == "8080"

    def test_write_partial_omits_absent_elements(self):
        rule = StreamFilterRuleIpTp()
        rule.setDestinationIpv6Address(StreamFilterIpv6Address())
        rule.addSourcePort(StreamFilterPortRange())

        element = _write(rule)

        assert [child.tag for child in element] == ["DESTINATION-IPV-6-ADDRESS", "SOURCE-PORTS"]
        assert [child.tag for child in element.find("SOURCE-PORTS")] == ["STREAM-FILTER-PORT-RANGE"]

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterRuleIpTp())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_rule())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterRuleIpTp()
        ARXMLParser(options={"warning": True}).readStreamFilterRuleIpTp(namespaced, recovered)

        assert isinstance(recovered.getDestinationIpv4Address(), StreamFilterIpv4Address)
        assert recovered.getDestinationIpv4Address().getIpv4Address().getValue() == "192.168.0.1"
        assert recovered.getDestinationIpv4Address().getIpv4AddressMask().getValue() == "255.255.0.0"
        assert isinstance(recovered.getDestinationIpv6Address(), StreamFilterIpv6Address)
        assert recovered.getDestinationIpv6Address().getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert recovered.getDestinationIpv6Address().getIpv6AddressMask().getValue() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"
        assert len(recovered.getDestinationPorts()) == 2
        assert all(isinstance(port, StreamFilterPortRange) for port in recovered.getDestinationPorts())
        assert recovered.getDestinationPorts()[0].getMax().getValue() == 65535
        assert recovered.getDestinationPorts()[0].getMin().getValue() == 1024
        assert recovered.getDestinationPorts()[1].getMax() is None
        assert recovered.getDestinationPorts()[1].getMin().getValue() == 443
        assert isinstance(recovered.getSourceIpv4Address(), StreamFilterIpv4Address)
        assert recovered.getSourceIpv4Address().getIpv4Address().getValue() == "10.0.0.1"
        assert recovered.getSourceIpv4Address().getIpv4AddressMask() is None
        assert isinstance(recovered.getSourceIpv6Address(), StreamFilterIpv6Address)
        assert recovered.getSourceIpv6Address().getIpv6Address().getValue() == "FE80:0000:0000:0000:0000:0000:0000:0001"
        assert recovered.getSourceIpv6Address().getIpv6AddressMask() is None
        assert len(recovered.getSourcePorts()) == 1
        assert isinstance(recovered.getSourcePorts()[0], StreamFilterPortRange)
        assert recovered.getSourcePorts()[0].getMax().getValue() == 8080
        assert recovered.getSourcePorts()[0].getMin() is None
