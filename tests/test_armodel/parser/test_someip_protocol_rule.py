"""
Reader tests for the SomeipProtocolRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class SomeipProtocolRule, AUTOSAR_00052.xsd line 110084 — XSD-only, no own table in repo corpus).

Covers the eight filter attributes behind the SOMEIP-RULE element (CLIENT-ID …
SERVICE-INTERFACE-ID, with the AR:BOOLEAN LENGTH-VERIFICATION), the absent-element
case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_someip_protocol_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import FirewallRule, SomeipProtocolRule
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


class TestReadFirewallRuleSomeipProtocolRule:
    def test_read_all_someip_protocol_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<SOMEIP-RULE>"
            "<CLIENT-ID>1</CLIENT-ID>"
            "<LENGTH-VERIFICATION>true</LENGTH-VERIFICATION>"
            "<MAJOR-VERSION>2</MAJOR-VERSION>"
            "<MESSAGE-TYPE>3</MESSAGE-TYPE>"
            "<METHOD-ID>4</METHOD-ID>"
            "<PROTOCOL-VERSION>5</PROTOCOL-VERSION>"
            "<RETURN-CODE>6</RETURN-CODE>"
            "<SERVICE-INTERFACE-ID>7</SERVICE-INTERFACE-ID>"
            "</SOMEIP-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        spr = rule.getSomeipRule()
        assert isinstance(spr, SomeipProtocolRule)
        assert spr.getClientId().getValue() == 1
        assert spr.getLengthVerification().getValue() is True
        assert spr.getMajorVersion().getValue() == 2
        assert spr.getMessageType().getValue() == 3
        assert spr.getMethodId().getValue() == 4
        assert spr.getProtocolVersion().getValue() == 5
        assert spr.getReturnCode().getValue() == 6
        assert spr.getServiceInterfaceId().getValue() == 7

    def test_read_partial_someip_protocol_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<SOMEIP-RULE>" "<METHOD-ID>4</METHOD-ID>" "</SOMEIP-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        spr = rule.getSomeipRule()
        assert spr.getMethodId().getValue() == 4
        assert spr.getClientId() is None
        assert spr.getLengthVerification() is None
        assert spr.getMajorVersion() is None
        assert spr.getMessageType() is None
        assert spr.getProtocolVersion() is None
        assert spr.getReturnCode() is None
        assert spr.getServiceInterfaceId() is None

    def test_read_no_someip_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getSomeipRule() is None

    def test_read_empty_someip_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<SOMEIP-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        spr = rule.getSomeipRule()
        assert isinstance(spr, SomeipProtocolRule)
        assert spr.getClientId() is None
        assert spr.getLengthVerification() is None
        assert spr.getServiceInterfaceId() is None
