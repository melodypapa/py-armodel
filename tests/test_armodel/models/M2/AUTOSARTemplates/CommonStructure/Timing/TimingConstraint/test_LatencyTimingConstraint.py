"""
This module contains tests for the LatencyTimingConstraint related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
    LatencyTimingConstraint,
)


class TestLatencyTimingConstraint:
    """
    Test class for LatencyTimingConstraint functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance().createARPackage("LatencyPkg")
        obj = LatencyTimingConstraint(parent, "Latency")
        assert obj.getShortName() == "Latency"

    def test_latency_constraint_type_enum(self):
        obj = LatencyConstraintTypeEnum()
        assert isinstance(obj, LatencyConstraintTypeEnum)
