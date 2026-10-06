"""
Reader tests for the TransportLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class TransportLayerRule, AUTOSAR_00052.xsd line 126190 — XSD-only, no own table in repo corpus).

The abstract class owns the 5 TRANSPORT-LAYER-RULE group members (checksumVerification and the
four port-number filters), which the concrete subtypes TcpRule/UdpRule inherit per the XSD group
composition; the bare TRANSPORT-LAYER-RULE element (no subtype child) reads as the instantiable
placeholder carrying those members.

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

    def test_read_bare_element_member_values(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<TRANSPORT-LAYER-RULE>"
            "<CHECKSUM-VERIFICATION>true</CHECKSUM-VERIFICATION>"
            "<MAX-DESTINATION-PORT-NUMBER>8080</MAX-DESTINATION-PORT-NUMBER>"
            "<MAX-SOURCE-PORT-NUMBER>9090</MAX-SOURCE-PORT-NUMBER>"
            "<MIN-DESTINATION-PORT-NUMBER>1000</MIN-DESTINATION-PORT-NUMBER>"
            "<MIN-SOURCE-PORT-NUMBER>2000</MIN-SOURCE-PORT-NUMBER>"
            "</TRANSPORT-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, TransportLayerRule)
        assert transport_rule.getChecksumVerification() is not None
        assert transport_rule.getChecksumVerification().getValue() is True
        assert transport_rule.getMaxDestinationPortNumber().getValue() == 8080
        assert transport_rule.getMaxSourcePortNumber().getValue() == 9090
        assert transport_rule.getMinDestinationPortNumber().getValue() == 1000
        assert transport_rule.getMinSourcePortNumber().getValue() == 2000
