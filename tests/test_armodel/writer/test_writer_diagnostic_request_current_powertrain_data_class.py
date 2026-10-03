"""
Tests for writing the DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS element —
DiagnosticRequestCurrentPowertrainDataClass, Table 4.131 (p.151, R23-11).

DiagnosticRequestCurrentPowertrainDataClass (Base most-derived
DiagnosticServiceClass) defines no own attributes; the writer emits the
IDENTIFIABLE wrapper only, and the dispatch entry is writeARPackageElementRest →
writeDiagnosticRequestCurrentPowertrainDataClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_current_powertrain_data_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestCurrentPowertrainDataClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRequestCurrentPowertrainDataClass:
    """Tests for writeDiagnosticRequestCurrentPowertrainDataClass — own element field values (Table 4.131)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode01Classes")
        package.createDiagnosticRequestCurrentPowertrainDataClass("Rcp1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestCurrentPowertrainDataClass(parent, package.getReferrableElement("Rcp1", DiagnosticRequestCurrentPowertrainDataClass))

        child = parent.find("DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rcp1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode01Classes")
        package.createDiagnosticRequestCurrentPowertrainDataClass("Rcp1")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Rcp1", DiagnosticRequestCurrentPowertrainDataClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest(
            "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"), reloaded_package
        )
        reloaded = reloaded_package.getReferrableElement("Rcp1", DiagnosticRequestCurrentPowertrainDataClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Rcp1"
