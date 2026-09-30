"""Writer/reader round-trip tests for IPSecRule (AUTOSAR_CP_TPS_SystemTemplate Table 6.222, p.572).

The writer emits the IP-SEC-RULE element per the XSD group IP-SEC-RULE
sequenceOffset order; empty reference lists emit no wrapper elements.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecHeaderTypeEnum,
    IPsecIpProtocolEnum,
    IPsecModeEnum,
    IPsecPolicyEnum,
    IPSecRule,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "DIRECTION",
    "HEADER-TYPE",
    "IP-PROTOCOL",
    "LOCAL-CERTIFICATE-REFS",
    "LOCAL-ID",
    "LOCAL-PORT-RANGE-END",
    "LOCAL-PORT-RANGE-START",
    "MODE",
    "POLICY",
    "PRE-SHARED-KEY-REF",
    "PRIORITY",
    "REMOTE-CERTIFICATE-REFS",
    "REMOTE-ID",
    "REMOTE-IP-ADDRESS-REFS",
    "REMOTE-PORT-RANGE-END",
    "REMOTE-PORT-RANGE-START",
]

BASE_GROUP_TAGS = {"SHORT-NAME", "LONG-NAME", "DESC", "CATEGORY", "INTRODUCTION", "ADMIN-DATA", "ANNOTATIONS", "VARIATION-POINT"}


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _enum(enum_cls, member):
    e = enum_cls()
    e.setValue(member)
    return e


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _full_rule() -> IPSecRule:
    rule = IPSecRule(AUTOSAR.getInstance(), "Rule1")
    rule.setDirection(_enum(CommunicationDirectionType, CommunicationDirectionType.IN))
    rule.setHeaderType(_enum(IPsecHeaderTypeEnum, IPsecHeaderTypeEnum.AH))
    rule.setIpProtocol(_enum(IPsecIpProtocolEnum, IPsecIpProtocolEnum.TCP))
    rule.addLocalCertificateRef(_ref("CRYPTO-SERVICE-CERTIFICATE", "/Crypto/Certs/Local1"))
    rule.addLocalCertificateRef(_ref("CRYPTO-SERVICE-CERTIFICATE", "/Crypto/Certs/Local2"))
    rule.setLocalId(_string("local-id"))
    rule.setLocalPortRangeEnd(_pos_int("8080"))
    rule.setLocalPortRangeStart(_pos_int("1024"))
    rule.setMode(_enum(IPsecModeEnum, IPsecModeEnum.TRANSPORT))
    rule.setPolicy(_enum(IPsecPolicyEnum, IPsecPolicyEnum.IPSEC))
    rule.setPreSharedKeyRef(_ref("CRYPTO-SERVICE-KEY", "/Crypto/Keys/Key1"))
    rule.setPriority(_pos_int("0"))
    rule.addRemoteCertificateRef(_ref("CRYPTO-SERVICE-CERTIFICATE", "/Crypto/Certs/Remote1"))
    rule.setRemoteId(_string("remote-id"))
    rule.addRemoteIpAddressRef(_ref("NETWORK-ENDPOINT", "/Cluster/NE1"))
    rule.addRemoteIpAddressRef(_ref("NETWORK-ENDPOINT", "/Cluster/NE2"))
    rule.setRemotePortRangeEnd(_pos_int("9090"))
    rule.setRemotePortRangeStart(_pos_int("2048"))
    return rule


class TestWriteIPSecRule:
    def _write(self, rule: IPSecRule) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIPSecRule(parent, rule)
        return parent.find("IP-SEC-RULE")

    def test_write_element_order(self):
        element = self._write(_full_rule())

        assert element is not None
        assert [child.tag for child in element if child.tag not in BASE_GROUP_TAGS] == XSD_ELEMENT_ORDER

    def test_write_empty_rule_emits_no_wrappers(self):
        rule = IPSecRule(AUTOSAR.getInstance(), "EmptyRule")
        element = self._write(rule)

        assert element is not None
        tags = [child.tag for child in element]
        assert "LOCAL-CERTIFICATE-REFS" not in tags
        assert "REMOTE-CERTIFICATE-REFS" not in tags
        assert "REMOTE-IP-ADDRESS-REFS" not in tags
        assert "DIRECTION" not in tags
        assert "PRE-SHARED-KEY-REF" not in tags

    def test_round_trip_field_values(self):
        element = self._write(_full_rule())
        xml = ET.tostring(element, encoding="unicode")

        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
        node = ARXMLParser().find(root, "IP-SEC-RULE")
        reparsed = IPSecRule(AUTOSAR.getInstance(), "Rule1")
        ARXMLParser().readIPSecRule(node, reparsed)

        assert reparsed.getDirection().getValue() == "in"
        assert reparsed.getHeaderType().getValue() == "ah"
        assert reparsed.getIpProtocol().getValue() == "tcp"
        assert [r.getValue() for r in reparsed.getLocalCertificateRefs()] == ["/Crypto/Certs/Local1", "/Crypto/Certs/Local2"]
        assert all(r.getDest() == "CRYPTO-SERVICE-CERTIFICATE" for r in reparsed.getLocalCertificateRefs())
        assert reparsed.getLocalId().getValue() == "local-id"
        assert reparsed.getLocalPortRangeEnd().getValue() == 8080
        assert reparsed.getLocalPortRangeStart().getValue() == 1024
        assert reparsed.getMode().getValue() == "transport"
        assert reparsed.getPolicy().getValue() == "ipsec"
        assert reparsed.getPreSharedKeyRef().getValue() == "/Crypto/Keys/Key1"
        assert reparsed.getPreSharedKeyRef().getDest() == "CRYPTO-SERVICE-KEY"
        assert reparsed.getPriority().getValue() == 0
        assert [r.getValue() for r in reparsed.getRemoteCertificateRefs()] == ["/Crypto/Certs/Remote1"]
        assert reparsed.getRemoteId().getValue() == "remote-id"
        assert [r.getValue() for r in reparsed.getRemoteIpAddressRefs()] == ["/Cluster/NE1", "/Cluster/NE2"]
        assert reparsed.getRemotePortRangeEnd().getValue() == 9090
        assert reparsed.getRemotePortRangeStart().getValue() == 2048
