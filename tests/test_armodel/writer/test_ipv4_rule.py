"""
Writer tests for the Ipv4Rule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class Ipv4Rule, AUTOSAR_00052.xsd line 74485 — XSD-only, no own table in repo corpus).

Checks the FirewallRule.networkLayerRule choice: an Ipv4Rule instance emits
NETWORK-LAYER-RULE/IPV-4-RULE with its members in XSD order
(CHECKSUM-VERIFICATION → DESTINATION-IP-ADDRESS → DESTINATION-NETWORK-MASK →
DIFFERENTIATED-SERVICE-CODE-POINT → DO-NOT-FRAGMENT → EXPLICIT-CONGESTION-NOTIFICATION →
ICMP-RULE → INTERNET-HEADER-LENGTH → MORE-FRAGMENTS → PROTOCOL → SOURCE-IP-ADDRESS →
SOURCE-NETWORK-MASK → TTL-MAX → TTL-MIN, the nested ICMP-RULE child carrying
CHECKSUM-VERIFICATION → CODE → TYPE), a plain abstract NetworkLayerRule keeps the bare
identity element (fallback), and the write→parse round-trip recovers the Ipv4Rule field
values.

Round-trip counterpart: tests/test_armodel/parser/test_ipv4_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, IcmpRule, Ipv4Rule, NetworkLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Ip4AddressString, PositiveInteger
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


def _ip4(value):
    ip = Ip4AddressString()
    ip.setValue(value)
    return ip


class TestWriteFirewallRuleIpv4Rule:
    def test_write_full_ipv4_rule_in_xsd_order(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ipv4_rule = Ipv4Rule()
        ipv4_rule.setChecksumVerification(_boolean(True))
        ipv4_rule.setDestinationIpAddress(_ip4("192.168.0.1"))
        ipv4_rule.setDestinationNetworkMask(_ip4("255.255.0.0"))
        ipv4_rule.setDifferentiatedServiceCodePoint(_pos_int(46))
        ipv4_rule.setDoNotFragment(_boolean(True))
        ipv4_rule.setExplicitCongestionNotification(_pos_int(2))
        icmp_rule = IcmpRule()
        icmp_rule.setChecksumVerification(_boolean(True))
        icmp_rule.setCode(_pos_int(1))
        icmp_rule.setType(_pos_int(8))
        ipv4_rule.setIcmpRule(icmp_rule)
        ipv4_rule.setInternetHeaderLength(_pos_int(5))
        ipv4_rule.setMoreFragments(_boolean(False))
        ipv4_rule.setProtocol(_pos_int(6))
        ipv4_rule.setSourceIpAddress(_ip4("10.0.0.1"))
        ipv4_rule.setSourceNetworkMask(_ip4("255.0.0.0"))
        ipv4_rule.setTtlMax(_pos_int(64))
        ipv4_rule.setTtlMin(_pos_int(1))
        rule.setNetworkLayerRule(ipv4_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        ipv4_rule_element = root.find("FIREWALL-RULE/NETWORK-LAYER-RULE/IPV-4-RULE")
        assert ipv4_rule_element is not None
        assert [child.tag for child in ipv4_rule_element] == [
            "CHECKSUM-VERIFICATION",
            "DESTINATION-IP-ADDRESS",
            "DESTINATION-NETWORK-MASK",
            "DIFFERENTIATED-SERVICE-CODE-POINT",
            "DO-NOT-FRAGMENT",
            "EXPLICIT-CONGESTION-NOTIFICATION",
            "ICMP-RULE",
            "INTERNET-HEADER-LENGTH",
            "MORE-FRAGMENTS",
            "PROTOCOL",
            "SOURCE-IP-ADDRESS",
            "SOURCE-NETWORK-MASK",
            "TTL-MAX",
            "TTL-MIN",
        ]
        assert ipv4_rule_element.find("CHECKSUM-VERIFICATION").text == "true"
        assert ipv4_rule_element.find("DESTINATION-IP-ADDRESS").text == "192.168.0.1"
        assert ipv4_rule_element.find("DESTINATION-NETWORK-MASK").text == "255.255.0.0"
        assert ipv4_rule_element.find("DIFFERENTIATED-SERVICE-CODE-POINT").text == "46"
        assert ipv4_rule_element.find("DO-NOT-FRAGMENT").text == "true"
        assert ipv4_rule_element.find("EXPLICIT-CONGESTION-NOTIFICATION").text == "2"
        icmp_rule_element = ipv4_rule_element.find("ICMP-RULE")
        assert [child.tag for child in icmp_rule_element] == ["CHECKSUM-VERIFICATION", "CODE", "TYPE"]
        assert icmp_rule_element.find("CHECKSUM-VERIFICATION").text == "true"
        assert icmp_rule_element.find("CODE").text == "1"
        assert icmp_rule_element.find("TYPE").text == "8"
        assert ipv4_rule_element.find("INTERNET-HEADER-LENGTH").text == "5"
        assert ipv4_rule_element.find("MORE-FRAGMENTS").text == "false"
        assert ipv4_rule_element.find("PROTOCOL").text == "6"
        assert ipv4_rule_element.find("SOURCE-IP-ADDRESS").text == "10.0.0.1"
        assert ipv4_rule_element.find("SOURCE-NETWORK-MASK").text == "255.0.0.0"
        assert ipv4_rule_element.find("TTL-MAX").text == "64"
        assert ipv4_rule_element.find("TTL-MIN").text == "1"

    def test_write_partial_ipv4_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ipv4_rule = Ipv4Rule()
        ipv4_rule.setDestinationIpAddress(_ip4("192.168.0.1"))
        ipv4_rule.setTtlMax(_pos_int(64))
        rule.setNetworkLayerRule(ipv4_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        ipv4_rule_element = root.find("FIREWALL-RULE/NETWORK-LAYER-RULE/IPV-4-RULE")
        assert ipv4_rule_element is not None
        assert [child.tag for child in ipv4_rule_element] == ["DESTINATION-IP-ADDRESS", "TTL-MAX"]
        assert ipv4_rule_element.find("DESTINATION-IP-ADDRESS").text == "192.168.0.1"
        assert ipv4_rule_element.find("TTL-MAX").text == "64"

    def test_write_plain_network_layer_rule_keeps_identity_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setNetworkLayerRule(NetworkLayerRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        network_rule_element = root.find("FIREWALL-RULE/NETWORK-LAYER-RULE")
        assert network_rule_element is not None
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
        ipv4_rule = Ipv4Rule()
        ipv4_rule.setChecksumVerification(_boolean(True))
        ipv4_rule.setDestinationIpAddress(_ip4("192.168.0.1"))
        ipv4_rule.setDestinationNetworkMask(_ip4("255.255.0.0"))
        ipv4_rule.setDifferentiatedServiceCodePoint(_pos_int(46))
        ipv4_rule.setDoNotFragment(_boolean(True))
        ipv4_rule.setExplicitCongestionNotification(_pos_int(2))
        icmp_rule = IcmpRule()
        icmp_rule.setChecksumVerification(_boolean(True))
        icmp_rule.setCode(_pos_int(1))
        icmp_rule.setType(_pos_int(8))
        ipv4_rule.setIcmpRule(icmp_rule)
        ipv4_rule.setInternetHeaderLength(_pos_int(5))
        ipv4_rule.setMoreFragments(_boolean(False))
        ipv4_rule.setProtocol(_pos_int(6))
        ipv4_rule.setSourceIpAddress(_ip4("10.0.0.1"))
        ipv4_rule.setSourceNetworkMask(_ip4("255.0.0.0"))
        ipv4_rule.setTtlMax(_pos_int(64))
        ipv4_rule.setTtlMin(_pos_int(1))
        rule.setNetworkLayerRule(ipv4_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        network_rule = recovered.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv4Rule)
        assert network_rule.getChecksumVerification().getValue() is True
        assert network_rule.getDestinationIpAddress().getValue() == "192.168.0.1"
        assert network_rule.getDestinationNetworkMask().getValue() == "255.255.0.0"
        assert network_rule.getDifferentiatedServiceCodePoint().getValue() == 46
        assert network_rule.getDoNotFragment().getValue() is True
        assert network_rule.getExplicitCongestionNotification().getValue() == 2
        recovered_icmp_rule = network_rule.getIcmpRule()
        assert isinstance(recovered_icmp_rule, IcmpRule)
        assert recovered_icmp_rule.getChecksumVerification().getValue() is True
        assert recovered_icmp_rule.getCode().getValue() == 1
        assert recovered_icmp_rule.getType().getValue() == 8
        assert network_rule.getInternetHeaderLength().getValue() == 5
        assert network_rule.getMoreFragments().getValue() is False
        assert network_rule.getProtocol().getValue() == 6
        assert network_rule.getSourceIpAddress().getValue() == "10.0.0.1"
        assert network_rule.getSourceNetworkMask().getValue() == "255.0.0.0"
        assert network_rule.getTtlMax().getValue() == 64
        assert network_rule.getTtlMin().getValue() == 1
