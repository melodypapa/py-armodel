"""Parser tests for CryptoServiceCertificate (AUTOSAR_CP_TPS_SystemTemplate, Table 6.218, p.565).

Top-level ARElement aggregated by ARPackage.element — dispatched through the
readARPackageElements ELEMENTS loop (XSD element CRYPTO-SERVICE-CERTIFICATE,
AUTOSAR_00052.xsd line 5029).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceCertificate
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
        "<SHORT-NAME>CryptoServiceCertificate</SHORT-NAME>"
        "<ELEMENTS>"
        "<CRYPTO-SERVICE-CERTIFICATE>"
        "<SHORT-NAME>Cert</SHORT-NAME>"
        "<ALGORITHM-FAMILY>RSA</ALGORITHM-FAMILY>"
        "<FORMAT>X-509</FORMAT>"
        "<MAXIMUM-LENGTH>4096</MAXIMUM-LENGTH>"
        "<NEXT-HIGHER-CERTIFICATE-REF DEST='CRYPTO-SERVICE-CERTIFICATE'>/Pkg/Higher</NEXT-HIGHER-CERTIFICATE-REF>"
        "<SERVER-NAME-IDENTIFICATION>example.com</SERVER-NAME-IDENTIFICATION>"
        "</CRYPTO-SERVICE-CERTIFICATE>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )


class TestCryptoServiceCertificateParser:
    def test_dispatch_creates_crypto_service_certificate_on_package(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoServiceCertificate")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        created = pkg.getElement("Cert", CryptoServiceCertificate)
        assert created is not None
        assert isinstance(created, CryptoServiceCertificate)
        assert created.getShortName() == "Cert"

    def test_parse_asserts_field_values(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoServiceCertificate")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        certificate = pkg.getElement("Cert", CryptoServiceCertificate)
        assert certificate.getAlgorithmFamily().getValue() == "RSA"
        assert certificate.getFormat().getValue() == "X-509"
        assert certificate.getMaximumLength().getValue() == 4096
        ref = certificate.getNextHigherCertificateRef()
        assert ref.getValue() == "/Pkg/Higher"
        assert ref.getDest() == "CRYPTO-SERVICE-CERTIFICATE"
        assert certificate.getServerNameIdentification().getValue() == "example.com"

    def test_parse_optional_attributes_absent(self):
        xml = (
            "<AR-PACKAGE xmlns='%s'>"
            "<SHORT-NAME>CryptoServiceCertificate</SHORT-NAME>"
            "<ELEMENTS>"
            "<CRYPTO-SERVICE-CERTIFICATE><SHORT-NAME>Empty</SHORT-NAME></CRYPTO-SERVICE-CERTIFICATE>"
            "</ELEMENTS>"
            "</AR-PACKAGE>" % NS
        )
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoServiceCertificate")
        ARXMLParser().readARPackageElements(ET.fromstring(xml), pkg)

        certificate = pkg.getElement("Empty", CryptoServiceCertificate)
        assert certificate.getAlgorithmFamily() is None
        assert certificate.getFormat() is None
        assert certificate.getMaximumLength() is None
        assert certificate.getNextHigherCertificateRef() is None
        assert certificate.getServerNameIdentification() is None

    def test_parse_write_reparse_round_trip(self):
        from armodel.writer.arxml_writer import ARXMLWriter

        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoServiceCertificate")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        writer_parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(writer_parent, pkg)
        reparsed = ET.fromstring(ET.tostring(writer_parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoServiceCertificate")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        certificate = reloaded.getElement("Cert", CryptoServiceCertificate)
        assert certificate is not None
        assert certificate.getAlgorithmFamily().getValue() == "RSA"
        assert certificate.getFormat().getValue() == "X-509"
        assert certificate.getMaximumLength().getValue() == 4096
        assert certificate.getNextHigherCertificateRef().getValue() == "/Pkg/Higher"
        assert certificate.getServerNameIdentification().getValue() == "example.com"
