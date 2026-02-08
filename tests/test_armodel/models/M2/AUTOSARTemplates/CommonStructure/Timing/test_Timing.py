import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
    EOCExecutableEntityRefAbstract,
    ExecutionOrderConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import (
    SwcTiming,
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTimingConstraint:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that TimingConstraint abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="TimingConstraint is an abstract class"):
            TimingConstraint(ar_root, "TestTimingConstraint")

    def test_timing_condition_ref_property(self):
        """Test timingConditionRef property"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        # Create a concrete subclass for testing
        class ConcreteTimingConstraint(TimingConstraint):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        constraint = ConcreteTimingConstraint(ar_root, "TestTimingConstraint")

        # Test property setter and getter
        test_ref = RefType().setValue("TestRef")
        constraint.timingConditionRef = test_ref
        assert constraint.timingConditionRef == test_ref


class TestEOCExecutableEntityRefAbstract:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that EOCExecutableEntityRefAbstract abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="EOCExecutableEntityRefAbstract is an abstract class"):
            EOCExecutableEntityRefAbstract(ar_root, "TestEOCExecutableEntityRefAbstract")


class TestEOCExecutableEntityRef:
    def test_initialization(self):
        """Test EOCExecutableEntityRef initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        entity_ref = EOCExecutableEntityRef(ar_root, "TestEntityRef")

        assert entity_ref is not None
        assert entity_ref.getShortName() == "TestEntityRef"
        assert entity_ref.successor_refs == []

    def test_add_successor_ref(self):
        """Test addSuccessorRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        entity_ref = EOCExecutableEntityRef(ar_root, "TestEntityRef")

        ref = RefType().setValue("SuccessorRef")
        entity_ref.addSuccessorRef(ref)
        assert ref in entity_ref.getSuccessorRefs()
        assert len(entity_ref.getSuccessorRefs()) == 1
        assert entity_ref.getSuccessorRefs()[0] == ref

    def test_get_successor_refs(self):
        """Test getSuccessorRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        entity_ref = EOCExecutableEntityRef(ar_root, "TestEntityRef")

        refs = entity_ref.getSuccessorRefs()
        assert refs == []
        assert isinstance(refs, list)


class TestExecutionOrderConstraint:
    def test_initialization(self):
        """Test ExecutionOrderConstraint initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        constraint = ExecutionOrderConstraint(ar_root, "TestConstraint")

        assert constraint is not None
        assert constraint.getShortName() == "TestConstraint"
        assert constraint.ordered_elements == []

    def test_create_eoc_executable_entity_ref(self):
        """Test createEOCExecutableEntityRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        constraint = ExecutionOrderConstraint(ar_root, "TestConstraint")

        entity_ref = constraint.createEOCExecutableEntityRef("EntityRef")
        assert isinstance(entity_ref, EOCExecutableEntityRef)
        assert entity_ref.getShortName() == "EntityRef"
        assert entity_ref in constraint.getOrderedElements()
        assert len(constraint.getOrderedElements()) == 1

    def test_create_eoc_executable_entity_ref_duplicate(self):
        """Test createEOCExecutableEntityRef with duplicate name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        constraint = ExecutionOrderConstraint(ar_root, "TestConstraint")

        entity_ref1 = constraint.createEOCExecutableEntityRef("EntityRef")
        entity_ref2 = constraint.createEOCExecutableEntityRef("EntityRef")  # Should return same instance

        assert entity_ref1 is entity_ref2
        assert len(constraint.getOrderedElements()) == 1

    def test_get_ordered_elements(self):
        """Test getOrderedElements method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        constraint = ExecutionOrderConstraint(ar_root, "TestConstraint")

        elements = constraint.getOrderedElements()
        assert elements == []
        assert isinstance(elements, list)


class TestTimingExtension:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that TimingExtension abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="TimingExtension is an abstract class."):
            TimingExtension(ar_root, "TestTimingExtension")

    def test_create_execution_order_constraint(self):
        """Test createExecutionOrderConstraint method for concrete subclass"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        # Create a concrete subclass for testing
        class ConcreteTimingExtension(TimingExtension):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        extension = ConcreteTimingExtension(ar_root, "TestTimingExtension")
        constraint = extension.createExecutionOrderConstraint("TestConstraint")

        assert isinstance(constraint, ExecutionOrderConstraint)
        assert constraint.getShortName() == "TestConstraint"
        assert constraint in extension.getTimingRequirements()
        assert len(extension.getTimingRequirements()) == 1


class TestSwcTiming:
    def test_initialization(self):
        """Test SwcTiming initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_timing = SwcTiming(ar_root, "TestSwcTiming")

        assert swc_timing is not None
        assert swc_timing.getShortName() == "TestSwcTiming"
        assert swc_timing.timing_requirements == []

    def test_create_execution_order_constraint(self):
        """Test createExecutionOrderConstraint method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_timing = SwcTiming(ar_root, "TestSwcTiming")

        constraint = swc_timing.createExecutionOrderConstraint("TestConstraint")
        assert isinstance(constraint, ExecutionOrderConstraint)
        assert constraint.getShortName() == "TestConstraint"
        assert constraint in swc_timing.getTimingRequirements()
        assert len(swc_timing.getTimingRequirements()) == 1

    def test_get_timing_requirements(self):
        """Test getTimingRequirements method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_timing = SwcTiming(ar_root, "TestSwcTiming")

        requirements = swc_timing.getTimingRequirements()
        assert requirements == []
        assert isinstance(requirements, list)
