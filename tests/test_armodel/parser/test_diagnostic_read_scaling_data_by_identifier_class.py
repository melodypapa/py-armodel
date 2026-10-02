"""
Tests for reading the DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS element —
DiagnosticReadScalingDataByIdentifierClass, Table 4.79 (p.116, R23-11).

DiagnosticReadScalingDataByIdentifierClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes —
AUTOSAR_00052.xsd group DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS
l.41566 is an empty sequence. The reader therefore only reads the IDENTIFIABLE
wrapper. The dispatch entry is readARPackageElements →
readDiagnosticReadScalingDataByIdentifierClass via the ARPackage create
factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_scaling_data_by_identifier_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadScalingDataByIdentifierClass:
    """Tests for readDiagnosticReadScalingDataByIdentifierClass — own element field values (Table 4.79)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadScalingDataByIdentifierClass

        read_scaling_data_by_identifier_class = DiagnosticReadScalingDataByIdentifierClass(parent=parser, short_name="Rsdibc")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS")
        parser.readDiagnosticReadScalingDataByIdentifierClass(element, read_scaling_data_by_identifier_class)
        return read_scaling_data_by_identifier_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        read_scaling_data_by_identifier_class = self._read(parser, "<SHORT-NAME>Rsdibc</SHORT-NAME>")
        assert read_scaling_data_by_identifier_class.getShortName() == "Rsdibc"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the class unchanged."""
        read_scaling_data_by_identifier_class = self._read(parser, "<SHORT-NAME>Rsdibc</SHORT-NAME>")
        assert read_scaling_data_by_identifier_class.getShortName() == "Rsdibc"
