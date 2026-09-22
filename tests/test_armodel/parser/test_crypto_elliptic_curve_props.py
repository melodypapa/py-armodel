"""Parser tests for CryptoEllipticCurveProps (AUTOSAR_CP_TPS_SystemTemplate, Table 6.216, p.564).

Top-level ARElement aggregated by ARPackage.element — dispatched through the
readARPackageElements ELEMENTS loop (XSD element CRYPTO-ELLIPTIC-CURVE-PROPS,
AUTOSAR_00052.xsd line 5024).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoEllipticCurveProps
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
        "<SHORT-NAME>CryptoEllipticCurveProps</SHORT-NAME>"
        "<ELEMENTS>"
        "<CRYPTO-ELLIPTIC-CURVE-PROPS>"
        "<SHORT-NAME>Curve</SHORT-NAME>"
        "<NAMED-CURVE-ID>23</NAMED-CURVE-ID>"
        "</CRYPTO-ELLIPTIC-CURVE-PROPS>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )


class TestCryptoEllipticCurvePropsParser:
    def test_dispatch_creates_crypto_elliptic_curve_props_on_package(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoEllipticCurveProps")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        created = pkg.getElement("Curve", CryptoEllipticCurveProps)
        assert created is not None
        assert isinstance(created, CryptoEllipticCurveProps)
        assert created.getShortName() == "Curve"

    def test_parse_asserts_field_values(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoEllipticCurveProps")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        props = pkg.getElement("Curve", CryptoEllipticCurveProps)
        assert props.getNamedCurveId().getValue() == 23

    def test_parse_optional_attributes_absent(self):
        xml = (
            "<AR-PACKAGE xmlns='%s'>"
            "<SHORT-NAME>CryptoEllipticCurveProps</SHORT-NAME>"
            "<ELEMENTS>"
            "<CRYPTO-ELLIPTIC-CURVE-PROPS><SHORT-NAME>Empty</SHORT-NAME></CRYPTO-ELLIPTIC-CURVE-PROPS>"
            "</ELEMENTS>"
            "</AR-PACKAGE>" % NS
        )
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoEllipticCurveProps")
        ARXMLParser().readARPackageElements(ET.fromstring(xml), pkg)

        props = pkg.getElement("Empty", CryptoEllipticCurveProps)
        assert props.getNamedCurveId() is None

    def test_parse_write_reparse_round_trip(self):
        from armodel.writer.arxml_writer import ARXMLWriter

        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoEllipticCurveProps")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        writer_parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(writer_parent, pkg)
        reparsed = ET.fromstring(ET.tostring(writer_parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoEllipticCurveProps")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        props = reloaded.getElement("Curve", CryptoEllipticCurveProps)
        assert props is not None
        assert props.getNamedCurveId().getValue() == 23
