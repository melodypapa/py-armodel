"""
Tests for writing DIAGNOSTIC-READ-DATA-BY-IDENTIFIER elements —
DiagnosticReadDataByIdentifier, Table 4.70 (p.112, R23-11).

DiagnosticReadDataByIdentifier (Base most-derived DiagnosticDataByIdentifier)
owns one attribute: the 0..1 readClass ref (READ-CLASS-REF, DEST
DIAGNOSTIC-READ-DATA-BY-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-IDENTIFIER l.41139. It inherits the 0..1
dataIdentifier ref (DATA-IDENTIFIER-REF) from the abstract
DiagnosticDataByIdentifier (Table 4.73); the writer delegates the inherited
field to the Rule 0001.7 helper writeDiagnosticDataByIdentifier. Per the XSD
complexType sequence (l.41164) the inherited DATA-IDENTIFIER-REF precedes the
own READ-CLASS-REF. The dispatch entry is writeARPackageElement →
writeDiagnosticReadDataByIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_data_by_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDataByIdentifier
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


class TestWriteDiagnosticReadDataByIdentifier:
    """Tests for writeDiagnosticReadDataByIdentifier — own element field values (Table 4.70)."""

    def _write(self, read_data_by_identifier: DiagnosticReadDataByIdentifier) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadDataByIdentifier(parent, read_data_by_identifier)
        return parent.find("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadDataByIdentifier without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifiers")
        package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")

        child = self._write(package.getReferrableElement("ReadDataByIdentifier1", DiagnosticReadDataByIdentifier))
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadDataByIdentifier1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_read_class_ref(self):
        """Test that the READ-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifiers")
        read_data_by_identifier = package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")
        read_data_by_identifier.setReadClass(_ref("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"))

        child = self._write(read_data_by_identifier)
        ref = child.find("READ-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"
        assert ref.get("DEST") == "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the inherited DATA-IDENTIFIER-REF precedes the own READ-CLASS-REF (XSD l.41164)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifiers")
        read_data_by_identifier = package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")
        read_data_by_identifier.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        read_data_by_identifier.setReadClass(_ref("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"))

        child = self._write(read_data_by_identifier)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["DATA-IDENTIFIER-REF", "READ-CLASS-REF"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadDataByIdentifier to a DIAGNOSTIC-READ-DATA-BY-IDENTIFIER element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByIdentifiers")
        package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("ReadDataByIdentifier1", DiagnosticReadDataByIdentifier))

        child = parent.find("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadDataByIdentifier1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadDataByIdentifiers")
        read_data_by_identifier = package.createDiagnosticReadDataByIdentifier("ReadDataByIdentifier1")
        read_data_by_identifier.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        read_data_by_identifier.setReadClass(_ref("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            read_data_by_identifier_2 = package_2.getReferrableElement("ReadDataByIdentifier1", DiagnosticReadDataByIdentifier)
            assert read_data_by_identifier_2 is not None
            assert read_data_by_identifier_2.getShortName() == "ReadDataByIdentifier1"
            data_identifier = read_data_by_identifier_2.getDataIdentifier()
            assert data_identifier is not None
            assert data_identifier.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
            assert data_identifier.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
            read_class = read_data_by_identifier_2.getReadClass()
            assert read_class is not None
            assert read_class.getValue() == "/AUTOSAR/DiagnosticReadDataByIdentifierClasses/ReadClass"
            assert read_class.getDest() == "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
