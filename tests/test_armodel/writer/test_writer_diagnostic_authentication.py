"""
Tests for writing the DIAGNOSTIC-AUTHENTICATION group —
DiagnosticAuthentication, Table 4.51 (p.99, R23-11).

DiagnosticAuthentication is abstract and has no ARPackage-level dispatch
(concrete subclasses own their XML tags); its group DIAGNOSTIC-AUTHENTICATION
carries AUTHENTICATION-CLASS-REF (DIAGNOSTIC-AUTHENTICATION-CLASS--SUBTYPES-ENUM)
— AUTOSAR_00052.xsd group DIAGNOSTIC-AUTHENTICATION l.43229. The removed
AUTHENTICATION-TIMEOUT (`atp.Status="removed"`) is not modeled (Rule 0015).
writeDiagnosticAuthentication is the Rule 0001.7 reusable helper that the
subclass writers call on their own typed SubElement.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_authentication.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAuthenticationConfiguration
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteDiagnosticAuthentication:
    """Tests for writeDiagnosticAuthentication — own group field values (Table 4.51)."""

    def _write(self, authentication):
        parent = ET.Element("DIAGNOSTIC-AUTHENTICATION-CONFIGURATION")
        ARXMLWriter().writeDiagnosticAuthentication(parent, authentication)
        return parent

    def test_write_authentication_class_ref(self):
        """Test that AUTHENTICATION-CLASS-REF is emitted with the spec values."""
        authentication = DiagnosticAuthenticationConfiguration(AUTOSAR.getInstance(), "Auth1")
        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTHENTICATION-CLASS")
        ref.setValue("/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass")
        authentication.setAuthenticationClass(ref)

        parent = self._write(authentication)
        ref_element = parent.find("AUTHENTICATION-CLASS-REF")
        assert ref_element is not None
        assert ref_element.text == "/AUTOSAR/DiagnosticAuthenticationClasses/AuthClass"
        assert ref_element.get("DEST") == "DIAGNOSTIC-AUTHENTICATION-CLASS"

    def test_write_unset_ref_omits_tag(self):
        """Test that an unset authenticationClass emits no element."""
        authentication = DiagnosticAuthenticationConfiguration(AUTOSAR.getInstance(), "Auth1")

        parent = self._write(authentication)
        assert parent.find("AUTHENTICATION-CLASS-REF") is None
        assert len(parent) == 0
