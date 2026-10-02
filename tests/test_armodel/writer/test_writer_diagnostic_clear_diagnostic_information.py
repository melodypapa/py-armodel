"""
Tests for writing DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION elements —
DiagnosticClearDiagnosticInformation, Table 4.108 (p.137, R23-11).

DiagnosticClearDiagnosticInformation (Base most-derived ARElement, aggregated
by ARPackage.element) owns a single attribute in XSD group
DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION, AUTOSAR_00052.xsd l.32349: the 0..1
clearDiagnosticInformationClass ref (CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF,
DEST DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS--SUBTYPES-ENUM). The writer
reads the model via the get* getters in XSD element order. The dispatch entry
is writeARPackageElement → writeDiagnosticClearDiagnosticInformation.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_clear_diagnostic_information.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticClearDiagnosticInformation
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


class TestWriteDiagnosticClearDiagnosticInformation:
    """Tests for writeDiagnosticClearDiagnosticInformation — own element field values (Table 4.108)."""

    def _write(self, clear_diagnostic_information: DiagnosticClearDiagnosticInformation) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticClearDiagnosticInformation(parent, clear_diagnostic_information)
        return parent.find("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticClearDiagnosticInformation without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticClearDiagnosticInformations")
        clear_diagnostic_information = package.createDiagnosticClearDiagnosticInformation("ClearDiagnosticInformation1")

        child = self._write(clear_diagnostic_information)
        assert child is not None
        assert child.find("SHORT-NAME").text == "ClearDiagnosticInformation1"
        assert child.find("CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF") is None

    def test_write_clear_diagnostic_information_class_ref(self):
        """Test that the CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticClearDiagnosticInformations")
        clear_diagnostic_information = package.createDiagnosticClearDiagnosticInformation("ClearDiagnosticInformation1")
        clear_diagnostic_information.setClearDiagnosticInformationClass(
            _ref("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS", "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass")
        )

        child = self._write(clear_diagnostic_information)
        ref = child.find("CLEAR-DIAGNOSTIC-INFORMATION-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass"
        assert ref.get("DEST") == "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticClearDiagnosticInformation to a DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticClearDiagnosticInformations")
        package.createDiagnosticClearDiagnosticInformation("ClearDiagnosticInformation1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("ClearDiagnosticInformation1", DiagnosticClearDiagnosticInformation))

        child = parent.find("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ClearDiagnosticInformation1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticClearDiagnosticInformations")
        clear_diagnostic_information = package.createDiagnosticClearDiagnosticInformation("ClearDiagnosticInformation1")
        clear_diagnostic_information.setClearDiagnosticInformationClass(
            _ref("DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS", "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass")
        )

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            clear_diagnostic_information_2 = package_2.getElement("ClearDiagnosticInformation1", DiagnosticClearDiagnosticInformation)
            assert clear_diagnostic_information_2 is not None
            assert clear_diagnostic_information_2.getShortName() == "ClearDiagnosticInformation1"
            ref = clear_diagnostic_information_2.getClearDiagnosticInformationClass()
            assert ref is not None
            assert ref.getValue() == "/AUTOSAR/DiagnosticClearDiagnosticInformations/ClearDiagnosticInformationClass"
            assert ref.getDest() == "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
