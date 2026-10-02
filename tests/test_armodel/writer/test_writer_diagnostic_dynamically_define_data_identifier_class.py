"""
Tests for writing DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS elements —
DiagnosticDynamicallyDefineDataIdentifierClass, Table 4.94 (p.128, R23-11).

DiagnosticDynamicallyDefineDataIdentifierClass (concrete DiagnosticServiceClass,
Aggregated by ARPackage.element) defines three attributes in displayed order:
checkPerSourceId (CHECK-PER-SOURCE-ID), configurationHandling
(CONFIGURATION-HANDLING) and subfunction (SUBFUNCTIONS wrapper of SUBFUNCTION
enum tokens) — AUTOSAR_00052.xsd group
DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS l.35199 / complexType l.35234.
The writer emits the children in XSD sequence order. The dispatch entry is
writeARPackageElement → writeDiagnosticDynamicallyDefineDataIdentifierClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_dynamically_define_data_identifier_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticDynamicallyDefineDataIdentifierClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum,
    DiagnosticHandleDDDIConfigurationEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticDynamicallyDefineDataIdentifierClass:
    """Tests for writeDiagnosticDynamicallyDefineDataIdentifierClass — own element field values (Table 4.94)."""

    def _write(self, dddi_class: DiagnosticDynamicallyDefineDataIdentifierClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDynamicallyDefineDataIdentifierClass(parent, dddi_class)
        return parent.find("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticDynamicallyDefineDataIdentifierClass without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")

        child = self._write(package.getReferrableElement("Dddic1", DiagnosticDynamicallyDefineDataIdentifierClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dddic1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_check_per_source_id(self):
        """Test that the CHECK-PER-SOURCE-ID is emitted from checkPerSourceId."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi_class = package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")
        dddi_class.setCheckPerSourceId(Boolean().setValue(True))

        child = self._write(dddi_class)
        assert child is not None
        element = child.find("CHECK-PER-SOURCE-ID")
        assert element is not None
        assert element.text == "true"

    def test_write_configuration_handling(self):
        """Test that the CONFIGURATION-HANDLING is emitted as its enum XML token."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi_class = package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")
        dddi_class.setConfigurationHandling(DiagnosticHandleDDDIConfigurationEnum().setValue(DiagnosticHandleDDDIConfigurationEnum.VOLATILE))

        child = self._write(dddi_class)
        assert child is not None
        element = child.find("CONFIGURATION-HANDLING")
        assert element is not None
        assert element.text == "VOLATILE"

    def test_write_subfunctions(self):
        """Test that the SUBFUNCTIONS wrapper emits one SUBFUNCTION token per enum value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi_class = package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")
        dddi_class.addSubfunction(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum().setValue(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_IDENTIFIER))
        dddi_class.addSubfunction(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum().setValue(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_MEMORY_ADDRESS))

        child = self._write(dddi_class)
        assert child is not None
        subfunctions = child.find("SUBFUNCTIONS")
        assert subfunctions is not None
        tokens = [subfunction.text for subfunction in subfunctions.findall("SUBFUNCTION")]
        assert tokens == ["DEFINE-BY-IDENTIFIER", "DEFINE-BY-MEMORY-ADDRESS"]

    def test_write_children_follow_xsd_sequence(self):
        """Test that the children are emitted in XSD sequence order (CHECK-PER-SOURCE-ID, CONFIGURATION-HANDLING, SUBFUNCTIONS)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi_class = package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")
        dddi_class.addSubfunction(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum().setValue(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_IDENTIFIER))
        dddi_class.setConfigurationHandling(DiagnosticHandleDDDIConfigurationEnum().setValue(DiagnosticHandleDDDIConfigurationEnum.NON_VOLATILE))
        dddi_class.setCheckPerSourceId(Boolean().setValue(False))

        child = self._write(dddi_class)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["CHECK-PER-SOURCE-ID", "CONFIGURATION-HANDLING", "SUBFUNCTIONS"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticDynamicallyDefineDataIdentifierClass to a DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Dddic1", DiagnosticDynamicallyDefineDataIdentifierClass))

        child = parent.find("DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dddic1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticDynamicallyDefineDataIdentifiers")
        dddi_class = package.createDiagnosticDynamicallyDefineDataIdentifierClass("Dddic1")
        dddi_class.setCheckPerSourceId(Boolean().setValue(True))
        dddi_class.setConfigurationHandling(DiagnosticHandleDDDIConfigurationEnum().setValue(DiagnosticHandleDDDIConfigurationEnum.NON_VOLATILE))
        dddi_class.addSubfunction(
            DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum().setValue(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER)
        )
        dddi_class.addSubfunction(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum().setValue(DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum.DEFINE_BY_MEMORY_ADDRESS))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            dddi_class_2 = package_2.getReferrableElement("Dddic1", DiagnosticDynamicallyDefineDataIdentifierClass)
            assert dddi_class_2 is not None
            assert dddi_class_2.getShortName() == "Dddic1"
            assert dddi_class_2.getCheckPerSourceId() is not None
            assert dddi_class_2.getCheckPerSourceId().getValue() is True
            assert dddi_class_2.getConfigurationHandling() is not None
            assert dddi_class_2.getConfigurationHandling().getValue() == "nonVolatile"
            values = [subfunction.getValue() for subfunction in dddi_class_2.getSubfunctions()]
            assert values == ["clearDynamicallyDefineDataIdentifier", "defineByMemoryAddress"]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
