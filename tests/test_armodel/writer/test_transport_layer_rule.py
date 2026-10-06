"""
Writer tests for the TransportLayerRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class TransportLayerRule, AUTOSAR_00052.xsd line 126190 — XSD-only, no own table in repo corpus).

The abstract class owns the 5 TRANSPORT-LAYER-RULE group members (checksumVerification and the
four port-number filters), so the bare TRANSPORT-LAYER-RULE element (no subtype child) carries
them; the concrete subtypes TcpRule/UdpRule inherit the members per the XSD group composition.

Round-trip counterpart: tests/test_armodel/parser/test_transport_layer_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, TransportLayerRule
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


class TestWriteFirewallRuleTransportLayerRule:
    def test_write_transport_layer_rule_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.setTransportLayerRule(TransportLayerRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE") is not None

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE") is None

    def test_write_bare_element_member_values_and_order(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        transport_rule = TransportLayerRule()
        transport_rule.setChecksumVerification(_boolean(True))
        transport_rule.setMaxDestinationPortNumber(_pos_int(8080))
        transport_rule.setMaxSourcePortNumber(_pos_int(9090))
        transport_rule.setMinDestinationPortNumber(_pos_int(1000))
        transport_rule.setMinSourcePortNumber(_pos_int(2000))
        rule.setTransportLayerRule(transport_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        element = root.find("FIREWALL-RULE/TRANSPORT-LAYER-RULE")
        assert element is not None
        assert [child.tag for child in element] == [
            "CHECKSUM-VERIFICATION",
            "MAX-DESTINATION-PORT-NUMBER",
            "MAX-SOURCE-PORT-NUMBER",
            "MIN-DESTINATION-PORT-NUMBER",
            "MIN-SOURCE-PORT-NUMBER",
        ]
        assert element.find("CHECKSUM-VERIFICATION").text == "true"
        assert element.find("MAX-DESTINATION-PORT-NUMBER").text == "8080"
        assert element.find("MAX-SOURCE-PORT-NUMBER").text == "9090"
        assert element.find("MIN-DESTINATION-PORT-NUMBER").text == "1000"
        assert element.find("MIN-SOURCE-PORT-NUMBER").text == "2000"

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        transport_rule = TransportLayerRule()
        transport_rule.setChecksumVerification(_boolean(True))
        transport_rule.setMaxDestinationPortNumber(_pos_int(8080))
        transport_rule.setMinSourcePortNumber(_pos_int(2000))
        rule.setTransportLayerRule(transport_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        recovered_rule = recovered.getTransportLayerRule()
        assert isinstance(recovered_rule, TransportLayerRule)
        assert recovered_rule.getChecksumVerification().getValue() is True
        assert recovered_rule.getMaxDestinationPortNumber().getValue() == 8080
        assert recovered_rule.getMinSourcePortNumber().getValue() == 2000
        assert recovered_rule.getMaxSourcePortNumber() is None
