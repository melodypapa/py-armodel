"""
Tests for reading the DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE element —
DiagnosticAuthTransmitCertificate, Table 4.58 (p.100, R23-11).

DiagnosticAuthTransmitCertificate (Base most-derived
DiagnosticAuthentication) owns one attribute: the 0..* aggregation
certificateEvaluation (DiagnosticAuthTransmitCertificateEvaluation), serialized
as a CERTIFICATE-EVALUATIONS wrapper holding an unbounded choice of
DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION elements, AUTOSAR_00052.xsd
group DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE l.31760 / complexType l.31781. It
inherits the 0..1 authenticationClass ref (AUTHENTICATION-CLASS-REF) from the
abstract DiagnosticAuthentication (Table 4.51). The reader delegates the
inherited field to the Rule 0001.7 helper readDiagnosticAuthentication and
creates each wrapper child through the create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_auth_transmit_certificate.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAuthTransmitCertificate:
    """Tests for readDiagnosticAuthTransmitCertificate — own element field values (Table 4.58)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthTransmitCertificate

        certificate = DiagnosticAuthTransmitCertificate(parent=MagicMock(), short_name="Certificate")
        element = _snip(inner, root_tag="DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE")
        parser.readDiagnosticAuthTransmitCertificate(element, certificate)
        return certificate

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        certificate = self._read(parser, "<SHORT-NAME>Certificate</SHORT-NAME>")
        assert certificate.getShortName() == "Certificate"

    def test_read_authentication_class_ref(self, parser):
        """Test that the inherited AUTHENTICATION-CLASS-REF is read with field values."""
        certificate = self._read(parser, '<AUTHENTICATION-CLASS-REF DEST="DIAGNOSTIC-AUTHENTICATION-CLASS">/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass</AUTHENTICATION-CLASS-REF>')
        ref = certificate.getAuthenticationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_read_certificate_evaluations(self, parser):
        """Test that the CERTIFICATE-EVALUATIONS wrapper children are created with their short names."""
        certificate = self._read(
            parser,
            """
            <CERTIFICATE-EVALUATIONS>
                <DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION>
                    <SHORT-NAME>Eval1</SHORT-NAME>
                </DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION>
                <DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION>
                    <SHORT-NAME>Eval2</SHORT-NAME>
                </DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION>
            </CERTIFICATE-EVALUATIONS>
        """,
        )
        evaluations = certificate.getCertificateEvaluations()
        assert [evaluation.getShortName() for evaluation in evaluations] == ["Eval1", "Eval2"]

    def test_read_empty_certificate_evaluations_wrapper(self, parser):
        """Test that an empty CERTIFICATE-EVALUATIONS wrapper (no children) parses to no evaluations."""
        certificate = self._read(parser, "<CERTIFICATE-EVALUATIONS></CERTIFICATE-EVALUATIONS>")
        assert certificate.getCertificateEvaluations() == []

    def test_read_no_wrapper(self, parser):
        """Test that a missing CERTIFICATE-EVALUATIONS wrapper parses leaving the aggregation unset."""
        certificate = self._read(parser, "<SHORT-NAME>Certificate</SHORT-NAME>")
        assert certificate.getCertificateEvaluations() == []

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the inherited ref unset."""
        certificate = self._read(parser, "")
        assert certificate.getShortName() == "Certificate"
        assert certificate.getAuthenticationClass() is None
