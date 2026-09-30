"""Parser tests for IPSecRule (AUTOSAR_CP_TPS_SystemTemplate Table 6.222, p.572).

Element order per XSD group IP-SEC-RULE (00052.xsd L73890): DIRECTION,
HEADER-TYPE, (IKE-AUTHENTICATION-METHOD — atp.Status="removed", not modeled),
IP-PROTOCOL, LOCAL-CERTIFICATE-REFS, LOCAL-ID, LOCAL-PORT-RANGE-END,
LOCAL-PORT-RANGE-START, MODE, POLICY, PRE-SHARED-KEY-REF, PRIORITY,
REMOTE-CERTIFICATE-REFS, REMOTE-ID, REMOTE-IP-ADDRESS-REFS,
REMOTE-PORT-RANGE-END, REMOTE-PORT-RANGE-START.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecRule
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _parse(inner: str) -> IPSecRule:
    root = _snip(inner)
    node = ARXMLParser().find(root, "IP-SEC-RULE")
    rule = IPSecRule(AUTOSAR.getInstance(), "Rule1")
    ARXMLParser().readIPSecRule(node, rule)
    return rule


FULL_INNER = (
    "<IP-SEC-RULE>"
    "<DIRECTION>IN</DIRECTION>"
    "<HEADER-TYPE>AH</HEADER-TYPE>"
    "<IP-PROTOCOL>TCP</IP-PROTOCOL>"
    "<LOCAL-CERTIFICATE-REFS>"
    '<LOCAL-CERTIFICATE-REF DEST="CRYPTO-SERVICE-CERTIFICATE">/Crypto/Certs/Local1</LOCAL-CERTIFICATE-REF>'
    '<LOCAL-CERTIFICATE-REF DEST="CRYPTO-SERVICE-CERTIFICATE">/Crypto/Certs/Local2</LOCAL-CERTIFICATE-REF>'
    "</LOCAL-CERTIFICATE-REFS>"
    "<LOCAL-ID>local-id</LOCAL-ID>"
    "<LOCAL-PORT-RANGE-END>8080</LOCAL-PORT-RANGE-END>"
    "<LOCAL-PORT-RANGE-START>1024</LOCAL-PORT-RANGE-START>"
    "<MODE>TRANSPORT</MODE>"
    "<POLICY>IPSEC</POLICY>"
    '<PRE-SHARED-KEY-REF DEST="CRYPTO-SERVICE-KEY">/Crypto/Keys/Key1</PRE-SHARED-KEY-REF>'
    "<PRIORITY>0</PRIORITY>"
    "<REMOTE-CERTIFICATE-REFS>"
    '<REMOTE-CERTIFICATE-REF DEST="CRYPTO-SERVICE-CERTIFICATE">/Crypto/Certs/Remote1</REMOTE-CERTIFICATE-REF>'
    "</REMOTE-CERTIFICATE-REFS>"
    "<REMOTE-ID>remote-id</REMOTE-ID>"
    "<REMOTE-IP-ADDRESS-REFS>"
    '<REMOTE-IP-ADDRESS-REF DEST="NETWORK-ENDPOINT">/Cluster/NE1</REMOTE-IP-ADDRESS-REF>'
    '<REMOTE-IP-ADDRESS-REF DEST="NETWORK-ENDPOINT">/Cluster/NE2</REMOTE-IP-ADDRESS-REF>'
    "</REMOTE-IP-ADDRESS-REFS>"
    "<REMOTE-PORT-RANGE-END>9090</REMOTE-PORT-RANGE-END>"
    "<REMOTE-PORT-RANGE-START>2048</REMOTE-PORT-RANGE-START>"
    "</IP-SEC-RULE>"
)


class TestReadIPSecRule:
    def test_read_field_values(self):
        rule = _parse(FULL_INNER)

        assert rule.getDirection() is not None
        assert rule.getDirection().getValue() == "IN"
        assert rule.getHeaderType() is not None
        assert rule.getHeaderType().getValue() == "AH"
        assert rule.getIpProtocol() is not None
        assert rule.getIpProtocol().getValue() == "TCP"
        assert [r.getValue() for r in rule.getLocalCertificateRefs()] == ["/Crypto/Certs/Local1", "/Crypto/Certs/Local2"]
        assert all(r.getDest() == "CRYPTO-SERVICE-CERTIFICATE" for r in rule.getLocalCertificateRefs())
        assert rule.getLocalId() is not None
        assert rule.getLocalId().getValue() == "local-id"
        assert rule.getLocalPortRangeEnd().getValue() == 8080
        assert rule.getLocalPortRangeStart().getValue() == 1024
        assert rule.getMode() is not None
        assert rule.getMode().getValue() == "TRANSPORT"
        assert rule.getPolicy() is not None
        assert rule.getPolicy().getValue() == "IPSEC"
        assert rule.getPreSharedKeyRef() is not None
        assert rule.getPreSharedKeyRef().getValue() == "/Crypto/Keys/Key1"
        assert rule.getPreSharedKeyRef().getDest() == "CRYPTO-SERVICE-KEY"
        assert rule.getPriority().getValue() == 0
        assert [r.getValue() for r in rule.getRemoteCertificateRefs()] == ["/Crypto/Certs/Remote1"]
        assert rule.getRemoteId() is not None
        assert rule.getRemoteId().getValue() == "remote-id"
        assert [r.getValue() for r in rule.getRemoteIpAddressRefs()] == ["/Cluster/NE1", "/Cluster/NE2"]
        assert all(r.getDest() == "NETWORK-ENDPOINT" for r in rule.getRemoteIpAddressRefs())
        assert rule.getRemotePortRangeEnd().getValue() == 9090
        assert rule.getRemotePortRangeStart().getValue() == 2048

    def test_read_absent_elements_yields_none(self):
        rule = _parse("<IP-SEC-RULE/>")

        assert rule.getDirection() is None
        assert rule.getHeaderType() is None
        assert rule.getIpProtocol() is None
        assert rule.getLocalCertificateRefs() == []
        assert rule.getLocalId() is None
        assert rule.getLocalPortRangeEnd() is None
        assert rule.getLocalPortRangeStart() is None
        assert rule.getMode() is None
        assert rule.getPolicy() is None
        assert rule.getPreSharedKeyRef() is None
        assert rule.getPriority() is None
        assert rule.getRemoteCertificateRefs() == []
        assert rule.getRemoteId() is None
        assert rule.getRemoteIpAddressRefs() == []
        assert rule.getRemotePortRangeEnd() is None
        assert rule.getRemotePortRangeStart() is None

    def test_read_partial_element(self):
        rule = _parse("<IP-SEC-RULE><DIRECTION>OUT</DIRECTION><PRIORITY>3</PRIORITY></IP-SEC-RULE>")

        assert rule.getDirection().getValue() == "OUT"
        assert rule.getPriority().getValue() == 3
        assert rule.getHeaderType() is None
        assert rule.getLocalCertificateRefs() == []
        assert rule.getPreSharedKeyRef() is None
        assert rule.getRemoteIpAddressRefs() == []
