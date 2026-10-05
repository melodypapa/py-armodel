"""
Tests for reading the DIAGNOSTIC-DATA-IDENTIFIER-SET element —
DiagnosticDataIdentifierSet, Table 4.178 (p.187, R23-11).

DiagnosticDataIdentifierSet (Base most-derived DiagnosticCommonElement) carries one
* ref attribute — dataIdentifier (ordered), read from the XSD wrapper
DATA-IDENTIFIER-REFS of DATA-IDENTIFIER-REF items (DEST
DIAGNOSTIC-DATA-IDENTIFIER--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-DATA-IDENTIFIER-SET, AUTOSAR_00052.xsd l.34388.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_data_identifier_set.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticDataIdentifierSet:
    """Tests for readDiagnosticDataIdentifierSet — own element field values (Table 4.178)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifierSet

        data_identifier_set = DiagnosticDataIdentifierSet(parent=MagicMock(), short_name="Set1")
        element = _snip(inner, root_tag="DIAGNOSTIC-DATA-IDENTIFIER-SET")
        parser.readDiagnosticDataIdentifierSet(element, data_identifier_set)
        return data_identifier_set

    def test_with_data_identifier_refs(self, parser):
        """Test that DATA-IDENTIFIER-REFS items are read in order with dest and value."""
        inner = (
            "<SHORT-NAME>Set1</SHORT-NAME>"
            "<DATA-IDENTIFIER-REFS>"
            '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/DID1</DATA-IDENTIFIER-REF>'
            '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDataIdentifiers/DID2</DATA-IDENTIFIER-REF>'
            "</DATA-IDENTIFIER-REFS>"
        )
        data_identifier_set = self._read(parser, inner)
        assert data_identifier_set.getShortName() == "Set1"
        refs = data_identifier_set.getDataIdentifierRefs()
        assert len(refs) == 2
        assert refs[0].getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1"
        assert refs[1].getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
        assert refs[1].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID2"

    def test_without_refs(self, parser):
        """Test that an absent DATA-IDENTIFIER-REFS wrapper leaves the list empty."""
        data_identifier_set = self._read(parser, "<SHORT-NAME>Set1</SHORT-NAME>")
        assert data_identifier_set.getDataIdentifierRefs() == []
