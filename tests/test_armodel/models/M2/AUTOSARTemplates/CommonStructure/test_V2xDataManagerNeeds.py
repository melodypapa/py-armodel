"""
This module contains tests for the V2xDataManagerNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    V2xDataManagerNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to define service needs for V2x Data Manager."


class TestV2xDataManagerNeeds:
    def test_initialization(self):
        """Test that the concrete V2xDataManagerNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = V2xDataManagerNeeds(ar_root, "TestV2xDataManagerNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestV2xDataManagerNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.79)"""
        assert V2xDataManagerNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert V2xDataManagerNeeds.__init__.__doc__ is None
