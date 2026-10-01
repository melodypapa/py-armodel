"""
Tests for reading the DIAGNOSTIC-VERIFY-CERTIFICATE-BIDIRECTIONAL element —
DiagnosticVerifyCertificateBidirectional, Table 4.54 (p.99, R23-11).

DiagnosticVerifyCertificateBidirectional (Base most-derived
DiagnosticAuthentication) defines no attributes of its own (Table 4.54
attribute row is "-") — it inherits the 0..1 authenticationClass ref
(AUTHENTICATION-CLASS-REF) from the abstract DiagnosticAuthentication
(Table 4.51); the wire element is an IDENTIFIABLE wrapper plus the inherited
group, AUTOSAR_00052.xsd complexType DIAGNOSTIC-VERIFY-CERTIFICATE-BIDIRECTIONAL
l.47114. The reader delegates the inherited field to the Rule 0001.7 helper
readDiagnosticAuthentication.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_verify_certificate_bidirectional.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticVerifyCertificateBidirectional:
    """Tests for readDiagnosticVerifyCertificateBidirectional — own element field values (Table 4.54)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticVerifyCertificateBidirectional

        verification = DiagnosticVerifyCertificateBidirectional(parent=MagicMock(), short_name="VerifyBidir")
        element = _snip(inner, root_tag="DIAGNOSTIC-VERIFY-CERTIFICATE-BIDIRECTIONAL")
        parser.readDiagnosticVerifyCertificateBidirectional(element, verification)
        return verification

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        verification = self._read(parser, "<SHORT-NAME>VerifyBidir</SHORT-NAME>")
        assert verification.getShortName() == "VerifyBidir"

    def test_read_authentication_class_ref(self, parser):
        """Test that the inherited AUTHENTICATION-CLASS-REF is read with field values."""
        verification = self._read(parser, '<AUTHENTICATION-CLASS-REF DEST="DIAGNOSTIC-AUTHENTICATION-CLASS">/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass</AUTHENTICATION-CLASS-REF>')
        ref = verification.getAuthenticationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the inherited ref unset."""
        verification = self._read(parser, "")
        assert verification.getShortName() == "VerifyBidir"
        assert verification.getAuthenticationClass() is None
