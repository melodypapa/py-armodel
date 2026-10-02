"""
Tests for writing DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS elements —
DiagnosticWriteDataByIdentifierClass, Table 4.72 (p.113, R23-11).

DiagnosticWriteDataByIdentifierClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — AUTOSAR_00052.xsd group
DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS l.47222 is an empty sequence. The
writer therefore only emits the DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS
element with its IDENTIFIABLE wrapper content. The dispatch entry is
writeARPackageElement → writeDiagnosticWriteDataByIdentifierClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_write_data_by_identifier_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticWriteDataByIdentifierClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticWriteDataByIdentifierClass:
    """Tests for writeDiagnosticWriteDataByIdentifierClass — own element field values (Table 4.72)."""

    def _write(self, write_data_by_identifier_class: DiagnosticWriteDataByIdentifierClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticWriteDataByIdentifierClass(parent, write_data_by_identifier_class)
        return parent.find("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticWriteDataByIdentifierClass emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifierClasses")
        package.createDiagnosticWriteDataByIdentifierClass("Wdibc1")

        child = self._write(package.getReferrableElement("Wdibc1", DiagnosticWriteDataByIdentifierClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Wdibc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticWriteDataByIdentifierClass to a DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifierClasses")
        package.createDiagnosticWriteDataByIdentifierClass("Wdibc1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Wdibc1", DiagnosticWriteDataByIdentifierClass))

        child = parent.find("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Wdibc1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving identity."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticWriteDataByIdentifierClasses")
        package.createDiagnosticWriteDataByIdentifierClass("Wdibc1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            write_data_by_identifier_class_2 = package_2.getReferrableElement("Wdibc1", DiagnosticWriteDataByIdentifierClass)
            assert write_data_by_identifier_class_2 is not None
            assert write_data_by_identifier_class_2.getShortName() == "Wdibc1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
