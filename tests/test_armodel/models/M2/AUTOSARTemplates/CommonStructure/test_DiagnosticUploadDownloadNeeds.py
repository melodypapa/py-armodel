"""
This module contains tests for the DiagnosticUploadDownloadNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
    DiagnosticUploadDownloadNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to specify needs regarding upload and download by means of diagnostic services."


class TestDiagnosticUploadDownloadNeeds:
    def test_initialization(self):
        """Test that the concrete DiagnosticUploadDownloadNeeds is a DiagnosticCapabilityElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticUploadDownloadNeeds(ar_root, "TestDiagnosticUploadDownloadNeeds")

        assert isinstance(needs, DiagnosticCapabilityElement)
        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestDiagnosticUploadDownloadNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.29)"""
        assert DiagnosticUploadDownloadNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticUploadDownloadNeeds.__init__.__doc__ is None
