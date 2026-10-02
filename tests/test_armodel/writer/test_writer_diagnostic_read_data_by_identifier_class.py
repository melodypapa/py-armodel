"""
Tests for writing DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS elements —
DiagnosticReadDataByIdentifierClass, Table 4.74 (p.114, R23-11).

DiagnosticReadDataByIdentifierClass (Base most-derived DiagnosticServiceClass,
concrete) defines one 0..1 attribute: maxDidToRead (PositiveInteger,
MAX-DID-TO-READ) — AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS l.41186 / complexType l.41203.
The dispatch entry is writeARPackageElement →
writeDiagnosticReadDataByIdentifierClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_data_by_identifier_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDataByIdentifierClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _positive_integer(value) -> PositiveInteger:
    positive_integer = PositiveInteger()
    positive_integer.setValue(value)
    return positive_integer


class TestWriteDiagnosticReadDataByIdentifierClass:
    """Tests for writeDiagnosticReadDataByIdentifierClass — own element field values (Table 4.74)."""

    def _write(self, read_data_by_identifier_class: DiagnosticReadDataByIdentifierClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadDataByIdentifierClass(parent, read_data_by_identifier_class)
        return parent.find("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadDataByIdentifierClass without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifierClasses")
        package.createDiagnosticReadDataByIdentifierClass("Rdibc1")

        child = self._write(package.getReferrableElement("Rdibc1", DiagnosticReadDataByIdentifierClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdibc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_max_did_to_read(self):
        """Test that MAX-DID-TO-READ is emitted with its value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifierClasses")
        read_data_by_identifier_class = package.createDiagnosticReadDataByIdentifierClass("Rdibc1")
        read_data_by_identifier_class.setMaxDidToRead(_positive_integer("10"))

        child = self._write(read_data_by_identifier_class)
        element = child.find("MAX-DID-TO-READ")
        assert element is not None
        assert element.text == "10"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadDataByIdentifierClass to a DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifierClasses")
        package.createDiagnosticReadDataByIdentifierClass("Rdibc1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Rdibc1", DiagnosticReadDataByIdentifierClass))

        child = parent.find("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdibc1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field value."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadDataByIdentifierClasses")
        read_data_by_identifier_class = package.createDiagnosticReadDataByIdentifierClass("Rdibc1")
        read_data_by_identifier_class.setMaxDidToRead(_positive_integer("10"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            read_data_by_identifier_class_2 = package_2.getReferrableElement("Rdibc1", DiagnosticReadDataByIdentifierClass)
            assert read_data_by_identifier_class_2 is not None
            assert read_data_by_identifier_class_2.getShortName() == "Rdibc1"
            assert read_data_by_identifier_class_2.getMaxDidToRead() is not None
            assert read_data_by_identifier_class_2.getMaxDidToRead().getValue() == 10
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
