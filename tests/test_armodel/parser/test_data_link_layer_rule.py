"""
Reader tests for the DataLinkLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class DataLinkLayerRule, AUTOSAR_00052.xsd line 27236 — XSD-only, no own table in repo corpus).

Covers the seven filter attributes behind the DATA-LINK-LAYER-RULE element, the absent-element
case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_data_link_layer_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import DataLinkLayerRule, FirewallRule
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


class TestReadFirewallRuleDataLinkLayerRule:
    def test_read_all_data_link_layer_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<DATA-LINK-LAYER-RULE>"
            "<DESTINATION-MAC-ADDRESS>FF:FF:FF:FF:FF:FF</DESTINATION-MAC-ADDRESS>"
            "<DESTINATION-MAC-ADDRESS-MASK>FF:00:00:00:00:00</DESTINATION-MAC-ADDRESS-MASK>"
            "<ETHER-TYPE>2048</ETHER-TYPE>"
            "<SOURCE-MAC-ADDRESS>AA:BB:CC:DD:EE:FF</SOURCE-MAC-ADDRESS>"
            "<SOURCE-MAC-ADDRESS-MASK>FF:FF:00:00:00:00</SOURCE-MAC-ADDRESS-MASK>"
            "<VLAN-ID>100</VLAN-ID>"
            "<VLAN-PRIORITY>3</VLAN-PRIORITY>"
            "</DATA-LINK-LAYER-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        dlr = rule.getDataLinkLayerRule()
        assert isinstance(dlr, DataLinkLayerRule)
        assert dlr.getDestinationMacAddress().getValue() == "FF:FF:FF:FF:FF:FF"
        assert dlr.getDestinationMacAddressMask().getValue() == "FF:00:00:00:00:00"
        assert dlr.getEtherType().getValue() == 2048
        assert dlr.getSourceMacAddress().getValue() == "AA:BB:CC:DD:EE:FF"
        assert dlr.getSourceMacAddressMask().getValue() == "FF:FF:00:00:00:00"
        assert dlr.getVlanId().getValue() == 100
        assert dlr.getVlanPriority().getValue() == 3

    def test_read_partial_data_link_layer_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<DATA-LINK-LAYER-RULE>" "<ETHER-TYPE>34525</ETHER-TYPE>" "</DATA-LINK-LAYER-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        dlr = rule.getDataLinkLayerRule()
        assert dlr.getEtherType().getValue() == 34525
        assert dlr.getDestinationMacAddress() is None
        assert dlr.getDestinationMacAddressMask() is None
        assert dlr.getSourceMacAddress() is None
        assert dlr.getSourceMacAddressMask() is None
        assert dlr.getVlanId() is None
        assert dlr.getVlanPriority() is None

    def test_read_no_data_link_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getDataLinkLayerRule() is None

    def test_read_empty_data_link_layer_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<DATA-LINK-LAYER-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        dlr = rule.getDataLinkLayerRule()
        assert isinstance(dlr, DataLinkLayerRule)
        assert dlr.getDestinationMacAddress() is None
        assert dlr.getEtherType() is None
        assert dlr.getVlanId() is None
