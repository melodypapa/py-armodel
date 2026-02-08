"""
This module contains comprehensive tests for the InstanceRefs module in SWComponentTemplate.Components.
Tests cover all classes and methods in the InstanceRefs.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
    ModeGroupInAtomicSwcInstanceRef,
    PModeGroupInAtomicSwcInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
    VariableInAtomicSwcInstanceRef,
)


class TestModeGroupInAtomicSwcInstanceRef:
    """Test class for ModeGroupInAtomicSwcInstanceRef abstract class."""

    def test_mode_group_in_atomic_swc_instance_ref_abstract(self):
        """Test that ModeGroupInAtomicSwcInstanceRef is an abstract class."""
        with pytest.raises(TypeError):
            ModeGroupInAtomicSwcInstanceRef()


class TestPModeGroupInAtomicSwcInstanceRef:
    """Test class for PModeGroupInAtomicSwcInstanceRef class."""

    def test_p_mode_group_in_atomic_swc_instance_ref_initialization(self):
        """Test PModeGroupInAtomicSwcInstanceRef initialization and methods."""
        instance_ref = PModeGroupInAtomicSwcInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.targetRef is None
        assert instance_ref.contextPPortRef is None
        assert instance_ref.targetModeGroupRef is None

        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref

        # Test contextPortRef methods
        context_port_ref = RefType()
        context_port_ref.setValue("/Context/Port")
        instance_ref.setContextPortRef(context_port_ref)
        assert instance_ref.getContextPortRef() == context_port_ref

        # Test targetRef methods
        target_ref = RefType()
        target_ref.setValue("/Target/Ref")
        instance_ref.setTargetRef(target_ref)
        assert instance_ref.getTargetRef() == target_ref

        # Test contextPPortRef methods
        context_p_port_ref = RefType()
        context_p_port_ref.setValue("/Context/P/Port")
        instance_ref.setContextPPortRef(context_p_port_ref)
        assert instance_ref.getContextPPortRef() == context_p_port_ref

        # Test targetModeGroupRef methods
        target_mode_group_ref = RefType()
        target_mode_group_ref.setValue("/Target/ModeGroup")
        instance_ref.setTargetModeGroupRef(target_mode_group_ref)
        assert instance_ref.getTargetModeGroupRef() == target_mode_group_ref


class TestRModeGroupInAtomicSWCInstanceRef:
    """Test class for RModeGroupInAtomicSWCInstanceRef class."""

    def test_r_mode_group_in_atomic_swc_instance_ref_initialization(self):
        """Test RModeGroupInAtomicSWCInstanceRef initialization and methods."""
        instance_ref = RModeGroupInAtomicSWCInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.targetRef is None
        assert instance_ref.contextRPortRef is None
        assert instance_ref.targetModeGroupRef is None

        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref

        # Test contextPortRef methods
        context_port_ref = RefType()
        context_port_ref.setValue("/Context/Port")
        instance_ref.setContextPortRef(context_port_ref)
        assert instance_ref.getContextPortRef() == context_port_ref

        # Test targetRef methods
        target_ref = RefType()
        target_ref.setValue("/Target/Ref")
        instance_ref.setTargetRef(target_ref)
        assert instance_ref.getTargetRef() == target_ref

        # Test contextRPortRef methods
        context_r_port_ref = RefType()
        context_r_port_ref.setValue("/Context/R/Port")
        instance_ref.setContextRPortRef(context_r_port_ref)
        assert instance_ref.getContextRPortRef() == context_r_port_ref

        # Test targetModeGroupRef methods
        target_mode_group_ref = RefType()
        target_mode_group_ref.setValue("/Target/ModeGroup")
        instance_ref.setTargetModeGroupRef(target_mode_group_ref)
        assert instance_ref.getTargetModeGroupRef() == target_mode_group_ref


class TestRModeInAtomicSwcInstanceRef:
    """Test class for RModeInAtomicSwcInstanceRef class."""

    def test_r_mode_in_atomic_swc_instance_ref_initialization(self):
        """Test RModeInAtomicSwcInstanceRef initialization and methods."""
        instance_ref = RModeInAtomicSwcInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextModeDeclarationGroupPrototypeRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.targetModeDeclarationRef is None

        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref

        # Test contextModeDeclarationGroupPrototypeRef methods
        context_mode_decl_group_ref = RefType()
        context_mode_decl_group_ref.setValue("/Context/ModeGroup")
        instance_ref.setContextModeDeclarationGroupPrototypeRef(context_mode_decl_group_ref)
        assert instance_ref.getContextModeDeclarationGroupPrototypeRef() == context_mode_decl_group_ref

        # Test contextPortRef methods
        context_port_ref = RefType()
        context_port_ref.setValue("/Context/Port")
        instance_ref.setContextPortRef(context_port_ref)
        assert instance_ref.getContextPortRef() == context_port_ref

        # Test targetModeDeclarationRef methods
        target_mode_decl_ref = RefType()
        target_mode_decl_ref.setValue("/Target/ModeDecl")
        instance_ref.setTargetModeDeclarationRef(target_mode_decl_ref)
        assert instance_ref.getTargetModeDeclarationRef() == target_mode_decl_ref


class TestVariableInAtomicSwcInstanceRef:
    """Test class for VariableInAtomicSwcInstanceRef abstract class."""

    def test_variable_in_atomic_swc_instance_ref_abstract(self):
        """Test that VariableInAtomicSwcInstanceRef is an abstract class."""
        with pytest.raises(TypeError):
            VariableInAtomicSwcInstanceRef()


class TestRVariableInAtomicSwcInstanceRef:
    """Test class for RVariableInAtomicSwcInstanceRef class."""

    def test_r_variable_in_atomic_swc_instance_ref_initialization(self):
        """Test RVariableInAtomicSwcInstanceRef initialization and methods."""
        instance_ref = RVariableInAtomicSwcInstanceRef()

        assert instance_ref.abstractTargetDataElementRef is None
        assert instance_ref.baseRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.contextRPortRef is None
        assert instance_ref.targetDataElementRef is None

        # Test abstractTargetDataElementRef direct access
        abstract_target_ref = RefType()
        abstract_target_ref.setValue("/Abstract/Target")
        instance_ref.abstractTargetDataElementRef = abstract_target_ref
        assert instance_ref.abstractTargetDataElementRef == abstract_target_ref

        # Test baseRef methods (inherited from VariableInAtomicSwcInstanceRef)
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.baseRef = base_ref
        assert instance_ref.baseRef == base_ref

        # Test contextPortRef methods (inherited from VariableInAtomicSwcInstanceRef)
        context_port_ref = RefType()
        context_port_ref.setValue("/Context/Port")
        instance_ref.contextPortRef = context_port_ref
        assert instance_ref.contextPortRef == context_port_ref

        # Test contextRPortRef methods
        context_r_port_ref = RefType()
        context_r_port_ref.setValue("/Context/R/Port")
        instance_ref.setContextRPortRef(context_r_port_ref)
        assert instance_ref.getContextRPortRef() == context_r_port_ref

        # Test targetDataElementRef methods
        target_data_element_ref = RefType()
        target_data_element_ref.setValue("/Target/DataElement")
        instance_ref.setTargetDataElementRef(target_data_element_ref)
        assert instance_ref.getTargetDataElementRef() == target_data_element_ref


class TestInnerPortGroupInCompositionInstanceRef:
    """Test class for InnerPortGroupInCompositionInstanceRef class."""

    def test_inner_port_group_in_composition_instance_ref_initialization(self):
        """Test InnerPortGroupInCompositionInstanceRef initialization and methods."""
        instance_ref = InnerPortGroupInCompositionInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextRefs == []
        assert instance_ref.targetRef is None

        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref

        # Test contextRefs methods
        context_ref = RefType()
        context_ref.setValue("/Context/Ref")
        instance_ref.addContextRefs(context_ref)
        assert context_ref in instance_ref.getContextRefs()

        # Test targetRef methods
        target_ref = RefType()
        target_ref.setValue("/Target/Ref")
        instance_ref.setTargetRef(target_ref)
        assert instance_ref.getTargetRef() == target_ref
