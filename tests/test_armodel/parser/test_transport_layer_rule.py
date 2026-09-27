"""
Reader tests for the TransportLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class TransportLayerRule, AUTOSAR_00052.xsd line 126190 — XSD-only, no own table in repo corpus).

The abstract class owns an empty group (no own attributes); the TRANSPORT-LAYER-RULE
element carries a choice of the concrete subtypes TcpRule/UdpRule, which are not yet
implemented, so the reader keeps identity-only placeholder serialization (Rule 0001.10).
These tests lock that placeholder round-trip behavior.

Round-trip counterpart: tests/test_armodel/writer/test_transport_layer_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, TransportLayerRule
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


class TestReadFirewallRuleTransportLayerRule:
    def test_read_transport_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<TRANSPORT-LAYER-RULE><TCP-RULE/></TRANSPORT-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert isinstance(rule.getTransportLayerRule(), TransportLayerRule)

    def test_read_no_transport_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getTransportLayerRule() is None

    def test_read_empty_transport_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<TRANSPORT-LAYER-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert isinstance(rule.getTransportLayerRule(), TransportLayerRule)
