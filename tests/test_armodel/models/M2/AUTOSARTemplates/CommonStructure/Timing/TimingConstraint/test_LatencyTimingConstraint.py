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


class TestLatencyConstraintTypeEnum:
    def test_initialization(self):
        """Test LatencyConstraintTypeEnum initialization"""
        enum = LatencyConstraintTypeEnum()
        assert isinstance(enum, LatencyConstraintTypeEnum)
        assert list(enum.getEnumValues()) == ["age", "reaction"]

    def test_enum_values(self):
        """Test LatencyConstraintTypeEnum literal values (Table 3.58)"""
        assert LatencyConstraintTypeEnum.AGE == "age"
        assert LatencyConstraintTypeEnum.REACTION == "reaction"

    def test_valid_values(self):
        """Test LatencyConstraintTypeEnum setValue round-trip for all literals"""
        enum = LatencyConstraintTypeEnum()
        for member in [LatencyConstraintTypeEnum.AGE, LatencyConstraintTypeEnum.REACTION]:
            assert enum.setValue(member).getValue() == member
