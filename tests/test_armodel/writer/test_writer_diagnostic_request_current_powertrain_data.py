"""
Tests for writing DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA elements —
DiagnosticRequestCurrentPowertrainData, Table 4.130 (p.151, R23-11).

DiagnosticRequestCurrentPowertrainData (Base most-derived DiagnosticServiceInstance)
owns two 0..1 references — pid (PID-REF) and requestCurrentPowertrainDiagnosticDataClass
(REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA l.41698.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_current_powertrain_data.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestCurrentPowertrainData
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


def _make_full_mode01() -> DiagnosticRequestCurrentPowertrainData:
    package = AUTOSAR.getInstance().createARPackage("OBDMode01Services")
    mode01 = package.createDiagnosticRequestCurrentPowertrainData("Mode01")
    mode01.setPidRef(RefType().setDest("DIAGNOSTIC-PARAMETER-IDENTIFIER").setValue("/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"))
    mode01.setRequestCurrentPowertrainDiagnosticDataClassRef(
        RefType().setDest("DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS").setValue("/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1")
    )
    return mode01


class TestWriteDiagnosticRequestCurrentPowertrainData:
    """Tests for writeDiagnosticRequestCurrentPowertrainData — own element field values (Table 4.130)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestCurrentPowertrainData without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode01Services")
        package.createDiagnosticRequestCurrentPowertrainData("Mode01")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestCurrentPowertrainData(parent, package.getReferrableElement("Mode01", DiagnosticRequestCurrentPowertrainData))

        child = parent.find("DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode01"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode01 = _make_full_mode01()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestCurrentPowertrainData(parent, mode01)

        child = parent.find("DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA")
        assert [c.tag for c in child] == ["SHORT-NAME", "PID-REF", "REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF"]
        assert child.find("PID-REF").text == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert child.find("PID-REF").get("DEST") == "DIAGNOSTIC-PARAMETER-IDENTIFIER"
        assert child.find("REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1"
        assert child.find("REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode01 = _make_full_mode01()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestCurrentPowertrainData(parent, mode01)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestCurrentPowertrainData(AUTOSAR.getInstance(), "Mode01")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA")
        ARXMLParser().readDiagnosticRequestCurrentPowertrainData(element, reloaded)
        assert reloaded.getPidRef() is not None
        assert reloaded.getPidRef().getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert reloaded.getPidRef().getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"
        assert reloaded.getRequestCurrentPowertrainDiagnosticDataClassRef() is not None
        assert reloaded.getRequestCurrentPowertrainDiagnosticDataClassRef().getValue() == "/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1"
        assert reloaded.getRequestCurrentPowertrainDiagnosticDataClassRef().getDest() == "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"
