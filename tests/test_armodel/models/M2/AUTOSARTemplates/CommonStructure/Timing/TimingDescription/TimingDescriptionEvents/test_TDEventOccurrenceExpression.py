from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingModeInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    TDEventOccurrenceExpression,
    TDEventOccurrenceExpressionFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TestTDEventOccurrenceExpression:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_ar_object(self):
        assert issubclass(TDEventOccurrenceExpression, ARObject)

    def test_instantiable_and_defaults(self):
        expression = TDEventOccurrenceExpression()
        assert expression.getArguments() == []
        assert expression.getFormula() is None
        assert expression.getModes() == []
        assert expression.getVariables() == []

    def test_create_argument_appends(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        argument = expression.createArgument(parent, "Arg1")
        assert isinstance(argument, AutosarOperationArgumentInstance)
        assert len(expression.getArguments()) == 1
        assert expression.getArguments()[0] is argument

    def test_create_argument_duplicate_returns_existing(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        first = expression.createArgument(parent, "Arg1")
        second = expression.createArgument(parent, "Arg1")
        assert first is second
        assert len(expression.getArguments()) == 1

    def test_set_get_formula(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        formula = TDEventOccurrenceExpressionFormula(parent, "Formula1")
        assert expression.setFormula(formula) is expression
        assert expression.getFormula() is formula
        expression.setFormula(None)
        assert expression.getFormula() is formula

    def test_create_mode_appends(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        mode = expression.createMode(parent, "Mode1")
        assert isinstance(mode, TimingModeInstance)
        assert len(expression.getModes()) == 1

    def test_create_mode_duplicate_returns_existing(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        first = expression.createMode(parent, "Mode1")
        second = expression.createMode(parent, "Mode1")
        assert first is second
        assert len(expression.getModes()) == 1

    def test_create_variable_appends(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        variable = expression.createVariable(parent, "Var1")
        assert isinstance(variable, AutosarVariableInstance)
        assert len(expression.getVariables()) == 1

    def test_create_variable_duplicate_returns_existing(self):
        parent = self._parent()
        expression = TDEventOccurrenceExpression()
        first = expression.createVariable(parent, "Var1")
        second = expression.createVariable(parent, "Var1")
        assert first is second
        assert len(expression.getVariables()) == 1
