"""
This module contains tests for the TimingExtensionResource class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingExtensionResource import (
    TimingExtensionResource,
)


class TestTimingExtensionResource:
    """
    Test class for TimingExtensionResource functionality.
    """

    def test_initialization(self):
        obj = TimingExtensionResource()
        assert isinstance(obj, TimingExtensionResource)
