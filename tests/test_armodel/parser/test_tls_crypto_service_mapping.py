"""Parser tests for TlsCryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.211, p.560).

Read through the SystemMapping CRYPTO-SERVICE-MAPPINGS wrapper; XML element
order per XSD group TLS-CRYPTO-SERVICE-MAPPING: KEY-EXCHANGE-REFS,
TLS-CIPHER-SUITES, USE-CLIENT-AUTHENTICATION-REQUEST,
USE-SECURITY-EXTENSION-RECORD-SIZE-LIMIT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import TlsCryptoServiceMapping
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


def _tls_fragment():
    return (
        "<SYSTEM-MAPPING xmlns='%s'>"
        "<SHORT-NAME>Mapping</SHORT-NAME>"
        "<CRYPTO-SERVICE-MAPPINGS>"
        "<TLS-CRYPTO-SERVICE-MAPPING>"
        "<SHORT-NAME>TlsMap</SHORT-NAME>"
        "<KEY-EXCHANGE-REFS>"
        '<KEY-EXCHANGE-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Ecdh</KEY-EXCHANGE-REF>'
        '<KEY-EXCHANGE-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Dh</KEY-EXCHANGE-REF>'
        "</KEY-EXCHANGE-REFS>"
        "<USE-CLIENT-AUTHENTICATION-REQUEST>true</USE-CLIENT-AUTHENTICATION-REQUEST>"
        "<USE-SECURITY-EXTENSION-RECORD-SIZE-LIMIT>false</USE-SECURITY-EXTENSION-RECORD-SIZE-LIMIT>"
        "</TLS-CRYPTO-SERVICE-MAPPING>"
        "</CRYPTO-SERVICE-MAPPINGS>"
        "</SYSTEM-MAPPING>" % NS
    )


def test_parse_tls_crypto_service_mapping_dispatch():
    mapping = SystemMapping(_MockParent(), "Mapping")
    root = ET.fromstring(_tls_fragment())
    ARXMLParser().readSystemMapping(root, mapping)

    mappings = mapping.getCryptoServiceMappings()
    assert len(mappings) == 1
    tls = mappings[0]
    assert isinstance(tls, TlsCryptoServiceMapping)
    assert tls.getShortName() == "TlsMap"
    refs = tls.getKeyExchangeRefs()
    assert [r.getValue() for r in refs] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert refs[0].getDest() == "CRYPTO-SERVICE-PRIMITIVE"
    assert tls.getUseClientAuthenticationRequest().getValue() is True
    assert tls.getUseSecurityExtensionRecordSizeLimit().getValue() is False


def test_parse_tls_crypto_service_mapping_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    mapping = SystemMapping(_MockParent(), "Mapping")
    root = ET.fromstring(_tls_fragment())
    ARXMLParser().readSystemMapping(root, mapping)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    remapping = SystemMapping(_MockParent(), "Mapping")
    ARXMLParser().readSystemMapping(reparsed[0], remapping)

    tls = remapping.getCryptoServiceMappings()[0]
    assert isinstance(tls, TlsCryptoServiceMapping)
    assert [r.getValue() for r in tls.getKeyExchangeRefs()] == ["/Crypto/Primitives/Ecdh", "/Crypto/Primitives/Dh"]
    assert tls.getUseClientAuthenticationRequest().getValue() is True
    assert tls.getUseSecurityExtensionRecordSizeLimit().getValue() is False
