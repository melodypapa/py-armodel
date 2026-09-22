"""Writer round-trip tests for CryptoServicePrimitive (AUTOSAR_CP_TPS_SystemTemplate, Table 6.50, p.376).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order ALGORITHM-FAMILY, ALGORITHM-MODE, ALGORITHM-SECONDARY-FAMILY.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServicePrimitive
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _new_primitive():
    pkg = AUTOSAR.getInstance().createARPackage("CryptoPrimitives")
    primitive = pkg.createCryptoServicePrimitive("Primitive")
    primitive.setAlgorithmFamily(_string("AES"))
    primitive.setAlgorithmMode(_string("CMAC"))
    primitive.setAlgorithmSecondaryFamily(_string("SHA2"))
    return primitive


class TestCryptoServicePrimitiveWriter:
    def test_write_dispatch_creates_correct_tag(self):
        primitive = _new_primitive()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, primitive)

        assert len(parent) == 1
        child = parent.find("CRYPTO-SERVICE-PRIMITIVE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Primitive"

    def test_write_field_values_and_xsd_element_order(self):
        primitive = _new_primitive()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, primitive)

        child = parent.find("CRYPTO-SERVICE-PRIMITIVE")
        assert child.find("ALGORITHM-FAMILY").text == "AES"
        assert child.find("ALGORITHM-MODE").text == "CMAC"
        assert child.find("ALGORITHM-SECONDARY-FAMILY").text == "SHA2"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME", "ALGORITHM-FAMILY", "ALGORITHM-MODE", "ALGORITHM-SECONDARY-FAMILY"]

    def test_write_empty_omits_optional_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoPrimitives")
        pkg.createCryptoServicePrimitive("Empty")
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, pkg.getElement("Empty", CryptoServicePrimitive))

        child = parent.find("CRYPTO-SERVICE-PRIMITIVE")
        assert child is not None
        assert child.find("ALGORITHM-FAMILY") is None
        assert child.find("ALGORITHM-MODE") is None
        assert child.find("ALGORITHM-SECONDARY-FAMILY") is None

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoPrimitives")
        first = pkg.createCryptoServicePrimitive("Primitive")
        second = pkg.createCryptoServicePrimitive("Primitive")
        assert first is second
        assert isinstance(first, CryptoServicePrimitive)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoPrimitives")
        primitive = pkg.createCryptoServicePrimitive("Primitive")
        primitive.setAlgorithmFamily(_string("AES"))
        primitive.setAlgorithmMode(_string("CMAC"))
        primitive.setAlgorithmSecondaryFamily(_string("SHA2"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))
        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoPrimitives")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        re_primitive = reloaded.getElement("Primitive", CryptoServicePrimitive)
        assert re_primitive is not None
        assert isinstance(re_primitive, CryptoServicePrimitive)
        assert re_primitive.getAlgorithmFamily().getValue() == "AES"
        assert re_primitive.getAlgorithmMode().getValue() == "CMAC"
        assert re_primitive.getAlgorithmSecondaryFamily().getValue() == "SHA2"
