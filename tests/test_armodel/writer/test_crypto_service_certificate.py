"""Writer round-trip tests for CryptoServiceCertificate (AUTOSAR_CP_TPS_SystemTemplate, Table 6.218, p.565).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order: SHORT-NAME, ALGORITHM-FAMILY, FORMAT, MAXIMUM-LENGTH,
NEXT-HIGHER-CERTIFICATE-REF, SERVER-NAME-IDENTIFICATION (group CRYPTO-SERVICE-CERTIFICATE).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoCertificateAlgorithmFamilyEnum, CryptoCertificateFormatEnum, CryptoServiceCertificate
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _pos_int(value):
    v = PositiveInteger()
    v.setValue(value)
    return v


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    ref.setDest("CRYPTO-SERVICE-CERTIFICATE")
    return ref


def _new_certificate():
    pkg = AUTOSAR.getInstance().createARPackage("CryptoServiceCertificate")
    certificate = pkg.createCryptoServiceCertificate("Cert")
    certificate.setAlgorithmFamily(CryptoCertificateAlgorithmFamilyEnum().setValue(CryptoCertificateAlgorithmFamilyEnum.RSA))
    certificate.setFormat(CryptoCertificateFormatEnum().setValue(CryptoCertificateFormatEnum.X_509))
    certificate.setMaximumLength(_pos_int("4096"))
    certificate.setNextHigherCertificateRef(_ref("/Pkg/Higher"))
    certificate.setServerNameIdentification(_string("example.com"))
    return certificate


def _string(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

    s = String()
    s.setValue(value)
    return s


class TestCryptoServiceCertificateWriter:
    def test_write_dispatch_creates_correct_tag(self):
        certificate = _new_certificate()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, certificate)

        assert len(parent) == 1
        child = parent.find("CRYPTO-SERVICE-CERTIFICATE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Cert"

    def test_write_field_values_and_xsd_element_order(self):
        certificate = _new_certificate()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, certificate)

        child = parent.find("CRYPTO-SERVICE-CERTIFICATE")
        assert child.find("ALGORITHM-FAMILY").text == "RSA"
        assert child.find("FORMAT").text == "X-509"
        assert child.find("MAXIMUM-LENGTH").text == "4096"
        ref_element = child.find("NEXT-HIGHER-CERTIFICATE-REF")
        assert ref_element.text == "/Pkg/Higher"
        assert ref_element.attrib["DEST"] == "CRYPTO-SERVICE-CERTIFICATE"
        assert child.find("SERVER-NAME-IDENTIFICATION").text == "example.com"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME", "ALGORITHM-FAMILY", "FORMAT", "MAXIMUM-LENGTH", "NEXT-HIGHER-CERTIFICATE-REF", "SERVER-NAME-IDENTIFICATION"]

    def test_write_empty_omits_optional_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoServiceCertificate")
        pkg.createCryptoServiceCertificate("Empty")
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, pkg.getElement("Empty", CryptoServiceCertificate))

        child = parent.find("CRYPTO-SERVICE-CERTIFICATE")
        assert child is not None
        assert child.find("ALGORITHM-FAMILY") is None
        assert child.find("FORMAT") is None
        assert child.find("MAXIMUM-LENGTH") is None
        assert child.find("NEXT-HIGHER-CERTIFICATE-REF") is None
        assert child.find("SERVER-NAME-IDENTIFICATION") is None

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoServiceCertificate")
        first = pkg.createCryptoServiceCertificate("Cert")
        second = pkg.createCryptoServiceCertificate("Cert")
        assert first is second
        assert isinstance(first, CryptoServiceCertificate)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoServiceCertificate")
        certificate = pkg.createCryptoServiceCertificate("Cert")
        certificate.setAlgorithmFamily(CryptoCertificateAlgorithmFamilyEnum().setValue(CryptoCertificateAlgorithmFamilyEnum.RSA))
        certificate.setFormat(CryptoCertificateFormatEnum().setValue(CryptoCertificateFormatEnum.X_509))
        certificate.setMaximumLength(_pos_int("4096"))
        certificate.setNextHigherCertificateRef(_ref("/Pkg/Higher"))
        certificate.setServerNameIdentification(_string("example.com"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))
        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoServiceCertificate")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        re_certificate = reloaded.getElement("Cert", CryptoServiceCertificate)
        assert re_certificate is not None
        assert isinstance(re_certificate, CryptoServiceCertificate)
        assert re_certificate.getAlgorithmFamily().getValue() == "RSA"
        assert re_certificate.getFormat().getValue() == "X-509"
        assert re_certificate.getMaximumLength().getValue() == 4096
        assert re_certificate.getNextHigherCertificateRef().getValue() == "/Pkg/Higher"
        assert re_certificate.getServerNameIdentification().getValue() == "example.com"
