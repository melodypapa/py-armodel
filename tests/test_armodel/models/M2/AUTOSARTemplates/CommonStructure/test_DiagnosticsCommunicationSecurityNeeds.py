"""
This module contains tests for the DiagnosticsCommunicationSecurityNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
    DiagnosticsCommunicationSecurityNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class represents the needs of a software-component to verify the access to security level via diagnostic services."


class TestDiagnosticsCommunicationSecurityNeeds:
    def test_initialization(self):
        """Test that the concrete DiagnosticsCommunicationSecurityNeeds is a DiagnosticCapabilityElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticsCommunicationSecurityNeeds(ar_root, "TestDiagnosticsCommunicationSecurityNeeds")

        assert isinstance(needs, DiagnosticCapabilityElement)
        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestDiagnosticsCommunicationSecurityNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.27)"""
        assert DiagnosticsCommunicationSecurityNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticsCommunicationSecurityNeeds.__init__.__doc__ is None
