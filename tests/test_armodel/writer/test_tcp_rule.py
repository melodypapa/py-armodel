"""
Writer tests for the TcpRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class TcpRule, AUTOSAR_00052.xsd line 120644 — XSD-only, no own table in repo corpus).

Checks the FirewallRule.transportLayerRule choice: a TcpRule instance emits
TRANSPORT-LAYER-RULE/TCP-RULE with its members in XSD order
(NUMBER-OF-PARALLEL-TCP-SESSIONS → STATE-MANAGEMENT-BASED-ON-TCP-FLAGS → TIMEOUT-CHECK),
a plain abstract TransportLayerRule keeps the bare identity element (fallback), and the
write→parse round-trip recovers the TcpRule field values.

Round-trip counterpart: tests/test_armodel/parser/test_tcp_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, TcpRule, TransportLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
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


class TestWriteFirewallRuleTcpRule:
    def test_write_full_tcp_rule_in_xsd_order(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        tcp_rule = TcpRule()
        tcp_rule.setNumberOfParallelTcpSessions(_pos_int(4))
        tcp_rule.setStateManagementBasedOnTcpFlags(_boolean(True))
        tcp_rule.setTimeoutCheck(_pos_int(30))
        rule.setTransportLayerRule(tcp_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        tcp_rule_element = root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE/TCP-RULE")
        assert tcp_rule_element is not None
        assert [child.tag for child in tcp_rule_element] == ["NUMBER-OF-PARALLEL-TCP-SESSIONS", "STATE-MANAGEMENT-BASED-ON-TCP-FLAGS", "TIMEOUT-CHECK"]
        assert tcp_rule_element.find("NUMBER-OF-PARALLEL-TCP-SESSIONS").text == "4"
        assert tcp_rule_element.find("STATE-MANAGEMENT-BASED-ON-TCP-FLAGS").text == "true"
        assert tcp_rule_element.find("TIMEOUT-CHECK").text == "30"

    def test_write_partial_tcp_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        tcp_rule = TcpRule()
        tcp_rule.setTimeoutCheck(_pos_int(60))
        rule.setTransportLayerRule(tcp_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        tcp_rule_element = root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE/TCP-RULE")
        assert tcp_rule_element is not None
        assert [child.tag for child in tcp_rule_element] == ["TIMEOUT-CHECK"]
        assert tcp_rule_element.find("TIMEOUT-CHECK").text == "60"

    def test_write_plain_transport_layer_rule_keeps_identity_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setTransportLayerRule(TransportLayerRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        transport_rule_element = root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE")
        assert transport_rule_element is not None
        assert transport_rule_element.find("TCP-RULE") is None
        assert transport_rule_element.find("UDP-RULE") is None

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        tcp_rule = TcpRule()
        tcp_rule.setNumberOfParallelTcpSessions(_pos_int(4))
        tcp_rule.setStateManagementBasedOnTcpFlags(_boolean(True))
        tcp_rule.setTimeoutCheck(_pos_int(30))
        rule.setTransportLayerRule(tcp_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        transport_rule = recovered.getTransportLayerRule()
        assert isinstance(transport_rule, TcpRule)
        assert transport_rule.getNumberOfParallelTcpSessions().getValue() == 4
        assert transport_rule.getStateManagementBasedOnTcpFlags().getValue() is True
        assert transport_rule.getTimeoutCheck().getValue() == 30
