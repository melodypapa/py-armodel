"""
Tests for reading the DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER XML group — DiagnosticAbstractDataIdentifier, Table 4.4 (p.34, R23-11).

DiagnosticAbstractDataIdentifier is an abstract base: its XML group
DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER (AUTOSAR_00052.xsd l.31403) carries the single
optional ID element whose XSD type is POSITIVE-INTEGER-VALUE-VARIATION-POINT
(attribute-value variation of the atpVariation-stereotyped id attribute). The
reusable readDiagnosticAbstractDataIdentifier helper is exercised through the
concrete subclass DiagnosticDataIdentifier.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_abstract_data_identifier.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAbstractDataIdentifier:
    """Tests for readDiagnosticAbstractDataIdentifier — own element field values (Table 4.4)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier

        did = DiagnosticDataIdentifier(parent=MagicMock(), short_name="Di")
        element = _snip(inner, root_tag="DIAGNOSTIC-DATA-IDENTIFIER")
        parser.readDiagnosticAbstractDataIdentifier(element, did)
        return did

    def test_with_id(self, parser):
        """Test that the ID element is read through the POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper."""
        did = self._read(
            parser,
            "<SHORT-NAME>Di</SHORT-NAME>" "<ID><POSITIVE-INTEGER-VALUE-VARIATION-POINT>4</POSITIVE-INTEGER-VALUE-VARIATION-POINT></ID>",
        )
        assert did.getShortName() == "Di"
        assert did.getId() is not None
        assert did.getId().getValue() == 4

    def test_without_id(self, parser):
        """Test that an absent ID element leaves the id field None."""
        did = self._read(parser, "<SHORT-NAME>Di</SHORT-NAME>")
        assert did.getId() is None

    def test_with_empty_id_wrapper(self, parser):
        """Test that an ID element without a variation point child leaves the id field None."""
        did = self._read(
            parser,
            "<SHORT-NAME>Di</SHORT-NAME>" "<ID></ID>",
        )
        assert did.getId() is None
