"""
Tests for writing DIAGNOSTIC-OPERATION-CYCLE elements —
DiagnosticOperationCycle, Table 4.196 (p.201, R23-11).

DiagnosticOperationCycle (Base most-derived ARElement) carries one own Attribute
row — type (DiagnosticOperationCycleTypeEnum, 0..1, attr) — written as the single
TYPE child in the XSD group's sequenceOffset order (AUTOSAR_00052.xsd l.40289;
the group's AUTOMATIC-END, CYCLE-AUTOSTART and CYCLE-STATUS-STORAGE elements
carry atp.Status="removed" and are not modeled). type round-trips as the typed
DiagnosticOperationCycleTypeEnum (Table 4.197) literal — the enum value maps
back to its TYPE XSD token.
The dispatch entries are writeARPackageElement → writeDiagnosticOperationCycle
and writeDiagnosticElement → writeDiagnosticOperationCycle (the Diagnostic
catch-all arm of writeARPackageElementRest).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_operation_cycle.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticOperationCycle
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticOperationCycleTypeEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_cycle(package) -> DiagnosticOperationCycle:
    cycle = package.createDiagnosticOperationCycle("OperationCycle1")
    cycle.setType(DiagnosticOperationCycleTypeEnum().setValue(DiagnosticOperationCycleTypeEnum.IGNITION))
    return cycle


class TestWriteDiagnosticOperationCycle:
    """Tests for writeDiagnosticOperationCycle — own element field values (Table 4.196)."""

    def test_write_type_in_xsd_sequence_order(self):
        """Test that a set element emits SHORT-NAME + the TYPE child (only kept group element) with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticOperationCycles")
        cycle = _make_cycle(package)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticOperationCycle(parent, cycle)

        child = parent.find("DIAGNOSTIC-OPERATION-CYCLE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "OperationCycle1"
        assert child.find("TYPE").text == "IGNITION"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an element without own values emits no attribute children (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticOperationCycles")
        package.createDiagnosticOperationCycle("OperationCycle1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticOperationCycle(parent, package.getReferrableElement("OperationCycle1", DiagnosticOperationCycle))

        child = parent.find("DIAGNOSTIC-OPERATION-CYCLE")
        assert child is not None
        assert child.find("TYPE") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticOperationCycle to a DIAGNOSTIC-OPERATION-CYCLE element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticOperationCycles")
        cycle = _make_cycle(package)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, cycle)

        child = parent.find("DIAGNOSTIC-OPERATION-CYCLE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "OperationCycle1"
        assert child.find("TYPE").text == "IGNITION"

    def test_diagnostic_element_dispatch_writes_element(self):
        """Test that writeDiagnosticElement dispatches DiagnosticOperationCycle to a DIAGNOSTIC-OPERATION-CYCLE element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticOperationCycles")
        cycle = package.createDiagnosticOperationCycle("OperationCycle1")
        cycle.setType(DiagnosticOperationCycleTypeEnum().setValue(DiagnosticOperationCycleTypeEnum.OBD_DRIVING_CYCLE))

        parent = ET.Element("AR-PACKAGE")
        assert ARXMLWriter().writeDiagnosticElement(parent, cycle) is True

        child = parent.find("DIAGNOSTIC-OPERATION-CYCLE")
        assert child is not None
        assert child.find("TYPE").text == "OBD-DRIVING-CYCLE"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with the own field value set."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticOperationCycles")
        _make_cycle(package)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            cycle_2 = package_2.getReferrableElement("OperationCycle1", DiagnosticOperationCycle)
            assert cycle_2 is not None
            assert cycle_2.getShortName() == "OperationCycle1"
            assert cycle_2.getType() is not None
            assert isinstance(cycle_2.getType(), DiagnosticOperationCycleTypeEnum)
            assert cycle_2.getType().getValue() == "ignition"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticOperationCycle without any attribute value round-trips with None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticOperationCycles")
        package.createDiagnosticOperationCycle("OperationCycle1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            cycle_2 = package_2.getReferrableElement("OperationCycle1", DiagnosticOperationCycle)
            assert cycle_2 is not None
            assert cycle_2.getType() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
