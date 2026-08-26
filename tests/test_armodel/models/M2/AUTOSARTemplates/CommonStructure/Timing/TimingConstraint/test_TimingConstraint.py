import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import (
    Traceable,
)


class ConcreteTimingConstraint(TimingConstraint):
    pass


class TestTimingConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_class_cannot_be_instantiated(self):
        parent = self._parent()
        with pytest.raises(TypeError, match="TimingConstraint is an abstract class"):
            TimingConstraint(parent, "Constraint1")

    def test_base_is_traceable(self):
        assert issubclass(TimingConstraint, Traceable)

    def test_initialization_defaults(self):
        constraint = ConcreteTimingConstraint(self._parent(), "Constraint1")
        assert constraint.getShortName() == "Constraint1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getTraceRefs() == []

    def test_get_set_timing_condition_ref(self):
        constraint = ConcreteTimingConstraint(self._parent(), "Constraint1")
        ref = RefType().setValue("/AUTOSAR/TimingCondition").setDest("TIMING-CONDITION")
        assert constraint.setTimingConditionRef(ref) is constraint
        assert constraint.getTimingConditionRef() is ref
        assert constraint.getTimingConditionRef().getValue() == "/AUTOSAR/TimingCondition"
        assert constraint.getTimingConditionRef().getDest() == "TIMING-CONDITION"

    def test_set_timing_condition_ref_none_is_no_op(self):
        constraint = ConcreteTimingConstraint(self._parent(), "Constraint1")
        ref = RefType().setValue("/AUTOSAR/TimingCondition").setDest("TIMING-CONDITION")
        constraint.setTimingConditionRef(ref)
        constraint.setTimingConditionRef(None)
        assert constraint.getTimingConditionRef() is ref
