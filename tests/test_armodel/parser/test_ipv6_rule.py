"""
Reader tests for the Ipv6Rule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class Ipv6Rule, AUTOSAR_00052.xsd line 75007 — XSD-only, no own table in repo corpus).

Covers the FirewallRule.networkLayerRule choice (00052 L59047-59060): the
NETWORK-LAYER-RULE element wraps a single IPV-6-RULE child carrying the Ipv6Rule members
DESTINATION-IP-ADDRESS / DESTINATION-NETWORK-MASK / FLOW-LABEL / HOP-LIMIT / ICMP-RULE /
NEXT-HEADER / SOURCE-IP-ADDRESS / SOURCE-NETWORK-MASK / TRAFFIC-CLASS in XSD order (the
nested ICMP-RULE child carries its CHECKSUM-VERIFICATION / CODE / TYPE members), plus the
absent/childless cases (childless falls back to the abstract NetworkLayerRule placeholder;
the IPV-4-RULE sibling dispatch is covered by tests/test_armodel/parser/test_ipv4_rule.py).

Round-trip counterpart: tests/test_armodel/writer/test_ipv6_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, IcmpRule, Ipv6Rule, NetworkLayerRule
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


def _full_ipv6_rule_inner() -> str:
    return (
        "<IPV-6-RULE>"
        "<DESTINATION-IP-ADDRESS>2001:db8::1</DESTINATION-IP-ADDRESS>"
        "<DESTINATION-NETWORK-MASK>ffff:ffff:ffff::</DESTINATION-NETWORK-MASK>"
        "<FLOW-LABEL>1048576</FLOW-LABEL>"
        "<HOP-LIMIT>64</HOP-LIMIT>"
        "<ICMP-RULE>"
        "<CHECKSUM-VERIFICATION>true</CHECKSUM-VERIFICATION>"
        "<CODE>1</CODE>"
        "<TYPE>8</TYPE>"
        "</ICMP-RULE>"
        "<NEXT-HEADER>58</NEXT-HEADER>"
        "<SOURCE-IP-ADDRESS>fe80::1</SOURCE-IP-ADDRESS>"
        "<SOURCE-NETWORK-MASK>ffff::</SOURCE-NETWORK-MASK>"
        "<TRAFFIC-CLASS>46</TRAFFIC-CLASS>"
        "</IPV-6-RULE>"
    )


def _assert_full_ipv6_rule(ipv6_rule: Ipv6Rule):
    assert ipv6_rule.getDestinationIpAddress().getValue() == "2001:db8::1"
    assert ipv6_rule.getDestinationNetworkMask().getValue() == "ffff:ffff:ffff::"
    assert ipv6_rule.getFlowLabel().getValue() == 1048576
    assert ipv6_rule.getHopLimit().getValue() == 64
    icmp_rule = ipv6_rule.getIcmpRule()
    assert isinstance(icmp_rule, IcmpRule)
    assert icmp_rule.getChecksumVerification().getValue() is True
    assert icmp_rule.getCode().getValue() == 1
    assert icmp_rule.getType().getValue() == 8
    assert ipv6_rule.getNextHeader().getValue() == 58
    assert ipv6_rule.getSourceIpAddress().getValue() == "fe80::1"
    assert ipv6_rule.getSourceNetworkMask().getValue() == "ffff::"
    assert ipv6_rule.getTrafficClass().getValue() == 46


class TestReadFirewallRuleIpv6Rule:
    def test_read_full_ipv6_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE>" + _full_ipv6_rule_inner() + "</NETWORK-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        network_rule = rule.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv6Rule)
        assert isinstance(network_rule, NetworkLayerRule)
        _assert_full_ipv6_rule(network_rule)

    def test_read_partial_ipv6_rule_omits_absent_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<NETWORK-LAYER-RULE>"
            "<IPV-6-RULE>"
            "<DESTINATION-IP-ADDRESS>2001:db8::1</DESTINATION-IP-ADDRESS>"
            "<HOP-LIMIT>64</HOP-LIMIT>"
            "</IPV-6-RULE>"
            "</NETWORK-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        network_rule = rule.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv6Rule)
        assert network_rule.getDestinationIpAddress().getValue() == "2001:db8::1"
        assert network_rule.getDestinationNetworkMask() is None
        assert network_rule.getFlowLabel() is None
        assert network_rule.getHopLimit().getValue() == 64
        assert network_rule.getIcmpRule() is None
        assert network_rule.getNextHeader() is None
        assert network_rule.getSourceIpAddress() is None
        assert network_rule.getSourceNetworkMask() is None
        assert network_rule.getTrafficClass() is None

    def test_read_empty_ipv6_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE><IPV-6-RULE/></NETWORK-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        network_rule = rule.getNetworkLayerRule()
        assert isinstance(network_rule, Ipv6Rule)
        assert network_rule.getDestinationIpAddress() is None
        assert network_rule.getDestinationNetworkMask() is None
        assert network_rule.getFlowLabel() is None
        assert network_rule.getHopLimit() is None
        assert network_rule.getIcmpRule() is None
        assert network_rule.getNextHeader() is None
        assert network_rule.getSourceIpAddress() is None
        assert network_rule.getSourceNetworkMask() is None
        assert network_rule.getTrafficClass() is None

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
