"""
Reader tests for the SomeipSdRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class SomeipSdRule, AUTOSAR_00052.xsd line 110652 — XSD-only, no own table in repo corpus).

Covers the eight filter attributes behind the SOMEIP-SD-RULE element (ENTRY-TYPE …
SERVICE-INTERFACE-ID), the absent-element case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_someip_sd_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, SomeipSdRule
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


class TestReadFirewallRuleSomeipSdRule:
    def test_read_all_someip_sd_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<SOMEIP-SD-RULE>"
            "<ENTRY-TYPE>1</ENTRY-TYPE>"
            "<EVENT-GROUP-ID>2</EVENT-GROUP-ID>"
            "<MAX-MAJOR-VERSION>3</MAX-MAJOR-VERSION>"
            "<MAX-MINOR-VERSION>4</MAX-MINOR-VERSION>"
            "<MIN-MAJOR-VERSION>5</MIN-MAJOR-VERSION>"
            "<MIN-MINOR-VERSION>6</MIN-MINOR-VERSION>"
            "<SERVICE-INSTANCE-ID>7</SERVICE-INSTANCE-ID>"
            "<SERVICE-INTERFACE-ID>8</SERVICE-INTERFACE-ID>"
            "</SOMEIP-SD-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        ssd = rule.getSomeipSdRule()
        assert isinstance(ssd, SomeipSdRule)
        assert ssd.getEntryType().getValue() == 1
        assert ssd.getEventGroupId().getValue() == 2
        assert ssd.getMaxMajorVersion().getValue() == 3
        assert ssd.getMaxMinorVersion().getValue() == 4
        assert ssd.getMinMajorVersion().getValue() == 5
        assert ssd.getMinMinorVersion().getValue() == 6
        assert ssd.getServiceInstanceId().getValue() == 7
        assert ssd.getServiceInterfaceId().getValue() == 8

    def test_read_partial_someip_sd_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<SOMEIP-SD-RULE>" "<EVENT-GROUP-ID>2</EVENT-GROUP-ID>" "</SOMEIP-SD-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        ssd = rule.getSomeipSdRule()
        assert ssd.getEventGroupId().getValue() == 2
        assert ssd.getEntryType() is None
        assert ssd.getMaxMajorVersion() is None
        assert ssd.getMaxMinorVersion() is None
        assert ssd.getMinMajorVersion() is None
        assert ssd.getMinMinorVersion() is None
        assert ssd.getServiceInstanceId() is None
        assert ssd.getServiceInterfaceId() is None

    def test_read_no_someip_sd_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getSomeipSdRule() is None

    def test_read_empty_someip_sd_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<SOMEIP-SD-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        ssd = rule.getSomeipSdRule()
        assert isinstance(ssd, SomeipSdRule)
        assert ssd.getEntryType() is None
        assert ssd.getServiceInterfaceId() is None
