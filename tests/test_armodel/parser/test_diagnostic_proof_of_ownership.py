"""
Tests for reading the DIAGNOSTIC-PROOF-OF-OWNERSHIP element —
DiagnosticProofOfOwnership, Table 4.57 (p.100, R23-11).

DiagnosticProofOfOwnership (Base most-derived
DiagnosticAuthentication) defines no attributes of its own (Table 4.57
attribute row is "-") — it inherits the 0..1 authenticationClass ref
(AUTHENTICATION-CLASS-REF) from the abstract DiagnosticAuthentication
(Table 4.51); the wire element is an IDENTIFIABLE wrapper plus the inherited
group, AUTOSAR_00052.xsd complexType DIAGNOSTIC-PROOF-OF-OWNERSHIP
l.40987. The reader delegates the inherited field to the Rule 0001.7 helper
readDiagnosticAuthentication.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_proof_of_ownership.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticProofOfOwnership:
    """Tests for readDiagnosticProofOfOwnership — own element field values (Table 4.57)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticProofOfOwnership

        proof_of_ownership = DiagnosticProofOfOwnership(parent=MagicMock(), short_name="ProofOfOwnership")
        element = _snip(inner, root_tag="DIAGNOSTIC-PROOF-OF-OWNERSHIP")
        parser.readDiagnosticProofOfOwnership(element, proof_of_ownership)
        return proof_of_ownership

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        proof_of_ownership = self._read(parser, "<SHORT-NAME>ProofOfOwnership</SHORT-NAME>")
        assert proof_of_ownership.getShortName() == "ProofOfOwnership"

    def test_read_authentication_class_ref(self, parser):
        """Test that the inherited AUTHENTICATION-CLASS-REF is read with field values."""
        proof_of_ownership = self._read(parser, '<AUTHENTICATION-CLASS-REF DEST="DIAGNOSTIC-AUTHENTICATION-CLASS">/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass</AUTHENTICATION-CLASS-REF>')
        ref = proof_of_ownership.getAuthenticationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the inherited ref unset."""
        proof_of_ownership = self._read(parser, "")
        assert proof_of_ownership.getShortName() == "ProofOfOwnership"
        assert proof_of_ownership.getAuthenticationClass() is None
