"""
This module contains tests for the TimingCondition class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingCondition,
    TimingConditionFormula,
)


class TestTimingCondition:
    """
    Test class for TimingCondition functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        obj = TimingCondition(self._parent(), "Cond1")
        assert isinstance(obj, TimingCondition)
        assert obj.getShortName() == "Cond1"
        assert obj.getTimingConditionFormula() is None

    def test_get_set_timing_condition_formula(self):
        parent = self._parent()
        obj = TimingCondition(parent, "Cond1")

        formula = TimingConditionFormula(obj, "Formula1")
        assert obj.setTimingConditionFormula(formula) is obj
        assert obj.getTimingConditionFormula() is formula

    def test_set_timing_condition_formula_none_no_op(self):
        parent = self._parent()
        obj = TimingCondition(parent, "Cond1")

        formula = TimingConditionFormula(obj, "Formula1")
        obj.setTimingConditionFormula(formula)
        obj.setTimingConditionFormula(None)
        assert obj.getTimingConditionFormula() is formula
