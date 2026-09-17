"""
This module contains tests for the GlobalSupervisionNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    GlobalSupervisionNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "Specifies the abstract needs on the configuration of the Watchdog Manager to get access on the Global Supervision control and status interface."


class TestGlobalSupervisionNeeds:
    def test_initialization(self):
        """Test that the concrete GlobalSupervisionNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = GlobalSupervisionNeeds(ar_root, "TestGlobalSupervisionNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestGlobalSupervisionNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.4)"""
        assert GlobalSupervisionNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert GlobalSupervisionNeeds.__init__.__doc__ is None
