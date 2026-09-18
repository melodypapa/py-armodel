"""
This module contains tests for the V2xMUserNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    V2xMUserNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to express service needs for the V2x management."


class TestV2xMUserNeeds:
    def test_initialization(self):
        """Test that the concrete V2xMUserNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = V2xMUserNeeds(ar_root, "TestV2xMUserNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestV2xMUserNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.78)"""
        assert V2xMUserNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert V2xMUserNeeds.__init__.__doc__ is None
