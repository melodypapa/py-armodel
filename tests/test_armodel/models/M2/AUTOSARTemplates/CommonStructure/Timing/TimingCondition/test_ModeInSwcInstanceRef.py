"""
This module contains tests for the ModeInSwcInstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.ModeInSwcInstanceRef import (
    ModeInSwcInstanceRef,
)


class TestModeInSwcInstanceRef:
    """
    Test class for ModeInSwcInstanceRef functionality.
    """

    def test_initialization(self):
        obj = ModeInSwcInstanceRef()
        assert isinstance(obj, ModeInSwcInstanceRef)
