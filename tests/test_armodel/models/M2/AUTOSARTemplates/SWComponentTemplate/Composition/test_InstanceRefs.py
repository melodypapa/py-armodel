"""
This module contains comprehensive tests for the InstanceRefs module in SWComponentTemplate.Composition.
Tests cover all classes and methods in the InstanceRefs.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    InstanceEventInCompositionInstanceRef,
    PortInCompositionTypeInstanceRef,
    PPortInCompositionInstanceRef,
    RPortInCompositionInstanceRef,
)


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


class TestInstanceEventInCompositionInstanceRef:
    """Test class for InstanceEventInCompositionInstanceRef class."""

    def test_initialization(self):
        """Test InstanceEventInCompositionInstanceRef initialization and defaults."""
        instance_ref = InstanceEventInCompositionInstanceRef()

        assert instance_ref.getBaseRef() is None
        assert instance_ref.getContextComponentPrototypeRefs() == []
        assert instance_ref.getTargetEventRef() is None

    def test_set_get_base_ref(self):
        """Test setBaseRef and getBaseRef methods."""
        instance_ref = InstanceEventInCompositionInstanceRef()

        base_ref = RefType()
        base_ref.setDest("COMPOSITION-SW-COMPONENT-TYPE")
        base_ref.setValue("/Composition")
        instance_ref.setBaseRef(base_ref)
        assert instance_ref.getBaseRef() == base_ref

        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef() == base_ref

    def test_add_get_context_component_prototype_refs(self):
        """Test addContextComponentPrototypeRef and getContextComponentPrototypeRefs methods."""
        instance_ref = InstanceEventInCompositionInstanceRef()

        ref1 = RefType()
        ref1.setDest("SW-COMPONENT-PROTOTYPE")
        ref1.setValue("/Comp/Inner")
        instance_ref.addContextComponentPrototypeRef(ref1)
        assert instance_ref.getContextComponentPrototypeRefs() == [ref1]

        ref2 = RefType()
        ref2.setDest("SW-COMPONENT-PROTOTYPE")
        ref2.setValue("/Comp/Inner2")
        instance_ref.addContextComponentPrototypeRef(ref2)
        assert instance_ref.getContextComponentPrototypeRefs() == [ref1, ref2]

        instance_ref.addContextComponentPrototypeRef(None)
        assert instance_ref.getContextComponentPrototypeRefs() == [ref1, ref2]

    def test_set_get_target_event_ref(self):
        """Test setTargetEventRef and getTargetEventRef methods."""
        instance_ref = InstanceEventInCompositionInstanceRef()

        target_event_ref = RefType()
        target_event_ref.setDest("TIMING-EVENT")
        target_event_ref.setValue("/Events/Evt")
        instance_ref.setTargetEventRef(target_event_ref)
        assert instance_ref.getTargetEventRef() == target_event_ref

        instance_ref.setTargetEventRef(None)
        assert instance_ref.getTargetEventRef() == target_event_ref
