"""
Tests for writing DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING elements —
DiagnosticTroubleCodeUdsToTroubleCodeObdMapping, Table 4.180 (p.188, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_trouble_code_uds_to_trouble_code_obd_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCodeUdsToTroubleCodeObdMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
    """Tests for writeDiagnosticTroubleCodeUdsToTroubleCodeObdMapping — own element field values (Table 4.180)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticTroubleCodeUdsToTroubleCodeObdMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticTroubleCodeUdsToTroubleCodeObdMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCodeUdsToTroubleCodeObdMapping(parent, package.getReferrableElement("M1", DiagnosticTroubleCodeUdsToTroubleCodeObdMapping))

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticTroubleCodeUdsToTroubleCodeObdMapping("M1")
        mapping.setTroubleCodeObdRef(RefType().setValue("/AUTOSAR/TroubleCodeObd1"))
        mapping.setTroubleCodeUdsRef(RefType().setValue("/AUTOSAR/TroubleCodeUds1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCodeUdsToTroubleCodeObdMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "TROUBLE-CODE-OBD-REF", "TROUBLE-CODE-UDS-REF"]
        assert child.find("TROUBLE-CODE-OBD-REF").text == "/AUTOSAR/TroubleCodeObd1"
        assert child.find("TROUBLE-CODE-UDS-REF").text == "/AUTOSAR/TroubleCodeUds1"
