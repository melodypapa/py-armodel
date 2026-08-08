"""
This module contains tests for the OffsetTimingConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import (
    OffsetTimingConstraint,
)


class TestOffsetTimingConstraint:
    """
    Test class for OffsetTimingConstraint functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = OffsetTimingConstraint(ar_root, "TestOffsetTimingConstraint")
        assert obj.getShortName() == "TestOffsetTimingConstraint"
        assert obj.getParent() == ar_root
