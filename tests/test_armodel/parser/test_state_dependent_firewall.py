"""
Reader tests for StateDependentFirewall (AUTOSAR_CP_TPS_SystemTemplate, Table 6.234).

Covers the three own attributes: defaultAction (attr), firewallRuleProps (ordered aggr
behind the FIREWALL-RULE-PROPSS wrapper) and firewallStateModeDeclaration (ref behind
the FIREWALL-STATE-MODE-DECLARATION-REFS wrapper), plus the absent-element and
empty-wrapper cases.

Round-trip counterpart: tests/test_armodel/writer/test_state_dependent_firewall.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallActionEnum, FirewallRuleProps, StateDependentFirewall
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<STATE-DEPENDENT-FIREWALL xmlns='{NS}'>{inner}</STATE-DEPENDENT-FIREWALL>")


def _firewall() -> StateDependentFirewall:
    return StateDependentFirewall(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "FW1")


class TestReadStateDependentFirewall:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>FW1</SHORT-NAME>"
            "<DEFAULT-ACTION>BLOCK</DEFAULT-ACTION>"
            "<FIREWALL-RULE-PROPSS>"
            "<FIREWALL-RULE-PROPS>"
            "<ACTION>ALLOW</ACTION>"
            "<MATCHING-EGRESS-RULE-REFS>"
            "<MATCHING-EGRESS-RULE-REF DEST='FIREWALL-RULE'>/AUTOSAR/FirewallRules/Rule</MATCHING-EGRESS-RULE-REF>"
            "</MATCHING-EGRESS-RULE-REFS>"
            "<MATCHING-INGRESS-RULE-REFS>"
            "<MATCHING-INGRESS-RULE-REF DEST='FIREWALL-RULE'>/AUTOSAR/FirewallRules/Rule2</MATCHING-INGRESS-RULE-REF>"
            "</MATCHING-INGRESS-RULE-REFS>"
            "</FIREWALL-RULE-PROPS>"
            "</FIREWALL-RULE-PROPSS>"
            "<FIREWALL-STATE-MODE-DECLARATION-REFS>"
            "<FIREWALL-STATE-MODE-DECLARATION-REF DEST='MODE-DECLARATION'>/AUTOSAR/Modes/State</FIREWALL-STATE-MODE-DECLARATION-REF>"
            "</FIREWALL-STATE-MODE-DECLARATION-REFS>"
        )
        firewall = _firewall()
        parser.readStateDependentFirewall(element, firewall)

        default_action = firewall.getDefaultAction()
        assert default_action is not None
        assert default_action.getValue() == FirewallActionEnum.BLOCK

        props_list = firewall.getFirewallRuleProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert isinstance(props, FirewallRuleProps)
        assert props.getAction() is not None and props.getAction().getValue() == FirewallActionEnum.ALLOW
        assert [ref.getValue() for ref in props.getMatchingEgressRuleRefs()] == ["/AUTOSAR/FirewallRules/Rule"]
        assert [ref.getValue() for ref in props.getMatchingIngressRuleRefs()] == ["/AUTOSAR/FirewallRules/Rule2"]

        assert [ref.getValue() for ref in firewall.getFirewallStateModeDeclarationRefs()] == ["/AUTOSAR/Modes/State"]

    def test_read_two_firewall_rule_props_keeps_order(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>FW1</SHORT-NAME>"
            "<FIREWALL-RULE-PROPSS>"
            "<FIREWALL-RULE-PROPS><ACTION>BLOCK</ACTION></FIREWALL-RULE-PROPS>"
            "<FIREWALL-RULE-PROPS><ACTION>ALLOW</ACTION></FIREWALL-RULE-PROPS>"
            "</FIREWALL-RULE-PROPSS>"
        )
        firewall = _firewall()
        parser.readStateDependentFirewall(element, firewall)

        props_list = firewall.getFirewallRuleProps()
        assert [props.getAction().getValue() for props in props_list] == [FirewallActionEnum.BLOCK, FirewallActionEnum.ALLOW]

    def test_read_no_optional_elements(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>FW1</SHORT-NAME>")
        firewall = _firewall()
        parser.readStateDependentFirewall(element, firewall)

        assert firewall.getDefaultAction() is None
        assert firewall.getFirewallRuleProps() == []
        assert firewall.getFirewallStateModeDeclarationRefs() == []

    def test_read_empty_wrappers(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>FW1</SHORT-NAME>" "<FIREWALL-RULE-PROPSS/>" "<FIREWALL-STATE-MODE-DECLARATION-REFS/>")
        firewall = _firewall()
        parser.readStateDependentFirewall(element, firewall)

        assert firewall.getFirewallRuleProps() == []
        assert firewall.getFirewallStateModeDeclarationRefs() == []
