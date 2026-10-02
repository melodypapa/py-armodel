"""
Tests for reading the DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER element —
DiagnosticDynamicallyDefineDataIdentifier, Table 4.93 (p.127, R23-11).

DiagnosticDynamicallyDefineDataIdentifier (concrete ARElement, Aggregated by
ARPackage.element) defines three 0..1 attributes: dataIdentifier (ref, DEST
DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER--SUBTYPES-ENUM, DATA-IDENTIFIER-REF),
dynamicallyDefineDataIdentifierClass (ref, DEST
DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS--SUBTYPES-ENUM,
DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF) and maxSourceElement
(PositiveInteger, MAX-SOURCE-ELEMENT) — AUTOSAR_00052.xsd group
DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER l.35133.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_dynamically_define_data_identifier.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticDynamicallyDefineDataIdentifier:
    """Tests for readDiagnosticDynamicallyDefineDataIdentifier — own element field values (Table 4.93)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDynamicallyDefineDataIdentifier

        dddi = DiagnosticDynamicallyDefineDataIdentifier(parent=MagicMock(), short_name="Dddi1")
        element = _snip(inner, root_tag="DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER")
        parser.readDiagnosticDynamicallyDefineDataIdentifier(element, dddi)
        return dddi

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        dddi = self._read(parser, "<SHORT-NAME>Dddi1</SHORT-NAME>")
        assert dddi.getShortName() == "Dddi1"

    def test_read_data_identifier_ref(self, parser):
        """Test that the DATA-IDENTIFIER-REF is read with its DEST attribute."""
        inner = '<DATA-IDENTIFIER-REF DEST="DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER">/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1</DATA-IDENTIFIER-REF>'
        dddi = self._read(parser, inner)
        assert dddi.getDataIdentifier() is not None
        assert dddi.getDataIdentifier().getValue() == "/AUTOSAR/DiagnosticDynamicDataIdentifiers/Did1"
        assert dddi.getDataIdentifier().getDest() == "DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER"

    def test_read_dynamically_define_data_identifier_class_ref(self, parser):
        """Test that the DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF is read with its DEST attribute."""
        inner = '<DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF DEST="DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS">/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1</DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS-REF>'
        dddi = self._read(parser, inner)
        assert dddi.getDynamicallyDefineDataIdentifierClass() is not None
        assert dddi.getDynamicallyDefineDataIdentifierClass().getValue() == "/AUTOSAR/DiagnosticDynamicallyDefineDataIdentifiers/Class1"
        assert dddi.getDynamicallyDefineDataIdentifierClass().getDest() == "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS"

    def test_read_max_source_element(self, parser):
        """Test that the MAX-SOURCE-ELEMENT is read into maxSourceElement."""
        dddi = self._read(parser, "<MAX-SOURCE-ELEMENT>9</MAX-SOURCE-ELEMENT>")
        assert dddi.getMaxSourceElement() is not None
        assert dddi.getMaxSourceElement().getValue() == 9

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        dddi = self._read(parser, "<SHORT-NAME>Dddi1</SHORT-NAME>")
        assert dddi.getDataIdentifier() is None
        assert dddi.getDynamicallyDefineDataIdentifierClass() is None
        assert dddi.getMaxSourceElement() is None
