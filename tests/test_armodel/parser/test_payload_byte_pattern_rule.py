"""
Reader tests for the PayloadBytePatternRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class PayloadBytePatternRule, AUTOSAR_00052.xsd line 88473 — XSD-only, no own table in repo corpus).

Covers the FirewallRule.payloadBytePatternRule aggregation behind the PAYLOAD-BYTE-PATTERN-RULES
wrapper (PAYLOAD-BYTE-PATTERN-RULE items) and the nested PAYLOAD-BYTE-PATTERN-RULE-PARTS wrapper
(PAYLOAD-BYTE-PATTERN-RULE-PART items with OFFSET / VALUE), plus the absent/empty cases.

Round-trip counterpart: tests/test_armodel/writer/test_payload_byte_pattern_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, PayloadBytePatternRule, PayloadBytePatternRulePart
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


class TestReadFirewallRulePayloadBytePatternRule:
    def test_read_all_payload_byte_pattern_rules(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<PAYLOAD-BYTE-PATTERN-RULES>"
            "<PAYLOAD-BYTE-PATTERN-RULE>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PARTS>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PART><OFFSET>0</OFFSET><VALUE>255</VALUE></PAYLOAD-BYTE-PATTERN-RULE-PART>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PART><OFFSET>1</OFFSET><VALUE>42</VALUE></PAYLOAD-BYTE-PATTERN-RULE-PART>"
            "</PAYLOAD-BYTE-PATTERN-RULE-PARTS>"
            "</PAYLOAD-BYTE-PATTERN-RULE>"
            "<PAYLOAD-BYTE-PATTERN-RULE>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PARTS>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PART><OFFSET>34</OFFSET></PAYLOAD-BYTE-PATTERN-RULE-PART>"
            "</PAYLOAD-BYTE-PATTERN-RULE-PARTS>"
            "</PAYLOAD-BYTE-PATTERN-RULE>"
            "</PAYLOAD-BYTE-PATTERN-RULES>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        rules = rule.getPayloadBytePatternRules()
        assert len(rules) == 2
        assert isinstance(rules[0], PayloadBytePatternRule)
        parts0 = rules[0].getPayloadBytePatternRuleParts()
        assert len(parts0) == 2
        assert isinstance(parts0[0], PayloadBytePatternRulePart)
        assert parts0[0].getOffset().getValue() == 0
        assert parts0[0].getValue().getValue() == 255
        assert parts0[1].getOffset().getValue() == 1
        assert parts0[1].getValue().getValue() == 42
        parts1 = rules[1].getPayloadBytePatternRuleParts()
        assert len(parts1) == 1
        assert parts1[0].getOffset().getValue() == 34
        assert parts1[0].getValue() is None

    def test_read_no_payload_byte_pattern_rules_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getPayloadBytePatternRules() == []

    def test_read_empty_payload_byte_pattern_rules_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<PAYLOAD-BYTE-PATTERN-RULES/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getPayloadBytePatternRules() == []

    def test_read_rule_without_parts_wrapper(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<PAYLOAD-BYTE-PATTERN-RULES>" "<PAYLOAD-BYTE-PATTERN-RULE/>" "</PAYLOAD-BYTE-PATTERN-RULES>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        rules = rule.getPayloadBytePatternRules()
        assert len(rules) == 1
        assert rules[0].getPayloadBytePatternRuleParts() == []

    def test_read_empty_parts_wrapper_and_empty_part(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<PAYLOAD-BYTE-PATTERN-RULES>"
            "<PAYLOAD-BYTE-PATTERN-RULE>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PARTS/>"
            "</PAYLOAD-BYTE-PATTERN-RULE>"
            "<PAYLOAD-BYTE-PATTERN-RULE>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PARTS>"
            "<PAYLOAD-BYTE-PATTERN-RULE-PART/>"
            "</PAYLOAD-BYTE-PATTERN-RULE-PARTS>"
            "</PAYLOAD-BYTE-PATTERN-RULE>"
            "</PAYLOAD-BYTE-PATTERN-RULES>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        rules = rule.getPayloadBytePatternRules()
        assert len(rules) == 2
        assert rules[0].getPayloadBytePatternRuleParts() == []
        parts = rules[1].getPayloadBytePatternRuleParts()
        assert len(parts) == 1
        assert parts[0].getOffset() is None
        assert parts[0].getValue() is None
