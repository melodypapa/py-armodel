import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingCondition,
    TimingExtensionResource,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    ExecutionOrderConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import (
    SwcTiming,
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def _ar_package():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document.createARPackage("AUTOSAR")


class ConcreteTimingExtension(TimingExtension):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class TestTimingExtension:
    def test_abstract_class_cannot_be_instantiated(self):
        parent = _ar_package()
        with pytest.raises(TypeError, match="TimingExtension is an abstract class."):
            TimingExtension(parent, "TestTimingExtension")

    def test_initialization(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        assert isinstance(extension, TimingExtension)
        assert extension.getTimingConditions() == []
        assert extension.getTimingGuarantees() == []
        assert extension.getTimingRequirements() == []
        assert extension.getTimingResource() is None

    def test_create_timing_condition(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        condition = extension.createTimingCondition("Cond1")
        assert isinstance(condition, TimingCondition)
        assert condition.getShortName() == "Cond1"
        assert len(extension.getTimingConditions()) == 1
        assert extension.getTimingConditions()[0] is condition

    def test_create_timing_condition_duplicate_returns_existing(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        condition1 = extension.createTimingCondition("Cond1")
        condition2 = extension.createTimingCondition("Cond1")
        assert condition2 is condition1
        assert len(extension.getTimingConditions()) == 1

    def test_add_timing_guarantee(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        constraint = ExecutionTimeConstraint(extension, "Guarantee1")
        extension.addElement(constraint)
        assert extension.addTimingGuarantee(constraint) is extension
        assert len(extension.getTimingGuarantees()) == 1
        assert extension.getTimingGuarantees()[0] is constraint

    def test_add_timing_guarantee_none_noop(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        assert extension.addTimingGuarantee(None) is extension
        assert extension.getTimingGuarantees() == []

    def test_add_timing_requirement(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        constraint = ExecutionOrderConstraint(extension, "Req1")
        extension.addElement(constraint)
        assert extension.addTimingRequirement(constraint) is extension
        assert len(extension.getTimingRequirements()) == 1
        assert extension.getTimingRequirements()[0] is constraint

    def test_add_timing_requirement_none_noop(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        assert extension.addTimingRequirement(None) is extension
        assert extension.getTimingRequirements() == []

    def test_create_execution_order_constraint_convenience(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        constraint = extension.createExecutionOrderConstraint("Eoc1")
        assert isinstance(constraint, ExecutionOrderConstraint)
        assert constraint in extension.getTimingRequirements()
        constraint2 = extension.createExecutionOrderConstraint("Eoc1")
        assert constraint2 is constraint

    def test_create_timing_resource(self):
        parent = _ar_package()
        extension = ConcreteTimingExtension(parent, "Ext1")
        resource = extension.createTimingResource("Res1")
        assert isinstance(resource, TimingExtensionResource)
        assert resource.getShortName() == "Res1"
        assert extension.getTimingResource() is resource
        resource2 = extension.createTimingResource("Res1")
        assert resource2 is resource


class TestSwcTiming:
    def test_initialization(self):
        parent = _ar_package()
        swc_timing = SwcTiming(parent, "TestSwcTiming")
        assert isinstance(swc_timing, SwcTiming)
        assert swc_timing.getShortName() == "TestSwcTiming"
        assert swc_timing.getBehaviorRef() is None
        assert swc_timing.getTimingRequirements() == []

    def test_get_set_behavior_ref(self):
        parent = _ar_package()
        swc_timing = SwcTiming(parent, "TestSwcTiming")
        ref = RefType().setValue("/AUTOSAR/Swc/IB").setDest("SWC-INTERNAL-BEHAVIOR")
        assert swc_timing.setBehaviorRef(ref) is swc_timing
        assert swc_timing.getBehaviorRef() is ref

        swc_timing.setBehaviorRef(None)
        assert swc_timing.getBehaviorRef() is ref

    def test_inherits_timing_extension_members(self):
        parent = _ar_package()
        swc_timing = SwcTiming(parent, "TestSwcTiming")
        condition = swc_timing.createTimingCondition("Cond1")
        assert isinstance(condition, TimingCondition)
        constraint = swc_timing.createExecutionOrderConstraint("Eoc1")
        assert isinstance(constraint, ExecutionOrderConstraint)
        assert len(swc_timing.getTimingRequirements()) == 1
