"""
Tests for writing DIAGNOSTIC-READ-DTC-INFORMATION-CLASS elements —
DiagnosticReadDTCInformationClass, Table 4.107 (p.136, R23-11).

DiagnosticReadDTCInformationClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-READ-DTC-INFORMATION-CLASS, AUTOSAR_00052.xsd
l.41397, is an empty sequence. Only the IDENTIFIABLE wrapper is written. The
dispatch entry is writeARPackageElement → writeDiagnosticReadDTCInformationClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_dtc_information_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDTCInformationClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticReadDTCInformationClass:
    """Tests for writeDiagnosticReadDTCInformationClass — own element field values (Table 4.107)."""

    def _write(self, read_dtc_information_class: DiagnosticReadDTCInformationClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadDTCInformationClass(parent, read_dtc_information_class)
        return parent.find("DIAGNOSTIC-READ-DTC-INFORMATION-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadDTCInformationClass emits only the IDENTIFIABLE wrapper content (no own attributes)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDtcInformations")
        package.createDiagnosticReadDTCInformationClass("Rdtci1")

        child = self._write(package.getElement("Rdtci1", DiagnosticReadDTCInformationClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdtci1"
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == []

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadDTCInformationClass to a DIAGNOSTIC-READ-DTC-INFORMATION-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDtcInformations")
        package.createDiagnosticReadDTCInformationClass("Rdtci1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Rdtci1", DiagnosticReadDTCInformationClass))

        child = parent.find("DIAGNOSTIC-READ-DTC-INFORMATION-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdtci1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadDtcInformations")
        package.createDiagnosticReadDTCInformationClass("Rdtci1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            read_dtc_information_class_2 = package_2.getElement("Rdtci1", DiagnosticReadDTCInformationClass)
            assert read_dtc_information_class_2 is not None
            assert read_dtc_information_class_2.getShortName() == "Rdtci1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
