"""
Tests for writing DIAGNOSTIC-ECU-RESET elements —
DiagnosticEcuReset, Table 4.60 (p.102, R23-11).

DiagnosticEcuReset (Base most-derived ARElement, concrete) defines two 0..1
attributes: customSubFunctionNumber (PositiveInteger, CUSTOM-SUB-FUNCTION-NUMBER)
and the ecuResetClass ref (RefType, ECU-RESET-CLASS-REF, DEST
DIAGNOSTIC-ECU-RESET-CLASS) — AUTOSAR_00052.xsd group DIAGNOSTIC-ECU-RESET
l.35369 / complexType l.35406. The inherited DIAGNOSTIC-COMMON-ELEMENT and
DIAGNOSTIC-SERVICE-INSTANCE groups are empty sequences in the XSD, so the
writer delegates only to writeIdentifiable and the dispatch entry is
writeARPackageElement → writeDiagnosticEcuReset.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_ecu_reset.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEcuReset
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEcuReset:
    """Tests for writeDiagnosticEcuReset — own element field values (Table 4.60)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEcuReset without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResets")
        package.createDiagnosticEcuReset("EcuReset1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuReset(parent, package.getElement("EcuReset1", DiagnosticEcuReset))

        child = parent.find("DIAGNOSTIC-ECU-RESET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EcuReset1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_custom_sub_function_number(self):
        """Test that CUSTOM-SUB-FUNCTION-NUMBER is emitted with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResets")
        ecu_reset = package.createDiagnosticEcuReset("EcuReset1")
        value = PositiveInteger()
        value.setValue("5")
        ecu_reset.setCustomSubFunctionNumber(value)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuReset(parent, ecu_reset)

        child = parent.find("DIAGNOSTIC-ECU-RESET")
        assert child is not None
        number_element = child.find("CUSTOM-SUB-FUNCTION-NUMBER")
        assert number_element is not None
        assert number_element.text == "5"

    def test_write_ecu_reset_class_ref(self):
        """Test that the ECU-RESET-CLASS-REF is emitted with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResets")
        ecu_reset = package.createDiagnosticEcuReset("EcuReset1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-ECU-RESET-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticEcuResetClasses/ResetClass")
        ecu_reset.setEcuResetClass(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuReset(parent, ecu_reset)

        child = parent.find("DIAGNOSTIC-ECU-RESET")
        assert child is not None
        ref_element = child.find("ECU-RESET-CLASS-REF")
        assert ref_element is not None
        assert ref_element.text == "/AUTOSAR/DiagnosticEcuResetClasses/ResetClass"
        assert ref_element.get("DEST") == "DIAGNOSTIC-ECU-RESET-CLASS"

    def test_write_field_order(self):
        """Test that both attributes are emitted in XSD order (CUSTOM-SUB-FUNCTION-NUMBER before ECU-RESET-CLASS-REF)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResets")
        ecu_reset = package.createDiagnosticEcuReset("EcuReset1")
        value = PositiveInteger()
        value.setValue("7")
        ecu_reset.setCustomSubFunctionNumber(value)
        ref = RefType()
        ref.setDest("DIAGNOSTIC-ECU-RESET-CLASS")
        ref.setValue("/Diag/ResetClass")
        ecu_reset.setEcuResetClass(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuReset(parent, ecu_reset)

        child = parent.find("DIAGNOSTIC-ECU-RESET")
        assert child is not None
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["CUSTOM-SUB-FUNCTION-NUMBER", "ECU-RESET-CLASS-REF"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticEcuReset to a DIAGNOSTIC-ECU-RESET element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResets")
        package.createDiagnosticEcuReset("EcuReset1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("EcuReset1", DiagnosticEcuReset))

        child = parent.find("DIAGNOSTIC-ECU-RESET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EcuReset1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEcuResets")
        ecu_reset = package.createDiagnosticEcuReset("EcuReset1")
        value = PositiveInteger()
        value.setValue("5")
        ecu_reset.setCustomSubFunctionNumber(value)
        ref = RefType()
        ref.setDest("DIAGNOSTIC-ECU-RESET-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticEcuResetClasses/ResetClass")
        ecu_reset.setEcuResetClass(ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            ecu_reset_2 = package_2.getElement("EcuReset1", DiagnosticEcuReset)
            assert ecu_reset_2 is not None
            assert ecu_reset_2.getShortName() == "EcuReset1"
            assert ecu_reset_2.getCustomSubFunctionNumber() is not None
            assert ecu_reset_2.getCustomSubFunctionNumber().getValue() == 5
            ref_2 = ecu_reset_2.getEcuResetClass()
            assert ref_2 is not None
            assert ref_2.getValue() == "/AUTOSAR/DiagnosticEcuResetClasses/ResetClass"
            assert ref_2.getDest() == "DIAGNOSTIC-ECU-RESET-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
