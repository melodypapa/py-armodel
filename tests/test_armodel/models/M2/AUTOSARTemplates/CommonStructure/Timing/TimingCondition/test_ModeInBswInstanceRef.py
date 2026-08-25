"""
This module contains tests for the ModeInBswInstanceRef class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import ModeInBswInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestModeInBswInstanceRef:
    """
    Test class for ModeInBswInstanceRef functionality.
    """

    def test_initialization(self):
        obj = ModeInBswInstanceRef()
        assert isinstance(obj, ModeInBswInstanceRef)
        assert obj.getContextBswImplementationRef() is None
        assert obj.getContextModeDeclarationGroupPrototypeRef() is None
        assert obj.getTargetModeDeclarationRef() is None

    def test_get_set_context_bsw_implementation_ref(self):
        obj = ModeInBswInstanceRef()
        ref = RefType().setValue("/Pkg/BswImpl").setDest("BSW-IMPLEMENTATION")
        assert obj.setContextBswImplementationRef(ref) is obj
        assert obj.getContextBswImplementationRef() is ref
        assert obj.getContextBswImplementationRef().getValue() == "/Pkg/BswImpl"
        assert obj.getContextBswImplementationRef().getDest() == "BSW-IMPLEMENTATION"

    def test_set_context_bsw_implementation_ref_none_noop(self):
        obj = ModeInBswInstanceRef()
        ref = RefType().setValue("/Pkg/BswImpl").setDest("BSW-IMPLEMENTATION")
        obj.setContextBswImplementationRef(ref)
        assert obj.setContextBswImplementationRef(None) is obj
        assert obj.getContextBswImplementationRef() is ref

    def test_get_set_context_mode_declaration_group_prototype_ref(self):
        obj = ModeInBswInstanceRef()
        ref = RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        assert obj.setContextModeDeclarationGroupPrototypeRef(ref) is obj
        assert obj.getContextModeDeclarationGroupPrototypeRef() is ref
        assert obj.getContextModeDeclarationGroupPrototypeRef().getValue() == "/Pkg/Mdgp"

    def test_set_context_mode_declaration_group_prototype_ref_none_noop(self):
        obj = ModeInBswInstanceRef()
        ref = RefType().setValue("/Pkg/Mdgp").setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        obj.setContextModeDeclarationGroupPrototypeRef(ref)
        assert obj.setContextModeDeclarationGroupPrototypeRef(None) is obj
        assert obj.getContextModeDeclarationGroupPrototypeRef() is ref

    def test_get_set_target_mode_declaration_ref(self):
        obj = ModeInBswInstanceRef()
        ref = RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION")
        assert obj.setTargetModeDeclarationRef(ref) is obj
        assert obj.getTargetModeDeclarationRef() is ref
        assert obj.getTargetModeDeclarationRef().getValue() == "/Pkg/Mode"

    def test_set_target_mode_declaration_ref_none_noop(self):
        obj = ModeInBswInstanceRef()
        ref = RefType().setValue("/Pkg/Mode").setDest("MODE-DECLARATION")
        obj.setTargetModeDeclarationRef(ref)
        assert obj.setTargetModeDeclarationRef(None) is obj
        assert obj.getTargetModeDeclarationRef() is ref
