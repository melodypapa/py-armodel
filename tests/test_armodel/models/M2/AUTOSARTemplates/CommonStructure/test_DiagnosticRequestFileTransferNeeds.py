"""
This module contains tests for the DiagnosticRequestFileTransferNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
    DiagnosticRequestFileTransferNeeds,
)

SPEC_NOTE = "This meta-class indicates the existence of a service use case that involves UDS service 0x38, Request File Transfer."


class TestDiagnosticRequestFileTransferNeeds:
    def test_initialization(self):
        """Test that the concrete DiagnosticRequestFileTransferNeeds is a DiagnosticCapabilityElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticRequestFileTransferNeeds(ar_root, "TestDiagnosticRequestFileTransferNeeds")

        assert isinstance(needs, DiagnosticCapabilityElement)
        assert needs.getShortName() == "TestDiagnosticRequestFileTransferNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.43)"""
        assert DiagnosticRequestFileTransferNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticRequestFileTransferNeeds.__init__.__doc__ is None
