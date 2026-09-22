"""Writer round-trip tests for CryptoSignatureScheme (AUTOSAR_CP_TPS_SystemTemplate, Table 6.217, p.564).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order: SHORT-NAME, SIGNATURE-SCHEME-ID (group CRYPTO-SIGNATURE-SCHEME).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoSignatureScheme
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


def _new_scheme():
    pkg = AUTOSAR.getInstance().createARPackage("CryptoSignatureScheme")
    scheme = pkg.createCryptoSignatureScheme("SigScheme")
    scheme.setSignatureSchemeId(_pos_int("7"))
    return scheme


class TestCryptoSignatureSchemeWriter:
    def test_write_dispatch_creates_correct_tag(self):
        scheme = _new_scheme()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, scheme)

        assert len(parent) == 1
        child = parent.find("CRYPTO-SIGNATURE-SCHEME")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SigScheme"

    def test_write_field_values_and_xsd_element_order(self):
        scheme = _new_scheme()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, scheme)

        child = parent.find("CRYPTO-SIGNATURE-SCHEME")
        assert child.find("SIGNATURE-SCHEME-ID").text == "7"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME", "SIGNATURE-SCHEME-ID"]

    def test_write_empty_omits_optional_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoSignatureScheme")
        pkg.createCryptoSignatureScheme("Empty")
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, pkg.getElement("Empty", CryptoSignatureScheme))

        child = parent.find("CRYPTO-SIGNATURE-SCHEME")
        assert child is not None
        assert child.find("SIGNATURE-SCHEME-ID") is None

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoSignatureScheme")
        first = pkg.createCryptoSignatureScheme("SigScheme")
        second = pkg.createCryptoSignatureScheme("SigScheme")
        assert first is second
        assert isinstance(first, CryptoSignatureScheme)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoSignatureScheme")
        scheme = pkg.createCryptoSignatureScheme("SigScheme")
        scheme.setSignatureSchemeId(_pos_int("7"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))
        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoSignatureScheme")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        re_scheme = reloaded.getElement("SigScheme", CryptoSignatureScheme)
        assert re_scheme is not None
        assert isinstance(re_scheme, CryptoSignatureScheme)
        assert re_scheme.getSignatureSchemeId().getValue() == 7
