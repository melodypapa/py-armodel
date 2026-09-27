"""
Reader tests for the NetworkLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class NetworkLayerRule, AUTOSAR_00052.xsd line 84252 — XSD-only, no own table in repo corpus).

The abstract class owns an empty group (no own attributes); the NETWORK-LAYER-RULE
element carries a choice of the concrete subtypes Ipv4Rule/Ipv6Rule, which are not yet
implemented, so the reader keeps identity-only placeholder serialization (Rule 0001.10).
These tests lock that placeholder round-trip behavior.

Round-trip counterpart: tests/test_armodel/writer/test_network_layer_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, NetworkLayerRule
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


class TestReadFirewallRuleNetworkLayerRule:
    def test_read_network_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE><IPV-4-RULE/></NETWORK-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert isinstance(rule.getNetworkLayerRule(), NetworkLayerRule)

    def test_read_no_network_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getNetworkLayerRule() is None

    def test_read_empty_network_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<NETWORK-LAYER-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert isinstance(rule.getNetworkLayerRule(), NetworkLayerRule)
