"""
This module contains tests for the AgeConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import (
    AgeConstraint,
)


class TestAgeConstraint:
    """
    Test class for AgeConstraint functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = AgeConstraint(ar_root, "TestAgeConstraint")
        assert obj.getShortName() == "TestAgeConstraint"
        assert obj.getParent() == ar_root
