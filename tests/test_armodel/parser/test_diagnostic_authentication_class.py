"""
Tests for reading the DIAGNOSTIC-AUTHENTICATION-CLASS element —
DiagnosticAuthenticationClass, Table 4.52 (p.99, R23-11).

DiagnosticAuthenticationClass (Base most-derived DiagnosticServiceClass)
defines no attributes of its own (Table 4.52 attribute row is "-") — the wire
element is an IDENTIFIABLE-only wrapper, AUTOSAR_00052.xsd complexType
DIAGNOSTIC-AUTHENTICATION-CLASS l.31963.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_authentication_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAuthenticationClass:
    """Tests for readDiagnosticAuthenticationClass — own element field values (Table 4.52)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticAuthenticationClass

        service_class = DiagnosticAuthenticationClass(parent=MagicMock(), short_name="AuthClass")
        element = _snip(inner, root_tag="DIAGNOSTIC-AUTHENTICATION-CLASS")
        parser.readDiagnosticAuthenticationClass(element, service_class)
        return service_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        service_class = self._read(parser, "<SHORT-NAME>AuthClass</SHORT-NAME>")
        assert service_class.getShortName() == "AuthClass"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the identifiable state empty."""
        service_class = self._read(parser, "")
        assert service_class.getShortName() == "AuthClass"
        assert service_class.getLongName() is None
