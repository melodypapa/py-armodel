"""
Tests for reading the DIAGNOSTIC-SECURITY-ACCESS-CLASS element —
DiagnosticSecurityAccessClass, Table 4.50 (p.96, R23-11).

DiagnosticSecurityAccessClass (Base most-derived DiagnosticServiceClass, stamped
abstract in the chain) defines no attributes of its own (Table 4.50 attribute
row is "-"; the XSD group DIAGNOSTIC-SECURITY-ACCESS-CLASS carries only the
AP-restricted SHARED-TIMER, out of CP scope) — the wire element is an
IDENTIFIABLE-only wrapper, AUTOSAR_00052.xsd complexType
DIAGNOSTIC-SECURITY-ACCESS-CLASS l.43331.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_security_access_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticSecurityAccessClass:
    """Tests for readDiagnosticSecurityAccessClass — own element field values (Table 4.50)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticSecurityAccessClass

        service_class = DiagnosticSecurityAccessClass(parent=MagicMock(), short_name="SecAccessClass")
        element = _snip(inner, root_tag="DIAGNOSTIC-SECURITY-ACCESS-CLASS")
        parser.readDiagnosticSecurityAccessClass(element, service_class)
        return service_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        service_class = self._read(parser, "<SHORT-NAME>SecAccessClass</SHORT-NAME>")
        assert service_class.getShortName() == "SecAccessClass"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the identifiable state empty."""
        service_class = self._read(parser, "")
        assert service_class.getShortName() == "SecAccessClass"
        assert service_class.getLongName() is None
