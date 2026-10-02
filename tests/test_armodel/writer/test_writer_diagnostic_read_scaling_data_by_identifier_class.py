"""
Tests for writing DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS elements —
DiagnosticReadScalingDataByIdentifierClass, Table 4.79 (p.116, R23-11).

DiagnosticReadScalingDataByIdentifierClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes —
AUTOSAR_00052.xsd group DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS
l.41566 is an empty sequence. The writer therefore only emits the
DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS element with its IDENTIFIABLE
wrapper content. The dispatch entry is writeARPackageElement →
writeDiagnosticReadScalingDataByIdentifierClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_scaling_data_by_identifier_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadScalingDataByIdentifierClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticReadScalingDataByIdentifierClass:
    """Tests for writeDiagnosticReadScalingDataByIdentifierClass — own element field values (Table 4.79)."""

    def _write(self, read_scaling_data_by_identifier_class: DiagnosticReadScalingDataByIdentifierClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadScalingDataByIdentifierClass(parent, read_scaling_data_by_identifier_class)
        return parent.find("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadScalingDataByIdentifierClass emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifierClasses")
        package.createDiagnosticReadScalingDataByIdentifierClass("Rsdibc1")

        child = self._write(package.getReferrableElement("Rsdibc1", DiagnosticReadScalingDataByIdentifierClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rsdibc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadScalingDataByIdentifierClass to a DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadScalingDataByIdentifierClasses")
        package.createDiagnosticReadScalingDataByIdentifierClass("Rsdibc1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Rsdibc1", DiagnosticReadScalingDataByIdentifierClass))

        child = parent.find("DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rsdibc1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving identity."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadScalingDataByIdentifierClasses")
        package.createDiagnosticReadScalingDataByIdentifierClass("Rsdibc1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            read_scaling_data_by_identifier_class_2 = package_2.getReferrableElement("Rsdibc1", DiagnosticReadScalingDataByIdentifierClass)
            assert read_scaling_data_by_identifier_class_2 is not None
            assert read_scaling_data_by_identifier_class_2.getShortName() == "Rsdibc1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
