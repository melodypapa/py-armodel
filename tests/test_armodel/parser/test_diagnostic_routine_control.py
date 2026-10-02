"""
Tests for reading the DIAGNOSTIC-ROUTINE-CONTROL element —
DiagnosticRoutineControl, Table 4.89 (p.125, R23-11).

DiagnosticRoutineControl (concrete ARElement, Aggregated by ARPackage.element)
defines two 0..1 refs: routineControlClass (DEST
DIAGNOSTIC-ROUTINE-CONTROL-CLASS--SUBTYPES-ENUM, ROUTINE-CONTROL-CLASS-REF) and
routine (DEST DIAGNOSTIC-ROUTINE--SUBTYPES-ENUM, ROUTINE-REF) — AUTOSAR_00052.xsd
group DIAGNOSTIC-ROUTINE-CONTROL l.42913. The XSD sequence order
(ROUTINE-CONTROL-CLASS-REF before ROUTINE-REF) governs the XML element order; the
markdown displayed order (routine, routineControlClass) governs the class member
order (Rule 0001.11).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_routine_control.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRoutineControl:
    """Tests for readDiagnosticRoutineControl — own element field values (Table 4.89)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRoutineControl

        routine_control = DiagnosticRoutineControl(parent=MagicMock(), short_name="RoutineControl1")
        element = _snip(inner, root_tag="DIAGNOSTIC-ROUTINE-CONTROL")
        parser.readDiagnosticRoutineControl(element, routine_control)
        return routine_control

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        routine_control = self._read(parser, "<SHORT-NAME>RoutineControl1</SHORT-NAME>")
        assert routine_control.getShortName() == "RoutineControl1"

    def test_read_routine_ref(self, parser):
        """Test that the ROUTINE-REF is read with its DEST attribute."""
        inner = '<ROUTINE-REF DEST="DIAGNOSTIC-ROUTINE">/AUTOSAR/DiagnosticRoutines/Routine1</ROUTINE-REF>'
        routine_control = self._read(parser, inner)
        assert routine_control.getRoutine() is not None
        assert routine_control.getRoutine().getValue() == "/AUTOSAR/DiagnosticRoutines/Routine1"
        assert routine_control.getRoutine().getDest() == "DIAGNOSTIC-ROUTINE"

    def test_read_routine_control_class_ref(self, parser):
        """Test that the ROUTINE-CONTROL-CLASS-REF is read with its DEST attribute."""
        inner = '<ROUTINE-CONTROL-CLASS-REF DEST="DIAGNOSTIC-ROUTINE-CONTROL-CLASS">/AUTOSAR/DiagnosticRoutineControls/ControlClass1</ROUTINE-CONTROL-CLASS-REF>'
        routine_control = self._read(parser, inner)
        assert routine_control.getRoutineControlClass() is not None
        assert routine_control.getRoutineControlClass().getValue() == "/AUTOSAR/DiagnosticRoutineControls/ControlClass1"
        assert routine_control.getRoutineControlClass().getDest() == "DIAGNOSTIC-ROUTINE-CONTROL-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both refs unset."""
        routine_control = self._read(parser, "<SHORT-NAME>RoutineControl1</SHORT-NAME>")
        assert routine_control.getRoutine() is None
        assert routine_control.getRoutineControlClass() is None
