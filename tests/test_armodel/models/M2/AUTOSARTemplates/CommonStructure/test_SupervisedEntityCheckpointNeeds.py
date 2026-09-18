"""
This module contains tests for the SupervisedEntityCheckpointNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    SupervisedEntityCheckpointNeeds,
)

SPEC_NOTE = "Specifies the abstract needs on the configuration of the Watchdog Manager to support a Checkpoint for a Supervised Entity."


class TestSupervisedEntityCheckpointNeeds:
    def test_initialization(self):
        """Test that the concrete SupervisedEntityCheckpointNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityCheckpointNeeds(ar_root, "TestSupervisedEntityCheckpointNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestSupervisedEntityCheckpointNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.30)"""
        assert SupervisedEntityCheckpointNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert SupervisedEntityCheckpointNeeds.__init__.__doc__ is None
