"""
This module contains tests for the ModeInBswInstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.ModeInBswInstanceRef import (
    ModeInBswInstanceRef,
)


class TestModeInBswInstanceRef:
    """
    Test class for ModeInBswInstanceRef functionality.
    """

    def test_initialization(self):
        obj = ModeInBswInstanceRef()
        assert isinstance(obj, ModeInBswInstanceRef)
