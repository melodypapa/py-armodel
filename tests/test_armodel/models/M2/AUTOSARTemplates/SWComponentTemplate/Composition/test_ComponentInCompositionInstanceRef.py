"""
This module contains tests for the ComponentInCompositionInstanceRef InstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ComponentInCompositionInstanceRef


class TestComponentInCompositionInstanceRef:
    """
    Test class for ComponentInCompositionInstanceRef functionality.
    """

    def test_initialization(self):
        iref = ComponentInCompositionInstanceRef()
        assert isinstance(iref, ComponentInCompositionInstanceRef)
        assert iref.getContextComponentRefs() == []
        assert iref.getTargetComponentRef() is None

    def test_add_context_component_ref(self):
        iref = ComponentInCompositionInstanceRef()
        ref = RefType().setValue("/Pkg/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE")
        assert iref.addContextComponentRef(ref) is iref
        refs = iref.getContextComponentRefs()
        assert len(refs) == 1
        assert refs[0] is ref

    def test_add_context_component_ref_none_noop(self):
        iref = ComponentInCompositionInstanceRef()
        assert iref.addContextComponentRef(None) is iref
        assert iref.getContextComponentRefs() == []

    def test_set_target_component_ref(self):
        iref = ComponentInCompositionInstanceRef()
        ref = RefType().setValue("/Pkg/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE")
        assert iref.setTargetComponentRef(ref) is iref
        assert iref.getTargetComponentRef() is ref

    def test_set_target_component_ref_none_noop(self):
        iref = ComponentInCompositionInstanceRef()
        ref = RefType().setValue("/Pkg/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE")
        iref.setTargetComponentRef(ref)
        assert iref.setTargetComponentRef(None) is iref
        assert iref.getTargetComponentRef() is ref
