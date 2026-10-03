"""
Tests for writing DIAGNOSTIC-REQUEST-VEHICLE-INFO elements —
DiagnosticRequestVehicleInfo, Table 4.144 (p.160, R23-11).

DiagnosticRequestVehicleInfo (Base most-derived DiagnosticServiceInstance) owns
two 0..1 references — infoType (INFO-TYPE-REF) and requestVehicleInformationClass
(REQUEST-VEHICLE-INFORMATION-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-VEHICLE-INFO l.42539.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_vehicle_info.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestVehicleInfo
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_full_mode09() -> DiagnosticRequestVehicleInfo:
    package = AUTOSAR.getInstance().createARPackage("OBDMode09Services")
    mode09 = package.createDiagnosticRequestVehicleInfo("Mode09")
    mode09.setInfoTypeRef(RefType().setDest("DIAGNOSTIC-INFO-TYPE").setValue("/AUTOSAR/DiagnosticInfoTypes/InfoType1"))
    mode09.setRequestVehicleInformationClassRef(RefType().setDest("DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS").setValue("/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1"))
    return mode09


class TestWriteDiagnosticRequestVehicleInfo:
    """Tests for writeDiagnosticRequestVehicleInfo — own element field values (Table 4.144)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestVehicleInfo without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode09Services")
        package.createDiagnosticRequestVehicleInfo("Mode09")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestVehicleInfo(parent, package.getReferrableElement("Mode09", DiagnosticRequestVehicleInfo))

        child = parent.find("DIAGNOSTIC-REQUEST-VEHICLE-INFO")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode09"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode09 = _make_full_mode09()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestVehicleInfo(parent, mode09)

        child = parent.find("DIAGNOSTIC-REQUEST-VEHICLE-INFO")
        assert [c.tag for c in child] == ["SHORT-NAME", "INFO-TYPE-REF", "REQUEST-VEHICLE-INFORMATION-CLASS-REF"]
        assert child.find("INFO-TYPE-REF").text == "/AUTOSAR/DiagnosticInfoTypes/InfoType1"
        assert child.find("INFO-TYPE-REF").get("DEST") == "DIAGNOSTIC-INFO-TYPE"
        assert child.find("REQUEST-VEHICLE-INFORMATION-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1"
        assert child.find("REQUEST-VEHICLE-INFORMATION-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode09 = _make_full_mode09()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestVehicleInfo(parent, mode09)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestVehicleInfo(AUTOSAR.getInstance(), "Mode09")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-VEHICLE-INFO")
        ARXMLParser().readDiagnosticRequestVehicleInfo(element, reloaded)
        assert reloaded.getInfoTypeRef() is not None
        assert reloaded.getInfoTypeRef().getValue() == "/AUTOSAR/DiagnosticInfoTypes/InfoType1"
        assert reloaded.getInfoTypeRef().getDest() == "DIAGNOSTIC-INFO-TYPE"
        assert reloaded.getRequestVehicleInformationClassRef() is not None
        assert reloaded.getRequestVehicleInformationClassRef().getValue() == "/AUTOSAR/DiagnosticRequestVehicleInfoClasses/Class1"
        assert reloaded.getRequestVehicleInformationClassRef().getDest() == "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS"
