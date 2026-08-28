from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingModeInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    TDEventOccurrenceExpressionFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventOccurrenceExpressionFormula:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_referrable(self):
        assert issubclass(TDEventOccurrenceExpressionFormula, Referrable)

    def test_initialization_defaults(self):
        formula = TDEventOccurrenceExpressionFormula(self._parent(), "Formula1")
        assert formula.getShortName() == "Formula1"
        assert formula.getText() is None
        assert formula.getArgumentRef() is None
        assert formula.getEventRef() is None
        assert formula.getModeRef() is None
        assert formula.getVariableRef() is None

    def test_set_text(self):
        formula = TDEventOccurrenceExpressionFormula(self._parent(), "Formula1")
        assert formula.setText("TIMEX_count(E1) > 3") is formula
        assert formula.getText() == "TIMEX_count(E1) > 3"

    def test_set_text_none_is_no_op(self):
        formula = TDEventOccurrenceExpressionFormula(self._parent(), "Formula1")
        formula.setText("A && B")
        formula.setText(None)
        assert formula.getText() == "A && B"

    def test_get_set_argument_ref(self):
        formula = TDEventOccurrenceExpressionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/AUTOSAR/Arg1").setDest("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        assert formula.setArgumentRef(ref) is formula
        assert formula.getArgumentRef() is ref
        assert formula.getArgumentRef().getValue() == "/AUTOSAR/Arg1"
        formula.setArgumentRef(None)
        assert formula.getArgumentRef() is ref

    def test_get_set_event_ref(self):
        formula = TDEventOccurrenceExpressionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/AUTOSAR/TDEvent1").setDest("TD-EVENT-VFB")
        assert formula.setEventRef(ref) is formula
        assert formula.getEventRef() is ref
        formula.setEventRef(None)
        assert formula.getEventRef() is ref

    def test_get_set_mode_ref(self):
        parent = self._parent()
        formula = TDEventOccurrenceExpressionFormula(parent, "Formula1")
        mode = TimingModeInstance(parent, "Mode1")
        mode_ref = RefType().setValue("/AUTOSAR/Mode1").setDest("TIMING-MODE-INSTANCE")
        assert formula.setModeRef(mode_ref) is formula
        assert formula.getModeRef() is mode_ref
        assert isinstance(mode, TimingModeInstance)
        formula.setModeRef(None)
        assert formula.getModeRef() is mode_ref

    def test_get_set_variable_ref(self):
        parent = self._parent()
        formula = TDEventOccurrenceExpressionFormula(parent, "Formula1")
        variable = AutosarVariableInstance(parent, "Var1")
        var_ref = RefType().setValue("/AUTOSAR/Var1").setDest("AUTOSAR-VARIABLE-INSTANCE")
        assert formula.setVariableRef(var_ref) is formula
        assert formula.getVariableRef() is var_ref
        assert isinstance(variable, AutosarVariableInstance)
        formula.setVariableRef(None)
        assert formula.getVariableRef() is var_ref

    def test_aggregated_instance_classes_exist(self):
        parent = self._parent()
        argument = AutosarOperationArgumentInstance(parent, "OpArg1")
        assert argument.getShortName() == "OpArg1"
