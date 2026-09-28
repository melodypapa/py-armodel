"""Parser tests for UserDefinedPdu (AUTOSAR_CP_TPS_SystemTemplate, Table 6.27, p.345).

Top-level ARElement aggregated by ARPackage.element — dispatched through the
readARPackageElements ELEMENTS loop (XSD element USER-DEFINED-PDU,
AUTOSAR_00052.xsd line 128940); the own group USER-DEFINED-PDU adds only
CDD-TYPE (String, 0..1) after the PDU group; no VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import UserDefinedPdu
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _fragment(with_cdd_type=True):
    cdd_type = "<CDD-TYPE>ComplexDriverCdd</CDD-TYPE>" if with_cdd_type else ""
    return (
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>Pdus</SHORT-NAME>"
        "<ELEMENTS>"
        "<USER-DEFINED-PDU>"
        "<SHORT-NAME>UDPdu</SHORT-NAME>"
        "<LENGTH>8</LENGTH>"
        "%s"
        "</USER-DEFINED-PDU>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % (NS, cdd_type)
    )


class TestUserDefinedPduParser:
    def test_dispatch_creates_user_defined_pdu_on_package(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="Pdus")
        ARXMLParser().readARPackageElements(ET.fromstring(_fragment()), pkg)

        created = pkg.getElement("UDPdu", UserDefinedPdu)
        assert created is not None
        assert isinstance(created, UserDefinedPdu)
        assert created.getShortName() == "UDPdu"

    def test_parse_asserts_field_values(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="Pdus")
        ARXMLParser().readARPackageElements(ET.fromstring(_fragment()), pkg)

        pdu = pkg.getElement("UDPdu", UserDefinedPdu)
        assert pdu.getLength().getValue() == 8
        assert pdu.getCddType().getValue() == "ComplexDriverCdd"

    def test_parse_optional_cdd_type_absent(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="Pdus")
        ARXMLParser().readARPackageElements(ET.fromstring(_fragment(with_cdd_type=False)), pkg)

        pdu = pkg.getElement("UDPdu", UserDefinedPdu)
        assert pdu.getCddType() is None
        assert pdu.getLength().getValue() == 8

    def test_parse_write_reparse_round_trip(self):
        from armodel.writer.arxml_writer import ARXMLWriter

        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="Pdus")
        ARXMLParser().readARPackageElements(ET.fromstring(_fragment()), pkg)

        writer_parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(writer_parent, pkg)
        reparsed = ET.fromstring(ET.tostring(writer_parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="Pdus")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        pdu = reloaded.getElement("UDPdu", UserDefinedPdu)
        assert pdu is not None
        assert pdu.getLength().getValue() == 8
        assert pdu.getCddType().getValue() == "ComplexDriverCdd"
