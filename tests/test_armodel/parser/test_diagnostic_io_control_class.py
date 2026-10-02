"""
Tests for reading the DIAGNOSTIC-IO-CONTROL-CLASS element —
DiagnosticIoControlClass, Table 4.81 (p.118, R23-11).

DiagnosticIoControlClass (Base most-derived DiagnosticServiceClass, concrete)
defines no own attributes — AUTOSAR_00052.xsd group DIAGNOSTIC-IO-CONTROL-CLASS
l.38515 is an empty sequence. The reader therefore only reads the IDENTIFIABLE
wrapper. The dispatch entry is readARPackageElements →
readDiagnosticIoControlClass via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_io_control_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticIoControlClass:
    """Tests for readDiagnosticIoControlClass — own element field values (Table 4.81)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticIoControlClass

        io_control_class = DiagnosticIoControlClass(parent=parser, short_name="Icc")
        element = _snip(inner, root_tag="DIAGNOSTIC-IO-CONTROL-CLASS")
        parser.readDiagnosticIoControlClass(element, io_control_class)
        return io_control_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        io_control_class = self._read(parser, "<SHORT-NAME>Icc</SHORT-NAME>")
        assert io_control_class.getShortName() == "Icc"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the class unchanged."""
        io_control_class = self._read(parser, "<SHORT-NAME>Icc</SHORT-NAME>")
        assert io_control_class.getShortName() == "Icc"
