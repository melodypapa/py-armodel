"""
This module contains tests for the TimingExtensionResource class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingExtensionResource,
    TimingModeInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
)


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

    def test_create_timing_argument(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        argument = obj.createTimingArgument("Arg1")
        assert isinstance(argument, AutosarOperationArgumentInstance)
        assert argument.getShortName() == "Arg1"
        assert len(obj.getTimingArguments()) == 1
        assert obj.getTimingArguments()[0] is argument

    def test_create_timing_argument_duplicate_returns_existing(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        argument1 = obj.createTimingArgument("Arg1")
        argument2 = obj.createTimingArgument("Arg1")
        assert argument2 is argument1
        assert len(obj.getTimingArguments()) == 1

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

    def test_create_timing_variable(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        variable = obj.createTimingVariable("Var1")
        assert isinstance(variable, AutosarVariableInstance)
        assert variable.getShortName() == "Var1"
        assert len(obj.getTimingVariables()) == 1
        assert obj.getTimingVariables()[0] is variable

    def test_create_timing_variable_duplicate_returns_existing(self):
        parent = self._parent()
        obj = TimingExtensionResource(parent, "Resource1")
        variable1 = obj.createTimingVariable("Var1")
        variable2 = obj.createTimingVariable("Var1")
        assert variable2 is variable1
        assert len(obj.getTimingVariables()) == 1

    def test_class_docstring_note(self):
        import inspect

        assert inspect.cleandoc(TimingExtensionResource.__doc__) == (
            "A TimingExtensionResource provides the capability to contain instance references "
            "referred from within a timing condition formula."
        )

    def test_member_docstrings_are_verbatim_spec_notes(self):
        import inspect

        arg_note = "This refers to an instance reference of an argument of an operation call. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=timingArgument.shortName, timing Argument.variationPoint.shortLabel vh.latestBindingTime=postBuild"
        mode_note = "This refers to an instance reference of a mode declaration. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=timingMode.shortName, timing Mode.variationPoint.shortLabel vh.latestBindingTime=postBuild"
        var_note = "This refers to an instance reference of a variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=timingVariable.shortName, timing Variable.variationPoint.shortLabel vh.latestBindingTime=postBuild"

        assert inspect.cleandoc(TimingExtensionResource.createTimingArgument.__doc__) == arg_note
        assert inspect.cleandoc(TimingExtensionResource.getTimingArguments.__doc__) == arg_note
        assert inspect.cleandoc(TimingExtensionResource.createTimingMode.__doc__) == mode_note
        assert inspect.cleandoc(TimingExtensionResource.getTimingModes.__doc__) == mode_note
        assert inspect.cleandoc(TimingExtensionResource.createTimingVariable.__doc__) == var_note
        assert inspect.cleandoc(TimingExtensionResource.getTimingVariables.__doc__) == var_note
