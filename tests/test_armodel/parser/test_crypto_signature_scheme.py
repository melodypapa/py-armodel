"""Parser tests for CryptoSignatureScheme (AUTOSAR_CP_TPS_SystemTemplate, Table 6.217, p.564).

Top-level ARElement aggregated by ARPackage.element — dispatched through the
readARPackageElements ELEMENTS loop (XSD element CRYPTO-SIGNATURE-SCHEME,
AUTOSAR_00052.xsd line 5033).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoSignatureScheme
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
        "<SHORT-NAME>CryptoSignatureScheme</SHORT-NAME>"
        "<ELEMENTS>"
        "<CRYPTO-SIGNATURE-SCHEME>"
        "<SHORT-NAME>SigScheme</SHORT-NAME>"
        "<SIGNATURE-SCHEME-ID>7</SIGNATURE-SCHEME-ID>"
        "</CRYPTO-SIGNATURE-SCHEME>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )


class TestCryptoSignatureSchemeParser:
    def test_dispatch_creates_crypto_signature_scheme_on_package(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoSignatureScheme")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        created = pkg.getElement("SigScheme", CryptoSignatureScheme)
        assert created is not None
        assert isinstance(created, CryptoSignatureScheme)
        assert created.getShortName() == "SigScheme"

    def test_parse_asserts_field_values(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoSignatureScheme")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        scheme = pkg.getElement("SigScheme", CryptoSignatureScheme)
        assert scheme.getSignatureSchemeId().getValue() == 7

    def test_parse_optional_attributes_absent(self):
        xml = (
            "<AR-PACKAGE xmlns='%s'>"
            "<SHORT-NAME>CryptoSignatureScheme</SHORT-NAME>"
            "<ELEMENTS>"
            "<CRYPTO-SIGNATURE-SCHEME><SHORT-NAME>Empty</SHORT-NAME></CRYPTO-SIGNATURE-SCHEME>"
            "</ELEMENTS>"
            "</AR-PACKAGE>" % NS
        )
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoSignatureScheme")
        ARXMLParser().readARPackageElements(ET.fromstring(xml), pkg)

        scheme = pkg.getElement("Empty", CryptoSignatureScheme)
        assert scheme.getSignatureSchemeId() is None

    def test_parse_write_reparse_round_trip(self):
        from armodel.writer.arxml_writer import ARXMLWriter

        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoSignatureScheme")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        writer_parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(writer_parent, pkg)
        reparsed = ET.fromstring(ET.tostring(writer_parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoSignatureScheme")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        scheme = reloaded.getElement("SigScheme", CryptoSignatureScheme)
        assert scheme is not None
        assert scheme.getSignatureSchemeId().getValue() == 7
