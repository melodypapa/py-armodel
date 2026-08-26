"""
This module contains tests for the TimingModeInstance class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import ModeInBswInstanceRef, TimingModeInstance


class TestTimingModeInstance:
    """
    Test class for TimingModeInstance functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        obj = TimingModeInstance(parent, "Mode1")
        assert isinstance(obj, TimingModeInstance)
        assert obj.getShortName() == "Mode1"
        assert obj.getModeInstance() is None

    def test_get_set_mode_instance_bsw(self):
        parent = self._parent()
        obj = TimingModeInstance(parent, "Mode1")
        iref = ModeInBswInstanceRef()
        assert obj.setModeInstance(iref) is obj
        assert obj.getModeInstance() is iref

    def test_set_mode_instance_none_noop(self):
        parent = self._parent()
        obj = TimingModeInstance(parent, "Mode1")
        iref = ModeInBswInstanceRef()
        obj.setModeInstance(iref)
        assert obj.setModeInstance(None) is obj
        assert obj.getModeInstance() is iref
