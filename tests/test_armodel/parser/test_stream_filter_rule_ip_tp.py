"""
Reader tests for StreamFilterRuleIpTp (CP_TPS_SystemTemplate Table 3.88, p.138, R23-11).

Covers the DESTINATION-IPV-4-ADDRESS / DESTINATION-IPV-6-ADDRESS / DESTINATION-PORTS /
SOURCE-IPV-4-ADDRESS / SOURCE-IPV-6-ADDRESS / SOURCE-PORTS children of the
STREAM-FILTER-RULE-IP-TP element shape (AUTOSAR_00052.xsd group
STREAM-FILTER-RULE-IP-TP — emitted in live documents as the IP-TP-RULE child of the
SWITCH-STREAM-FILTER-RULE element), the nested DESTINATION-PORTS / SOURCE-PORTS
STREAM-FILTER-PORT-RANGE children (full MAX/MIN round-trip via
readStreamFilterPortRange), the absent-element case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_rule_ip_tp.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIpv4Address,
    StreamFilterIpv6Address,
    StreamFilterPortRange,
    StreamFilterRuleIpTp,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<STREAM-FILTER-RULE-IP-TP xmlns='{NS}'>{inner}</STREAM-FILTER-RULE-IP-TP>")


class TestReadStreamFilterRuleIpTp:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<DESTINATION-IPV-4-ADDRESS S='1'><IPV-4-ADDRESS>192.168.0.1</IPV-4-ADDRESS><IPV-4-ADDRESS-MASK>255.255.0.0</IPV-4-ADDRESS-MASK></DESTINATION-IPV-4-ADDRESS>"
            "<DESTINATION-IPV-6-ADDRESS S='2'><IPV-6-ADDRESS>2001:0DB8:0000:0000:0000:0000:0000:0001</IPV-6-ADDRESS><IPV-6-ADDRESS-MASK>FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00</IPV-6-ADDRESS-MASK></DESTINATION-IPV-6-ADDRESS>"
            "<DESTINATION-PORTS><STREAM-FILTER-PORT-RANGE S='31'><MAX>65535</MAX><MIN>1024</MIN></STREAM-FILTER-PORT-RANGE><STREAM-FILTER-PORT-RANGE S='32'><MIN>443</MIN></STREAM-FILTER-PORT-RANGE></DESTINATION-PORTS>"
            "<SOURCE-IPV-4-ADDRESS S='3'><IPV-4-ADDRESS>10.0.0.1</IPV-4-ADDRESS></SOURCE-IPV-4-ADDRESS>"
            "<SOURCE-IPV-6-ADDRESS S='4'><IPV-6-ADDRESS>FE80:0000:0000:0000:0000:0000:0000:0001</IPV-6-ADDRESS></SOURCE-IPV-6-ADDRESS>"
            "<SOURCE-PORTS><STREAM-FILTER-PORT-RANGE S='33'><MAX>8080</MAX></STREAM-FILTER-PORT-RANGE></SOURCE-PORTS>"
        )
        rule = StreamFilterRuleIpTp()
        parser.readStreamFilterRuleIpTp(element, rule)

        assert isinstance(rule.getDestinationIpv4Address(), StreamFilterIpv4Address)
        assert rule.getDestinationIpv4Address().getChecksum().getValue() == "1"
        assert rule.getDestinationIpv4Address().getIpv4Address().getValue() == "192.168.0.1"
        assert rule.getDestinationIpv4Address().getIpv4AddressMask().getValue() == "255.255.0.0"
        assert isinstance(rule.getDestinationIpv6Address(), StreamFilterIpv6Address)
        assert rule.getDestinationIpv6Address().getChecksum().getValue() == "2"
        assert rule.getDestinationIpv6Address().getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"
        assert rule.getDestinationIpv6Address().getIpv6AddressMask().getValue() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FF00"
        destination_ports = rule.getDestinationPorts()
        assert len(destination_ports) == 2
        assert all(isinstance(port, StreamFilterPortRange) for port in destination_ports)
        assert destination_ports[0].getChecksum().getValue() == "31"
        assert destination_ports[0].getMax().getValue() == 65535
        assert destination_ports[0].getMin().getValue() == 1024
        assert destination_ports[1].getChecksum().getValue() == "32"
        assert destination_ports[1].getMax() is None
        assert destination_ports[1].getMin().getValue() == 443
        assert isinstance(rule.getSourceIpv4Address(), StreamFilterIpv4Address)
        assert rule.getSourceIpv4Address().getChecksum().getValue() == "3"
        assert rule.getSourceIpv4Address().getIpv4Address().getValue() == "10.0.0.1"
        assert rule.getSourceIpv4Address().getIpv4AddressMask() is None
        assert isinstance(rule.getSourceIpv6Address(), StreamFilterIpv6Address)
        assert rule.getSourceIpv6Address().getChecksum().getValue() == "4"
        assert rule.getSourceIpv6Address().getIpv6Address().getValue() == "FE80:0000:0000:0000:0000:0000:0000:0001"
        assert rule.getSourceIpv6Address().getIpv6AddressMask() is None
        source_ports = rule.getSourcePorts()
        assert len(source_ports) == 1
        assert isinstance(source_ports[0], StreamFilterPortRange)
        assert source_ports[0].getChecksum().getValue() == "33"
        assert source_ports[0].getMax().getValue() == 8080
        assert source_ports[0].getMin() is None

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<DESTINATION-IPV-6-ADDRESS S='2'/><SOURCE-PORTS><STREAM-FILTER-PORT-RANGE S='33'/></SOURCE-PORTS>")
        rule = StreamFilterRuleIpTp()
        parser.readStreamFilterRuleIpTp(element, rule)

        assert rule.getDestinationIpv4Address() is None
        assert isinstance(rule.getDestinationIpv6Address(), StreamFilterIpv6Address)
        assert rule.getDestinationPorts() == []
        assert rule.getSourceIpv4Address() is None
        assert rule.getSourceIpv6Address() is None
        assert len(rule.getSourcePorts()) == 1

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        rule = StreamFilterRuleIpTp()
        parser.readStreamFilterRuleIpTp(element, rule)

        assert rule.getDestinationIpv4Address() is None
        assert rule.getDestinationIpv6Address() is None
        assert rule.getDestinationPorts() == []
        assert rule.getSourceIpv4Address() is None
        assert rule.getSourceIpv6Address() is None
        assert rule.getSourcePorts() == []
