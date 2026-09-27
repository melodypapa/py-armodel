"""
Writer tests for the NetworkLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class NetworkLayerRule, AUTOSAR_00052.xsd line 84252 — XSD-only, no own table in repo corpus).

The abstract class owns an empty group (no own attributes), so the writer emits the
bare NETWORK-LAYER-RULE element when the aggregation is set (placeholder until the
concrete subtypes Ipv4Rule/Ipv6Rule sync, Rule 0001.10).

Round-trip counterpart: tests/test_armodel/parser/test_network_layer_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, NetworkLayerRule
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


class TestWriteFirewallRuleNetworkLayerRule:
    def test_write_network_layer_rule_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setNetworkLayerRule(NetworkLayerRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/NETWORK-LAYER-RULE") is not None

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/NETWORK-LAYER-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setNetworkLayerRule(NetworkLayerRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        assert isinstance(recovered.getNetworkLayerRule(), NetworkLayerRule)
