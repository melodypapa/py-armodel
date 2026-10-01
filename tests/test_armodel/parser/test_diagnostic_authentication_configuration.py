"""
Tests for reading the DIAGNOSTIC-AUTHENTICATION-CONFIGURATION element —
DiagnosticAuthenticationConfiguration, Table 4.53 (p.99, R23-11).

DiagnosticAuthenticationConfiguration (Base most-derived DiagnosticAuthentication)
defines no attributes of its own (Table 4.53 attribute row is "-") — it inherits
the 0..1 authenticationClass ref (AUTHENTICATION-CLASS-REF) from the abstract
DiagnosticAuthentication (Table 4.51); the wire element is an
IDENTIFIABLE wrapper plus the inherited group, AUTOSAR_00052.xsd complexType
DIAGNOSTIC-AUTHENTICATION-CONFIGURATION l.31999. The reader delegates the
inherited field to the Rule 0001.7 helper readDiagnosticAuthentication.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_authentication_configuration.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAuthenticationConfiguration:
    """Tests for readDiagnosticAuthenticationConfiguration — own element field values (Table 4.53)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthenticationConfiguration

        configuration = DiagnosticAuthenticationConfiguration(parent=MagicMock(), short_name="AuthCfg")
        element = _snip(inner, root_tag="DIAGNOSTIC-AUTHENTICATION-CONFIGURATION")
        parser.readDiagnosticAuthenticationConfiguration(element, configuration)
        return configuration

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        configuration = self._read(parser, "<SHORT-NAME>AuthCfg</SHORT-NAME>")
        assert configuration.getShortName() == "AuthCfg"

    def test_read_authentication_class_ref(self, parser):
        """Test that the inherited AUTHENTICATION-CLASS-REF is read with field values."""
        configuration = self._read(parser, '<AUTHENTICATION-CLASS-REF DEST="DIAGNOSTIC-AUTHENTICATION-CLASS">/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass</AUTHENTICATION-CLASS-REF>')
        ref = configuration.getAuthenticationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the inherited ref unset."""
        configuration = self._read(parser, "")
        assert configuration.getShortName() == "AuthCfg"
        assert configuration.getAuthenticationClass() is None
