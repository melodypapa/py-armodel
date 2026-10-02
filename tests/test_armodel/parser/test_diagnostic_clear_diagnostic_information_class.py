"""
Tests for reading the DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS element —
DiagnosticClearDiagnosticInformationClass, Table 4.109 (p.137, R23-11).

DiagnosticClearDiagnosticInformationClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11
table's attribute row is `-` and XSD group
DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS, AUTOSAR_00052.xsd l.32396, is
an empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry
is readARPackageElements → readDiagnosticClearDiagnosticInformationClass via
the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_clear_diagnostic_information_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticClearDiagnosticInformationClass:
    """Tests for readDiagnosticClearDiagnosticInformationClass — own element field values (Table 4.109)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticClearDiagnosticInformationClass

        clear_diagnostic_information_class = DiagnosticClearDiagnosticInformationClass(parent=parser, short_name="Cdci")
        element = _snip(inner, root_tag="DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS")
        parser.readDiagnosticClearDiagnosticInformationClass(element, clear_diagnostic_information_class)
        return clear_diagnostic_information_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        clear_diagnostic_information_class = self._read(parser, "<SHORT-NAME>Cdci</SHORT-NAME>")
        assert clear_diagnostic_information_class.getShortName() == "Cdci"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element unnamed but valid."""
        clear_diagnostic_information_class = self._read(parser, "")
        assert clear_diagnostic_information_class.getShortName() == "Cdci"
