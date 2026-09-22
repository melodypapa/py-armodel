"""Parser tests for TlsPskIdentity (AUTOSAR_CP_TPS_SystemTemplate, Table 6.214, p.563).

Direct readTlsPskIdentity helper; XML element order per XSD group
TLS-PSK-IDENTITY: PRE-SHARED-KEY-REF, PSK-IDENTITY, PSK-IDENTITY-HINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import TlsPskIdentity
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _psk_fragment():
    return (
        "<TLS-PSK-IDENTITY xmlns='%s'>"
        '<PRE-SHARED-KEY-REF DEST="CRYPTO-SERVICE-KEY">/Crypto/Keys/Master</PRE-SHARED-KEY-REF>'
        "<PSK-IDENTITY>psk_id_1</PSK-IDENTITY>"
        "<PSK-IDENTITY-HINT>hint_1</PSK-IDENTITY-HINT>"
        "</TLS-PSK-IDENTITY>" % NS
    )


def test_parse_tls_psk_identity():
    psk = TlsPskIdentity()
    root = ET.fromstring(_psk_fragment())
    ARXMLParser().readTlsPskIdentity(root, psk)

    ref = psk.getPreSharedKeyRef()
    assert ref is not None
    assert ref.getValue() == "/Crypto/Keys/Master"
    assert ref.getDest() == "CRYPTO-SERVICE-KEY"
    assert psk.getPskIdentity().getValue() == "psk_id_1"
    assert psk.getPskIdentityHint().getValue() == "hint_1"


def test_parse_tls_psk_identity_empty_element():
    psk = TlsPskIdentity()
    root = ET.fromstring("<TLS-PSK-IDENTITY xmlns='%s'/>" % NS)
    ARXMLParser().readTlsPskIdentity(root, psk)

    assert psk.getPreSharedKeyRef() is None
    assert psk.getPskIdentity() is None
    assert psk.getPskIdentityHint() is None


def test_parse_tls_psk_identity_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    psk = TlsPskIdentity()
    root = ET.fromstring(_psk_fragment())
    ARXMLParser().readTlsPskIdentity(root, psk)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlsPskIdentity(parent, psk)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    psk2 = TlsPskIdentity()
    ARXMLParser().readTlsPskIdentity(reparsed[0], psk2)

    assert psk2.getPreSharedKeyRef().getValue() == "/Crypto/Keys/Master"
    assert psk2.getPreSharedKeyRef().getDest() == "CRYPTO-SERVICE-KEY"
    assert psk2.getPskIdentity().getValue() == "psk_id_1"
    assert psk2.getPskIdentityHint().getValue() == "hint_1"
