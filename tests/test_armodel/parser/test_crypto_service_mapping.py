"""Parser tests for CryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.48, p.375).

Abstract class with zero attribute rows — exercised through its concrete
subclass SecOcCryptoServiceMapping (Table 6.49) inside the SystemMapping
CRYPTO-SERVICE-MAPPINGS wrapper (XSD choice SEC-OC-/TLS-CRYPTO-SERVICE-MAPPING).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceMapping, SecOcCryptoServiceMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _sec_oc_fragment():
    return (
        "<SYSTEM-MAPPING xmlns='%s'>"
        "<SHORT-NAME>Mapping</SHORT-NAME>"
        "<CRYPTO-SERVICE-MAPPINGS>"
        "<SEC-OC-CRYPTO-SERVICE-MAPPING>"
        "<SHORT-NAME>SecOcMap</SHORT-NAME>"
        '<AUTHENTICATION-REF DEST="CRYPTO-SERVICE-PRIMITIVE">/Crypto/Primitives/Auth</AUTHENTICATION-REF>'
        '<CRYPTO-SERVICE-KEY-REF DEST="CRYPTO-SERVICE-KEY">/Crypto/Keys/Key1</CRYPTO-SERVICE-KEY-REF>'
        '<CRYPTO-SERVICE-QUEUE-REF DEST="CRYPTO-SERVICE-QUEUE">/Crypto/Queues/Q1</CRYPTO-SERVICE-QUEUE-REF>'
        "</SEC-OC-CRYPTO-SERVICE-MAPPING>"
        "</CRYPTO-SERVICE-MAPPINGS>"
        "</SYSTEM-MAPPING>" % NS
    )


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def test_parse_sec_oc_crypto_service_mapping_dispatch():
    mapping = SystemMapping(_MockParent(), "Mapping")
    root = ET.fromstring(_sec_oc_fragment())
    ARXMLParser().readSystemMapping(root, mapping)

    mappings = mapping.getCryptoServiceMappings()
    assert len(mappings) == 1
    sec_oc = mappings[0]
    assert isinstance(sec_oc, SecOcCryptoServiceMapping)
    assert isinstance(sec_oc, CryptoServiceMapping)
    assert sec_oc.getShortName() == "SecOcMap"
    assert sec_oc.getAuthenticationRef().getValue() == "/Crypto/Primitives/Auth"
    assert sec_oc.getAuthenticationRef().getDest() == "CRYPTO-SERVICE-PRIMITIVE"
    assert sec_oc.getCryptoServiceKeyRef().getValue() == "/Crypto/Keys/Key1"
    assert sec_oc.getCryptoServiceQueueRef().getValue() == "/Crypto/Queues/Q1"


def test_parse_crypto_service_mapping_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    mapping = SystemMapping(_MockParent(), "Mapping")
    root = ET.fromstring(_sec_oc_fragment())
    ARXMLParser().readSystemMapping(root, mapping)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    remapping = SystemMapping(_MockParent(), "Mapping")
    ARXMLParser().readSystemMapping(reparsed[0], remapping)

    mappings = remapping.getCryptoServiceMappings()
    assert len(mappings) == 1
    sec_oc = mappings[0]
    assert isinstance(sec_oc, SecOcCryptoServiceMapping)
    assert sec_oc.getAuthenticationRef().getValue() == "/Crypto/Primitives/Auth"
    assert sec_oc.getCryptoServiceKeyRef().getValue() == "/Crypto/Keys/Key1"
    assert sec_oc.getCryptoServiceQueueRef().getValue() == "/Crypto/Queues/Q1"
