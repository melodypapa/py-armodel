"""
This module contains tests for the TimingConditionFormula class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingConditionFormula
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestTimingConditionFormula:
    """
    Test class for TimingConditionFormula functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        obj = TimingConditionFormula(parent, "Formula1")
        assert isinstance(obj, TimingConditionFormula)
        assert obj.getShortName() == "Formula1"
        assert obj.getText() is None
        assert obj.getTimingArgumentRef() is None
        assert obj.getTimingConditionRef() is None
        assert obj.getTimingEventRef() is None
        assert obj.getTimingModeRef() is None
        assert obj.getTimingVariableRef() is None

    def test_get_set_text(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        assert obj.setText("a == b && modeActive") is obj
        assert obj.getText() == "a == b && modeActive"

    def test_set_text_none_noop(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        obj.setText("expr")
        assert obj.setText(None) is obj
        assert obj.getText() == "expr"

    def test_get_set_timing_argument_ref(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Arg").setDest("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        assert obj.setTimingArgumentRef(ref) is obj
        assert obj.getTimingArgumentRef() is ref
        assert obj.getTimingArgumentRef().getValue() == "/Pkg/Arg"

    def test_set_timing_argument_ref_none_noop(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Arg").setDest("AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
        obj.setTimingArgumentRef(ref)
        assert obj.setTimingArgumentRef(None) is obj
        assert obj.getTimingArgumentRef() is ref

    def test_get_set_timing_condition_ref(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Cond").setDest("TIMING-CONDITION")
        assert obj.setTimingConditionRef(ref) is obj
        assert obj.getTimingConditionRef() is ref
        assert obj.getTimingConditionRef().getValue() == "/Pkg/Cond"

    def test_set_timing_condition_ref_none_noop(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Cond").setDest("TIMING-CONDITION")
        obj.setTimingConditionRef(ref)
        assert obj.setTimingConditionRef(None) is obj
        assert obj.getTimingConditionRef() is ref

    def test_get_set_timing_event_ref(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Event").setDest("TIMING-DESCRIPTION-EVENT")
        assert obj.setTimingEventRef(ref) is obj
        assert obj.getTimingEventRef() is ref
        assert obj.getTimingEventRef().getValue() == "/Pkg/Event"

    def test_set_timing_event_ref_none_noop(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Event").setDest("TIMING-DESCRIPTION-EVENT")
        obj.setTimingEventRef(ref)
        assert obj.setTimingEventRef(None) is obj
        assert obj.getTimingEventRef() is ref

    def test_get_set_timing_mode_ref(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Mode").setDest("TIMING-MODE-INSTANCE")
        assert obj.setTimingModeRef(ref) is obj
        assert obj.getTimingModeRef() is ref
        assert obj.getTimingModeRef().getValue() == "/Pkg/Mode"

    def test_set_timing_mode_ref_none_noop(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Mode").setDest("TIMING-MODE-INSTANCE")
        obj.setTimingModeRef(ref)
        assert obj.setTimingModeRef(None) is obj
        assert obj.getTimingModeRef() is ref

    def test_get_set_timing_variable_ref(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Var").setDest("AUTOSAR-VARIABLE-INSTANCE")
        assert obj.setTimingVariableRef(ref) is obj
        assert obj.getTimingVariableRef() is ref
        assert obj.getTimingVariableRef().getValue() == "/Pkg/Var"

    def test_set_timing_variable_ref_none_noop(self):
        obj = TimingConditionFormula(self._parent(), "Formula1")
        ref = RefType().setValue("/Pkg/Var").setDest("AUTOSAR-VARIABLE-INSTANCE")
        obj.setTimingVariableRef(ref)
        assert obj.setTimingVariableRef(None) is obj
        assert obj.getTimingVariableRef() is ref
