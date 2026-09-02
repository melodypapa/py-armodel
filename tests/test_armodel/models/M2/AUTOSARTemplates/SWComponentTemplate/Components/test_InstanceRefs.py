"""
This module contains comprehensive tests for the InstanceRefs module in SWComponentTemplate.Components.
Tests cover all classes and methods in the InstanceRefs.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
    ModeGroupInAtomicSwcInstanceRef,
    OperationInAtomicSwcInstanceRef,
    PModeGroupInAtomicSwcInstanceRef,
    POperationInAtomicSwcInstanceRef,
    PTriggerInAtomicSwcTypeInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
    TriggerInAtomicSwcInstanceRef,
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


class TestTriggerInAtomicSwcInstanceRef:
    """Test class for TriggerInAtomicSwcInstanceRef abstract class."""

    def test_trigger_in_atomic_swc_instance_ref_abstract(self):
        """Test that TriggerInAtomicSwcInstanceRef is an abstract class."""
        with pytest.raises(TypeError):
            TriggerInAtomicSwcInstanceRef()

    def test_concrete_subclass_initialization(self):
        """Test __init__ defaults of the abstract class through a concrete subclass."""
        instance_ref = PTriggerInAtomicSwcTypeInstanceRef()

        assert instance_ref.baseRef is None
        assert instance_ref.contextPortRef is None
        assert instance_ref.targetRef is None


class TestPTriggerInAtomicSwcTypeInstanceRef:
    """Test class for PTriggerInAtomicSwcTypeInstanceRef class."""

    def test_p_trigger_in_atomic_swc_type_instance_ref_initialization(self):
        """Test PTriggerInAtomicSwcTypeInstanceRef initialization and methods."""
        instance_ref = PTriggerInAtomicSwcTypeInstanceRef()

        assert instance_ref.contextPPortRef is None
        assert instance_ref.targetTriggerRef is None

        # Test baseRef methods (inherited from TriggerInAtomicSwcInstanceRef)
        base_ref = RefType()
        base_ref.setValue("/Base/Ref")
        result = instance_ref.setBaseRef(base_ref)
        assert result is instance_ref
        assert instance_ref.getBaseRef() == base_ref

        # Test contextPortRef methods (inherited from TriggerInAtomicSwcInstanceRef)
        context_port_ref = RefType()
        context_port_ref.setValue("/Context/Port")
        instance_ref.setContextPortRef(context_port_ref)
        assert instance_ref.getContextPortRef() == context_port_ref

        # Test targetRef methods (inherited from TriggerInAtomicSwcInstanceRef)
        target_ref = RefType()
        target_ref.setValue("/Target/Ref")
        instance_ref.setTargetRef(target_ref)
        assert instance_ref.getTargetRef() == target_ref

        # Test contextPPortRef methods
        context_p_port_ref = RefType()
        context_p_port_ref.setValue("/Context/P/Port")
        instance_ref.setContextPPortRef(context_p_port_ref)
        assert instance_ref.getContextPPortRef() == context_p_port_ref

        # Test targetTriggerRef methods
        target_trigger_ref = RefType()
        target_trigger_ref.setValue("/Target/Trigger")
        instance_ref.setTargetTriggerRef(target_trigger_ref)
        assert instance_ref.getTargetTriggerRef() == target_trigger_ref

    def test_set_none_is_noop(self):
        """Test that setters are no-ops when the value is None."""
        instance_ref = PTriggerInAtomicSwcTypeInstanceRef()

        context_ref = RefType().setValue("/Context/P/Port")
        instance_ref.setContextPPortRef(context_ref)
        instance_ref.setContextPPortRef(None)
        assert instance_ref.getContextPPortRef() == context_ref

        trigger_ref = RefType().setValue("/Target/Trigger")
        instance_ref.setTargetTriggerRef(trigger_ref)
        instance_ref.setTargetTriggerRef(None)
        assert instance_ref.getTargetTriggerRef() == trigger_ref


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

    def test_initialization(self):
        """Defaults: baseRef None, contextRefs [], targetRef None; isinstance AtpInstanceRef, not Referrable."""
        instance_ref = InnerPortGroupInCompositionInstanceRef()

        assert instance_ref.getBaseRef() is None
        assert instance_ref.getContextRefs() == []
        assert instance_ref.getTargetRef() is None
        assert isinstance(instance_ref, AtpInstanceRef)
        assert not isinstance(instance_ref, Referrable)

    def test_base_round_trip_and_none_noop(self):
        """set/get baseRef round-trips and returns self; None is a no-op."""
        base_ref = RefType()
        base_ref.setValue("/Base/Comp")
        base_ref.setDest("COMPOSITION-SW-COMPONENT-TYPE")
        instance_ref = InnerPortGroupInCompositionInstanceRef()

        assert instance_ref.setBaseRef(base_ref) is instance_ref
        assert instance_ref.getBaseRef() == base_ref

        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef() == base_ref

    def test_context_refs_ordered_and_none_noop(self):
        """addContextRef appends in order and returns self; None is a no-op."""
        c1 = RefType()
        c1.setValue("/Ctx/A")
        c2 = RefType()
        c2.setValue("/Ctx/B")
        instance_ref = InnerPortGroupInCompositionInstanceRef()

        assert instance_ref.addContextRef(c1) is instance_ref
        instance_ref.addContextRef(c2)
        assert instance_ref.getContextRefs() == [c1, c2]

        instance_ref.addContextRef(None)
        assert instance_ref.getContextRefs() == [c1, c2]

    def test_target_round_trip_and_none_noop(self):
        """set/get targetRef round-trips and returns self; None is a no-op."""
        tref = RefType()
        tref.setValue("/Pkg/InnerGroup")
        tref.setDest("PORT-GROUP")
        instance_ref = InnerPortGroupInCompositionInstanceRef()

        assert instance_ref.setTargetRef(tref) is instance_ref
        assert instance_ref.getTargetRef() == tref

        instance_ref.setTargetRef(None)
        assert instance_ref.getTargetRef() == tref


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
