"""
This module contains comprehensive tests for the InstanceRefs module in
SWComponentTemplate.ImplicitCommunicationBehavior.
Tests cover all classes and methods in the InstanceRefs.py file to achieve
100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)


class TestInnerDataPrototypeGroupInCompositionInstanceRef:
    """Test class for InnerDataPrototypeGroupInCompositionInstanceRef class."""

    def test_initialization(self):
        """Test InnerDataPrototypeGroupInCompositionInstanceRef initialization."""
        instance_ref = InnerDataPrototypeGroupInCompositionInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextSwComponentPrototypeRefs == []
        assert instance_ref.targetDataPrototypeGroupRef is None

    def test_base_ref(self):
        """Test baseRef getter/setter with round-trip and None no-op."""
        instance_ref = InnerDataPrototypeGroupInCompositionInstanceRef()

        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        result = instance_ref.setBaseRef(base_ref)
        assert result is instance_ref
        assert instance_ref.getBaseRef() == base_ref

        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef() == base_ref

    def test_context_sw_component_prototype_refs(self):
        """Test contextSwComponentPrototypeRefs add/get."""
        instance_ref = InnerDataPrototypeGroupInCompositionInstanceRef()

        context_ref = RefType()
        context_ref.setValue("/Context/Component")
        result = instance_ref.addContextSwComponentPrototypeRef(context_ref)
        assert result is instance_ref
        assert context_ref in instance_ref.getContextSwComponentPrototypeRefs()

    def test_target_data_prototype_group_ref(self):
        """Test targetDataPrototypeGroupRef getter/setter with None no-op."""
        instance_ref = InnerDataPrototypeGroupInCompositionInstanceRef()

        target_ref = RefType()
        target_ref.setValue("/Target/DataPrototypeGroup")
        result = instance_ref.setTargetDataPrototypeGroupRef(target_ref)
        assert result is instance_ref
        assert instance_ref.getTargetDataPrototypeGroupRef() == target_ref

        instance_ref.setTargetDataPrototypeGroupRef(None)
        assert instance_ref.getTargetDataPrototypeGroupRef() == target_ref


class TestInnerRunnableEntityGroupInCompositionInstanceRef:
    """Test class for InnerRunnableEntityGroupInCompositionInstanceRef class."""

    def test_initialization(self):
        """Test InnerRunnableEntityGroupInCompositionInstanceRef initialization."""
        instance_ref = InnerRunnableEntityGroupInCompositionInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextSwComponentPrototypeRefs == []
        assert instance_ref.targetRunnableEntityGroupRef is None

    def test_base_ref(self):
        """Test baseRef getter/setter with round-trip and None no-op."""
        instance_ref = InnerRunnableEntityGroupInCompositionInstanceRef()

        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        result = instance_ref.setBaseRef(base_ref)
        assert result is instance_ref
        assert instance_ref.getBaseRef() == base_ref

        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef() == base_ref

    def test_context_sw_component_prototype_refs(self):
        """Test contextSwComponentPrototypeRefs add/get."""
        instance_ref = InnerRunnableEntityGroupInCompositionInstanceRef()

        context_ref = RefType()
        context_ref.setValue("/Context/Component")
        result = instance_ref.addContextSwComponentPrototypeRef(context_ref)
        assert result is instance_ref
        assert context_ref in instance_ref.getContextSwComponentPrototypeRefs()

    def test_target_runnable_entity_group_ref(self):
        """Test targetRunnableEntityGroupRef getter/setter with None no-op."""
        instance_ref = InnerRunnableEntityGroupInCompositionInstanceRef()

        target_ref = RefType()
        target_ref.setValue("/Target/RunnableEntityGroup")
        result = instance_ref.setTargetRunnableEntityGroupRef(target_ref)
        assert result is instance_ref
        assert instance_ref.getTargetRunnableEntityGroupRef() == target_ref

        instance_ref.setTargetRunnableEntityGroupRef(None)
        assert instance_ref.getTargetRunnableEntityGroupRef() == target_ref


class TestRunnableEntityInCompositionInstanceRef:
    """Test class for RunnableEntityInCompositionInstanceRef class."""

    def test_initialization(self):
        """Test RunnableEntityInCompositionInstanceRef initialization."""
        instance_ref = RunnableEntityInCompositionInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextSwComponentPrototypeRefs == []
        assert instance_ref.targetRunnableEntityRef is None

    def test_base_ref(self):
        """Test baseRef getter/setter with round-trip and None no-op."""
        instance_ref = RunnableEntityInCompositionInstanceRef()

        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        result = instance_ref.setBaseRef(base_ref)
        assert result is instance_ref
        assert instance_ref.getBaseRef() == base_ref

        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef() == base_ref

    def test_context_sw_component_prototype_refs(self):
        """Test contextSwComponentPrototypeRefs add/get."""
        instance_ref = RunnableEntityInCompositionInstanceRef()

        context_ref = RefType()
        context_ref.setValue("/Context/Component")
        result = instance_ref.addContextSwComponentPrototypeRef(context_ref)
        assert result is instance_ref
        assert context_ref in instance_ref.getContextSwComponentPrototypeRefs()

    def test_target_runnable_entity_ref(self):
        """Test targetRunnableEntityRef getter/setter with None no-op."""
        instance_ref = RunnableEntityInCompositionInstanceRef()

        target_ref = RefType()
        target_ref.setValue("/Target/RunnableEntity")
        result = instance_ref.setTargetRunnableEntityRef(target_ref)
        assert result is instance_ref
        assert instance_ref.getTargetRunnableEntityRef() == target_ref

        instance_ref.setTargetRunnableEntityRef(None)
        assert instance_ref.getTargetRunnableEntityRef() == target_ref


class TestVariableDataPrototypeInCompositionInstanceRef:
    """Test class for VariableDataPrototypeInCompositionInstanceRef class."""

    def test_initialization(self):
        """Test VariableDataPrototypeInCompositionInstanceRef initialization."""
        instance_ref = VariableDataPrototypeInCompositionInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextPortPrototypeRef is None
        assert instance_ref.contextSwComponentPrototypeRefs == []
        assert instance_ref.targetVariableDataPrototypeRef is None

    def test_base_ref(self):
        """Test baseRef getter/setter with round-trip and None no-op."""
        instance_ref = VariableDataPrototypeInCompositionInstanceRef()

        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        result = instance_ref.setBaseRef(base_ref)
        assert result is instance_ref
        assert instance_ref.getBaseRef() == base_ref

        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef() == base_ref

    def test_context_port_prototype_ref(self):
        """Test contextPortPrototypeRef getter/setter with None no-op."""
        instance_ref = VariableDataPrototypeInCompositionInstanceRef()

        context_port_ref = RefType()
        context_port_ref.setValue("/Context/Port")
        result = instance_ref.setContextPortPrototypeRef(context_port_ref)
        assert result is instance_ref
        assert instance_ref.getContextPortPrototypeRef() == context_port_ref

        instance_ref.setContextPortPrototypeRef(None)
        assert instance_ref.getContextPortPrototypeRef() == context_port_ref

    def test_context_sw_component_prototype_refs(self):
        """Test contextSwComponentPrototypeRefs add/get."""
        instance_ref = VariableDataPrototypeInCompositionInstanceRef()

        context_ref = RefType()
        context_ref.setValue("/Context/Component")
        result = instance_ref.addContextSwComponentPrototypeRef(context_ref)
        assert result is instance_ref
        assert context_ref in instance_ref.getContextSwComponentPrototypeRefs()

    def test_target_variable_data_prototype_ref(self):
        """Test targetVariableDataPrototypeRef getter/setter with None no-op."""
        instance_ref = VariableDataPrototypeInCompositionInstanceRef()

        target_ref = RefType()
        target_ref.setValue("/Target/VariableDataPrototype")
        result = instance_ref.setTargetVariableDataPrototypeRef(target_ref)
        assert result is instance_ref
        assert instance_ref.getTargetVariableDataPrototypeRef() == target_ref

        instance_ref.setTargetVariableDataPrototypeRef(None)
        assert instance_ref.getTargetVariableDataPrototypeRef() == target_ref
