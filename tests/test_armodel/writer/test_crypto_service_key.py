"""Writer round-trip tests for CryptoServiceKey (Table 6.51, p.377).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order ALGORITHM-FAMILY, DEVELOPMENT-VALUE, KEY-GENERATION,
KEY-STORAGE-TYPE, LENGTH (CRYPTO-SERVICE-KEY group, AUTOSAR_00052.xsd l.26314).
DEVELOPMENT-VALUE is a polymorphic ValueSpecification choice serialized through
the shared setChildValueSpecification dispatcher.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, CryptoServiceKey
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CryptoServiceKeyGenerationEnum,
    DateTime,
    PositiveInteger,
    String,
    VerbatimString,
)
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "ALGORITHM-FAMILY",
    "DEVELOPMENT-VALUE",
    "KEY-GENERATION",
    "KEY-STORAGE-TYPE",
    "LENGTH",
]

UUID_VALUE = "7a1b2c3d-4e5f-4a6b-8c9d-0e1f2a3b4c5d"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _populate(key: CryptoServiceKey):
    key.setAlgorithmFamily(_string("AES"))
    key.setDevelopmentValue(TextValueSpecification().setValue(VerbatimString().setValue("0xAFFE")))
    key.setKeyGeneration(CryptoServiceKeyGenerationEnum().setValue(CryptoServiceKeyGenerationEnum.KEY_DERIVATION))
    key.setKeyStorageType(_string("LOCAL"))
    length = PositiveInteger()
    length.setValue("256")
    key.setLength(length)


def _write_ar_package_element(key: CryptoServiceKey) -> ET.Element:
    parent = ET.Element("ELEMENTS")
    ARXMLWriter().writeARPackageElement(parent, key)
    return parent


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))


class TestCryptoServiceKeyWriter:
    def test_write_dispatch_creates_correct_tag(self):
        key = AUTOSAR.getInstance().createARPackage("CryptoKeys").createCryptoServiceKey("Key1")
        parent = _write_ar_package_element(key)

        assert len(parent) == 1
        child = parent.find("CRYPTO-SERVICE-KEY")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Key1"

    def test_write_field_values_and_xsd_element_order(self):
        key = AUTOSAR.getInstance().createARPackage("CryptoKeys").createCryptoServiceKey("Key1")
        _populate(key)

        child = _write_ar_package_element(key).find("CRYPTO-SERVICE-KEY")
        assert child.find("ALGORITHM-FAMILY").text == "AES"
        assert child.find("DEVELOPMENT-VALUE/TEXT-VALUE-SPECIFICATION/VALUE").text == "0xAFFE"
        assert child.find("KEY-GENERATION").text == "KEY-DERIVATION"
        assert child.find("KEY-STORAGE-TYPE").text == "LOCAL"
        assert child.find("LENGTH").text == "256"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME"] + XSD_CHILD_ORDER

    def test_write_empty_omits_optional_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoKeys")
        pkg.createCryptoServiceKey("Empty")
        child = _write_ar_package_element(pkg.getReferrableElement("Empty", CryptoServiceKey)).find("CRYPTO-SERVICE-KEY")

        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None, tag

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoKeys")
        first = pkg.createCryptoServiceKey("Key1")
        second = pkg.createCryptoServiceKey("Key1")
        assert first is second
        assert isinstance(first, CryptoServiceKey)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoKeys")
        key = pkg.createCryptoServiceKey("Key1")
        _populate(key)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reparsed = _with_ns(parent)
        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoKeys")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        re_key = reloaded.getReferrableElement("Key1", CryptoServiceKey)
        assert re_key is not None
        assert isinstance(re_key, CryptoServiceKey)
        assert re_key.getAlgorithmFamily().getValue() == "AES"
        assert re_key.getDevelopmentValue().getValue().getValue() == "0xAFFE"
        assert re_key.getKeyGeneration().getValue() == CryptoServiceKeyGenerationEnum.KEY_DERIVATION
        assert re_key.getKeyStorageType().getValue() == "LOCAL"
        assert re_key.getLength().getValue() == 256

    def test_round_trip_base_level_attributes(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoKeys")
        key = pkg.createCryptoServiceKey("Key1")
        key.setUuid(String().setValue(UUID_VALUE))
        key.setChecksum(String().setValue("7"))
        key.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
        key.setCategory("CRYPTO")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)
        node = _with_ns(parent).find("{%s}ELEMENTS" % NS).find("{%s}CRYPTO-SERVICE-KEY" % NS)
        assert node.attrib["UUID"] == UUID_VALUE
        assert node.attrib["S"] == "7"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"
        assert node.find("{%s}CATEGORY" % NS).text == "CRYPTO"

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoKeys")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)
        re_key = reloaded.getReferrableElement("Key1", CryptoServiceKey)
        assert re_key.getUuid().getValue() == UUID_VALUE
        assert re_key.getChecksum().getValue() == "7"
        assert re_key.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert re_key.getCategory().getValue() == "CRYPTO"

    def test_round_trip_empty(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoKeys")
        pkg.createCryptoServiceKey("Key1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoKeys")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)

        re_key = reloaded.getReferrableElement("Key1", CryptoServiceKey)
        assert re_key is not None
        assert re_key.getAlgorithmFamily() is None
        assert re_key.getDevelopmentValue() is None
        assert re_key.getKeyGeneration() is None
        assert re_key.getKeyStorageType() is None
        assert re_key.getLength() is None
