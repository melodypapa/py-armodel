"""Writer round-trip tests for CryptoEllipticCurveProps (AUTOSAR_CP_TPS_SystemTemplate, Table 6.216, p.564).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order: SHORT-NAME, NAMED-CURVE-ID (group CRYPTO-ELLIPTIC-CURVE-PROPS).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoEllipticCurveProps
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


def _new_props():
    pkg = AUTOSAR.getInstance().createARPackage("CryptoEllipticCurveProps")
    props = pkg.createCryptoEllipticCurveProps("Curve")
    props.setNamedCurveId(_pos_int("23"))
    return props


class TestCryptoEllipticCurvePropsWriter:
    def test_write_dispatch_creates_correct_tag(self):
        props = _new_props()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, props)

        assert len(parent) == 1
        child = parent.find("CRYPTO-ELLIPTIC-CURVE-PROPS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Curve"

    def test_write_field_values_and_xsd_element_order(self):
        props = _new_props()
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, props)

        child = parent.find("CRYPTO-ELLIPTIC-CURVE-PROPS")
        assert child.find("NAMED-CURVE-ID").text == "23"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME", "NAMED-CURVE-ID"]

    def test_write_empty_omits_optional_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoEllipticCurveProps")
        pkg.createCryptoEllipticCurveProps("Empty")
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeARPackageElement(parent, pkg.getElement("Empty", CryptoEllipticCurveProps))

        child = parent.find("CRYPTO-ELLIPTIC-CURVE-PROPS")
        assert child is not None
        assert child.find("NAMED-CURVE-ID") is None

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoEllipticCurveProps")
        first = pkg.createCryptoEllipticCurveProps("Curve")
        second = pkg.createCryptoEllipticCurveProps("Curve")
        assert first is second
        assert isinstance(first, CryptoEllipticCurveProps)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoEllipticCurveProps")
        props = pkg.createCryptoEllipticCurveProps("Curve")
        props.setNamedCurveId(_pos_int("23"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))
        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoEllipticCurveProps")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        re_props = reloaded.getElement("Curve", CryptoEllipticCurveProps)
        assert re_props is not None
        assert isinstance(re_props, CryptoEllipticCurveProps)
        assert re_props.getNamedCurveId().getValue() == 23
