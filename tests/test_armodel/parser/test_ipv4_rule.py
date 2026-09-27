"""
Reader tests for the Ipv4Rule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class Ipv4Rule, AUTOSAR_00052.xsd line 74485 — XSD-only, no own table in repo corpus).

Covers the FirewallRule.networkLayerRule choice (00052 L59047-59060): the
NETWORK-LAYER-RULE element wraps a single IPV-4-RULE child carrying the Ipv4Rule members
CHECKSUM-VERIFICATION / DESTINATION-IP-ADDRESS / DESTINATION-NETWORK-MASK /
DIFFERENTIATED-SERVICE-CODE-POINT / DO-NOT-FRAGMENT / EXPLICIT-CONGESTION-NOTIFICATION /
ICMP-RULE / INTERNET-HEADER-LENGTH / MORE-FRAGMENTS / PROTOCOL / SOURCE-IP-ADDRESS /
SOURCE-NETWORK-MASK / TTL-MAX / TTL-MIN in XSD order (the nested ICMP-RULE child carries
its CHECKSUM-VERIFICATION / CODE / TYPE members), plus the absent/childless cases
(childless falls back to the abstract NetworkLayerRule placeholder).

Round-trip counterpart: tests/test_armodel/writer/test_ipv4_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, IcmpRule, Ipv4Rule, NetworkLayerRule
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<FIREWALL-RULE xmlns='{NS}'>{inner}</FIREWALL-RULE>")


def _rule() -> FirewallRule:
    return FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")


def _full_ipv4_rule_inner() -> str:
    return (
        "<IPV-4-RULE>"
        "<CHECKSUM-VERIFICATION>true</CHECKSUM-VERIFICATION>"
        "<DESTINATION-IP-ADDRESS>192.168.0.1</DESTINATION-IP-ADDRESS>"
        "<DESTINATION-NETWORK-MASK>255.255.0.0</DESTINATION-NETWORK-MASK>"
        "<DIFFERENTIATED-SERVICE-CODE-POINT>46</DIFFERENTIATED-SERVICE-CODE-POINT>"
        "<DO-NOT-FRAGMENT>true</DO-NOT-FRAGMENT>"
        "<EXPLICIT-CONGESTION-NOTIFICATION>2</EXPLICIT-CONGESTION-NOTIFICATION>"
        "<ICMP-RULE>"
        "<CHECKSUM-VERIFICATION>true</CHECKSUM-VERIFICATION>"
        "<CODE>1</CODE>"
        "<TYPE>8</TYPE>"
        "</ICMP-RULE>"
        "<INTERNET-HEADER-LENGTH>5</INTERNET-HEADER-LENGTH>"
        "<MORE-FRAGMENTS>false</MORE-FRAGMENTS>"
        "<PROTOCOL>6</PROTOCOL>"
        "<SOURCE-IP-ADDRESS>10.0.0.1</SOURCE-IP-ADDRESS>"
        "<SOURCE-NETWORK-MASK>255.0.0.0</SOURCE-NETWORK-MASK>"
        "<TTL-MAX>64</TTL-MAX>"
        "<TTL-MIN>1</TTL-MIN>"
        "</IPV-4-RULE>"
    )


def _assert_full_ipv4_rule(ipv4_rule: Ipv4Rule):
    assert ipv4_rule.getChecksumVerification().getValue() is True
    assert ipv4_rule.getDestinationIpAddress().getValue() == "192.168.0.1"
    assert ipv4_rule.getDestinationNetworkMask().getValue() == "255.255.0.0"
    assert ipv4_rule.getDifferentiatedServiceCodePoint().getValue() == 46
    assert ipv4_rule.getDoNotFragment().getValue() is True
    assert ipv4_rule.getExplicitCongestionNotification().getValue() == 2
    icmp_rule = ipv4_rule.getIcmpRule()
    assert isinstance(icmp_rule, IcmpRule)
    assert icmp_rule.getChecksumVerification().getValue() is True
    assert icmp_rule.getCode().getValue() == 1
    assert icmp_rule.getType().getValue() == 8
    assert ipv4_rule.getInternetHeaderLength().getValue() == 5
    assert ipv4_rule.getMoreFragments().getValue() is False
    assert ipv4_rule.getProtocol().getValue() == 6
    assert ipv4_rule.getSourceIpAddress().getValue() == "10.0.0.1"
    assert ipv4_rule.getSourceNetworkMask().getValue() == "255.0.0.0"
    assert ipv4_rule.getTtlMax().getValue() == 64
    assert ipv4_rule.getTtlMin().getValue() == 1


class TestReadFirewallRuleIpv4Rule:
    def test_read_full_ipv4_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE>" + _full_ipv4_rule_inner() + "</NETWORK-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        network_rule = rule.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv4Rule)
        assert isinstance(network_rule, NetworkLayerRule)
        _assert_full_ipv4_rule(network_rule)

    def test_read_partial_ipv4_rule_omits_absent_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<NETWORK-LAYER-RULE>"
            "<IPV-4-RULE>"
            "<DESTINATION-IP-ADDRESS>192.168.0.1</DESTINATION-IP-ADDRESS>"
            "<TTL-MAX>64</TTL-MAX>"
            "</IPV-4-RULE>"
            "</NETWORK-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        network_rule = rule.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv4Rule)
        assert network_rule.getChecksumVerification() is None
        assert network_rule.getDestinationIpAddress().getValue() == "192.168.0.1"
        assert network_rule.getDestinationNetworkMask() is None
        assert network_rule.getDifferentiatedServiceCodePoint() is None
        assert network_rule.getDoNotFragment() is None
        assert network_rule.getExplicitCongestionNotification() is None
        assert network_rule.getIcmpRule() is None
        assert network_rule.getInternetHeaderLength() is None
        assert network_rule.getMoreFragments() is None
        assert network_rule.getProtocol() is None
        assert network_rule.getSourceIpAddress() is None
        assert network_rule.getSourceNetworkMask() is None
        assert network_rule.getTtlMax().getValue() == 64
        assert network_rule.getTtlMin() is None

    def test_read_empty_ipv4_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE><IPV-4-RULE/></NETWORK-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        network_rule = rule.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv4Rule)
        assert network_rule.getChecksumVerification() is None
        assert network_rule.getDestinationIpAddress() is None
        assert network_rule.getDestinationNetworkMask() is None
        assert network_rule.getDifferentiatedServiceCodePoint() is None
        assert network_rule.getDoNotFragment() is None
        assert network_rule.getExplicitCongestionNotification() is None
        assert network_rule.getIcmpRule() is None
        assert network_rule.getInternetHeaderLength() is None
        assert network_rule.getMoreFragments() is None
        assert network_rule.getProtocol() is None
        assert network_rule.getSourceIpAddress() is None
        assert network_rule.getSourceNetworkMask() is None
        assert network_rule.getTtlMax() is None
        assert network_rule.getTtlMin() is None

    def test_read_no_network_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getNetworkLayerRule() is None

    def test_read_childless_network_layer_rule_falls_back_to_abstract(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert type(rule.getNetworkLayerRule()) is NetworkLayerRule
