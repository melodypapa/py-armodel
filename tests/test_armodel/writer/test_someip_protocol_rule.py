"""
Writer tests for the SomeipProtocolRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class SomeipProtocolRule, AUTOSAR_00052.xsd line 110084 — XSD-only, no own table in repo corpus).

Checks the child element values and the XSD sequence order (CLIENT-ID, LENGTH-VERIFICATION,
MAJOR-VERSION, MESSAGE-TYPE, METHOD-ID, PROTOCOL-VERSION, RETURN-CODE, SERVICE-INTERFACE-ID),
the absent-element case and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_someip_protocol_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, SomeipProtocolRule
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


def _full_rule() -> FirewallRule:
    rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
    spr = SomeipProtocolRule()
    spr.setClientId(_pos_int(1))
    spr.setLengthVerification(_boolean(True))
    spr.setMajorVersion(_pos_int(2))
    spr.setMessageType(_pos_int(3))
    spr.setMethodId(_pos_int(4))
    spr.setProtocolVersion(_pos_int(5))
    spr.setReturnCode(_pos_int(6))
    spr.setServiceInterfaceId(_pos_int(7))
    rule.setSomeipRule(spr)
    return rule


class TestWriteFirewallRuleSomeipProtocolRule:
    def test_write_all_attributes_in_xsd_order(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        spr_el = root.find("FIREWALL-RULE/SOMEIP-RULE")
        assert spr_el is not None
        assert [child.tag for child in spr_el] == [
            "CLIENT-ID",
            "LENGTH-VERIFICATION",
            "MAJOR-VERSION",
            "MESSAGE-TYPE",
            "METHOD-ID",
            "PROTOCOL-VERSION",
            "RETURN-CODE",
            "SERVICE-INTERFACE-ID",
        ]
        assert spr_el.find("CLIENT-ID").text == "1"
        assert spr_el.find("LENGTH-VERIFICATION").text == "true"
        assert spr_el.find("MAJOR-VERSION").text == "2"
        assert spr_el.find("MESSAGE-TYPE").text == "3"
        assert spr_el.find("METHOD-ID").text == "4"
        assert spr_el.find("PROTOCOL-VERSION").text == "5"
        assert spr_el.find("RETURN-CODE").text == "6"
        assert spr_el.find("SERVICE-INTERFACE-ID").text == "7"

    def test_write_partial_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        spr = SomeipProtocolRule()
        spr.setMethodId(_pos_int(4))
        rule.setSomeipRule(spr)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        spr_el = root.find("FIREWALL-RULE/SOMEIP-RULE")
        assert spr_el is not None
        assert [child.tag for child in spr_el] == ["METHOD-ID"]
        assert spr_el.find("METHOD-ID").text == "4"

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/SOMEIP-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        spr = recovered.getSomeipRule()
        assert isinstance(spr, SomeipProtocolRule)
        assert spr.getClientId().getValue() == 1
        assert spr.getLengthVerification().getValue() is True
        assert spr.getMajorVersion().getValue() == 2
        assert spr.getMessageType().getValue() == 3
        assert spr.getMethodId().getValue() == 4
        assert spr.getProtocolVersion().getValue() == 5
        assert spr.getReturnCode().getValue() == 6
        assert spr.getServiceInterfaceId().getValue() == 7
