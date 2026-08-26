"""
This module contains tests for the ModeInSwcInstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import ModeInSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestModeInSwcInstanceRef:
    """
    Test class for ModeInSwcInstanceRef functionality.
    """

    def test_initialization(self):
        obj = ModeInSwcInstanceRef()
        assert isinstance(obj, ModeInSwcInstanceRef)
        assert obj.getBaseRef() is None
        assert obj.getContextComponentRefs() == []
        assert obj.getContextModeDeclarationGroupPrototypeRef() is None
        assert obj.getContextPortRef() is None
        assert obj.getTargetModeDeclarationRef() is None

    def test_get_set_base_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/SwcType").setDest("SW-COMPONENT-TYPE")
        assert obj.setBaseRef(ref) is obj
        assert obj.getBaseRef() is ref
        assert obj.getBaseRef().getValue() == "/Pkg/SwcType"

    def test_set_base_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/SwcType").setDest("SW-COMPONENT-TYPE")
        obj.setBaseRef(ref)
        assert obj.setBaseRef(None) is obj
        assert obj.getBaseRef() is ref

    def test_add_context_component_ref(self):
        obj = ModeInSwcInstanceRef()
        ref1 = RefType().setValue("/Pkg/SwcProto1").setDest("SW-COMPONENT-PROTOTYPE")
        ref2 = RefType().setValue("/Pkg/SwcProto2").setDest("SW-COMPONENT-PROTOTYPE")
        assert obj.addContextComponentRef(ref1) is obj
        obj.addContextComponentRef(ref2)
        refs = obj.getContextComponentRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_add_context_component_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref1 = RefType().setValue("/Pkg/SwcProto1").setDest("SW-COMPONENT-PROTOTYPE")
        obj.addContextComponentRef(ref1)
        assert obj.addContextComponentRef(None) is obj
        assert len(obj.getContextComponentRefs()) == 1

    def test_get_set_context_mode_declaration_group_prototype_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        assert obj.setContextModeDeclarationGroupPrototypeRef(ref) is obj
        assert obj.getContextModeDeclarationGroupPrototypeRef() is ref
        assert obj.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"

    def test_set_context_mode_declaration_group_prototype_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        obj.setContextModeDeclarationGroupPrototypeRef(ref)
        assert obj.setContextModeDeclarationGroupPrototypeRef(None) is obj
        assert obj.getContextModeDeclarationGroupPrototypeRef() is ref

    def test_get_set_context_port_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE")
        assert obj.setContextPortRef(ref) is obj
        assert obj.getContextPortRef() is ref
        assert obj.getContextPortRef().getValue() == "/Pkg/Port"

    def test_set_context_port_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Port").setDest("PORT-PROTOTYPE")
        obj.setContextPortRef(ref)
        assert obj.setContextPortRef(None) is obj
        assert obj.getContextPortRef() is ref

    def test_get_set_target_mode_declaration_ref(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION")
        assert obj.setTargetModeDeclarationRef(ref) is obj
        assert obj.getTargetModeDeclarationRef() is ref
        assert obj.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_set_target_mode_declaration_ref_none_noop(self):
        obj = ModeInSwcInstanceRef()
        ref = RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION")
        obj.setTargetModeDeclarationRef(ref)
        assert obj.setTargetModeDeclarationRef(None) is obj
        assert obj.getTargetModeDeclarationRef() is ref
