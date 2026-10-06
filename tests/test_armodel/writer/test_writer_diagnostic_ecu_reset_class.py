"""
Tests for writing DIAGNOSTIC-ECU-RESET-CLASS elements —
DiagnosticEcuResetClass, Table 4.61 (p.102, R23-11).

DiagnosticEcuResetClass (Base most-derived DiagnosticServiceClass, concrete)
defines one 0..1 attribute: respondToReset (DiagnosticResponseToEcuResetEnum,
RESPOND-TO-RESET) — AUTOSAR_00052.xsd group DIAGNOSTIC-ECU-RESET-CLASS
l.35423 / complexType l.35442. The literal value is mapped to the
AR:DIAGNOSTIC-RESPONSE-TO-ECU-RESET-ENUM--SIMPLE token via
DIAGNOSTIC_RESPONSE_TO_ECU_RESET_XML_MAP and the dispatch entry is
writeARPackageElement → writeDiagnosticEcuResetClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_ecu_reset_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticEcuResetClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticResponseToEcuResetEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _respond_to_reset(value):
    """Build a DiagnosticResponseToEcuResetEnum holding the given literal value."""
    return DiagnosticResponseToEcuResetEnum().setValue(value)


class TestWriteDiagnosticEcuResetClass:
    """Tests for writeDiagnosticEcuResetClass — own element field values (Table 4.61)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEcuResetClass without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResetClasses")
        package.createDiagnosticEcuResetClass("EcuResetClass1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuResetClass(parent, package.getReferrableElement("EcuResetClass1", DiagnosticEcuResetClass))

        child = parent.find("DIAGNOSTIC-ECU-RESET-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EcuResetClass1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_respond_to_reset(self):
        """Test that RESPOND-TO-RESET is emitted with the XSD token of the literal value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResetClasses")
        ecu_reset_class = package.createDiagnosticEcuResetClass("EcuResetClass1")
        ecu_reset_class.setRespondToReset(_respond_to_reset("RESPOND-BEFORE-RESET"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuResetClass(parent, ecu_reset_class)

        child = parent.find("DIAGNOSTIC-ECU-RESET-CLASS")
        assert child is not None
        respond_element = child.find("RESPOND-TO-RESET")
        assert respond_element is not None
        assert respond_element.text == "RESPOND-BEFORE-RESET"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticEcuResetClass to a DIAGNOSTIC-ECU-RESET-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuResetClasses")
        package.createDiagnosticEcuResetClass("EcuResetClass1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("EcuResetClass1", DiagnosticEcuResetClass))

        child = parent.find("DIAGNOSTIC-ECU-RESET-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EcuResetClass1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage (empty wrapper)."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEcuResetClasses")
        package.createDiagnosticEcuResetClass("EcuResetClass1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            ecu_reset_class_2 = package_2.getReferrableElement("EcuResetClass1", DiagnosticEcuResetClass)
            assert ecu_reset_class_2 is not None
            assert ecu_reset_class_2.getShortName() == "EcuResetClass1"
            assert ecu_reset_class_2.getRespondToReset() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_with_respond_to_reset(self):
        """Test the full cycle including RESPOND-TO-RESET (literal ↔ XSD token via DIAGNOSTIC_RESPONSE_TO_ECU_RESET_XML_MAP)."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEcuResetClasses")
        ecu_reset_class = package.createDiagnosticEcuResetClass("EcuResetClass1")
        ecu_reset_class.setRespondToReset(_respond_to_reset("RESPOND-AFTER-RESET"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            ecu_reset_class_2 = package_2.getReferrableElement("EcuResetClass1", DiagnosticEcuResetClass)
            assert ecu_reset_class_2 is not None
            respond_to_reset = ecu_reset_class_2.getRespondToReset()
            assert respond_to_reset is not None
            assert isinstance(respond_to_reset, DiagnosticResponseToEcuResetEnum)
            assert respond_to_reset.getValue() == DiagnosticResponseToEcuResetEnum.RESPOND_AFTER_RESET
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
