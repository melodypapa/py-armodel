import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
    EOCExecutableEntityRefAbstract,
    ExecutionOrderConstraint,
    ExecutionOrderConstraintTypeEnum,
    LetDataExchangeParadigmEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


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


class TestExecutionOrderConstraintTypeEnum:
    def test_initialization(self):
        """Test ExecutionOrderConstraintTypeEnum initialization"""
        enum = ExecutionOrderConstraintTypeEnum()
        assert isinstance(enum, ExecutionOrderConstraintTypeEnum)
        assert list(enum.getEnumValues()) == ["hierarchicalEOC", "ordinaryEOC", "repetitiveEOC"]

    def test_enum_values(self):
        """Test ExecutionOrderConstraintTypeEnum literal values (Table 3.69)"""
        assert ExecutionOrderConstraintTypeEnum.HIERARCHICAL_EOC == "hierarchicalEOC"
        assert ExecutionOrderConstraintTypeEnum.ORDINARY_EOC == "ordinaryEOC"
        assert ExecutionOrderConstraintTypeEnum.REPETITIVE_EOC == "repetitiveEOC"

    def test_valid_values(self):
        """Test ExecutionOrderConstraintTypeEnum setValue round-trip for all literals"""
        enum = ExecutionOrderConstraintTypeEnum()
        for member in [ExecutionOrderConstraintTypeEnum.HIERARCHICAL_EOC, ExecutionOrderConstraintTypeEnum.ORDINARY_EOC, ExecutionOrderConstraintTypeEnum.REPETITIVE_EOC]:
            assert enum.setValue(member).getValue() == member


class TestLetDataExchangeParadigmEnum:
    def test_initialization(self):
        """Test LetDataExchangeParadigmEnum initialization"""
        enum = LetDataExchangeParadigmEnum()
        assert isinstance(enum, LetDataExchangeParadigmEnum)
        assert list(enum.getEnumValues()) == ["interLetOnly", "intraLetEOC"]

    def test_enum_values(self):
        """Test LetDataExchangeParadigmEnum literal values (Table 4.4)"""
        assert LetDataExchangeParadigmEnum.INTER_LET_ONLY == "interLetOnly"
        assert LetDataExchangeParadigmEnum.INTRA_LET_EOC == "intraLetEOC"

    def test_valid_values(self):
        """Test LetDataExchangeParadigmEnum setValue round-trip for all literals"""
        enum = LetDataExchangeParadigmEnum()
        for member in [LetDataExchangeParadigmEnum.INTER_LET_ONLY, LetDataExchangeParadigmEnum.INTRA_LET_EOC]:
            assert enum.setValue(member).getValue() == member
