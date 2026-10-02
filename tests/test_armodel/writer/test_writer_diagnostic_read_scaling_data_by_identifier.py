"""
Tests for writing DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER elements —
DiagnosticReadScalingDataByIdentifier, Table 4.78 (p.116, R23-11).

DiagnosticReadScalingDataByIdentifier (Base most-derived
DiagnosticDataByIdentifier) owns one attribute: the 0..1 readScalingDataClass
ref (READ-SCALING-DATA-CLASS-REF, DEST
DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER--SUBTYPES-ENUM), AUTOSAR_00052.xsd
group DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER l.41518. It inherits the
0..1 dataIdentifier ref (DATA-IDENTIFIER-REF) from the abstract
DiagnosticDataByIdentifier (Table 4.73); the writer delegates the inherited
field to the Rule 0001.7 helper writeDiagnosticDataByIdentifier. Per the XSD
complexType sequence (l.41543) the inherited DATA-IDENTIFIER-REF precedes the
own READ-SCALING-DATA-CLASS-REF. The dispatch entry is writeARPackageElement →
writeDiagnosticReadScalingDataByIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_scaling_data_by_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadScalingDataByIdentifier
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


class TestWriteDiagnosticReadScalingDataByIdentifier:
    """Tests for writeDiagnosticReadScalingDataByIdentifier — own element field values (Table 4.78)."""

    def _write(self, read_scaling_data_by_identifier: DiagnosticReadScalingDataByIdentifier) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadScalingDataByIdentifier(parent, read_scaling_data_by_identifier)
        return parent.find("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadScalingDataByIdentifier without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifiers")
        package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")

        child = self._write(package.getReferrableElement("ReadScalingDataByIdentifier1", DiagnosticReadScalingDataByIdentifier))
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadScalingDataByIdentifier1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_read_scaling_data_class_ref(self):
        """Test that the READ-SCALING-DATA-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifiers")
        read_scaling_data_by_identifier = package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")
        read_scaling_data_by_identifier.setReadScalingDataClass(_ref("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"))

        child = self._write(read_scaling_data_by_identifier)
        ref = child.find("READ-SCALING-DATA-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"
        assert ref.get("DEST") == "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the inherited DATA-IDENTIFIER-REF precedes the own READ-SCALING-DATA-CLASS-REF (XSD l.41543)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifiers")
        read_scaling_data_by_identifier = package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")
        read_scaling_data_by_identifier.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        read_scaling_data_by_identifier.setReadScalingDataClass(_ref("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"))

        child = self._write(read_scaling_data_by_identifier)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["DATA-IDENTIFIER-REF", "READ-SCALING-DATA-CLASS-REF"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadScalingDataByIdentifier to a DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifiers")
        package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("ReadScalingDataByIdentifier1", DiagnosticReadScalingDataByIdentifier))

        child = parent.find("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadScalingDataByIdentifier1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadScalingDataByIdentifiers")
        read_scaling_data_by_identifier = package.createDiagnosticReadScalingDataByIdentifier("ReadScalingDataByIdentifier1")
        read_scaling_data_by_identifier.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))
        read_scaling_data_by_identifier.setReadScalingDataClass(_ref("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS", "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            read_scaling_data_by_identifier_2 = package_2.getReferrableElement("ReadScalingDataByIdentifier1", DiagnosticReadScalingDataByIdentifier)
            assert read_scaling_data_by_identifier_2 is not None
            assert read_scaling_data_by_identifier_2.getShortName() == "ReadScalingDataByIdentifier1"
            data_identifier = read_scaling_data_by_identifier_2.getDataIdentifier()
            assert data_identifier is not None
            assert data_identifier.getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
            assert data_identifier.getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
            read_scaling_data_class = read_scaling_data_by_identifier_2.getReadScalingDataClass()
            assert read_scaling_data_class is not None
            assert read_scaling_data_class.getValue() == "/AUTOSAR/DiagnosticReadScalingDataByIdentifierClasses/ReadScalingClass"
            assert read_scaling_data_class.getDest() == "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
