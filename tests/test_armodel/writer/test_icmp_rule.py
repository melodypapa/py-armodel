"""
Writer tests for the IcmpRule nested child of Ipv4Rule/Ipv6Rule (AUTOSAR_AP_TPS_PlatformModuleDeployment,
class IcmpRule, AUTOSAR_00052.xsd line 67721 — XSD-only, no own table in repo corpus).

The ICMP-RULE element never appears standalone: it is a child of IPV-4-RULE / IPV-6-RULE
(00052 L74433 / L74973), which wrap the FirewallRule.networkLayerRule choice. Until the
IPV-4-RULE/IPV-6-RULE wrappers sync, coverage exercises the writeIcmpRule helper directly:
it emits the members in XSD order (CHECKSUM-VERIFICATION → CODE → TYPE) inside a caller-created
ICMP-RULE element, omits absent members, and the write→parse round-trip recovers the values.

Round-trip counterpart: tests/test_armodel/parser/test_icmp_rule.py
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import IcmpRule
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


class TestWriteIcmpRule:
    def test_write_full_icmp_rule_in_xsd_order(self):
        writer = _make_writer()
        icmp_rule = IcmpRule()
        icmp_rule.setChecksumVerification(_boolean(True))
        icmp_rule.setCode(_pos_int(3))
        icmp_rule.setType(_pos_int(8))

        element = ET.Element("ICMP-RULE")
        writer.writeIcmpRule(element, icmp_rule)

        assert [child.tag for child in element] == ["CHECKSUM-VERIFICATION", "CODE", "TYPE"]
        assert element.find("CHECKSUM-VERIFICATION").text == "true"
        assert element.find("CODE").text == "3"
        assert element.find("TYPE").text == "8"

    def test_write_partial_icmp_rule_omits_absent_elements(self):
        writer = _make_writer()
        icmp_rule = IcmpRule()
        icmp_rule.setCode(_pos_int(0))

        element = ET.Element("ICMP-RULE")
        writer.writeIcmpRule(element, icmp_rule)

        assert [child.tag for child in element] == ["CODE"]
        assert element.find("CODE").text == "0"

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        icmp_rule = IcmpRule()
        icmp_rule.setChecksumVerification(_boolean(True))
        icmp_rule.setCode(_pos_int(3))
        icmp_rule.setType(_pos_int(8))

        element = ET.Element("ICMP-RULE")
        writer.writeIcmpRule(element, icmp_rule)

        inner = ET.tostring(element).decode("utf-8")
        parsed = ET.fromstring(f"<WRAP xmlns='{QNS}'>{inner}</WRAP>")[0]

        recovered = IcmpRule()
        ARXMLParser(options={"warning": True}).readIcmpRule(parsed, recovered)

        assert recovered.getChecksumVerification().getValue() is True
        assert recovered.getCode().getValue() == 3
        assert recovered.getType().getValue() == 8
