"""
Writer tests for the PayloadBytePatternRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class PayloadBytePatternRule, AUTOSAR_00052.xsd line 88473 — XSD-only, no own table in repo corpus).

Checks the FirewallRule.payloadBytePatternRule aggregation behind the PAYLOAD-BYTE-PATTERN-RULES
wrapper (PAYLOAD-BYTE-PATTERN-RULE items) and the nested PAYLOAD-BYTE-PATTERN-RULE-PARTS wrapper
(PAYLOAD-BYTE-PATTERN-RULE-PART items with OFFSET before VALUE), plus the absent-element case and
the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_payload_byte_pattern_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, PayloadBytePatternRule, PayloadBytePatternRulePart
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


def _part(offset, value) -> PayloadBytePatternRulePart:
    part = PayloadBytePatternRulePart()
    part.setOffset(_pos_int(offset))
    part.setValue(_pos_int(value))
    return part


def _partial_part() -> PayloadBytePatternRulePart:
    part = PayloadBytePatternRulePart()
    part.setOffset(_pos_int(34))
    return part


def _full_rule() -> FirewallRule:
    rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
    payload_rule = PayloadBytePatternRule()
    payload_rule.addPayloadBytePatternRulePart(_part(0, 255))
    payload_rule.addPayloadBytePatternRulePart(_part(1, 42))
    rule.addPayloadBytePatternRule(payload_rule)
    return rule


class TestWriteFirewallRulePayloadBytePatternRule:
    def test_write_all_parts_in_xsd_order(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        wrapper = root.find("FIREWALL-RULE/PAYLOAD-BYTE-PATTERN-RULES")
        assert wrapper is not None
        rules = wrapper.findall("PAYLOAD-BYTE-PATTERN-RULE")
        assert len(rules) == 1
        parts_wrapper = rules[0].find("PAYLOAD-BYTE-PATTERN-RULE-PARTS")
        assert parts_wrapper is not None
        parts = parts_wrapper.findall("PAYLOAD-BYTE-PATTERN-RULE-PART")
        assert len(parts) == 2
        assert [child.tag for child in parts[0]] == ["OFFSET", "VALUE"]
        assert parts[0].find("OFFSET").text == "0"
        assert parts[0].find("VALUE").text == "255"
        assert [child.tag for child in parts[1]] == ["OFFSET", "VALUE"]
        assert parts[1].find("OFFSET").text == "1"
        assert parts[1].find("VALUE").text == "42"

    def test_write_partial_part_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        payload_rule = PayloadBytePatternRule()
        payload_rule.addPayloadBytePatternRulePart(_partial_part())
        rule.addPayloadBytePatternRule(payload_rule)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        parts = root.findall("FIREWALL-RULE/PAYLOAD-BYTE-PATTERN-RULES/PAYLOAD-BYTE-PATTERN-RULE/PAYLOAD-BYTE-PATTERN-RULE-PARTS/PAYLOAD-BYTE-PATTERN-RULE-PART")
        assert len(parts) == 1
        assert [child.tag for child in parts[0]] == ["OFFSET"]
        assert parts[0].find("OFFSET").text == "34"

    def test_write_rule_without_parts_omits_parts_wrapper(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        rule.addPayloadBytePatternRule(PayloadBytePatternRule())

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        rules = root.findall("FIREWALL-RULE/PAYLOAD-BYTE-PATTERN-RULES/PAYLOAD-BYTE-PATTERN-RULE")
        assert len(rules) == 1
        assert rules[0].find("PAYLOAD-BYTE-PATTERN-RULE-PARTS") is None

    def test_write_no_rules_omits_wrapper_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/PAYLOAD-BYTE-PATTERN-RULES") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        rules = recovered.getPayloadBytePatternRules()
        assert len(rules) == 1
        parts = rules[0].getPayloadBytePatternRuleParts()
        assert len(parts) == 2
        assert parts[0].getOffset().getValue() == 0
        assert parts[0].getValue().getValue() == 255
        assert parts[1].getOffset().getValue() == 1
        assert parts[1].getValue().getValue() == 42
