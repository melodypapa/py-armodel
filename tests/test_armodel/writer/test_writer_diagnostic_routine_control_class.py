"""
Tests for writing DIAGNOSTIC-ROUTINE-CONTROL-CLASS elements —
DiagnosticRoutineControlClass, Table 4.90 (p.126, R23-11).

DiagnosticRoutineControlClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — AUTOSAR_00052.xsd group
DIAGNOSTIC-ROUTINE-CONTROL-CLASS l.42973 is an empty sequence. The writer
therefore only emits the DIAGNOSTIC-ROUTINE-CONTROL-CLASS element with its
IDENTIFIABLE wrapper content. The dispatch entry is writeARPackageElement →
writeDiagnosticRoutineControlClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_routine_control_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRoutineControlClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRoutineControlClass:
    """Tests for writeDiagnosticRoutineControlClass — own element field values (Table 4.90)."""

    def _write(self, routine_control_class: DiagnosticRoutineControlClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRoutineControlClass(parent, routine_control_class)
        return parent.find("DIAGNOSTIC-ROUTINE-CONTROL-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticRoutineControlClass emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        package.createDiagnosticRoutineControlClass("Rcc1")

        child = self._write(package.getElement("Rcc1", DiagnosticRoutineControlClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rcc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticRoutineControlClass to a DIAGNOSTIC-ROUTINE-CONTROL-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        package.createDiagnosticRoutineControlClass("Rcc1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Rcc1", DiagnosticRoutineControlClass))

        child = parent.find("DIAGNOSTIC-ROUTINE-CONTROL-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rcc1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving identity."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticRoutineControls")
        package.createDiagnosticRoutineControlClass("Rcc1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            routine_control_class_2 = package_2.getElement("Rcc1", DiagnosticRoutineControlClass)
            assert routine_control_class_2 is not None
            assert routine_control_class_2.getShortName() == "Rcc1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
