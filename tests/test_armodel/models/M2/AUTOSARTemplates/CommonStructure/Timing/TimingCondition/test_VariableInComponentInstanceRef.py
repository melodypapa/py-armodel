"""
This module contains tests for the VariableInComponentInstanceRef InstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import VariableInComponentInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestVariableInComponentInstanceRef:
    """
    Test class for VariableInComponentInstanceRef functionality.
    """

    def test_initialization(self):
        iref = VariableInComponentInstanceRef()
        assert isinstance(iref, VariableInComponentInstanceRef)
        assert iref.getContextComponentRefs() == []
        assert iref.getContextPortPrototypeRef() is None
        assert iref.getRootVariableDataPrototypeRef() is None
        assert iref.getContextDataPrototypeRefs() == []
        assert iref.getTargetDataPrototypeRef() is None

    def test_set_context_port_prototype_ref(self):
        iref = VariableInComponentInstanceRef()
        ref = RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE")
        assert iref.setContextPortPrototypeRef(ref) is iref
        assert iref.getContextPortPrototypeRef() is ref

    def test_set_context_port_prototype_ref_none_noop(self):
        iref = VariableInComponentInstanceRef()
        ref = RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE")
        iref.setContextPortPrototypeRef(ref)
        assert iref.setContextPortPrototypeRef(None) is iref
        assert iref.getContextPortPrototypeRef() is ref

    def test_add_context_component_ref(self):
        iref = VariableInComponentInstanceRef()
        ref = RefType().setValue("/Pkg/SwcProto").setDest("SW-COMPONENT-PROTOTYPE")
        assert iref.addContextComponentRef(ref) is iref
        assert len(iref.getContextComponentRefs()) == 1

    def test_add_context_component_ref_none_noop(self):
        iref = VariableInComponentInstanceRef()
        assert iref.addContextComponentRef(None) is iref
        assert iref.getContextComponentRefs() == []

    def test_set_root_variable_data_prototype_ref(self):
        iref = VariableInComponentInstanceRef()
        ref = RefType().setValue("/Pkg/Var").setDest("VARIABLE-DATA-PROTOTYPE")
        assert iref.setRootVariableDataPrototypeRef(ref) is iref
        assert iref.getRootVariableDataPrototypeRef() is ref

    def test_add_context_data_prototype_ref(self):
        iref = VariableInComponentInstanceRef()
        ref = RefType().setValue("/Pkg/CDP").setDest("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE")
        assert iref.addContextDataPrototypeRef(ref) is iref
        assert len(iref.getContextDataPrototypeRefs()) == 1

    def test_set_target_data_prototype_ref(self):
        iref = VariableInComponentInstanceRef()
        ref = RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE")
        assert iref.setTargetDataPrototypeRef(ref) is iref
        assert iref.getTargetDataPrototypeRef() is ref
