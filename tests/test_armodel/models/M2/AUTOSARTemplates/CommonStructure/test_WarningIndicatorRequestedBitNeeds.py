"""
This module contains tests for the WarningIndicatorRequestedBitNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    WarningIndicatorRequestedBitNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to explicitly request the existence of the WarningIndicatorRequestedBit."


class TestWarningIndicatorRequestedBitNeeds:
    def test_initialization(self):
        """Test that the concrete WarningIndicatorRequestedBitNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = WarningIndicatorRequestedBitNeeds(ar_root, "TestWarningIndicatorRequestedBitNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestWarningIndicatorRequestedBitNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.61)"""
        assert WarningIndicatorRequestedBitNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert WarningIndicatorRequestedBitNeeds.__init__.__doc__ is None
