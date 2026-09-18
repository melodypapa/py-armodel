"""
This module contains tests for the IdsMgrCustomTimestampNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    IdsMgrCustomTimestampNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class is used to indicate that the enclosing SwcServiceDependency represents a service use case for the retrieval of a custom timestamp by the Intrusion Detection System Manager. Tags: atp.Status=draft"


class TestIdsMgrCustomTimestampNeeds:
    def test_initialization(self):
        """Test that the concrete IdsMgrCustomTimestampNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = IdsMgrCustomTimestampNeeds(ar_root, "TestIdsMgrCustomTimestampNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestIdsMgrCustomTimestampNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.82)"""
        assert IdsMgrCustomTimestampNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert IdsMgrCustomTimestampNeeds.__init__.__doc__ is None
