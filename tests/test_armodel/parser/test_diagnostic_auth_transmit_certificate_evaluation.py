"""
Tests for reading the DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION element —
DiagnosticAuthTransmitCertificateEvaluation, Table 4.59 (p.101, R23-11).

DiagnosticAuthTransmitCertificateEvaluation (Base most-derived Identifiable,
stamped) defines two 0..1 attributes: evaluationId (PositiveInteger,
EVALUATION-ID) and function (String, FUNCTION) — AUTOSAR_00052.xsd group
DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION l.31804 / complexType l.31826.
It is not an ARPackage element: it is aggregated by
DiagnosticAuthTransmitCertificate.certificateEvaluation (Table 4.58), so the
reader is dispatched from readDiagnosticAuthTransmitCertificate over the
CERTIFICATE-EVALUATIONS wrapper.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_auth_transmit_certificate_evaluation.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAuthTransmitCertificateEvaluation:
    """Tests for readDiagnosticAuthTransmitCertificateEvaluation — own element field values (Table 4.59)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticAuthTransmitCertificateEvaluation

        evaluation = DiagnosticAuthTransmitCertificateEvaluation(parent=MagicMock(), short_name="Eval1")
        element = _snip(inner, root_tag="DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION")
        parser.readDiagnosticAuthTransmitCertificateEvaluation(element, evaluation)
        return evaluation

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        evaluation = self._read(parser, "<SHORT-NAME>Eval1</SHORT-NAME>")
        assert evaluation.getShortName() == "Eval1"

    def test_read_evaluation_id(self, parser):
        """Test that EVALUATION-ID is read with the field value."""
        evaluation = self._read(parser, "<EVALUATION-ID>2</EVALUATION-ID>")
        assert evaluation.getEvaluationId() is not None
        assert evaluation.getEvaluationId().getValue() == 2

    def test_read_function(self, parser):
        """Test that FUNCTION is read with the field value."""
        evaluation = self._read(parser, "<FUNCTION>FUNCTION_SECURE_CODING</FUNCTION>")
        assert evaluation.getFunction() is not None
        assert evaluation.getFunction().getValue() == "FUNCTION_SECURE_CODING"

    def test_read_both_fields(self, parser):
        """Test that both attributes are read in XSD order (EVALUATION-ID before FUNCTION)."""
        evaluation = self._read(parser, "<EVALUATION-ID>1</EVALUATION-ID><FUNCTION>FUNCTION_SECURE_CODING</FUNCTION>")
        assert evaluation.getEvaluationId().getValue() == 1
        assert evaluation.getFunction().getValue() == "FUNCTION_SECURE_CODING"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving both attributes unset."""
        evaluation = self._read(parser, "<SHORT-NAME>Eval1</SHORT-NAME>")
        assert evaluation.getEvaluationId() is None
        assert evaluation.getFunction() is None
