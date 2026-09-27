"""
Reader tests for the IcmpRule nested child of Ipv4Rule/Ipv6Rule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class IcmpRule, AUTOSAR_00052.xsd line 67721 — XSD-only, no own table in repo corpus).

The ICMP-RULE element never appears standalone: it is a child of IPV-4-RULE / IPV-6-RULE
(00052 L74433 / L74973), which wrap the FirewallRule.networkLayerRule choice. Until the
IPV-4-RULE/IPV-6-RULE wrappers sync, coverage exercises the readIcmpRule helper directly
on a manually built ICMP-RULE fragment (CHECKSUM-VERIFICATION / CODE / TYPE in XSD order).

Round-trip counterpart: tests/test_armodel/writer/test_icmp_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import IcmpRule
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ICMP-RULE xmlns='{NS}'>{inner}</ICMP-RULE>")


class TestReadIcmpRule:
    def test_read_full_icmp_rule(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<CHECKSUM-VERIFICATION>true</CHECKSUM-VERIFICATION>" "<CODE>3</CODE>" "<TYPE>8</TYPE>")
        rule = IcmpRule()
        parser.readIcmpRule(element, rule)

        assert rule.getChecksumVerification().getValue() is True
        assert rule.getCode().getValue() == 3
        assert rule.getType().getValue() == 8

    def test_read_partial_icmp_rule_omits_absent_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<TYPE>0</TYPE>")
        rule = IcmpRule()
        parser.readIcmpRule(element, rule)

        assert rule.getChecksumVerification() is None
        assert rule.getCode() is None
        assert rule.getType().getValue() == 0

    def test_read_empty_icmp_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(f"<ICMP-RULE xmlns='{NS}'/>")
        rule = IcmpRule()
        parser.readIcmpRule(element, rule)

        assert rule.getChecksumVerification() is None
        assert rule.getCode() is None
        assert rule.getType() is None
