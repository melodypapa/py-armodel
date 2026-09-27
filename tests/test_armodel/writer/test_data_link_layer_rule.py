"""
Writer tests for the DataLinkLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class DataLinkLayerRule, AUTOSAR_00052.xsd line 27236 — XSD-only, no own table in repo corpus).

Checks the child element values and the XSD sequence order (DESTINATION-MAC-ADDRESS …
VLAN-PRIORITY), the absent-element case, and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_data_link_layer_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import DataLinkLayerRule, FirewallRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString, PositiveInteger
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


def _mac(value):
    m = MacAddressString()
    m.setValue(value)
    return m


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _full_rule() -> FirewallRule:
    rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
    dlr = DataLinkLayerRule()
    dlr.setDestinationMacAddress(_mac("FF:FF:FF:FF:FF:FF"))
    dlr.setDestinationMacAddressMask(_mac("FF:00:00:00:00:00"))
    dlr.setEtherType(_pos_int(2048))
    dlr.setSourceMacAddress(_mac("AA:BB:CC:DD:EE:FF"))
    dlr.setSourceMacAddressMask(_mac("FF:FF:00:00:00:00"))
    dlr.setVlanId(_pos_int(100))
    dlr.setVlanPriority(_pos_int(3))
    rule.setDataLinkLayerRule(dlr)
    return rule


class TestWriteFirewallRuleDataLinkLayerRule:
    def test_write_all_attributes_in_xsd_order(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        dlr_el = root.find("FIREWALL-RULE/DATA-LINK-LAYER-RULE")
        assert dlr_el is not None
        assert [child.tag for child in dlr_el] == [
            "DESTINATION-MAC-ADDRESS",
            "DESTINATION-MAC-ADDRESS-MASK",
            "ETHER-TYPE",
            "SOURCE-MAC-ADDRESS",
            "SOURCE-MAC-ADDRESS-MASK",
            "VLAN-ID",
            "VLAN-PRIORITY",
        ]
        assert dlr_el.find("DESTINATION-MAC-ADDRESS").text == "FF:FF:FF:FF:FF:FF"
        assert dlr_el.find("DESTINATION-MAC-ADDRESS-MASK").text == "FF:00:00:00:00:00"
        assert dlr_el.find("ETHER-TYPE").text == "2048"
        assert dlr_el.find("SOURCE-MAC-ADDRESS").text == "AA:BB:CC:DD:EE:FF"
        assert dlr_el.find("SOURCE-MAC-ADDRESS-MASK").text == "FF:FF:00:00:00:00"
        assert dlr_el.find("VLAN-ID").text == "100"
        assert dlr_el.find("VLAN-PRIORITY").text == "3"

    def test_write_partial_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        dlr = DataLinkLayerRule()
        dlr.setVlanId(_pos_int(100))
        rule.setDataLinkLayerRule(dlr)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        dlr_el = root.find("FIREWALL-RULE/DATA-LINK-LAYER-RULE")
        assert dlr_el is not None
        assert [child.tag for child in dlr_el] == ["VLAN-ID"]

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/DATA-LINK-LAYER-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        dlr = recovered.getDataLinkLayerRule()
        assert isinstance(dlr, DataLinkLayerRule)
        assert dlr.getDestinationMacAddress().getValue() == "FF:FF:FF:FF:FF:FF"
        assert dlr.getDestinationMacAddressMask().getValue() == "FF:00:00:00:00:00"
        assert dlr.getEtherType().getValue() == 2048
        assert dlr.getSourceMacAddress().getValue() == "AA:BB:CC:DD:EE:FF"
        assert dlr.getSourceMacAddressMask().getValue() == "FF:FF:00:00:00:00"
        assert dlr.getVlanId().getValue() == 100
        assert dlr.getVlanPriority().getValue() == 3
