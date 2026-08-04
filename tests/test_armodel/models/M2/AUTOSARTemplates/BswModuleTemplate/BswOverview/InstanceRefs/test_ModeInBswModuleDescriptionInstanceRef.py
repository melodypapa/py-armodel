from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import ModeInBswModuleDescriptionInstanceRef


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
        value = "BaseRefValue"
        result = obj.setBaseRef(value)
        assert result == obj
        assert obj.getBaseRef() == value
        obj.setBaseRef(None)
        assert obj.getBaseRef() == value

    def test_get_set_context_mode_declaration_group_ref(self):
        obj = ModeInBswModuleDescriptionInstanceRef()
        value = "ContextRefValue"
        result = obj.setContextModeDeclarationGroupRef(value)
        assert result == obj
        assert obj.getContextModeDeclarationGroupRef() == value
        obj.setContextModeDeclarationGroupRef(None)
        assert obj.getContextModeDeclarationGroupRef() == value

    def test_get_set_target_mode_ref(self):
        obj = ModeInBswModuleDescriptionInstanceRef()
        value = "TargetModeValue"
        result = obj.setTargetModeRef(value)
        assert result == obj
        assert obj.getTargetModeRef() == value
        obj.setTargetModeRef(None)
        assert obj.getTargetModeRef() == value
