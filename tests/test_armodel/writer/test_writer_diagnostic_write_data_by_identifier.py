"""
Tests for writing DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER elements —
DiagnosticWriteDataByIdentifier, Table 4.71 (p.113, R23-11).

DiagnosticWriteDataByIdentifier (Base most-derived DiagnosticDataByIdentifier)
owns one attribute: the 0..1 writeClass ref (WRITE-CLASS-REF, DEST
DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd group
DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER l.47169. It inherits the 0..1
dataIdentifier ref (DATA-IDENTIFIER-REF) from the abstract
DiagnosticDataByIdentifier (Table 4.73); the writer delegates the inherited
field to the Rule 0001.7 helper writeDiagnosticDataByIdentifier. Per the XSD
complexType sequence (l.47194) the inherited DATA-IDENTIFIER-REF precedes the
own WRITE-CLASS-REF. The dispatch entry is writeARPackageElement →
writeDiagnosticWriteDataByIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_write_data_by_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticWriteDataByIdentifier
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


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticWriteDataByIdentifier:
    """Tests for writeDiagnosticWriteDataByIdentifier — own element field values (Table 4.71)."""

    def _write(self, write_data_by_identifier: DiagnosticWriteDataByIdentifier) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticWriteDataByIdentifier(parent, write_data_by_identifier)
        return parent.find("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticWriteDataByIdentifier without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifiers")
        package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")

        child = self._write(package.getElement("WriteDataByIdentifier1", DiagnosticWriteDataByIdentifier))
        assert child is not None
        assert child.find("SHORT-NAME").text == "WriteDataByIdentifier1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_write_class_ref(self):
        """Test that the WRITE-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifiers")
        write_data_by_identifier = package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")
        write_data_by_identifier.setWriteClass(_ref("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"))

        child = self._write(write_data_by_identifier)
        ref = child.find("WRITE-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"
        assert ref.get("DEST") == "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the inherited DATA-IDENTIFIER-REF precedes the own WRITE-CLASS-REF (XSD l.47194)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifiers")
        write_data_by_identifier = package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")
        write_data_by_identifier.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        write_data_by_identifier.setWriteClass(_ref("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"))

        child = self._write(write_data_by_identifier)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["DATA-IDENTIFIER-REF", "WRITE-CLASS-REF"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticWriteDataByIdentifier to a DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteDataByIdentifiers")
        package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("WriteDataByIdentifier1", DiagnosticWriteDataByIdentifier))

        child = parent.find("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "WriteDataByIdentifier1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticWriteDataByIdentifiers")
        write_data_by_identifier = package.createDiagnosticWriteDataByIdentifier("WriteDataByIdentifier1")
        write_data_by_identifier.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        write_data_by_identifier.setWriteClass(_ref("DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            write_data_by_identifier_2 = package_2.getElement("WriteDataByIdentifier1", DiagnosticWriteDataByIdentifier)
            assert write_data_by_identifier_2 is not None
            assert write_data_by_identifier_2.getShortName() == "WriteDataByIdentifier1"
            data_identifier = write_data_by_identifier_2.getDataIdentifier()
            assert data_identifier is not None
            assert data_identifier.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
            assert data_identifier.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
            write_class = write_data_by_identifier_2.getWriteClass()
            assert write_class is not None
            assert write_class.getValue() == "/AUTOSAR/DiagnosticWriteDataByIdentifierClasses/WriteClass"
            assert write_class.getDest() == "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
