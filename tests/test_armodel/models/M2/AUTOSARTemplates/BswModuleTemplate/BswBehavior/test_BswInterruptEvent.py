"""
This module contains tests for the BswInterruptEvent class in the
AUTOSAR BswModuleTemplate.BswBehavior module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent, BswInterruptEvent


class TestBswInterruptEvent:
    """
    Test class for BswInterruptEvent functionality.
    """

    def test_class_is_defined(self):
        assert BswInterruptEvent is not None
        assert issubclass(BswInterruptEvent, BswEvent)

    def test_initialization(self):
        """BswInterruptEvent is constructed with parent and short name like its sibling events."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        event = BswInterruptEvent(ar_root, "test_interrupt_event")

        assert event.getShortName() == "test_interrupt_event"
        assert event.getParent() is ar_root
