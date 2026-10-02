"""
Tests for reading the DIAGNOSTIC-ROUTINE-CONTROL-CLASS element —
DiagnosticRoutineControlClass, Table 4.90 (p.126, R23-11).

DiagnosticRoutineControlClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — AUTOSAR_00052.xsd group
DIAGNOSTIC-ROUTINE-CONTROL-CLASS l.42973 is an empty sequence. The reader
therefore only reads the IDENTIFIABLE wrapper. The dispatch entry is
readARPackageElements → readDiagnosticRoutineControlClass via the ARPackage
create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_routine_control_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRoutineControlClass:
    """Tests for readDiagnosticRoutineControlClass — own element field values (Table 4.90)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRoutineControlClass

        routine_control_class = DiagnosticRoutineControlClass(parent=parser, short_name="Rcc")
        element = _snip(inner, root_tag="DIAGNOSTIC-ROUTINE-CONTROL-CLASS")
        parser.readDiagnosticRoutineControlClass(element, routine_control_class)
        return routine_control_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        routine_control_class = self._read(parser, "<SHORT-NAME>Rcc</SHORT-NAME>")
        assert routine_control_class.getShortName() == "Rcc"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the class unchanged."""
        routine_control_class = self._read(parser, "<SHORT-NAME>Rcc</SHORT-NAME>")
        assert routine_control_class.getShortName() == "Rcc"
