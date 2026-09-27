"""
Writer tests for the SomeipSdRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class SomeipSdRule, AUTOSAR_00052.xsd line 110652 — XSD-only, no own table in repo corpus).

Checks the child element values and the XSD sequence order (ENTRY-TYPE, EVENT-GROUP-ID,
MAX-MAJOR-VERSION, MAX-MINOR-VERSION, MIN-MAJOR-VERSION, MIN-MINOR-VERSION,
SERVICE-INSTANCE-ID, SERVICE-INTERFACE-ID), the absent-element case and the write→parse
round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_someip_sd_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, SomeipSdRule
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
    ssd = SomeipSdRule()
    ssd.setEntryType(_pos_int(1))
    ssd.setEventGroupId(_pos_int(2))
    ssd.setMaxMajorVersion(_pos_int(3))
    ssd.setMaxMinorVersion(_pos_int(4))
    ssd.setMinMajorVersion(_pos_int(5))
    ssd.setMinMinorVersion(_pos_int(6))
    ssd.setServiceInstanceId(_pos_int(7))
    ssd.setServiceInterfaceId(_pos_int(8))
    rule.setSomeipSdRule(ssd)
    return rule


class TestWriteFirewallRuleSomeipSdRule:
    def test_write_all_attributes_in_xsd_order(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        ssd_el = root.find("FIREWALL-RULE/SOMEIP-SD-RULE")
        assert ssd_el is not None
        assert [child.tag for child in ssd_el] == [
            "ENTRY-TYPE",
            "EVENT-GROUP-ID",
            "MAX-MAJOR-VERSION",
            "MAX-MINOR-VERSION",
            "MIN-MAJOR-VERSION",
            "MIN-MINOR-VERSION",
            "SERVICE-INSTANCE-ID",
            "SERVICE-INTERFACE-ID",
        ]
        assert ssd_el.find("ENTRY-TYPE").text == "1"
        assert ssd_el.find("EVENT-GROUP-ID").text == "2"
        assert ssd_el.find("MAX-MAJOR-VERSION").text == "3"
        assert ssd_el.find("MAX-MINOR-VERSION").text == "4"
        assert ssd_el.find("MIN-MAJOR-VERSION").text == "5"
        assert ssd_el.find("MIN-MINOR-VERSION").text == "6"
        assert ssd_el.find("SERVICE-INSTANCE-ID").text == "7"
        assert ssd_el.find("SERVICE-INTERFACE-ID").text == "8"

    def test_write_partial_rule_omits_absent_elements(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ssd = SomeipSdRule()
        ssd.setEventGroupId(_pos_int(2))
        rule.setSomeipSdRule(ssd)

        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        ssd_el = root.find("FIREWALL-RULE/SOMEIP-SD-RULE")
        assert ssd_el is not None
        assert [child.tag for child in ssd_el] == ["EVENT-GROUP-ID"]
        assert ssd_el.find("EVENT-GROUP-ID").text == "2"

    def test_write_no_rule_omits_element(self):
        writer = _make_writer()
        rule = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, rule)

        assert root.find("FIREWALL-RULE/SOMEIP-SD-RULE") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        root = ET.Element("AR-PACKAGE")
        writer.writeFirewallRule(root, _full_rule())

        inner = ET.tostring(root).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='{QNS}'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Rule1")
        ARXMLParser(options={"warning": True}).readFirewallRule(element, recovered)

        ssd = recovered.getSomeipSdRule()
        assert isinstance(ssd, SomeipSdRule)
        assert ssd.getEntryType().getValue() == 1
        assert ssd.getEventGroupId().getValue() == 2
        assert ssd.getMaxMajorVersion().getValue() == 3
        assert ssd.getMaxMinorVersion().getValue() == 4
        assert ssd.getMinMajorVersion().getValue() == 5
        assert ssd.getMinMinorVersion().getValue() == 6
        assert ssd.getServiceInstanceId().getValue() == 7
        assert ssd.getServiceInterfaceId().getValue() == 8
