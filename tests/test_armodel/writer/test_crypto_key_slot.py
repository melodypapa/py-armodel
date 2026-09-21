"""Writer round-trip tests for CryptoKeySlot (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.5, p.58).

The aggregating parent CryptoProvider is not yet modeled, so the writer helper
is exercised directly; child order per XSD group CRYPTO-KEY-SLOT
(AUTOSAR_00052.xsd): ALLOCATE-SHADOW-COPY, CRYPTO-ALG-ID, CRYPTO-OBJECT-TYPE,
KEY-SLOT-ALLOWED-MODIFICATION, KEY-SLOT-CONTENT-ALLOWED-USAGES, SLOT-CAPACITY,
SLOT-TYPE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment import (
    CryptoKeySlot,
    CryptoKeySlotAllowedModification,
    CryptoKeySlotContentAllowedUsage,
    CryptoKeySlotTypeEnum,
    CryptoObjectTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, String
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


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _new_key_slot():
    slot = CryptoKeySlot(_MockParent(), "KeySlot1")
    slot.setAllocateShadowCopy(_bool("true"))
    slot.setCryptoAlgId(_string("AES-128"))
    object_type = CryptoObjectTypeEnum()
    object_type.setValue("SYMMETRIC-KEY")
    slot.setCryptoObjectType(object_type)
    modification = CryptoKeySlotAllowedModification()
    modification.setAllowContentTypeChange(_bool("false"))
    modification.setRestrictUpdate(_bool("true"))
    slot.setKeySlotAllowedModification(modification)
    usage = CryptoKeySlotContentAllowedUsage()
    usage.setAllowedKeyslotUsage(_string("ENCRYPT"))
    slot.addKeySlotContentAllowedUsage(usage)
    slot.setSlotCapacity(_pos_int("256"))
    slot_type = CryptoKeySlotTypeEnum()
    slot_type.setValue("APPLICATION")
    slot.setSlotType(slot_type)
    return slot


def test_write_crypto_key_slot_xml():
    slot = _new_key_slot()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeCryptoKeySlot(parent, slot)

    node = parent.find("CRYPTO-KEY-SLOT")
    assert node is not None
    assert node.find("SHORT-NAME").text == "KeySlot1"
    assert node.find("ALLOCATE-SHADOW-COPY").text == "true"
    assert node.find("CRYPTO-ALG-ID").text == "AES-128"
    assert node.find("CRYPTO-OBJECT-TYPE").text == "SYMMETRIC-KEY"
    modification = node.find("KEY-SLOT-ALLOWED-MODIFICATION")
    assert modification is not None
    assert modification.find("ALLOW-CONTENT-TYPE-CHANGE").text == "false"
    assert modification.find("RESTRICT-UPDATE").text == "true"
    usages = node.findall("KEY-SLOT-CONTENT-ALLOWED-USAGES/CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE")
    assert len(usages) == 1
    assert usages[0].find("ALLOWED-KEYSLOT-USAGE").text == "ENCRYPT"
    assert node.find("SLOT-CAPACITY").text == "256"
    assert node.find("SLOT-TYPE").text == "APPLICATION"
    children = [child.tag for child in node]
    assert children == [
        "SHORT-NAME",
        "ALLOCATE-SHADOW-COPY",
        "CRYPTO-ALG-ID",
        "CRYPTO-OBJECT-TYPE",
        "KEY-SLOT-ALLOWED-MODIFICATION",
        "KEY-SLOT-CONTENT-ALLOWED-USAGES",
        "SLOT-CAPACITY",
        "SLOT-TYPE",
    ]


def test_write_empty_crypto_key_slot_omits_optional_tags():
    slot = CryptoKeySlot(_MockParent(), "EmptySlot")
    parent = ET.Element("ROOT")
    ARXMLWriter().writeCryptoKeySlot(parent, slot)

    node = parent.find("CRYPTO-KEY-SLOT")
    assert node is not None
    assert [child.tag for child in node] == ["SHORT-NAME"]
