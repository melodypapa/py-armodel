"""Parser tests for CryptoKeySlot (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.5, p.58).

The aggregating parent CryptoProvider is not yet modeled, so the reader helper
is exercised directly on a CRYPTO-KEY-SLOT fragment; XML element order per XSD
group CRYPTO-KEY-SLOT (AUTOSAR_00052.xsd): ALLOCATE-SHADOW-COPY, CRYPTO-ALG-ID,
CRYPTO-OBJECT-TYPE, KEY-SLOT-ALLOWED-MODIFICATION,
KEY-SLOT-CONTENT-ALLOWED-USAGES, SLOT-CAPACITY, SLOT-TYPE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment import (
    CryptoKeySlot,
    CryptoKeySlotAllowedModification,
    CryptoKeySlotContentAllowedUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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


def _key_slot_fragment():
    return (
        "<CRYPTO-KEY-SLOT xmlns='%s'>"
        "<SHORT-NAME>KeySlot1</SHORT-NAME>"
        "<ALLOCATE-SHADOW-COPY>true</ALLOCATE-SHADOW-COPY>"
        "<CRYPTO-ALG-ID>AES-128</CRYPTO-ALG-ID>"
        "<CRYPTO-OBJECT-TYPE>SYMMETRIC-KEY</CRYPTO-OBJECT-TYPE>"
        "<KEY-SLOT-ALLOWED-MODIFICATION>"
        "<ALLOW-CONTENT-TYPE-CHANGE>false</ALLOW-CONTENT-TYPE-CHANGE>"
        "<EXPORTABILITY>true</EXPORTABILITY>"
        "<MAX-NUMBER-OF-ALLOWED-UPDATES>10</MAX-NUMBER-OF-ALLOWED-UPDATES>"
        "<RESTRICT-UPDATE>true</RESTRICT-UPDATE>"
        "</KEY-SLOT-ALLOWED-MODIFICATION>"
        "<KEY-SLOT-CONTENT-ALLOWED-USAGES>"
        "<CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE><ALLOWED-KEYSLOT-USAGE>ENCRYPT</ALLOWED-KEYSLOT-USAGE></CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE>"
        "<CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE><ALLOWED-KEYSLOT-USAGE>DECRYPT</ALLOWED-KEYSLOT-USAGE></CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE>"
        "</KEY-SLOT-CONTENT-ALLOWED-USAGES>"
        "<SLOT-CAPACITY>256</SLOT-CAPACITY>"
        "<SLOT-TYPE>APPLICATION</SLOT-TYPE>"
        "</CRYPTO-KEY-SLOT>" % NS
    )


def test_parse_crypto_key_slot():
    slot = CryptoKeySlot(_MockParent(), "KeySlot1")
    root = ET.fromstring(_key_slot_fragment())
    ARXMLParser().readCryptoKeySlot(root, slot)

    assert slot.getShortName() == "KeySlot1"
    assert slot.getAllocateShadowCopy().getValue() is True
    assert slot.getCryptoAlgId().getValue() == "AES-128"
    assert slot.getCryptoObjectType().getValue() == "SYMMETRIC-KEY"
    modification = slot.getKeySlotAllowedModification()
    assert isinstance(modification, CryptoKeySlotAllowedModification)
    assert modification.getAllowContentTypeChange().getValue() is False
    assert modification.getExportability().getValue() is True
    assert modification.getMaxNumberOfAllowedUpdates().getValue() == 10
    assert modification.getRestrictUpdate().getValue() is True
    usages = slot.getKeySlotContentAllowedUsages()
    assert len(usages) == 2
    assert all(isinstance(usage, CryptoKeySlotContentAllowedUsage) for usage in usages)
    assert [u.getAllowedKeyslotUsage().getValue() for u in usages] == ["ENCRYPT", "DECRYPT"]
    assert slot.getSlotCapacity().getValue() == 256
    assert slot.getSlotType().getValue() == "APPLICATION"


def test_parse_crypto_key_slot_round_trip():
    from armodel.writer.arxml_writer import ARXMLWriter

    slot = CryptoKeySlot(_MockParent(), "KeySlot1")
    root = ET.fromstring(_key_slot_fragment())
    ARXMLParser().readCryptoKeySlot(root, slot)

    parent = ET.Element("ROOT")
    ARXMLWriter().writeCryptoKeySlot(parent, slot)
    reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))
    reloaded = CryptoKeySlot(_MockParent(), "KeySlot1")
    ARXMLParser().readCryptoKeySlot(reparsed[0], reloaded)

    assert reloaded.getAllocateShadowCopy().getValue() is True
    assert reloaded.getCryptoAlgId().getValue() == "AES-128"
    assert reloaded.getCryptoObjectType().getValue() == "SYMMETRIC-KEY"
    assert reloaded.getKeySlotAllowedModification().getMaxNumberOfAllowedUpdates().getValue() == 10
    assert [u.getAllowedKeyslotUsage().getValue() for u in reloaded.getKeySlotContentAllowedUsages()] == ["ENCRYPT", "DECRYPT"]
    assert reloaded.getSlotCapacity().getValue() == 256
    assert reloaded.getSlotType().getValue() == "APPLICATION"


def test_parse_crypto_key_slot_empty():
    slot = CryptoKeySlot(_MockParent(), "EmptySlot")
    root = ET.fromstring("<CRYPTO-KEY-SLOT xmlns='%s'><SHORT-NAME>EmptySlot</SHORT-NAME></CRYPTO-KEY-SLOT>" % NS)
    ARXMLParser().readCryptoKeySlot(root, slot)

    assert slot.getAllocateShadowCopy() is None
    assert slot.getCryptoAlgId() is None
    assert slot.getCryptoObjectType() is None
    assert slot.getKeySlotAllowedModification() is None
    assert slot.getKeySlotContentAllowedUsages() == []
    assert slot.getSlotCapacity() is None
    assert slot.getSlotType() is None
