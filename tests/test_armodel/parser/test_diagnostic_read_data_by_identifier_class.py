"""
Tests for reading the DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS element —
DiagnosticReadDataByIdentifierClass, Table 4.74 (p.114, R23-11).

DiagnosticReadDataByIdentifierClass (Base most-derived DiagnosticServiceClass,
concrete) defines one 0..1 attribute: maxDidToRead (PositiveInteger,
MAX-DID-TO-READ) — AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS l.41186 / complexType l.41203.
The dispatch entry is readARPackageElements →
readDiagnosticReadDataByIdentifierClass via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_data_by_identifier_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadDataByIdentifierClass:
    """Tests for readDiagnosticReadDataByIdentifierClass — own element field values (Table 4.74)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDataByIdentifierClass

        read_data_by_identifier_class = DiagnosticReadDataByIdentifierClass(parent=parser, short_name="Rdibc")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS")
        parser.readDiagnosticReadDataByIdentifierClass(element, read_data_by_identifier_class)
        return read_data_by_identifier_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        read_data_by_identifier_class = self._read(parser, "<SHORT-NAME>Rdibc</SHORT-NAME>")
        assert read_data_by_identifier_class.getShortName() == "Rdibc"

    def test_read_max_did_to_read(self, parser):
        """Test that MAX-DID-TO-READ is read as a PositiveInteger value."""
        read_data_by_identifier_class = self._read(parser, "<MAX-DID-TO-READ>10</MAX-DID-TO-READ>")
        value = read_data_by_identifier_class.getMaxDidToRead()
        assert value is not None
        assert value.getValue() == 10

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving maxDidToRead unset."""
        read_data_by_identifier_class = self._read(parser, "<SHORT-NAME>Rdibc</SHORT-NAME>")
        assert read_data_by_identifier_class.getMaxDidToRead() is None
