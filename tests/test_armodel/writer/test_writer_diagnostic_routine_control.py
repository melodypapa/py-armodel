"""
Tests for writing DIAGNOSTIC-ROUTINE-CONTROL elements —
DiagnosticRoutineControl, Table 4.89 (p.125, R23-11).

DiagnosticRoutineControl (concrete ARElement, Aggregated by ARPackage.element)
defines two 0..1 refs: routineControlClass (ROUTINE-CONTROL-CLASS-REF) and
routine (ROUTINE-REF) — AUTOSAR_00052.xsd group DIAGNOSTIC-ROUTINE-CONTROL
l.42913 / complexType l.42949. The writer emits the refs in XSD sequence order
(ROUTINE-CONTROL-CLASS-REF before ROUTINE-REF). The dispatch entry is
writeARPackageElement → writeDiagnosticRoutineControl.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_routine_control.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRoutineControl
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


class TestWriteDiagnosticRoutineControl:
    """Tests for writeDiagnosticRoutineControl — own element field values (Table 4.89)."""

    def _write(self, routine_control: DiagnosticRoutineControl) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRoutineControl(parent, routine_control)
        return parent.find("DIAGNOSTIC-ROUTINE-CONTROL")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticRoutineControl without refs emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        package.createDiagnosticRoutineControl("RoutineControl1")

        child = self._write(package.getReferrableElement("RoutineControl1", DiagnosticRoutineControl))
        assert child is not None
        assert child.find("SHORT-NAME").text == "RoutineControl1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_routine_ref(self):
        """Test that the ROUTINE-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        routine_control = package.createDiagnosticRoutineControl("RoutineControl1")
        routine_control.setRoutine(_ref("DIAGNOSTIC-ROUTINE", "/AUTOSAR/DiagnosticRoutines/Routine1"))

        child = self._write(routine_control)
        assert child is not None
        ref = child.find("ROUTINE-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticRoutines/Routine1"
        assert ref.get("DEST") == "DIAGNOSTIC-ROUTINE"

    def test_write_routine_control_class_ref(self):
        """Test that the ROUTINE-CONTROL-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        routine_control = package.createDiagnosticRoutineControl("RoutineControl1")
        routine_control.setRoutineControlClass(_ref("DIAGNOSTIC-ROUTINE-CONTROL-CLASS", "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"))

        child = self._write(routine_control)
        assert child is not None
        ref = child.find("ROUTINE-CONTROL-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"
        assert ref.get("DEST") == "DIAGNOSTIC-ROUTINE-CONTROL-CLASS"

    def test_write_ref_order_follows_xsd_sequence(self):
        """Test that ROUTINE-CONTROL-CLASS-REF is emitted before ROUTINE-REF (XSD sequenceOffset order)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        routine_control = package.createDiagnosticRoutineControl("RoutineControl1")
        routine_control.setRoutine(_ref("DIAGNOSTIC-ROUTINE", "/AUTOSAR/DiagnosticRoutines/Routine1"))
        routine_control.setRoutineControlClass(_ref("DIAGNOSTIC-ROUTINE-CONTROL-CLASS", "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"))

        child = self._write(routine_control)
        assert [c.tag for c in child if c.tag.endswith("-REF")] == ["ROUTINE-CONTROL-CLASS-REF", "ROUTINE-REF"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticRoutineControl to a DIAGNOSTIC-ROUTINE-CONTROL element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutineControls")
        package.createDiagnosticRoutineControl("RoutineControl1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("RoutineControl1", DiagnosticRoutineControl))

        child = parent.find("DIAGNOSTIC-ROUTINE-CONTROL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "RoutineControl1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticRoutineControls")
        routine_control = package.createDiagnosticRoutineControl("RoutineControl1")
        routine_control.setRoutine(_ref("DIAGNOSTIC-ROUTINE", "/AUTOSAR/DiagnosticRoutines/Routine1"))
        routine_control.setRoutineControlClass(_ref("DIAGNOSTIC-ROUTINE-CONTROL-CLASS", "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            routine_control_2 = package_2.getReferrableElement("RoutineControl1", DiagnosticRoutineControl)
            assert routine_control_2 is not None
            assert routine_control_2.getShortName() == "RoutineControl1"
            routine_ref = routine_control_2.getRoutine()
            assert routine_ref is not None
            assert routine_ref.getValue() == "/AUTOSAR/DiagnosticRoutines/Routine1"
            assert routine_ref.getDest() == "DIAGNOSTIC-ROUTINE"
            class_ref = routine_control_2.getRoutineControlClass()
            assert class_ref is not None
            assert class_ref.getValue() == "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"
            assert class_ref.getDest() == "DIAGNOSTIC-ROUTINE-CONTROL-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
