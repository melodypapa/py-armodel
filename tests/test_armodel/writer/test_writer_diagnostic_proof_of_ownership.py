"""
Tests for writing DIAGNOSTIC-PROOF-OF-OWNERSHIP elements —
DiagnosticProofOfOwnership, Table 4.57 (p.100, R23-11).

DiagnosticProofOfOwnership (Base most-derived
DiagnosticAuthentication) defines no attributes of its own (Table 4.57
attribute row is "-") — it inherits the 0..1 authenticationClass ref
(AUTHENTICATION-CLASS-REF) from the abstract DiagnosticAuthentication
(Table 4.51); the wire element is an IDENTIFIABLE wrapper plus the inherited
group, AUTOSAR_00052.xsd complexType DIAGNOSTIC-PROOF-OF-OWNERSHIP
l.40987. The writer delegates the inherited field to the Rule 0001.7 helper
writeDiagnosticAuthentication and the dispatch entry is
writeARPackageElement → writeDiagnosticProofOfOwnership.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_proof_of_ownership.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticProofOfOwnership
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


class TestWriteDiagnosticProofOfOwnership:
    """Tests for writeDiagnosticProofOfOwnership — own element field values (Table 4.57)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticProofOfOwnership without refs emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("ProofOfOwnerships")
        package.createDiagnosticProofOfOwnership("Proof1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticProofOfOwnership(parent, package.getElement("Proof1", DiagnosticProofOfOwnership))

        child = parent.find("DIAGNOSTIC-PROOF-OF-OWNERSHIP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Proof1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_authentication_class_ref(self):
        """Test that the inherited AUTHENTICATION-CLASS-REF is emitted with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("ProofOfOwnerships")
        proof_of_ownership = package.createDiagnosticProofOfOwnership("Proof1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        proof_of_ownership.setAuthenticationClass(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticProofOfOwnership(parent, proof_of_ownership)

        child = parent.find("DIAGNOSTIC-PROOF-OF-OWNERSHIP")
        assert child is not None
        ref_element = child.find("AUTHENTICATION-CLASS-REF")
        assert ref_element is not None
        assert ref_element.text == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref_element.get("DEST") == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticProofOfOwnership to a DIAGNOSTIC-PROOF-OF-OWNERSHIP element."""
        package = AUTOSAR.getInstance().createARPackage("ProofOfOwnerships")
        package.createDiagnosticProofOfOwnership("Proof1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Proof1", DiagnosticProofOfOwnership))

        child = parent.find("DIAGNOSTIC-PROOF-OF-OWNERSHIP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Proof1"

    def test_round_trip(self):
        """Test the full create → save → reload → assert cycle over an ARPackage."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ProofOfOwnerships")
        proof_of_ownership = package.createDiagnosticProofOfOwnership("Proof1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        proof_of_ownership.setAuthenticationClass(ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            proof_of_ownership_2 = package_2.getElement("Proof1", DiagnosticProofOfOwnership)
            assert proof_of_ownership_2 is not None
            assert proof_of_ownership_2.getShortName() == "Proof1"
            ref_2 = proof_of_ownership_2.getAuthenticationClass()
            assert ref_2 is not None
            assert ref_2.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
            assert ref_2.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
