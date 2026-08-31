"""
Writer tests for StateDependentFirewall (AUTOSAR_CP_TPS_SystemTemplate, Table 6.234).

The writer emits unprefixed child elements, so structure checks inspect the in-memory
tree with unprefixed names. The round-trip serializes and reparses so the default
AUTOSAR namespace applies (the parser's find() is namespace-aware), then re-reads the
model.

Round-trip counterpart: tests/test_armodel/parser/test_state_dependent_firewall.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallActionEnum, FirewallRuleProps, StateDependentFirewall
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
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


def _full_firewall() -> StateDependentFirewall:
    firewall = StateDependentFirewall(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "FW1")
    firewall.setDefaultAction(FirewallActionEnum().setValue(FirewallActionEnum.BLOCK))
    props = FirewallRuleProps()
    props.setAction(FirewallActionEnum().setValue(FirewallActionEnum.ALLOW))
    egress_ref = RefType()
    egress_ref.setValue("/AUTOSAR/FirewallRules/Rule")
    props.addMatchingEgressRuleRef(egress_ref)
    firewall.addFirewallRuleProps(props)
    mode_ref = RefType()
    mode_ref.setValue("/AUTOSAR/Modes/State")
    firewall.addFirewallStateModeDeclarationRef(mode_ref)
    return firewall


class TestWriteStateDependentFirewall:
    def test_write_all_attributes(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeStateDependentFirewall(root, _full_firewall())

        firewall_el = root.find("STATE-DEPENDENT-FIREWALL")
        assert firewall_el is not None
        assert firewall_el.find("SHORT-NAME").text == "FW1"
        assert firewall_el.find("DEFAULT-ACTION").text == "BLOCK"

        props_el = firewall_el.find("FIREWALL-RULE-PROPSS/FIREWALL-RULE-PROPS")
        assert props_el is not None
        assert props_el.find("ACTION").text == "ALLOW"
        assert props_el.find("MATCHING-EGRESS-RULE-REFS/MATCHING-EGRESS-RULE-REF").text == "/AUTOSAR/FirewallRules/Rule"
        assert props_el.find("MATCHING-INGRESS-RULE-REFS") is None

        mode_ref_el = firewall_el.find("FIREWALL-STATE-MODE-DECLARATION-REFS/FIREWALL-STATE-MODE-DECLARATION-REF")
        assert mode_ref_el is not None
        assert mode_ref_el.text == "/AUTOSAR/Modes/State"

    def test_write_empty_lists_emits_no_wrappers(self):
        writer = _make_writer()
        firewall = StateDependentFirewall(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "FW1")
        root = ET.Element("AR-PACKAGE")
        writer.writeStateDependentFirewall(root, firewall)

        firewall_el = root.find("STATE-DEPENDENT-FIREWALL")
        assert firewall_el.find("DEFAULT-ACTION") is None
        assert firewall_el.find("FIREWALL-RULE-PROPSS") is None
        assert firewall_el.find("FIREWALL-STATE-MODE-DECLARATION-REFS") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeStateDependentFirewall(root, _full_firewall())

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = StateDependentFirewall(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "FW1")
        ARXMLParser(options={"warning": True}).readStateDependentFirewall(element, recovered)

        assert recovered.getShortName() == "FW1"
        assert recovered.getDefaultAction() is not None and recovered.getDefaultAction().getValue() == FirewallActionEnum.BLOCK
        props_list = recovered.getFirewallRuleProps()
        assert len(props_list) == 1
        assert props_list[0].getAction() is not None and props_list[0].getAction().getValue() == FirewallActionEnum.ALLOW
        assert [ref.getValue() for ref in props_list[0].getMatchingEgressRuleRefs()] == ["/AUTOSAR/FirewallRules/Rule"]
        assert [ref.getValue() for ref in recovered.getFirewallStateModeDeclarationRefs()] == ["/AUTOSAR/Modes/State"]
