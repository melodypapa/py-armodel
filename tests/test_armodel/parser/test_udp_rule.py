"""
Reader tests for the UdpRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class UdpRule, AUTOSAR_00052.xsd line 127875 — XSD-only, no own table in repo corpus).

Covers the FirewallRule.transportLayerRule choice (00052 L59088-59098): the
TRANSPORT-LAYER-RULE element wraps a single identity-only UDP-RULE child (the UDP-RULE
group is an empty sequence — no own members), plus the absent/childless cases (childless
falls back to the abstract TransportLayerRule placeholder).

Round-trip counterpart: tests/test_armodel/writer/test_udp_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, TransportLayerRule, UdpRule
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


class TestReadFirewallRuleUdpRule:
    def test_read_udp_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<TRANSPORT-LAYER-RULE><UDP-RULE/></TRANSPORT-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, UdpRule)
        assert isinstance(transport_rule, TransportLayerRule)

    def test_read_udp_rule_inherited_transport_layer_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<TRANSPORT-LAYER-RULE>"
            "<UDP-RULE>"
            "<CHECKSUM-VERIFICATION>false</CHECKSUM-VERIFICATION>"
            "<MAX-SOURCE-PORT-NUMBER>9090</MAX-SOURCE-PORT-NUMBER>"
            "<MIN-DESTINATION-PORT-NUMBER>1000</MIN-DESTINATION-PORT-NUMBER>"
            "</UDP-RULE>"
            "</TRANSPORT-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, UdpRule)
        assert transport_rule.getChecksumVerification().getValue() is False
        assert transport_rule.getMaxSourcePortNumber().getValue() == 9090
        assert transport_rule.getMinDestinationPortNumber().getValue() == 1000

    def test_read_no_transport_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getTransportLayerRule() is None

    def test_read_childless_transport_layer_rule_falls_back_to_abstract(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<TRANSPORT-LAYER-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert type(rule.getTransportLayerRule()) is TransportLayerRule
