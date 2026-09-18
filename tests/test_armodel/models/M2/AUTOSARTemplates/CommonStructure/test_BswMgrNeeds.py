"""
This module contains tests for the BswMgrNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    BswMgrNeeds,
    ServiceNeeds,
)

SPEC_NOTE = 'Specifies the abstract needs on the configuration of the Basic Software Manager for one "user".'


class TestBswMgrNeeds:
    def test_initialization(self):
        """Test that the concrete BswMgrNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = BswMgrNeeds(ar_root, "TestBswMgrNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestBswMgrNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.8)"""
        assert BswMgrNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert BswMgrNeeds.__init__.__doc__ is None
