"""Writer round-trip tests for CryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.48, p.375).

Abstract class with zero attribute rows — the CRYPTO-SERVICE-MAPPINGS wrapper
dispatch is verified through its concrete subclass SecOcCryptoServiceMapping
(Table 6.49); XSD wrapper position in SYSTEM-MAPPING group is after
COM-MANAGEMENT-MAPPINGS and before DATA-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import SecOcCryptoServiceMapping
from armodel.writer.arxml_writer import ARXMLWriter


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
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_mapping():
    mapping = SystemMapping(_MockParent(), "Mapping")
    sec_oc = SecOcCryptoServiceMapping(mapping, "SecOcMap")
    mapping.addCryptoServiceMapping(sec_oc)
    sec_oc.setAuthenticationRef(_ref("CRYPTO-SERVICE-PRIMITIVE", "/Crypto/Primitives/Auth"))
    sec_oc.setCryptoServiceKeyRef(_ref("CRYPTO-SERVICE-KEY", "/Crypto/Keys/Key1"))
    sec_oc.setCryptoServiceQueueRef(_ref("CRYPTO-SERVICE-QUEUE", "/Crypto/Queues/Q1"))
    return mapping


def test_write_crypto_service_mappings_wrapper():
    mapping = _new_mapping()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)

    node = parent.find("SYSTEM-MAPPING")
    wrapper = node.find("CRYPTO-SERVICE-MAPPINGS")
    assert wrapper is not None
    sec_oc = wrapper.find("SEC-OC-CRYPTO-SERVICE-MAPPING")
    assert sec_oc is not None
    assert sec_oc.find("SHORT-NAME").text == "SecOcMap"
    auth_ref = sec_oc.find("AUTHENTICATION-REF")
    assert auth_ref.text == "/Crypto/Primitives/Auth"
    assert auth_ref.attrib["DEST"] == "CRYPTO-SERVICE-PRIMITIVE"
    children = [child.tag for child in sec_oc]
    assert children == ["SHORT-NAME", "AUTHENTICATION-REF", "CRYPTO-SERVICE-KEY-REF", "CRYPTO-SERVICE-QUEUE-REF"]


def test_write_wrapper_position_between_com_management_and_data_mappings():
    mapping = _new_mapping()
    mapping.createComManagementMapping("ComMap")
    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)

    node = parent.find("SYSTEM-MAPPING")
    children = [child.tag for child in node]
    assert children.index("COM-MANAGEMENT-MAPPINGS") < children.index("CRYPTO-SERVICE-MAPPINGS")


def test_write_empty_crypto_service_mappings_omits_wrapper():
    mapping = SystemMapping(_MockParent(), "Mapping")
    parent = ET.Element("ROOT")
    ARXMLWriter().writeSystemMapping(parent, mapping)

    node = parent.find("SYSTEM-MAPPING")
    assert node.find("CRYPTO-SERVICE-MAPPINGS") is None
