from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import ModeInBswModuleDescriptionInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestModeInBswModuleDescriptionInstanceRef:
    """Test cases for the ModeInBswModuleDescriptionInstanceRef class."""

    def test_initialization(self):
        obj = ModeInBswModuleDescriptionInstanceRef()
        assert obj is not None
        assert obj.getBaseRef() is None
        assert obj.getContextModeDeclarationGroupRef() is None
        assert obj.getTargetModeRef() is None

    def test_get_set_base_ref(self):
        obj = ModeInBswModuleDescriptionInstanceRef()
        value = RefType().setValue("/BswModuleDescription")
        result = obj.setBaseRef(value)
        assert result == obj
        assert obj.getBaseRef() == value
        assert obj.getBaseRef().getValue() == "/BswModuleDescription"
        obj.setBaseRef(None)
        assert obj.getBaseRef() == value

    def test_get_set_context_mode_declaration_group_ref(self):
        obj = ModeInBswModuleDescriptionInstanceRef()
        value = RefType().setValue("/ModeDeclarationGroup")
        result = obj.setContextModeDeclarationGroupRef(value)
        assert result == obj
        assert obj.getContextModeDeclarationGroupRef() == value
        assert obj.getContextModeDeclarationGroupRef().getValue() == "/ModeDeclarationGroup"
        obj.setContextModeDeclarationGroupRef(None)
        assert obj.getContextModeDeclarationGroupRef() == value

    def test_get_set_target_mode_ref(self):
        obj = ModeInBswModuleDescriptionInstanceRef()
        value = RefType().setValue("/ModeDeclaration")
        result = obj.setTargetModeRef(value)
        assert result == obj
        assert obj.getTargetModeRef() == value
        assert obj.getTargetModeRef().getValue() == "/ModeDeclaration"
        obj.setTargetModeRef(None)
        assert obj.getTargetModeRef() == value
