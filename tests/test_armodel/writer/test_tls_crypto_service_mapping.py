"""Writer round-trip tests for TlsCryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.211, p.560).

Written via the SystemMapping CRYPTO-SERVICE-MAPPINGS wrapper dispatch; child
order per XSD group TLS-CRYPTO-SERVICE-MAPPING: KEY-EXCHANGE-REFS,
TLS-CIPHER-SUITES, USE-CLIENT-AUTHENTICATION-REQUEST,
USE-SECURITY-EXTENSION-RECORD-SIZE-LIMIT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import TlsCryptoServiceMapping
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


def _ref(value):
    ref = RefType()
    ref.setDest("CRYPTO-SERVICE-PRIMITIVE")
    ref.setValue(value)
    return ref


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _new_mapping():
    mapping = SystemMapping(_MockParent(), "Mapping")
    tls = TlsCryptoServiceMapping(mapping, "TlsMap")
    mapping.addCryptoServiceMapping(tls)
    tls.addKeyExchangeRef(_ref("/Crypto/Primitives/Ecdh"))
    tls.addKeyExchangeRef(_ref("/Crypto/Primitives/Dh"))
    tls.setUseClientAuthenticationRequest(_bool("true"))
    tls.setUseSecurityExtensionRecordSizeLimit(_bool("false"))
    return mapping


def test_write_tls_crypto_service_mapping_xml():
    mapping = _new_mapping()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)

    node = parent.find("SYSTEM-MAPPING")
    tls = node.find("CRYPTO-SERVICE-MAPPINGS/TLS-CRYPTO-SERVICE-MAPPING")
    assert tls is not None
    assert tls.find("SHORT-NAME").text == "TlsMap"
    refs = tls.findall("KEY-EXCHANGE-REFS/KEY-EXCHANGE-REF")
    assert [r.text for r in refs] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert refs[0].attrib["DEST"] == "CRYPTO-SERVICE-PRIMITIVE"
    assert tls.find("USE-CLIENT-AUTHENTICATION-REQUEST").text == "true"
    assert tls.find("USE-SECURITY-EXTENSION-RECORD-SIZE-LIMIT").text == "false"
    children = [child.tag for child in tls]
    assert children == ["SHORT-NAME", "KEY-EXCHANGE-REFS", "USE-CLIENT-AUTHENTICATION-REQUEST", "USE-SECURITY-EXTENSION-RECORD-SIZE-LIMIT"]


def test_write_empty_tls_crypto_service_mapping_omits_optional_tags():
    mapping = SystemMapping(_MockParent(), "Mapping")
    tls = TlsCryptoServiceMapping(mapping, "EmptyTlsMap")
    mapping.addCryptoServiceMapping(tls)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)

    node = parent.find("SYSTEM-MAPPING")
    tls_elem = node.find("CRYPTO-SERVICE-MAPPINGS/TLS-CRYPTO-SERVICE-MAPPING")
    assert tls_elem is not None
    assert [child.tag for child in tls_elem] == ["SHORT-NAME"]
