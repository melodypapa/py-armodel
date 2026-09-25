"""Parser tests for TlsCryptoCipherSuite (AUTOSAR_CP_TPS_SystemTemplate, Table 6.212, p.562).

Read through the TlsCryptoServiceMapping TLS-CIPHER-SUITES wrapper; XML element
order per XSD group TLS-CRYPTO-CIPHER-SUITE: AUTHENTICATION-REF, CERTIFICATE-REF,
CIPHER-SUITE-ID, CIPHER-SUITE-SHORT-LABEL, ELLIPTIC-CURVE-REFS, ENCRYPTION-REF,
KEY-EXCHANGE-AUTHENTICATION-REFS, KEY-EXCHANGE-REFS, PRIORITY, PROPS,
PSK-IDENTITY, REMOTE-CERTIFICATE-REF, SIGNATURE-SCHEME-REFS, VERSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    TlsCryptoCipherSuite,
    TlsCryptoServiceMapping,
    TlsVersionEnum,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _cipher_suite_fragment():
    return (
        "<SYSTEM-MAPPING xmlns='%s'>"
        "<SHORT-NAME>Mapping</SHORT-NAME>"
        "<CRYPTO-SERVICE-MAPPINGS>"
        "<TLS-CRYPTO-SERVICE-MAPPING>"
        "<SHORT-NAME>TlsMap</SHORT-NAME>"
        "<TLS-CIPHER-SUITES>"
        "<TLS-CRYPTO-CIPHER-SUITE>"
        "<SHORT-NAME>Suite1</SHORT-NAME>"
        '<AUTHENTICATION-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Mac</AUTHENTICATION-REF>'
        '<CERTIFICATE-REF DEST="CRYPTO-SERVICE-CERTIFICATE">/Crypto/Certs/Local</CERTIFICATE-REF>'
        "<CIPHER-SUITE-ID>4865</CIPHER-SUITE-ID>"
        "<CIPHER-SUITE-SHORT-LABEL>TLS_AES_128_GCM_SHA256</CIPHER-SUITE-SHORT-LABEL>"
        "<ELLIPTIC-CURVE-REFS>"
        '<ELLIPTIC-CURVE-REF DEST="CRYPTO-ELLIPTIC-CURVE-PROPS">/Crypto/Curves/C1</ELLIPTIC-CURVE-REF>'
        '<ELLIPTIC-CURVE-REF DEST="CRYPTO-ELLIPTIC-CURVE-PROPS">/Crypto/Curves/C2</ELLIPTIC-CURVE-REF>'
        "</ELLIPTIC-CURVE-REFS>"
        '<ENCRYPTION-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Enc</ENCRYPTION-REF>'
        "<KEY-EXCHANGE-AUTHENTICATION-REFS>"
        '<KEY-EXCHANGE-AUTHENTICATION-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Sig</KEY-EXCHANGE-AUTHENTICATION-REF>'
        "</KEY-EXCHANGE-AUTHENTICATION-REFS>"
        "<KEY-EXCHANGE-REFS>"
        '<KEY-EXCHANGE-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Ecdh</KEY-EXCHANGE-REF>'
        '<KEY-EXCHANGE-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Dh</KEY-EXCHANGE-REF>'
        "</KEY-EXCHANGE-REFS>"
        "<PRIORITY>10</PRIORITY>"
        "<PROPS>"
        "<SHORT-NAME>Props1</SHORT-NAME>"
        "<TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC>true</TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC>"
        "</PROPS>"
        "<PSK-IDENTITY>"
        '<PRE-SHARED-KEY-REF DEST="CRYPTO-SERVICE-KEY">/Crypto/Keys/Psk</PRE-SHARED-KEY-REF>'
        "<PSK-IDENTITY>psk-id</PSK-IDENTITY>"
        "<PSK-IDENTITY-HINT>psk-hint</PSK-IDENTITY-HINT>"
        "</PSK-IDENTITY>"
        '<REMOTE-CERTIFICATE-REF DEST="CRYPTO-SERVICE-CERTIFICATE">/Crypto/Certs/Remote</REMOTE-CERTIFICATE-REF>'
        "<SIGNATURE-SCHEME-REFS>"
        '<SIGNATURE-SCHEME-REF DEST="CRYPTO-SIGNATURE-SCHEME">/Crypto/Schemes/S1</SIGNATURE-SCHEME-REF>'
        "</SIGNATURE-SCHEME-REFS>"
        "<VERSION>TLS-13</VERSION>"
        "</TLS-CRYPTO-CIPHER-SUITE>"
        "</TLS-CIPHER-SUITES>"
        "</TLS-CRYPTO-SERVICE-MAPPING>"
        "</CRYPTO-SERVICE-MAPPINGS>"
        "</SYSTEM-MAPPING>" % NS
    )


def _parse_mapping(fragment):
    mapping = SystemMapping(_MockParent(), "Mapping")
    root = ET.fromstring(fragment)
    ARXMLParser().readSystemMapping(root, mapping)
    return mapping


def _first_cipher_suite(mapping):
    tls = mapping.getCryptoServiceMappings()[0]
    assert isinstance(tls, TlsCryptoServiceMapping)
    suites = tls.getTlsCipherSuites()
    assert len(suites) == 1
    suite = suites[0]
    assert isinstance(suite, TlsCryptoCipherSuite)
    return suite


def test_parse_tls_crypto_cipher_suite_dispatch():
    suite = _first_cipher_suite(_parse_mapping(_cipher_suite_fragment()))
    assert suite.getShortName() == "Suite1"
    assert suite.getAuthenticationRef().getValue() == "/Crypto/Primitives/Mac"
    assert suite.getAuthenticationRef().getDest() == "CRYPTO-SERVICE-PRIMITIVE"
    assert suite.getCertificateRef().getValue() == "/Crypto/Certs/Local"
    assert suite.getCipherSuiteId().getValue() == 4865
    assert suite.getCipherSuiteShortLabel().getValue() == "TLS_AES_128_GCM_SHA256"
    assert [r.getValue() for r in suite.getEllipticCurveRefs()] == ["/Crypto/Curves/C1", "/Crypto/Curves/C2"]
    assert suite.getEncryptionRef().getValue() == "/Crypto/Primitives/Enc"
    assert [r.getValue() for r in suite.getKeyExchangeAuthenticationRefs()] == ["/Crypto/Primitives/Sig"]
    assert [r.getValue() for r in suite.getKeyExchangeRefs()] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert suite.getPriority().getValue() == 10
    assert suite.getProps() is not None
    assert suite.getProps().getShortName() == "Props1"
    assert suite.getProps().getTcpIpTlsUseSecurityExtensionForceEncryptThenMac().getValue() is True
    assert suite.getPskIdentity() is not None
    assert suite.getPskIdentity().getPreSharedKeyRef().getValue() == "/Crypto/Keys/Psk"
    assert suite.getPskIdentity().getPskIdentity().getValue() == "psk-id"
    assert suite.getPskIdentity().getPskIdentityHint().getValue() == "psk-hint"
    assert suite.getRemoteCertificateRef().getValue() == "/Crypto/Certs/Remote"
    assert [r.getValue() for r in suite.getSignatureSchemeRefs()] == ["/Crypto/Schemes/S1"]
    assert isinstance(suite.getVersion(), TlsVersionEnum)
    assert suite.getVersion().getValue() == "TLS-13"


def test_parse_tls_crypto_cipher_suite_empty_wrapper():
    fragment = (
        "<SYSTEM-MAPPING xmlns='%s'>"
        "<SHORT-NAME>Mapping</SHORT-NAME>"
        "<CRYPTO-SERVICE-MAPPINGS>"
        "<TLS-CRYPTO-SERVICE-MAPPING>"
        "<SHORT-NAME>TlsMap</SHORT-NAME>"
        "<TLS-CIPHER-SUITES />"
        "</TLS-CRYPTO-SERVICE-MAPPING>"
        "</CRYPTO-SERVICE-MAPPINGS>"
        "</SYSTEM-MAPPING>" % NS
    )
    tls = _parse_mapping(fragment).getCryptoServiceMappings()[0]
    assert tls.getTlsCipherSuites() == []


def test_parse_tls_crypto_cipher_suite_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    mapping = _parse_mapping(_cipher_suite_fragment())

    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    remapping = SystemMapping(_MockParent(), "Mapping")
    ARXMLParser().readSystemMapping(reparsed[0], remapping)

    suite = _first_cipher_suite(remapping)
    assert suite.getShortName() == "Suite1"
    assert suite.getAuthenticationRef().getValue() == "/Crypto/Primitives/Mac"
    assert suite.getCipherSuiteId().getValue() == 4865
    assert [r.getValue() for r in suite.getKeyExchangeRefs()] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert suite.getPriority().getValue() == 10
    assert suite.getProps().getTcpIpTlsUseSecurityExtensionForceEncryptThenMac().getValue() is True
    assert suite.getPskIdentity().getPskIdentityHint().getValue() == "psk-hint"
    assert suite.getVersion().getValue() == "TLS-13"
