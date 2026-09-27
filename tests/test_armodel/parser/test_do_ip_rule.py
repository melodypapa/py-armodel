"""
Reader tests for the DoIpRule child of FirewallRule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class DoIpRule, AUTOSAR_00052.xsd line 49327 — XSD-only, no own table in repo corpus).

Covers the nine filter attributes behind the DO-IP-RULE element (DESTINATION-MAX-ADDRESS …
UDS-SERVICE), the absent-element case and the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_do_ip_rule.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import DoIpRule, FirewallRule
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


class TestReadFirewallRuleDoIpRule:
    def test_read_all_do_ip_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Rule1</SHORT-NAME>"
            "<DO-IP-RULE>"
            "<DESTINATION-MAX-ADDRESS>1</DESTINATION-MAX-ADDRESS>"
            "<DESTINATION-MIN-ADDRESS>2</DESTINATION-MIN-ADDRESS>"
            "<INVERSE-PROTOCOL-VERSION>3</INVERSE-PROTOCOL-VERSION>"
            "<PAYLOAD-LENGTH>4</PAYLOAD-LENGTH>"
            "<PAYLOAD-TYPE>5</PAYLOAD-TYPE>"
            "<PROTOCOL-VERSION>6</PROTOCOL-VERSION>"
            "<SOURCE-MAX-ADDRESS>7</SOURCE-MAX-ADDRESS>"
            "<SOURCE-MIN-ADDRESS>8</SOURCE-MIN-ADDRESS>"
            "<UDS-SERVICE>9</UDS-SERVICE>"
            "</DO-IP-RULE>"
        )
        rule = _rule()
        parser.readFirewallRule(element, rule)

        do_ip = rule.getDoIpRule()
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

    def test_read_partial_do_ip_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<DO-IP-RULE>" "<PAYLOAD-TYPE>5</PAYLOAD-TYPE>" "</DO-IP-RULE>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        do_ip = rule.getDoIpRule()
        assert do_ip.getPayloadType().getValue() == 5
        assert do_ip.getDestinationMaxAddress() is None
        assert do_ip.getDestinationMinAddress() is None
        assert do_ip.getInverseProtocolVersion() is None
        assert do_ip.getPayloadLength() is None
        assert do_ip.getProtocolVersion() is None
        assert do_ip.getSourceMaxAddress() is None
        assert do_ip.getSourceMinAddress() is None
        assert do_ip.getUdsService() is None

    def test_read_no_do_ip_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        assert rule.getDoIpRule() is None

    def test_read_empty_do_ip_rule_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Rule1</SHORT-NAME>" "<DO-IP-RULE/>")
        rule = _rule()
        parser.readFirewallRule(element, rule)

        do_ip = rule.getDoIpRule()
        assert isinstance(do_ip, DoIpRule)
        assert do_ip.getDestinationMaxAddress() is None
        assert do_ip.getUdsService() is None
