"""
Reader tests for the TcpRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class TcpRule, AUTOSAR_00052.xsd line 120644 — XSD-only, no own table in repo corpus).

Covers the FirewallRule.transportLayerRule choice (00052 L59088-59098): the
TRANSPORT-LAYER-RULE element wraps a single TCP-RULE child carrying the TcpRule members
NUMBER-OF-PARALLEL-TCP-SESSIONS / STATE-MANAGEMENT-BASED-ON-TCP-FLAGS / TIMEOUT-CHECK in
XSD order, plus the absent/childless cases (childless falls back to the abstract
TransportLayerRule placeholder).

Round-trip counterpart: tests/test_armodel/writer/test_tcp_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, TcpRule, TransportLayerRule
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


class TestReadFirewallRuleTcpRule:
    def test_read_full_tcp_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<TRANSPORT-LAYER-RULE>"
            "<TCP-RULE>"
            "<NUMBER-OF-PARALLEL-TCP-SESSIONS>4</NUMBER-OF-PARALLEL-TCP-SESSIONS>"
            "<STATE-MANAGEMENT-BASED-ON-TCP-FLAGS>true</STATE-MANAGEMENT-BASED-ON-TCP-FLAGS>"
            "<TIMEOUT-CHECK>30</TIMEOUT-CHECK>"
            "</TCP-RULE>"
            "</TRANSPORT-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, TcpRule)
        assert isinstance(transport_rule, TransportLayerRule)
        assert transport_rule.getNumberOfParallelTcpSessions().getValue() == 4
        assert transport_rule.getStateManagementBasedOnTcpFlags().getValue() is True
        assert transport_rule.getTimeoutCheck().getValue() == 30

    def test_read_partial_tcp_rule_omits_absent_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<TRANSPORT-LAYER-RULE>" "<TCP-RULE>" "<TIMEOUT-CHECK>60</TIMEOUT-CHECK>" "</TCP-RULE>" "</TRANSPORT-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, TcpRule)
        assert transport_rule.getNumberOfParallelTcpSessions() is None
        assert transport_rule.getStateManagementBasedOnTcpFlags() is None
        assert transport_rule.getTimeoutCheck().getValue() == 60

    def test_read_empty_tcp_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<TRANSPORT-LAYER-RULE><TCP-RULE/></TRANSPORT-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, TcpRule)
        assert transport_rule.getNumberOfParallelTcpSessions() is None
        assert transport_rule.getStateManagementBasedOnTcpFlags() is None
        assert transport_rule.getTimeoutCheck() is None

    def test_read_tcp_rule_inherited_transport_layer_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<TRANSPORT-LAYER-RULE>"
            "<TCP-RULE>"
            "<CHECKSUM-VERIFICATION>true</CHECKSUM-VERIFICATION>"
            "<MAX-DESTINATION-PORT-NUMBER>8080</MAX-DESTINATION-PORT-NUMBER>"
            "<MIN-SOURCE-PORT-NUMBER>2000</MIN-SOURCE-PORT-NUMBER>"
            "</TCP-RULE>"
            "</TRANSPORT-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        transport_rule = rule.getTransportLayerRule()
        assert isinstance(transport_rule, TcpRule)
        assert transport_rule.getChecksumVerification().getValue() is True
        assert transport_rule.getMaxDestinationPortNumber().getValue() == 8080
        assert transport_rule.getMinSourcePortNumber().getValue() == 2000
        assert transport_rule.getNumberOfParallelTcpSessions() is None

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
