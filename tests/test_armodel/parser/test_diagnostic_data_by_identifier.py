"""
Tests for reading the DIAGNOSTIC-DATA-BY-IDENTIFIER XML group — DiagnosticDataByIdentifier, Table 4.73 (p.113, R23-11).

DiagnosticDataByIdentifier is an abstract base: its XML group
DIAGNOSTIC-DATA-BY-IDENTIFIER (AUTOSAR_00052.xsd l.34064) carries the single
optional DATA-IDENTIFIER-REF element (DEST
DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER--SUBTYPES-ENUM). The reusable
readDiagnosticDataByIdentifier helper is exercised through the concrete
subclass DiagnosticReadDataByIdentifier.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_data_by_identifier.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticDataByIdentifier:
    """Tests for readDiagnosticDataByIdentifier — own element field values (Table 4.73)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDataByIdentifier

        data_by_identifier = DiagnosticReadDataByIdentifier(parent=MagicMock(), short_name="ReadDataByIdentifier")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-DATA-BY-IDENTIFIER")
        parser.readDiagnosticDataByIdentifier(element, data_by_identifier)
        return data_by_identifier

    def test_read_data_identifier_ref(self, parser):
        """Test that the DATA-IDENTIFIER-REF is read with its DEST attribute."""
        inner = '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID</DATA-IDENTIFIER-REF>'
        data_by_identifier = self._read(parser, inner)
        assert data_by_identifier.getDataIdentifier() is not None
        assert data_by_identifier.getDataIdentifier().getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert data_by_identifier.getDataIdentifier().getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_read_absent_ref(self, parser):
        """Test that an absent DATA-IDENTIFIER-REF leaves the dataIdentifier field None."""
        data_by_identifier = self._read(parser, "")
        assert data_by_identifier.getDataIdentifier() is None

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving dataIdentifier unset."""
        data_by_identifier = self._read(parser, "<SHORT-NAME>ReadDataByIdentifier</SHORT-NAME>")
        assert data_by_identifier.getDataIdentifier() is None
