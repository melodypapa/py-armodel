"""
Tests for reading the DIAGNOSTIC-AUTHENTICATION group —
DiagnosticAuthentication, Table 4.51 (p.99, R23-11).

DiagnosticAuthentication is abstract and has no ARPackage-level dispatch
(concrete subclasses own their XML tags); its group DIAGNOSTIC-AUTHENTICATION
carries AUTHENTICATION-CLASS-REF (DIAGNOSTIC-AUTHENTICATION-CLASS--SUBTYPES-ENUM)
— AUTOSAR_00052.xsd group DIAGNOSTIC-AUTHENTICATION l.43229. The removed
AUTHENTICATION-TIMEOUT (`atp.Status="removed"`) is not modeled (Rule 0015).
readDiagnosticAuthentication is the Rule 0001.7 reusable helper that the
subclass readers call after their own readIdentifiable.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_authentication.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthenticationConfiguration
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticAuthentication:
    """Tests for readDiagnosticAuthentication — own group field values (Table 4.51)."""

    def _read(self, parser, inner):
        authentication = DiagnosticAuthenticationConfiguration(AUTOSAR.getInstance(), "Auth1")
        element = _snip(inner, root_tag="DIAGNOSTIC-AUTHENTICATION-CONFIGURATION")
        parser.readDiagnosticAuthentication(element, authentication)
        return authentication

    def test_read_authentication_class_ref(self, parser):
        """Test that AUTHENTICATION-CLASS-REF is read with field values."""
        authentication = self._read(parser, '<AUTHENTICATION-CLASS-REF DEST="DIAGNOSTIC-AUTHENTICATION-CLASS">/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass</AUTHENTICATION-CLASS-REF>')
        ref = authentication.getAuthenticationClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref.getDest() == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_read_empty(self, parser):
        """Test that an absent AUTHENTICATION-CLASS-REF leaves the field None."""
        authentication = self._read(parser, "")
        assert authentication.getAuthenticationClass() is None
