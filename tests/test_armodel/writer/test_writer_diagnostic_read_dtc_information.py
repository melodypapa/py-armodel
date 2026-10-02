"""
Tests for writing DIAGNOSTIC-READ-DTC-INFORMATION elements —
DiagnosticReadDTCInformation, Table 4.106 (p.136, R23-11).

DiagnosticReadDTCInformation (Base most-derived ARElement, aggregated by
ARPackage.element) owns a single attribute in XSD group
DIAGNOSTIC-READ-DTC-INFORMATION, AUTOSAR_00052.xsd l.41350: the 0..1
readDTCInformationClass ref (READ-DTC-INFORMATION-CLASS-REF, DEST
DIAGNOSTIC-READ-DTC-INFORMATION-CLASS--SUBTYPES-ENUM). The writer reads the
model via the get* getters in XSD element order. The dispatch entry is
writeARPackageElement → writeDiagnosticReadDTCInformation.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_dtc_information.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDTCInformation
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


class TestWriteDiagnosticReadDTCInformation:
    """Tests for writeDiagnosticReadDTCInformation — own element field values (Table 4.106)."""

    def _write(self, read_dtc_information: DiagnosticReadDTCInformation) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadDTCInformation(parent, read_dtc_information)
        return parent.find("DIAGNOSTIC-READ-DTC-INFORMATION")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadDTCInformation without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDtcInformations")
        read_dtc_information = package.createDiagnosticReadDTCInformation("ReadDTCInformation1")

        child = self._write(read_dtc_information)
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadDTCInformation1"
        assert child.find("READ-DTC-INFORMATION-CLASS-REF") is None

    def test_write_read_dtc_information_class_ref(self):
        """Test that the READ-DTC-INFORMATION-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDtcInformations")
        read_dtc_information = package.createDiagnosticReadDTCInformation("ReadDTCInformation1")
        read_dtc_information.setReadDTCInformationClass(_ref("DIAGNOSTIC-READ-DTC-INFORMATION-CLASS", "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass"))

        child = self._write(read_dtc_information)
        ref = child.find("READ-DTC-INFORMATION-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass"
        assert ref.get("DEST") == "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadDTCInformation to a DIAGNOSTIC-READ-DTC-INFORMATION element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDtcInformations")
        package.createDiagnosticReadDTCInformation("ReadDTCInformation1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("ReadDTCInformation1", DiagnosticReadDTCInformation))

        child = parent.find("DIAGNOSTIC-READ-DTC-INFORMATION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ReadDTCInformation1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadDtcInformations")
        read_dtc_information = package.createDiagnosticReadDTCInformation("ReadDTCInformation1")
        read_dtc_information.setReadDTCInformationClass(_ref("DIAGNOSTIC-READ-DTC-INFORMATION-CLASS", "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            read_dtc_information_2 = package_2.getElement("ReadDTCInformation1", DiagnosticReadDTCInformation)
            assert read_dtc_information_2 is not None
            assert read_dtc_information_2.getShortName() == "ReadDTCInformation1"
            ref = read_dtc_information_2.getReadDTCInformationClass()
            assert ref is not None
            assert ref.getValue() == "/AUTOSAR/DiagnosticReadDtcInformations/ReadDTCInformationClass"
            assert ref.getDest() == "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
