"""
Tests for writing DIAGNOSTIC-IO-CONTROL-CLASS elements —
DiagnosticIoControlClass, Table 4.81 (p.118, R23-11).

DiagnosticIoControlClass (Base most-derived DiagnosticServiceClass, concrete)
defines no own attributes — AUTOSAR_00052.xsd group DIAGNOSTIC-IO-CONTROL-CLASS
l.38515 is an empty sequence. The writer therefore only emits the
DIAGNOSTIC-IO-CONTROL-CLASS element with its IDENTIFIABLE wrapper content.
The dispatch entry is writeARPackageElement → writeDiagnosticIoControlClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_io_control_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticIoControlClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticIoControlClass:
    """Tests for writeDiagnosticIoControlClass — own element field values (Table 4.81)."""

    def _write(self, io_control_class: DiagnosticIoControlClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIoControlClass(parent, io_control_class)
        return parent.find("DIAGNOSTIC-IO-CONTROL-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticIoControlClass emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControlClasses")
        package.createDiagnosticIoControlClass("Icc1")

        child = self._write(package.getElement("Icc1", DiagnosticIoControlClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Icc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticIoControlClass to a DIAGNOSTIC-IO-CONTROL-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIoControlClasses")
        package.createDiagnosticIoControlClass("Icc1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Icc1", DiagnosticIoControlClass))

        child = parent.find("DIAGNOSTIC-IO-CONTROL-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Icc1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving identity."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIoControlClasses")
        package.createDiagnosticIoControlClass("Icc1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            io_control_class_2 = package_2.getElement("Icc1", DiagnosticIoControlClass)
            assert io_control_class_2 is not None
            assert io_control_class_2.getShortName() == "Icc1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
