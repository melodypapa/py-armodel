"""
This module contains tests for the TimingExtensionResource class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingExtensionResource, TimingModeInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestTimingExtensionResource:
    """
    Test class for TimingExtensionResource functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        assert isinstance(obj, TimingExtensionResource)
        assert obj.getShortName() == "Resource1"
        assert obj.getTimingArguments() == []
        assert obj.getTimingModes() == []
        assert obj.getTimingVariables() == []

    def test_add_timing_argument(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        ref = RefType().setValue("/Pkg/Arg").setDest("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        assert obj.addTimingArgument(ref) is obj
        args = obj.getTimingArguments()
        assert len(args) == 1
        assert args[0] is ref

    def test_add_timing_argument_none_noop(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        assert obj.addTimingArgument(None) is obj
        assert obj.getTimingArguments() == []

    def test_add_timing_mode(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        mode = obj.createTimingMode("Mode1")
        assert isinstance(mode, TimingModeInstance)
        assert mode.getShortName() == "Mode1"
        assert len(obj.getTimingModes()) == 1

    def test_create_timing_mode_duplicate_returns_existing(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        mode1 = obj.createTimingMode("Mode1")
        mode2 = obj.createTimingMode("Mode1")
        assert mode2 is mode1
        assert len(obj.getTimingModes()) == 1

    def test_add_timing_variable(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        ref = RefType().setValue("/Pkg/Var").setDest("AUTOSAR-VARIABLE-INSTANCE")
        assert obj.addTimingVariable(ref) is obj
        variables = obj.getTimingVariables()
        assert len(variables) == 1
        assert variables[0] is ref

    def test_add_timing_variable_none_noop(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        assert obj.addTimingVariable(None) is obj
        assert obj.getTimingVariables() == []
