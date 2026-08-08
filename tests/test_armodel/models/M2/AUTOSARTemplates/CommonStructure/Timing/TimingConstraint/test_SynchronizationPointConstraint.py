"""
This module contains tests for the SynchronizationPointConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import (
    SynchronizationPointConstraint,
)


class TestSynchronizationPointConstraint:
    """
    Test class for SynchronizationPointConstraint functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = SynchronizationPointConstraint(ar_root, "TestSynchronizationPointConstraint")
        assert obj.getShortName() == "TestSynchronizationPointConstraint"
        assert obj.getParent() == ar_root
