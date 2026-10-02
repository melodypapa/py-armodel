"""
Tests for writing DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS elements —
DiagnosticClearDiagnosticInformationClass, Table 4.109 (p.137, R23-11).

DiagnosticClearDiagnosticInformationClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11
table's attribute row is `-` and XSD group
DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS, AUTOSAR_00052.xsd l.32396, is
an empty sequence. Only the IDENTIFIABLE wrapper is written. The dispatch
entry is writeARPackageElement → writeDiagnosticClearDiagnosticInformationClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_clear_diagnostic_information_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticClearDiagnosticInformationClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticClearDiagnosticInformationClass:
    """Tests for writeDiagnosticClearDiagnosticInformationClass — own element field values (Table 4.109)."""

    def _write(self, clear_diagnostic_information_class: DiagnosticClearDiagnosticInformationClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticClearDiagnosticInformationClass(parent, clear_diagnostic_information_class)
        return parent.find("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticClearDiagnosticInformationClass emits only the IDENTIFIABLE wrapper content (no own attributes)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticClearDiagnosticInformations")
        package.createDiagnosticClearDiagnosticInformationClass("Cdci1")

        child = self._write(package.getElement("Cdci1", DiagnosticClearDiagnosticInformationClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Cdci1"
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == []

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticClearDiagnosticInformationClass to a DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticClearDiagnosticInformations")
        package.createDiagnosticClearDiagnosticInformationClass("Cdci1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Cdci1", DiagnosticClearDiagnosticInformationClass))

        child = parent.find("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Cdci1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticClearDiagnosticInformations")
        package.createDiagnosticClearDiagnosticInformationClass("Cdci1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            clear_diagnostic_information_class_2 = package_2.getElement("Cdci1", DiagnosticClearDiagnosticInformationClass)
            assert clear_diagnostic_information_class_2 is not None
            assert clear_diagnostic_information_class_2.getShortName() == "Cdci1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
