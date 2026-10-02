"""
Tests for writing DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE elements —
DiagnosticAuthTransmitCertificate, Table 4.58 (p.100, R23-11).

DiagnosticAuthTransmitCertificate (Base most-derived
DiagnosticAuthentication) owns one attribute: the 0..* aggregation
certificateEvaluation (DiagnosticAuthTransmitCertificateEvaluation), serialized
as a CERTIFICATE-EVALUATIONS wrapper holding an unbounded choice of
DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION elements, AUTOSAR_00052.xsd
group DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE l.31760 / complexType l.31781. It
inherits the 0..1 authenticationClass ref (AUTHENTICATION-CLASS-REF) from the
abstract DiagnosticAuthentication (Table 4.51). The writer delegates the
inherited field to the Rule 0001.7 helper writeDiagnosticAuthentication and the
dispatch entry is writeARPackageElement →
writeDiagnosticAuthTransmitCertificate.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_auth_transmit_certificate.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthTransmitCertificate
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticAuthTransmitCertificate:
    """Tests for writeDiagnosticAuthTransmitCertificate — own element field values (Table 4.58)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticAuthTransmitCertificate without content emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        package.createDiagnosticAuthTransmitCertificate("Certificate1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificate(parent, package.getReferrableElement("Certificate1", DiagnosticAuthTransmitCertificate))

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Certificate1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_authentication_class_ref(self):
        """Test that the inherited AUTHENTICATION-CLASS-REF is emitted with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        certificate.setAuthenticationClass(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificate(parent, certificate)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE")
        assert child is not None
        ref_element = child.find("AUTHENTICATION-CLASS-REF")
        assert ref_element is not None
        assert ref_element.text == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref_element.get("DEST") == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_write_certificate_evaluations(self):
        """Test that the CERTIFICATE-EVALUATIONS wrapper is emitted after the inherited group content."""
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")
        certificate.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")
        certificate.createDiagnosticAuthTransmitCertificateEvaluation("Eval2")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificate(parent, certificate)

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE")
        assert child is not None
        evaluations_element = child.find("CERTIFICATE-EVALUATIONS")
        assert evaluations_element is not None
        evaluation_elements = evaluations_element.findall("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION")
        assert [evaluation_element.find("SHORT-NAME").text for evaluation_element in evaluation_elements] == ["Eval1", "Eval2"]

    def test_write_no_wrapper_when_no_evaluations(self):
        """Test that no CERTIFICATE-EVALUATIONS wrapper is emitted when the aggregation is empty."""
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        package.createDiagnosticAuthTransmitCertificate("Certificate1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAuthTransmitCertificate(parent, package.getReferrableElement("Certificate1", DiagnosticAuthTransmitCertificate))

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE")
        assert child is not None
        assert child.find("CERTIFICATE-EVALUATIONS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticAuthTransmitCertificate to a DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE element."""
        package = AUTOSAR.getInstance().createARPackage("AuthTransmitCertificates")
        package.createDiagnosticAuthTransmitCertificate("Certificate1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Certificate1", DiagnosticAuthTransmitCertificate))

        child = parent.find("DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Certificate1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("AuthTransmitCertificates")
        certificate = package.createDiagnosticAuthTransmitCertificate("Certificate1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        certificate.setAuthenticationClass(ref)
        certificate.createDiagnosticAuthTransmitCertificateEvaluation("Eval1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            certificate_2 = package_2.getReferrableElement("Certificate1", DiagnosticAuthTransmitCertificate)
            assert certificate_2 is not None
            assert certificate_2.getShortName() == "Certificate1"
            ref_2 = certificate_2.getAuthenticationClass()
            assert ref_2 is not None
            assert ref_2.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
            assert ref_2.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"
            evaluations_2 = certificate_2.getCertificateEvaluations()
            assert [evaluation.getShortName() for evaluation in evaluations_2] == ["Eval1"]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
