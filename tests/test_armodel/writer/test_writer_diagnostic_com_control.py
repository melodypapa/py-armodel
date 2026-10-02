"""
Tests for writing DIAGNOSTIC-COM-CONTROL elements —
DiagnosticComControl, Table 4.64 (p.108, R23-11).

DiagnosticComControl (Base most-derived ARElement, concrete) defines two 0..1
attributes: the comControlClass ref (RefType, COM-CONTROL-CLASS-REF, DEST
DIAGNOSTIC-COM-CONTROL-CLASS) and customSubFunctionNumber (PositiveInteger,
CUSTOM-SUB-FUNCTION-NUMBER) — AUTOSAR_00052.xsd group DIAGNOSTIC-COM-CONTROL
l.32515 / complexType l.32546. The inherited DIAGNOSTIC-COMMON-ELEMENT and
DIAGNOSTIC-SERVICE-INSTANCE groups are empty sequences in the XSD, so the
writer delegates only to writeIdentifiable and the dispatch entry is
writeARPackageElement → writeDiagnosticComControl.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_com_control.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticComControl
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


class TestWriteDiagnosticComControl:
    """Tests for writeDiagnosticComControl — own element field values (Table 4.64)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticComControl without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        package.createDiagnosticComControl("ComControl1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControl(parent, package.getReferrableElement("ComControl1", DiagnosticComControl))

        child = parent.find("DIAGNOSTIC-COM-CONTROL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ComControl1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_com_control_class_ref(self):
        """Test that the COM-CONTROL-CLASS-REF is emitted with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control = package.createDiagnosticComControl("ComControl1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-COM-CONTROL-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticCommunicationControls/ComControlClass")
        com_control.setComControlClass(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControl(parent, com_control)

        child = parent.find("DIAGNOSTIC-COM-CONTROL")
        assert child is not None
        ref_element = child.find("COM-CONTROL-CLASS-REF")
        assert ref_element is not None
        assert ref_element.text == "/AUTOSAR/DiagnosticCommunicationControls/ComControlClass"
        assert ref_element.get("DEST") == "DIAGNOSTIC-COM-CONTROL-CLASS"

    def test_write_custom_sub_function_number(self):
        """Test that CUSTOM-SUB-FUNCTION-NUMBER is emitted with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control = package.createDiagnosticComControl("ComControl1")
        value = PositiveInteger()
        value.setValue("5")
        com_control.setCustomSubFunctionNumber(value)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControl(parent, com_control)

        child = parent.find("DIAGNOSTIC-COM-CONTROL")
        assert child is not None
        number_element = child.find("CUSTOM-SUB-FUNCTION-NUMBER")
        assert number_element is not None
        assert number_element.text == "5"

    def test_write_field_order(self):
        """Test that both attributes are emitted in XSD order (COM-CONTROL-CLASS-REF before CUSTOM-SUB-FUNCTION-NUMBER)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control = package.createDiagnosticComControl("ComControl1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-COM-CONTROL-CLASS")
        ref.setValue("/Diag/ComControlClass")
        com_control.setComControlClass(ref)
        value = PositiveInteger()
        value.setValue("7")
        com_control.setCustomSubFunctionNumber(value)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControl(parent, com_control)

        child = parent.find("DIAGNOSTIC-COM-CONTROL")
        assert child is not None
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["COM-CONTROL-CLASS-REF", "CUSTOM-SUB-FUNCTION-NUMBER"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticComControl to a DIAGNOSTIC-COM-CONTROL element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        package.createDiagnosticComControl("ComControl1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("ComControl1", DiagnosticComControl))

        child = parent.find("DIAGNOSTIC-COM-CONTROL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ComControl1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticCommunicationControls")
        com_control = package.createDiagnosticComControl("ComControl1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-COM-CONTROL-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticCommunicationControls/ComControlClass")
        com_control.setComControlClass(ref)
        value = PositiveInteger()
        value.setValue("5")
        com_control.setCustomSubFunctionNumber(value)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            com_control_2 = package_2.getReferrableElement("ComControl1", DiagnosticComControl)
            assert com_control_2 is not None
            assert com_control_2.getShortName() == "ComControl1"
            ref_2 = com_control_2.getComControlClass()
            assert ref_2 is not None
            assert ref_2.getValue() == "/AUTOSAR/DiagnosticCommunicationControls/ComControlClass"
            assert ref_2.getDest() == "DIAGNOSTIC-COM-CONTROL-CLASS"
            assert com_control_2.getCustomSubFunctionNumber() is not None
            assert com_control_2.getCustomSubFunctionNumber().getValue() == 5
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
