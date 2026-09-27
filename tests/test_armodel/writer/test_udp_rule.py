"""
Writer tests for the UdpRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class UdpRule, AUTOSAR_00052.xsd line 127875 — XSD-only, no own table in repo corpus).

Checks the FirewallRule.transportLayerRule choice: a UdpRule instance emits an
identity-only TRANSPORT-LAYER-RULE/UDP-RULE element (the UDP-RULE group is an empty
sequence — no own members), a TcpRule still dispatches to TCP-RULE, and the write→parse
round-trip recovers the UdpRule instance.

Round-trip counterpart: tests/test_armodel/parser/test_udp_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, UdpRule
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


class TestWriteFirewallRuleUdpRule:
    def test_write_identity_only_udp_rule_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setTransportLayerRule(UdpRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        udp_rule_element = root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE/UDP-RULE")
        assert udp_rule_element is not None
        assert len(list(udp_rule_element)) == 0

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setTransportLayerRule(UdpRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        assert isinstance(recovered.getTransportLayerRule(), UdpRule)
