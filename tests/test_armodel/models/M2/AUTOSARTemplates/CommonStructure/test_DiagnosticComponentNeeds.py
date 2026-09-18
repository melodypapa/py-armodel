"""
This module contains tests for the DiagnosticComponentNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
    DiagnosticComponentNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to specify the service needs for the configuration of component events."


class TestDiagnosticComponentNeeds:
    def test_initialization(self):
        """Test that the concrete DiagnosticComponentNeeds is a DiagnosticCapabilityElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticComponentNeeds(ar_root, "TestDiagnosticComponentNeeds")

        assert isinstance(needs, DiagnosticCapabilityElement)
        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestDiagnosticComponentNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.64)"""
        assert DiagnosticComponentNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticComponentNeeds.__init__.__doc__ is None
