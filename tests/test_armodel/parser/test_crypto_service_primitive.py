"""Parser tests for CryptoServicePrimitive (AUTOSAR_CP_TPS_SystemTemplate, Table 6.50, p.376).

Top-level ARElement aggregated by ARPackage.element — dispatched through the
readARPackageElements ELEMENTS loop (XSD element CRYPTO-SERVICE-PRIMITIVE,
AUTOSAR_00052.xsd line 5031).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServicePrimitive
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _fragment():
    return (
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>CryptoPrimitives</SHORT-NAME>"
        "<ELEMENTS>"
        "<CRYPTO-SERVICE-PRIMITIVE>"
        "<SHORT-NAME>Primitive</SHORT-NAME>"
        "<ALGORITHM-FAMILY>AES</ALGORITHM-FAMILY>"
        "<ALGORITHM-MODE>CMAC</ALGORITHM-MODE>"
        "<ALGORITHM-SECONDARY-FAMILY>SHA2</ALGORITHM-SECONDARY-FAMILY>"
        "</CRYPTO-SERVICE-PRIMITIVE>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )


class TestCryptoServicePrimitiveParser:
    def test_dispatch_creates_crypto_service_primitive_on_package(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoPrimitives")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        created = pkg.getElement("Primitive", CryptoServicePrimitive)
        assert created is not None
        assert isinstance(created, CryptoServicePrimitive)
        assert created.getShortName() == "Primitive"

    def test_parse_asserts_field_values(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoPrimitives")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        primitive = pkg.getElement("Primitive", CryptoServicePrimitive)
        assert primitive.getAlgorithmFamily().getValue() == "AES"
        assert primitive.getAlgorithmMode().getValue() == "CMAC"
        assert primitive.getAlgorithmSecondaryFamily().getValue() == "SHA2"

    def test_parse_optional_attributes_absent(self):
        xml = (
            "<AR-PACKAGE xmlns='%s'>"
            "<SHORT-NAME>CryptoPrimitives</SHORT-NAME>"
            "<ELEMENTS>"
            "<CRYPTO-SERVICE-PRIMITIVE><SHORT-NAME>Empty</SHORT-NAME></CRYPTO-SERVICE-PRIMITIVE>"
            "</ELEMENTS>"
            "</AR-PACKAGE>" % NS
        )
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoPrimitives")
        ARXMLParser().readARPackageElements(ET.fromstring(xml), pkg)

        primitive = pkg.getElement("Empty", CryptoServicePrimitive)
        assert primitive.getAlgorithmFamily() is None
        assert primitive.getAlgorithmMode() is None
        assert primitive.getAlgorithmSecondaryFamily() is None

    def test_parse_write_reparse_round_trip(self):
        from armodel.writer.arxml_writer import ARXMLWriter

        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoPrimitives")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        writer_parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(writer_parent, pkg)
        reparsed = ET.fromstring(ET.tostring(writer_parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoPrimitives")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        primitive = reloaded.getElement("Primitive", CryptoServicePrimitive)
        assert primitive is not None
        assert primitive.getAlgorithmFamily().getValue() == "AES"
        assert primitive.getAlgorithmMode().getValue() == "CMAC"
        assert primitive.getAlgorithmSecondaryFamily().getValue() == "SHA2"
