"""
Tests for writing DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION elements —
DiagnosticAuthTransmitCertificateEvaluation, Table 4.59 (p.101, R23-11).

DiagnosticAuthTransmitCertificateEvaluation (Base most-derived Identifiable,
stamped) defines two 0..1 attributes: evaluationId (PositiveInteger,
EVALUATION-ID) and function (String, FUNCTION) — AUTOSAR_00052.xsd group
DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION l.31804 / complexType l.31826.
It is not an ARPackage element: it is aggregated by
DiagnosticAuthTransmitCertificate.certificateEvaluation (Table 4.58), so the
writer is dispatched from writeDiagnosticAuthTransmitCertificate over the
CERTIFICATE-EVALUATIONS wrapper.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_auth_transmit_certificate_evaluation.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthTransmitCertificate
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_evaluation(short_name: str = "Eval1"):
    package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
    certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")
    return certificate.createDiagnosticAuthTransmitCertificateEvaluation(short_name)


class TestWriteDiagnosticAuthTransmitCertificateEvaluation:
    """Tests for writeDiagnosticAuthTransmitCertificateEvaluation — own element field values (Table 4.59)."""

    def test_write_empty_wrapper(self):
        """Test that an evaluation without attributes emits only the IDENTIFIABLE wrapper content."""
        evaluation = _make_evaluation()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificateEvaluation(parent, evaluation)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Eval1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_evaluation_id(self):
        """Test that EVALUATION-ID is emitted with the spec value."""
        evaluation = _make_evaluation()
        evaluation_id = PositiveInteger()
        evaluation_id.setValue("2")
        evaluation.setEvaluationId(evaluation_id)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificateEvaluation(parent, evaluation)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION")
        assert child is not None
        evaluation_id_element = child.find("EVALUATION-ID")
        assert evaluation_id_element is not None
        assert evaluation_id_element.text == "2"

    def test_write_function(self):
        """Test that FUNCTION is emitted with the spec value."""
        evaluation = _make_evaluation()
        function = String()
        function.setValue("FUNCTION_SECURE_CODING")
        evaluation.setFunction(function)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificateEvaluation(parent, evaluation)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION")
        assert child is not None
        function_element = child.find("FUNCTION")
        assert function_element is not None
        assert function_element.text == "FUNCTION_SECURE_CODING"

    def test_write_field_order(self):
        """Test that both attributes are emitted in XSD order (EVALUATION-ID before FUNCTION)."""
        evaluation = _make_evaluation()
        evaluation_id = PositiveInteger()
        evaluation_id.setValue("1")
        evaluation.setEvaluationId(evaluation_id)
        function = String()
        function.setValue("FUNCTION_SECURE_CODING")
        evaluation.setFunction(function)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificateEvaluation(parent, evaluation)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION")
        assert child is not None
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["EVALUATION-ID", "FUNCTION"]

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle nested in a DiagnosticAuthTransmitCertificate."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("AuthTransmitCertificates")
        certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")
        evaluation = certificate.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")
        evaluation_id = PositiveInteger()
        evaluation_id.setValue("3")
        evaluation.setEvaluationId(evaluation_id)
        function = String()
        function.setValue("FUNCTION_SECURE_CODING")
        evaluation.setFunction(function)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            certificate_2 = package_2.getElement("Certificate1", DiagnosticAuthTransmitCertificate)
            evaluations_2 = certificate_2.getCertificateEvaluations()
            assert [item.getShortName() for item in evaluations_2] == ["Eval1"]
            evaluation_2 = evaluations_2[0]
            assert evaluation_2.getEvaluationId() is not None
            assert evaluation_2.getEvaluationId().getValue() == 3
            assert evaluation_2.getFunction() is not None
            assert evaluation_2.getFunction().getValue() == "FUNCTION_SECURE_CODING"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
