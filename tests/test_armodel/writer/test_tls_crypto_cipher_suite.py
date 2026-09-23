"""Writer round-trip tests for TlsCryptoCipherSuite (AUTOSAR_CP_TPS_SystemTemplate, Table 6.212, p.562).

Written via the TlsCryptoServiceMapping TLS-CIPHER-SUITES wrapper; child order
per XSD group TLS-CRYPTO-CIPHER-SUITE: AUTHENTICATION-REF, CERTIFICATE-REF,
CIPHER-SUITE-ID, CIPHER-SUITE-SHORT-LABEL, ELLIPTIC-CURVE-REFS, ENCRYPTION-REF,
KEY-EXCHANGE-AUTHENTICATION-REFS, KEY-EXCHANGE-REFS, PRIORITY, PROPS,
PSK-IDENTITY, REMOTE-CERTIFICATE-REF, SIGNATURE-SCHEME-REFS, VERSION
(KEY-EXCHANGE-AUTHENTICATION-REFS precedes KEY-EXCHANGE-REFS per XSD, although
the markdown table displays keyExchange first).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    TlsCryptoCipherSuite,
    TlsCryptoCipherSuiteProps,
    TlsCryptoServiceMapping,
    TlsPskIdentity,
    TlsVersionEnum,
)
from armodel.writer.arxml_writer import ARXMLWriter

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


def _ref(dest, value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _new_mapping_with_suite():
    mapping = SystemMapping(_MockParent(), "Mapping")
    tls = TlsCryptoServiceMapping(mapping, "TlsMap")
    mapping.addCryptoServiceMapping(tls)

    suite = TlsCryptoCipherSuite(tls, "Suite1")
    tls.addTlsCipherSuite(suite)
    suite.setAuthenticationRef(_ref("CRYPTO-SERVICE-PRIMITIVE", "/Crypto/Primitives/Mac"))
    suite.setCertificateRef(_ref("CRYPTO-SERVICE-CERTIFICATE", "/Crypto/Certs/Local"))
    suite.setCipherSuiteId(_pos_int("4865"))
    suite.setCipherSuiteShortLabel(_string("TLS_AES_128_GCM_SHA256"))
    suite.addEllipticCurveRef(_ref("CRYPTO-ELLIPTIC-CURVE-PROPS", "/Crypto/Curves/C1"))
    suite.addEllipticCurveRef(_ref("CRYPTO-ELLIPTIC-CURVE-PROPS", "/Crypto/Curves/C2"))
    suite.setEncryptionRef(_ref("CRYPTO-SERVICE-PRIMITIVE", "/Crypto/Primitives/Enc"))
    suite.addKeyExchangeAuthenticationRef(_ref("CRYPTO-SERVICE-PRIMITIVE", "/Crypto/Primitives/Sig"))
    suite.addKeyExchangeRef(_ref("CRYPTO-SERVICE-PRIMITIVE", "/Crypto/Primitives/Ecdh"))
    suite.addKeyExchangeRef(_ref("CRYPTO-SERVICE-PRIMITIVE", "/Crypto/Primitives/Dh"))
    suite.setPriority(_pos_int("10"))
    props = TlsCryptoCipherSuiteProps(suite, "Props1")
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

    props.setTcpIpTlsUseSecurityExtensionForceEncryptThenMac(Boolean().setValue("true"))
    suite.setProps(props)
    psk = TlsPskIdentity()
    psk.setPreSharedKeyRef(_ref("CRYPTO-SERVICE-KEY", "/Crypto/Keys/Psk"))
    psk.setPskIdentity(_string("psk-id"))
    psk.setPskIdentityHint(_string("psk-hint"))
    suite.setPskIdentity(psk)
    suite.setRemoteCertificateRef(_ref("CRYPTO-SERVICE-CERTIFICATE", "/Crypto/Certs/Remote"))
    suite.addSignatureSchemeRef(_ref("CRYPTO-SIGNATURE-SCHEME", "/Crypto/Schemes/S1"))
    suite.setVersion(TlsVersionEnum().setValue(TlsVersionEnum.TLS_13))
    return mapping


def _write(mapping):
    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)
    return parent.find("SYSTEM-MAPPING")


def test_write_tls_crypto_cipher_suite_xml():
    mapping = _new_mapping_with_suite()
    node = _write(mapping)

    suite = node.find("CRYPTO-SERVICE-MAPPINGS/TLS-CRYPTO-SERVICE-MAPPING/TLS-CIPHER-SUITES/TLS-CRYPTO-CIPHER-SUITE")
    assert suite is not None
    assert suite.find("SHORT-NAME").text == "Suite1"
    assert suite.find("AUTHENTICATION-REF").text == "/Crypto/Primitives/Mac"
    assert suite.find("AUTHENTICATION-REF").attrib["DEST"] == "CRYPTO-SERVICE-PRIMITIVE"
    assert suite.find("CERTIFICATE-REF").text == "/Crypto/Certs/Local"
    assert suite.find("CIPHER-SUITE-ID").text == "4865"
    assert suite.find("CIPHER-SUITE-SHORT-LABEL").text == "TLS_AES_128_GCM_SHA256"
    refs = suite.findall("ELLIPTIC-CURVE-REFS/ELLIPTIC-CURVE-REF")
    assert [r.text for r in refs] == ["/Crypto/Curves/C1", "/Crypto/Curves/C2"]
    assert suite.find("ENCRYPTION-REF").text == "/Crypto/Primitives/Enc"
    assert suite.find("KEY-EXCHANGE-AUTHENTICATION-REFS/KEY-EXCHANGE-AUTHENTICATION-REF").text == "/Crypto/Primitives/Sig"
    refs = suite.findall("KEY-EXCHANGE-REFS/KEY-EXCHANGE-REF")
    assert [r.text for r in refs] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert suite.find("PRIORITY").text == "10"
    assert suite.find("PROPS/SHORT-NAME").text == "Props1"
    assert suite.find("PROPS/TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC").text == "true"
    assert suite.find("PSK-IDENTITY/PRE-SHARED-KEY-REF").text == "/Crypto/Keys/Psk"
    assert suite.find("PSK-IDENTITY/PSK-IDENTITY-HINT").text == "psk-hint"
    assert suite.find("REMOTE-CERTIFICATE-REF").text == "/Crypto/Certs/Remote"
    assert suite.find("SIGNATURE-SCHEME-REFS/SIGNATURE-SCHEME-REF").text == "/Crypto/Schemes/S1"
    assert suite.find("VERSION").text == "TLS-13"


def test_write_tls_crypto_cipher_suite_xsd_element_order():
    mapping = _new_mapping_with_suite()
    node = _write(mapping)

    suite = node.find("CRYPTO-SERVICE-MAPPINGS/TLS-CRYPTO-SERVICE-MAPPING/TLS-CIPHER-SUITES/TLS-CRYPTO-CIPHER-SUITE")
    children = [child.tag for child in suite]
    assert children == [
        "SHORT-NAME",
        "AUTHENTICATION-REF",
        "CERTIFICATE-REF",
        "CIPHER-SUITE-ID",
        "CIPHER-SUITE-SHORT-LABEL",
        "ELLIPTIC-CURVE-REFS",
        "ENCRYPTION-REF",
        "KEY-EXCHANGE-AUTHENTICATION-REFS",
        "KEY-EXCHANGE-REFS",
        "PRIORITY",
        "PROPS",
        "PSK-IDENTITY",
        "REMOTE-CERTIFICATE-REF",
        "SIGNATURE-SCHEME-REFS",
        "VERSION",
    ]
    # TLS-CIPHER-SUITES wrapper sits between KEY-EXCHANGE-REFS and the booleans of the mapping
    tls = node.find("CRYPTO-SERVICE-MAPPINGS/TLS-CRYPTO-SERVICE-MAPPING")
    assert [child.tag for child in tls] == ["SHORT-NAME", "TLS-CIPHER-SUITES"]


def test_write_empty_tls_crypto_cipher_suite_omits_optional_tags():
    mapping = SystemMapping(_MockParent(), "Mapping")
    tls = TlsCryptoServiceMapping(mapping, "TlsMap")
    mapping.addCryptoServiceMapping(tls)
    suite = TlsCryptoCipherSuite(tls, "EmptySuite")
    tls.addTlsCipherSuite(suite)

    node = _write(mapping)
    suite_elem = node.find("CRYPTO-SERVICE-MAPPINGS/TLS-CRYPTO-SERVICE-MAPPING/TLS-CIPHER-SUITES/TLS-CRYPTO-CIPHER-SUITE")
    assert suite_elem is not None
    assert [child.tag for child in suite_elem] == ["SHORT-NAME"]


def test_write_tls_crypto_cipher_suite_round_trip():
    from armodel.parser.arxml_parser import ARXMLParser

    mapping = _new_mapping_with_suite()
    node = _write(mapping)

    reparsed = ET.fromstring(ET.tostring(node).decode("utf-8").replace("<SYSTEM-MAPPING>", "<SYSTEM-MAPPING xmlns='%s'>" % NS, 1))
    remapping = SystemMapping(_MockParent(), "Mapping")
    ARXMLParser().readSystemMapping(reparsed, remapping)

    suite = remapping.getCryptoServiceMappings()[0].getTlsCipherSuites()[0]
    assert suite.getShortName() == "Suite1"
    assert suite.getAuthenticationRef().getValue() == "/Crypto/Primitives/Mac"
    assert suite.getCipherSuiteId().getValue() == 4865
    assert [r.getValue() for r in suite.getKeyExchangeRefs()] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert suite.getPriority().getValue() == 10
    assert suite.getPskIdentity().getPskIdentity().getValue() == "psk-id"
    assert suite.getVersion().getValue() == "TLS-13"
