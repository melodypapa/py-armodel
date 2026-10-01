"""
Tests for reading the DIAGNOSTIC-DE-AUTHENTICATION element —
DiagnosticDeAuthentication, Table 4.56 (p.100, R23-11).

DiagnosticDeAuthentication (Base most-derived
DiagnosticAuthentication) defines no attributes of its own (Table 4.56
attribute row is "-") — it inherits the 0..1 authenticationClass ref
(AUTHENTICATION-CLASS-REF) from the abstract DiagnosticAuthentication
(Table 4.51); the wire element is an IDENTIFIABLE wrapper plus the inherited
group, AUTOSAR_00052.xsd complexType DIAGNOSTIC-DE-AUTHENTICATION
l.34659. The reader delegates the inherited field to the Rule 0001.7 helper
readDiagnosticAuthentication.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_de_authentication.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticDeAuthentication:
    """Tests for readDiagnosticDeAuthentication — own element field values (Table 4.56)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDeAuthentication

        de_authentication = DiagnosticDeAuthentication(parent=MagicMock(), short_name="DeAuth")
        element = _snip(inner, root_tag="DIAGNOSTIC-DE-AUTHENTICATION")
        parser.readDiagnosticDeAuthentication(element, de_authentication)
        return de_authentication

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        de_authentication = self._read(parser, "<SHORT-NAME>DeAuth</SHORT-NAME>")
        assert de_authentication.getShortName() == "DeAuth"

    def test_read_authentication_class_ref(self, parser):
        """Test that the inherited AUTHENTICATION-CLASS-REF is read with field values."""
        de_authentication = self._read(parser, '<AUTHENTICATION-CLASS-REF DEST="DIAGNOSTIC-AUTHENTICATION-CLASS">/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass</AUTHENTICATION-CLASS-REF>')
        ref = de_authentication.getAuthenticationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the inherited ref unset."""
        de_authentication = self._read(parser, "")
        assert de_authentication.getShortName() == "DeAuth"
        assert de_authentication.getAuthenticationClass() is None
