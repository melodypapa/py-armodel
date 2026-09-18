"""
This module contains tests for the V2xFacUserNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    V2xFacUserNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to define service needs for V2x facilities."


class TestV2xFacUserNeeds:
    def test_initialization(self):
        """Test that the concrete V2xFacUserNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = V2xFacUserNeeds(ar_root, "TestV2xFacUserNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestV2xFacUserNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.77)"""
        assert V2xFacUserNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert V2xFacUserNeeds.__init__.__doc__ is None
