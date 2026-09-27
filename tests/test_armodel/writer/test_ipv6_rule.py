"""
Writer tests for the Ipv6Rule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class Ipv6Rule, AUTOSAR_00052.xsd line 75007 — XSD-only, no own table in repo corpus).

Checks the FirewallRule.networkLayerRule choice: an Ipv6Rule instance emits
NETWORK-LAYER-RULE/IPV-6-RULE with its members in XSD order
(DESTINATION-IP-ADDRESS → DESTINATION-NETWORK-MASK → FLOW-LABEL → HOP-LIMIT → ICMP-RULE →
NEXT-HEADER → SOURCE-IP-ADDRESS → SOURCE-NETWORK-MASK → TRAFFIC-CLASS, the nested
ICMP-RULE child carrying CHECKSUM-VERIFICATION → CODE → TYPE), a plain abstract
NetworkLayerRule keeps the bare identity element (fallback; the IPV-4-RULE sibling
dispatch is covered by tests/test_armodel/writer/test_ipv4_rule.py), and the write→parse
round-trip recovers the Ipv6Rule field values.

Round-trip counterpart: tests/test_armodel/parser/test_ipv6_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, IcmpRule, Ipv6Rule, NetworkLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Ip6AddressString, PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

QNS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _boolean(value):
    b = Boolean()
    b.setValue(value)
    return b


def _ip6(value):
    ip = Ip6AddressString()
    ip.setValue(value)
    return ip


class TestWriteFirewallRuleIpv6Rule:
    def test_write_full_ipv6_rule_in_xsd_order(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ipv6_rule = Ipv6Rule()
        ipv6_rule.setDestinationIpAddress(_ip6("2001:db8::1"))
        ipv6_rule.setDestinationNetworkMask(_ip6("ffff:ffff:ffff::"))
        ipv6_rule.setFlowLabel(_pos_int(1048576))
        ipv6_rule.setHopLimit(_pos_int(64))
        icmp_rule = IcmpRule()
        icmp_rule.setChecksumVerification(_boolean(True))
        icmp_rule.setCode(_pos_int(1))
        icmp_rule.setType(_pos_int(8))
        ipv6_rule.setIcmpRule(icmp_rule)
        ipv6_rule.setNextHeader(_pos_int(58))
        ipv6_rule.setSourceIpAddress(_ip6("fe80::1"))
        ipv6_rule.setSourceNetworkMask(_ip6("ffff::"))
        ipv6_rule.setTrafficClass(_pos_int(46))
        rule.setNetworkLayerRule(ipv6_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        ipv6_rule_element = root.find("FIREWALL-RULE/NETWORK-LAYER-RULE/IPV-6-RULE")
        assert ipv6_rule_element is not None
        assert [child.tag for child in ipv6_rule_element] == [
            "DESTINATION-IP-ADDRESS",
            "DESTINATION-NETWORK-MASK",
            "FLOW-LABEL",
            "HOP-LIMIT",
            "ICMP-RULE",
            "NEXT-HEADER",
            "SOURCE-IP-ADDRESS",
            "SOURCE-NETWORK-MASK",
            "TRAFFIC-CLASS",
        ]
        assert ipv6_rule_element.find("DESTINATION-IP-ADDRESS").text == "2001:db8::1"
        assert ipv6_rule_element.find("DESTINATION-NETWORK-MASK").text == "ffff:ffff:ffff::"
        assert ipv6_rule_element.find("FLOW-LABEL").text == "1048576"
        assert ipv6_rule_element.find("HOP-LIMIT").text == "64"
        icmp_rule_element = ipv6_rule_element.find("ICMP-RULE")
        assert [child.tag for child in icmp_rule_element] == ["CHECKSUM-VERIFICATION", "CODE", "TYPE"]
        assert icmp_rule_element.find("CHECKSUM-VERIFICATION").text == "true"
        assert icmp_rule_element.find("CODE").text == "1"
        assert icmp_rule_element.find("TYPE").text == "8"
        assert ipv6_rule_element.find("NEXT-HEADER").text == "58"
        assert ipv6_rule_element.find("SOURCE-IP-ADDRESS").text == "fe80::1"
        assert ipv6_rule_element.find("SOURCE-NETWORK-MASK").text == "ffff::"
        assert ipv6_rule_element.find("TRAFFIC-CLASS").text == "46"

    def test_write_partial_ipv6_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ipv6_rule = Ipv6Rule()
        ipv6_rule.setDestinationIpAddress(_ip6("2001:db8::1"))
        ipv6_rule.setHopLimit(_pos_int(64))
        rule.setNetworkLayerRule(ipv6_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        ipv6_rule_element = root.find("FIREWALL-RULE/NETWORK-LAYER-RULE/IPV-6-RULE")
        assert ipv6_rule_element is not None
        assert [child.tag for child in ipv6_rule_element] == ["DESTINATION-IP-ADDRESS", "HOP-LIMIT"]
        assert ipv6_rule_element.find("DESTINATION-IP-ADDRESS").text == "2001:db8::1"
        assert ipv6_rule_element.find("HOP-LIMIT").text == "64"

    def test_write_plain_network_layer_rule_keeps_identity_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setNetworkLayerRule(NetworkLayerRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        network_rule_element = root.find("FIREWALL-RULE/NETWORK-LAYER-RULE")
        assert network_rule_element is not None
        assert network_rule_element.find("IPV-6-RULE") is None
        assert network_rule_element.find("IPV-4-RULE") is None

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/NETWORK-LAYER-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ipv6_rule = Ipv6Rule()
        ipv6_rule.setDestinationIpAddress(_ip6("2001:db8::1"))
        ipv6_rule.setDestinationNetworkMask(_ip6("ffff:ffff:ffff::"))
        ipv6_rule.setFlowLabel(_pos_int(1048576))
        ipv6_rule.setHopLimit(_pos_int(64))
        icmp_rule = IcmpRule()
        icmp_rule.setCode(_pos_int(1))
        icmp_rule.setType(_pos_int(8))
        ipv6_rule.setIcmpRule(icmp_rule)
        ipv6_rule.setNextHeader(_pos_int(58))
        ipv6_rule.setSourceIpAddress(_ip6("fe80::1"))
        ipv6_rule.setSourceNetworkMask(_ip6("ffff::"))
        ipv6_rule.setTrafficClass(_pos_int(46))
        rule.setNetworkLayerRule(ipv6_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        network_rule = recovered.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv6Rule)
        assert network_rule.getDestinationIpAddress().getValue() == "2001:db8::1"
        assert network_rule.getDestinationNetworkMask().getValue() == "ffff:ffff:ffff::"
        assert network_rule.getFlowLabel().getValue() == 1048576
        assert network_rule.getHopLimit().getValue() == 64
        recovered_icmp_rule = network_rule.getIcmpRule()
        assert isinstance(recovered_icmp_rule, IcmpRule)
        assert recovered_icmp_rule.getChecksumVerification() is None
        assert recovered_icmp_rule.getCode().getValue() == 1
        assert recovered_icmp_rule.getType().getValue() == 8
        assert network_rule.getNextHeader().getValue() == 58
        assert network_rule.getSourceIpAddress().getValue() == "fe80::1"
        assert network_rule.getSourceNetworkMask().getValue() == "ffff::"
        assert network_rule.getTrafficClass().getValue() == 46
