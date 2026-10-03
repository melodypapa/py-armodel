"""
Tests for writing DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS elements —
DiagnosticWriteMemoryByAddressClass, Table 4.114 (p.141, R23-11).

DiagnosticWriteMemoryByAddressClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS, AUTOSAR_00052.xsd
l.47307, is an empty sequence. Only the IDENTIFIABLE wrapper is written. The
dispatch entry is writeARPackageElementRest → writeDiagnosticWriteMemoryByAddressClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_write_memory_by_address_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticWriteMemoryByAddressClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticWriteMemoryByAddressClass:
    """Tests for writeDiagnosticWriteMemoryByAddressClass — own element field values (Table 4.114)."""

    def _write(self, write_memory_by_address_class: DiagnosticWriteMemoryByAddressClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticWriteMemoryByAddressClass(parent, write_memory_by_address_class)
        return parent.find("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticWriteMemoryByAddressClass emits only the IDENTIFIABLE wrapper content (no own attributes)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressClasses")
        package.createDiagnosticWriteMemoryByAddressClass("Wmba1")

        child = self._write(package.getReferrableElement("Wmba1", DiagnosticWriteMemoryByAddressClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Wmba1"
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == []

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElementRest dispatches DiagnosticWriteMemoryByAddressClass to a DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressClasses")
        package.createDiagnosticWriteMemoryByAddressClass("Wmba1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Wmba1", DiagnosticWriteMemoryByAddressClass))

        child = parent.find("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Wmba1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticWriteMemoryByAddressClasses")
        package.createDiagnosticWriteMemoryByAddressClass("Wmba1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            write_memory_by_address_class_2 = package_2.getReferrableElement("Wmba1", DiagnosticWriteMemoryByAddressClass)
            assert write_memory_by_address_class_2 is not None
            assert write_memory_by_address_class_2.getShortName() == "Wmba1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
