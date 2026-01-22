"""
This module contains comprehensive tests for the InstanceRefs module in SWComponentTemplate.Composition.
Tests cover all classes and methods in the InstanceRefs.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    PortInCompositionTypeInstanceRef, PPortInCompositionInstanceRef,
    RPortInCompositionInstanceRef, OperationInAtomicSwcInstanceRef,
    POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestPortInCompositionTypeInstanceRef:
    """Test class for PortInCompositionTypeInstanceRef abstract class."""
    
    def test_port_in_composition_type_instance_ref_abstract(self):
        """Test that PortInCompositionTypeInstanceRef is an abstract class."""
        with pytest.raises(TypeError):
            PortInCompositionTypeInstanceRef()


class TestPPortInCompositionInstanceRef:
    """Test class for PPortInCompositionInstanceRef class."""
    
    def test_p_port_in_composition_instance_ref_initialization(self):
        """Test PPortInCompositionInstanceRef initialization and methods."""
        instance_ref = PPortInCompositionInstanceRef()
        
        assert instance_ref.abstractContextComponentRef is None
        assert instance_ref.baseRef is None
        assert instance_ref.targetPortRef is None
        assert instance_ref.contextComponentRef is None
        assert instance_ref.targetPPortRef is None
        
        # Test abstractContextComponentRef methods
        abstract_context_ref = RefType()
        abstract_context_ref.setValue("/Abstract/Context/Component")
        instance_ref.setAbstractContextComponentRef(abstract_context_ref)
        assert instance_ref.getAbstractContextComponentRef() == abstract_context_ref
        
        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref
        
        # Test targetPortRef methods
        target_port_ref = RefType()
        target_port_ref.setValue("/Target/Port")
        instance_ref.setTargetPortRef(target_port_ref)
        assert instance_ref.getTargetPortRef() == target_port_ref
        
        # Test contextComponentRef methods
        context_component_ref = RefType()
        context_component_ref.setValue("/Context/Component")
        instance_ref.setContextComponentRef(context_component_ref)
        assert instance_ref.getContextComponentRef() == context_component_ref
        
        # Test targetPPortRef methods
        target_p_port_ref = RefType()
        target_p_port_ref.setValue("/Target/P/Port")
        instance_ref.setTargetPPortRef(target_p_port_ref)
        assert instance_ref.getTargetPPortRef() == target_p_port_ref


class TestRPortInCompositionInstanceRef:
    """Test class for RPortInCompositionInstanceRef class."""
    
    def test_r_port_in_composition_instance_ref_initialization(self):
        """Test RPortInCompositionInstanceRef initialization and methods."""
        instance_ref = RPortInCompositionInstanceRef()
        
        assert instance_ref.abstractContextComponentRef is None
        assert instance_ref.baseRef is None
        assert instance_ref.targetPortRef is None
        assert instance_ref.contextComponentRef is None
        assert instance_ref.targetRPortRef is None
        
        # Test abstractContextComponentRef methods
        abstract_context_ref = RefType()
        abstract_context_ref.setValue("/Abstract/Context/Component")
        instance_ref.setAbstractContextComponentRef(abstract_context_ref)
        assert instance_ref.getAbstractContextComponentRef() == abstract_context_ref
        
        # Test baseRef methods
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref
        
        # Test targetPortRef methods
        target_port_ref = RefType()
        target_port_ref.setValue("/Target/Port")
        instance_ref.setTargetPortRef(target_port_ref)
        assert instance_ref.getTargetPortRef() == target_port_ref
        
        # Test contextComponentRef methods
        context_component_ref = RefType()
        context_component_ref.setValue("/Context/Component")
        instance_ref.setContextComponentRef(context_component_ref)
        assert instance_ref.getContextComponentRef() == context_component_ref
        
        # Test targetRPortRef methods
        target_r_port_ref = RefType()
        target_r_port_ref.setValue("/Target/R/Port")
        instance_ref.setTargetRPortRef(target_r_port_ref)
        assert instance_ref.getTargetRPortRef() == target_r_port_ref


class TestOperationInAtomicSwcInstanceRef:
    """Test class for OperationInAtomicSwcInstanceRef abstract class."""
    
    def test_operation_in_atomic_swc_instance_ref_abstract(self):
        """Test that OperationInAtomicSwcInstanceRef is an abstract class."""
        with pytest.raises(TypeError):
            OperationInAtomicSwcInstanceRef()


class TestPOperationInAtomicSwcInstanceRef:
    """Test class for POperationInAtomicSwcInstanceRef class."""
    
    def test_p_operation_in_atomic_swc_instance_ref_initialization(self):
        """Test POperationInAtomicSwcInstanceRef initialization and methods."""
        instance_ref = POperationInAtomicSwcInstanceRef()
        
        assert instance_ref.baseRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.targetOperationRef is None
        assert instance_ref.contextPPortRef is None
        assert instance_ref.targetProvidedOperationRef is None
        
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
        
        # Test targetOperationRef methods
        target_operation_ref = RefType()
        target_operation_ref.setValue("/Target/Operation")
        instance_ref.setTargetOperationRef(target_operation_ref)
        assert instance_ref.getTargetOperationRef() == target_operation_ref
        
        # Test contextPPortRef methods
        context_p_port_ref = RefType()
        context_p_port_ref.setValue("/Context/P/Port")
        instance_ref.setContextPPortRef(context_p_port_ref)
        assert instance_ref.getContextPPortRef() == context_p_port_ref
        
        # Test targetProvidedOperationRef methods
        target_provided_operation_ref = RefType()
        target_provided_operation_ref.setValue("/Target/Provided/Operation")
        instance_ref.setTargetProvidedOperationRef(target_provided_operation_ref)
        assert instance_ref.getTargetProvidedOperationRef() == target_provided_operation_ref


class TestROperationInAtomicSwcInstanceRef:
    """Test class for ROperationInAtomicSwcInstanceRef class."""
    
    def test_r_operation_in_atomic_swc_instance_ref_initialization(self):
        """Test ROperationInAtomicSwcInstanceRef initialization and methods."""
        instance_ref = ROperationInAtomicSwcInstanceRef()
        
        assert instance_ref.baseRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.targetOperationRef is None
        assert instance_ref.contextRPortRef is None
        assert instance_ref.targetRequiredOperationRef is None
        
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
        
        # Test targetOperationRef methods
        target_operation_ref = RefType()
        target_operation_ref.setValue("/Target/Operation")
        instance_ref.setTargetOperationRef(target_operation_ref)
        assert instance_ref.getTargetOperationRef() == target_operation_ref
        
        # Test contextRPortRef methods
        context_r_port_ref = RefType()
        context_r_port_ref.setValue("/Context/R/Port")
        instance_ref.setContextRPortRef(context_r_port_ref)
        assert instance_ref.getContextRPortRef() == context_r_port_ref
        
        # Test targetRequiredOperationRef methods
        target_required_operation_ref = RefType()
        target_required_operation_ref.setValue("/Target/Required/Operation")
        instance_ref.setTargetRequiredOperationRef(target_required_operation_ref)
        assert instance_ref.getTargetRequiredOperationRef() == target_required_operation_ref