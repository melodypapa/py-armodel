"""
Tests for reading the DIAGNOSTIC-ROUTINE-SUBFUNCTION XML group — DiagnosticRoutineSubfunction, Table 4.84 (p.121, R23-11).

DiagnosticRoutineSubfunction is an abstract base: its XML group
DIAGNOSTIC-ROUTINE-SUBFUNCTION (AUTOSAR_00052.xsd l.43145) carries the single
optional ACCESS-PERMISSION-REF element (DEST
DIAGNOSTIC-ACCESS-PERMISSION--SUBTYPES-ENUM). The reusable
readDiagnosticRoutineSubfunction helper is exercised through the concrete
subclass DiagnosticStartRoutine.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_routine_subfunction.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRoutineSubfunction:
    """Tests for readDiagnosticRoutineSubfunction — own element field values (Table 4.84)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticStartRoutine

        routine_subfunction = DiagnosticStartRoutine(parent=MagicMock(), short_name="StartRoutine1")
        element = _snip(inner, root_tag="DIAGNOSTIC-START-ROUTINE")
        parser.readDiagnosticRoutineSubfunction(element, routine_subfunction)
        return routine_subfunction

    def test_read_access_permission_ref(self, parser):
        """Test that the ACCESS-PERMISSION-REF is read with its DEST attribute."""
        inner = '<ACCESS-PERMISSION-REF DEST="DIAGNOSTIC-ACCESS-PERMISSION">/AUTOSAR/DiagnosticAccessPermissions/Level1</ACCESS-PERMISSION-REF>'
        routine_subfunction = self._read(parser, inner)
        assert routine_subfunction.getAccessPermission() is not None
        assert routine_subfunction.getAccessPermission().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert routine_subfunction.getAccessPermission().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"

    def test_read_absent_ref(self, parser):
        """Test that an absent ACCESS-PERMISSION-REF leaves the accessPermission field None."""
        routine_subfunction = self._read(parser, "")
        assert routine_subfunction.getAccessPermission() is None

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving accessPermission unset."""
        routine_subfunction = self._read(parser, "<SHORT-NAME>StartRoutine1</SHORT-NAME>")
        assert routine_subfunction.getAccessPermission() is None
