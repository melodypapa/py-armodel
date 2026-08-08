"""
This module contains tests for the BswInterruptEvent class in the
AUTOSAR BswModuleTemplate.BswBehavior module.
"""

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswInterruptEvent import (
    BswInterruptEvent,
)


class TestBswInterruptEvent:
    """
    Test class for BswInterruptEvent functionality.
    """

    def test_class_is_defined(self):
        assert BswInterruptEvent is not None
        assert issubclass(BswInterruptEvent, BswEvent)
