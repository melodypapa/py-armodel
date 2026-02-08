import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
    EOCExecutableEntityRefAbstract,
    ExecutionOrderConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
