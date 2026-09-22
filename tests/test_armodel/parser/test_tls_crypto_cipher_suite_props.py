"""Parser tests for TlsCryptoCipherSuiteProps (AUTOSAR_CP_TPS_SystemTemplate, Table 6.215, p.563).

Direct readTlsCryptoCipherSuiteProps helper; XML element order per XSD group
TLS-CRYPTO-CIPHER-SUITE-PROPS: TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import TlsCryptoCipherSuiteProps
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


def _props_fragment():
    return (
        "<TLS-CRYPTO-CIPHER-SUITE-PROPS xmlns='%s'>"
        "<SHORT-NAME>Props</SHORT-NAME>"
        "<TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC>true</TCP-IP-TLS-USE-SECURITY-EXTENSION-FORCE-ENCRYPT-THEN-MAC>"
        "</TLS-CRYPTO-CIPHER-SUITE-PROPS>" % NS
    )


def test_parse_tls_crypto_cipher_suite_props():
    props = TlsCryptoCipherSuiteProps(_MockParent(), "Props")
    root = ET.fromstring(_props_fragment())
    ARXMLParser().readTlsCryptoCipherSuiteProps(root, props)

    assert props.getShortName() == "Props"
    flag = props.getTcpIpTlsUseSecurityExtensionForceEncryptThenMac()
    assert flag is not None
    assert flag.getValue() is True


def test_parse_tls_crypto_cipher_suite_props_empty_element():
    props = TlsCryptoCipherSuiteProps(_MockParent(), "Props")
    root = ET.fromstring("<TLS-CRYPTO-CIPHER-SUITE-PROPS xmlns='%s'/>" % NS)
    ARXMLParser().readTlsCryptoCipherSuiteProps(root, props)

    assert props.getTcpIpTlsUseSecurityExtensionForceEncryptThenMac() is None


def test_parse_tls_crypto_cipher_suite_props_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    props = TlsCryptoCipherSuiteProps(_MockParent(), "Props")
    root = ET.fromstring(_props_fragment())
    ARXMLParser().readTlsCryptoCipherSuiteProps(root, props)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeTlsCryptoCipherSuiteProps(parent, props)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    props2 = TlsCryptoCipherSuiteProps(_MockParent(), "Props")
    ARXMLParser().readTlsCryptoCipherSuiteProps(reparsed[0], props2)

    assert props2.getShortName() == "Props"
    assert props2.getTcpIpTlsUseSecurityExtensionForceEncryptThenMac().getValue() is True
