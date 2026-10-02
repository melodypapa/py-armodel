"""
Tests for reading the DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS element —
DiagnosticWriteDataByIdentifierClass, Table 4.72 (p.113, R23-11).

DiagnosticWriteDataByIdentifierClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — AUTOSAR_00052.xsd group
DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS l.47222 is an empty sequence. The
reader therefore only reads the IDENTIFIABLE wrapper. The dispatch entry is
readARPackageElements → readDiagnosticWriteDataByIdentifierClass via the
ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_write_data_by_identifier_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticWriteDataByIdentifierClass:
    """Tests for readDiagnosticWriteDataByIdentifierClass — own element field values (Table 4.72)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticWriteDataByIdentifierClass

        write_data_by_identifier_class = DiagnosticWriteDataByIdentifierClass(parent=parser, short_name="Wdibc")
        element = _snip(inner, root_tag="DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS")
        parser.readDiagnosticWriteDataByIdentifierClass(element, write_data_by_identifier_class)
        return write_data_by_identifier_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        write_data_by_identifier_class = self._read(parser, "<SHORT-NAME>Wdibc</SHORT-NAME>")
        assert write_data_by_identifier_class.getShortName() == "Wdibc"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the class unchanged."""
        write_data_by_identifier_class = self._read(parser, "<SHORT-NAME>Wdibc</SHORT-NAME>")
        assert write_data_by_identifier_class.getShortName() == "Wdibc"
