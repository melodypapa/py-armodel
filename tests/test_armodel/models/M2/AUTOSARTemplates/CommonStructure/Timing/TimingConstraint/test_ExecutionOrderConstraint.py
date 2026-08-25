from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
    EOCExecutableEntityRef,
    EOCExecutableEntityRefGroup,
    ExecutionOrderConstraint,
    ExecutionOrderConstraintTypeEnum,
    LetDataExchangeParadigmEnum,
)


class TestExecutionOrderConstraint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        assert constraint is not None
        assert constraint.getShortName() == "TestConstraint"
        assert constraint.getOrderedElements() == []

    def test_create_eoc_executable_entity_ref(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        entity_ref = constraint.createEOCExecutableEntityRef("EntityRef")
        assert isinstance(entity_ref, EOCExecutableEntityRef)
        assert entity_ref.getShortName() == "EntityRef"
        assert entity_ref in constraint.getOrderedElements()
        assert len(constraint.getOrderedElements()) == 1

    def test_create_eoc_executable_entity_ref_duplicate(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        entity_ref1 = constraint.createEOCExecutableEntityRef("EntityRef")
        entity_ref2 = constraint.createEOCExecutableEntityRef("EntityRef")  # Should return same instance

        assert entity_ref1 is entity_ref2
        assert len(constraint.getOrderedElements()) == 1

    def test_create_eoc_event_ref(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        event_ref = constraint.createEOCEventRef("EventRef")
        assert isinstance(event_ref, EOCEventRef)
        assert event_ref.getShortName() == "EventRef"
        assert event_ref in constraint.getOrderedElements()
        assert len(constraint.getOrderedElements()) == 1

    def test_create_eoc_event_ref_duplicate(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        event_ref1 = constraint.createEOCEventRef("EventRef")
        event_ref2 = constraint.createEOCEventRef("EventRef")

        assert event_ref1 is event_ref2
        assert len(constraint.getOrderedElements()) == 1

    def test_create_eoc_executable_entity_ref_group(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        group = constraint.createEOCExecutableEntityRefGroup("Group")
        assert isinstance(group, EOCExecutableEntityRefGroup)
        assert group.getShortName() == "Group"
        assert group in constraint.getOrderedElements()
        assert len(constraint.getOrderedElements()) == 1

    def test_create_eoc_executable_entity_ref_group_duplicate(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        group1 = constraint.createEOCExecutableEntityRefGroup("Group")
        group2 = constraint.createEOCExecutableEntityRefGroup("Group")

        assert group1 is group2
        assert len(constraint.getOrderedElements()) == 1

    def test_get_ordered_elements_mixed_subtypes(self):
        parent = self._parent()
        constraint = ExecutionOrderConstraint(parent, "TestConstraint")

        entity_ref = constraint.createEOCExecutableEntityRef("EntityRef")
        event_ref = constraint.createEOCEventRef("EventRef")
        group = constraint.createEOCExecutableEntityRefGroup("Group")

        elements = constraint.getOrderedElements()
        assert elements == [entity_ref, event_ref, group]
        assert len(elements) == 3


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


def test_imports():
    """Ensure the module re-exports stay stable."""
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import (
        EOCEventRef as _eoc_event_ref,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import (
        EOCExecutableEntityRefGroup as _eoc_group,
    )

    assert _eoc_event_ref is EOCEventRef
    assert _eoc_group is EOCExecutableEntityRefGroup
