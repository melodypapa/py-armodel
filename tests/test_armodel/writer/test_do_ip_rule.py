"""
Writer tests for the DoIpRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class DoIpRule, AUTOSAR_00052.xsd line 49327 — XSD-only, no own table in repo corpus).

Checks the child element values and the XSD sequence order (DESTINATION-MAX-ADDRESS,
DESTINATION-MIN-ADDRESS, INVERSE-PROTOCOL-VERSION, PAYLOAD-LENGTH, PAYLOAD-TYPE,
PROTOCOL-VERSION, SOURCE-MAX-ADDRESS, SOURCE-MIN-ADDRESS, UDS-SERVICE), the
absent-element case and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_do_ip_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import DoIpRule, FirewallRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
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


def _full_rule() -> FirewallRule:
    rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
    do_ip = DoIpRule()
    do_ip.setDestinationMaxAddress(_pos_int(1))
    do_ip.setDestinationMinAddress(_pos_int(2))
    do_ip.setInverseProtocolVersion(_pos_int(3))
    do_ip.setPayloadLength(_pos_int(4))
    do_ip.setPayloadType(_pos_int(5))
    do_ip.setProtocolVersion(_pos_int(6))
    do_ip.setSourceMaxAddress(_pos_int(7))
    do_ip.setSourceMinAddress(_pos_int(8))
    do_ip.setUdsService(_pos_int(9))
    rule.setDoIpRule(do_ip)
    return rule


class TestWriteFirewallRuleDoIpRule:
    def test_write_all_attributes_in_xsd_order(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        do_ip_el = root.find("FIREWALL-RULE/DO-IP-RULE")
        assert do_ip_el is not None
        assert [child.tag for child in do_ip_el] == [
            "DESTINATION-MAX-ADDRESS",
            "DESTINATION-MIN-ADDRESS",
            "INVERSE-PROTOCOL-VERSION",
            "PAYLOAD-LENGTH",
            "PAYLOAD-TYPE",
            "PROTOCOL-VERSION",
            "SOURCE-MAX-ADDRESS",
            "SOURCE-MIN-ADDRESS",
            "UDS-SERVICE",
        ]
        assert do_ip_el.find("DESTINATION-MAX-ADDRESS").text == "1"
        assert do_ip_el.find("DESTINATION-MIN-ADDRESS").text == "2"
        assert do_ip_el.find("INVERSE-PROTOCOL-VERSION").text == "3"
        assert do_ip_el.find("PAYLOAD-LENGTH").text == "4"
        assert do_ip_el.find("PAYLOAD-TYPE").text == "5"
        assert do_ip_el.find("PROTOCOL-VERSION").text == "6"
        assert do_ip_el.find("SOURCE-MAX-ADDRESS").text == "7"
        assert do_ip_el.find("SOURCE-MIN-ADDRESS").text == "8"
        assert do_ip_el.find("UDS-SERVICE").text == "9"

    def test_write_partial_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        do_ip = DoIpRule()
        do_ip.setPayloadType(_pos_int(5))
        rule.setDoIpRule(do_ip)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        do_ip_el = root.find("FIREWALL-RULE/DO-IP-RULE")
        assert do_ip_el is not None
        assert [child.tag for child in do_ip_el] == ["PAYLOAD-TYPE"]
        assert do_ip_el.find("PAYLOAD-TYPE").text == "5"

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/DO-IP-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        do_ip = recovered.getDoIpRule()
        assert isinstance(do_ip, DoIpRule)
        assert do_ip.getDestinationMaxAddress().getValue() == 1
        assert do_ip.getDestinationMinAddress().getValue() == 2
        assert do_ip.getInverseProtocolVersion().getValue() == 3
        assert do_ip.getPayloadLength().getValue() == 4
        assert do_ip.getPayloadType().getValue() == 5
        assert do_ip.getProtocolVersion().getValue() == 6
        assert do_ip.getSourceMaxAddress().getValue() == 7
        assert do_ip.getSourceMinAddress().getValue() == 8
        assert do_ip.getUdsService().getValue() == 9
