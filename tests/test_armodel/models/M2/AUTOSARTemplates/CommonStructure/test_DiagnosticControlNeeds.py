"""
This module contains tests for the DiagnosticControlNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
    DiagnosticControlNeeds,
)

SPEC_NOTE = "This meta-class indicates a service use-case for reporting the controlled status by diagnostic services."


class TestDiagnosticControlNeeds:
    def test_initialization(self):
        """Test that the concrete DiagnosticControlNeeds is a DiagnosticCapabilityElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticControlNeeds(ar_root, "TestDiagnosticControlNeeds")

        assert isinstance(needs, DiagnosticCapabilityElement)
        assert needs.getShortName() == "TestDiagnosticControlNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.63)"""
        assert DiagnosticControlNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticControlNeeds.__init__.__doc__ is None
