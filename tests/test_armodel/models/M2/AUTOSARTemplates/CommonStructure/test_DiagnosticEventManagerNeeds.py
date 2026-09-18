"""
This module contains tests for the DiagnosticEventManagerNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
    DiagnosticEventManagerNeeds,
)

SPEC_NOTE = "Specifies the general needs on the configuration of the Diagnostic Event Manager (Dem) which are not related to a particular item."


class TestDiagnosticEventManagerNeeds:
    def test_initialization(self):
        """Test that the concrete DiagnosticEventManagerNeeds is a DiagnosticCapabilityElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticEventManagerNeeds(ar_root, "TestDiagnosticEventManagerNeeds")

        assert isinstance(needs, DiagnosticCapabilityElement)
        assert needs.getShortName() == "TestDiagnosticEventManagerNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.14)"""
        assert DiagnosticEventManagerNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticEventManagerNeeds.__init__.__doc__ is None
