import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototypeMapping, ModeDeclaration, ModeRequestTypeMap, ModeDeclarationGroup, ModeDeclarationGroupPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, PositiveInteger, RefType, TRefType


class TestModeDeclarationGroupPrototypeMapping:
    def test_initialization(self):
        """Test ModeDeclarationGroupPrototypeMapping initialization"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping is not None
        assert mapping.firstModeGroupRef is None
        assert mapping.modeDeclarationMappingSetRef is None
        assert mapping.secondModeGroupRef is None

    def test_get_first_mode_group_ref(self):
        """Test getFirstModeGroupRef method"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping.getFirstModeGroupRef() is None

    def test_set_first_mode_group_ref(self):
        """Test setFirstModeGroupRef method"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        test_value = RefType().setValue("ModeGroup1")
        result = mapping.setFirstModeGroupRef(test_value)
        assert result is mapping  # Method chaining
        assert mapping.getFirstModeGroupRef() == test_value

    def test_set_first_mode_group_ref_none(self):
        """Test setFirstModeGroupRef with None value"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        result = mapping.setFirstModeGroupRef(None)
        assert result is mapping  # Method chaining
        assert mapping.getFirstModeGroupRef() is None

    def test_get_mode_declaration_mapping_set_ref(self):
        """Test getModeDeclarationMappingSetRef method"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping.getModeDeclarationMappingSetRef() is None

    def test_set_mode_declaration_mapping_set_ref(self):
        """Test setModeDeclarationMappingSetRef method"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        test_value = RefType().setValue("MappingSetRef")
        result = mapping.setModeDeclarationMappingSetRef(test_value)
        assert result is mapping  # Method chaining
        assert mapping.getModeDeclarationMappingSetRef() == test_value

    def test_set_mode_declaration_mapping_set_ref_none(self):
        """Test setModeDeclarationMappingSetRef with None value"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        result = mapping.setModeDeclarationMappingSetRef(None)
        assert result is mapping  # Method chaining
        assert mapping.getModeDeclarationMappingSetRef() is None

    def test_get_second_mode_group_ref(self):
        """Test getSecondModeGroupRef method"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping.getSecondModeGroupRef() is None

    def test_set_second_mode_group_ref(self):
        """Test setSecondModeGroupRef method"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        test_value = RefType().setValue("ModeGroup2")
        result = mapping.setSecondModeGroupRef(test_value)
        assert result is mapping  # Method chaining
        assert mapping.getSecondModeGroupRef() == test_value

    def test_set_second_mode_group_ref_none(self):
        """Test setSecondModeGroupRef with None value"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        result = mapping.setSecondModeGroupRef(None)
        assert result is mapping  # Method chaining
        assert mapping.getSecondModeGroupRef() is None

    def test_all_properties(self):
        """Test setting all properties"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        
        ref1 = RefType().setValue("ModeGroup1")
        ref2 = RefType().setValue("ModeGroup2")
        set_ref = RefType().setValue("MappingSetRef")
        
        mapping.setFirstModeGroupRef(ref1)
        mapping.setSecondModeGroupRef(ref2)
        mapping.setModeDeclarationMappingSetRef(set_ref)
        
        assert mapping.getFirstModeGroupRef() == ref1
        assert mapping.getSecondModeGroupRef() == ref2
        assert mapping.getModeDeclarationMappingSetRef() == set_ref


class TestModeDeclaration:
    def test_initialization(self):
        """Test ModeDeclaration initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_decl = ModeDeclaration(ar_root, "TestMode")
        
        assert mode_decl is not None
        assert mode_decl.getShortName() == "TestMode"
        assert mode_decl.value is None

    def test_set_value(self):
        """Test setValue method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_decl = ModeDeclaration(ar_root, "TestMode")
        
        test_value = ARNumerical().setValue(1)
        result = mode_decl.setValue(test_value)
        assert result is mode_decl  # Method chaining
        assert mode_decl.getValue() == test_value

    def test_set_value_none(self):
        """Test setValue with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_decl = ModeDeclaration(ar_root, "TestMode")
        
        result = mode_decl.setValue(None)
        assert result is mode_decl  # Method chaining
        assert mode_decl.getValue() is None

    def test_get_value(self):
        """Test getValue method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_decl = ModeDeclaration(ar_root, "TestMode")
        assert mode_decl.getValue() is None


class TestModeRequestTypeMap:
    def test_initialization(self):
        """Test ModeRequestTypeMap initialization"""
        map_obj = ModeRequestTypeMap()
        assert map_obj is not None
        assert map_obj.implementationDataTypeRef is None
        assert map_obj.modeGroupRef is None

    def test_get_implementation_data_type_ref(self):
        """Test getImplementationDataTypeRef method"""
        map_obj = ModeRequestTypeMap()
        assert map_obj.getImplementationDataTypeRef() is None

    def test_set_implementation_data_type_ref(self):
        """Test setImplementationDataTypeRef method"""
        map_obj = ModeRequestTypeMap()
        test_value = RefType().setValue("ImplDataTypeRef")
        result = map_obj.setImplementationDataTypeRef(test_value)
        assert result is map_obj  # Method chaining
        assert map_obj.getImplementationDataTypeRef() == test_value

    def test_get_mode_group_ref(self):
        """Test getModeGroupRef method"""
        map_obj = ModeRequestTypeMap()
        assert map_obj.getModeGroupRef() is None

    def test_set_mode_group_ref(self):
        """Test setModeGroupRef method"""
        map_obj = ModeRequestTypeMap()
        test_value = RefType().setValue("ModeGroupRef")
        result = map_obj.setModeGroupRef(test_value)
        assert result is map_obj  # Method chaining
        assert map_obj.getModeGroupRef() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        map_obj = ModeRequestTypeMap()
        
        impl_ref = RefType().setValue("ImplDataTypeRef")
        group_ref = RefType().setValue("ModeGroupRef")
        
        map_obj.setImplementationDataTypeRef(impl_ref)
        map_obj.setModeGroupRef(group_ref)
        
        assert map_obj.getImplementationDataTypeRef() == impl_ref
        assert map_obj.getModeGroupRef() == group_ref


class TestModeDeclarationGroup:
    def test_initialization(self):
        """Test ModeDeclarationGroup initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        
        assert mode_group is not None
        assert mode_group.getShortName() == "TestModeGroup"
        assert mode_group.initialModeRef is None
        assert mode_group.modeDeclarations == []
        assert mode_group.modeManagerErrorBehavior is None
        assert mode_group.modeTransition is None
        assert mode_group.modeUserErrorBehavior is None
        assert mode_group.onTransitionValue is None

    def test_create_mode_declaration(self):
        """Test createModeDeclaration method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        
        mode_decl = mode_group.createModeDeclaration("TestMode")
        assert mode_decl is not None
        assert mode_decl.getShortName() == "TestMode"
        # Note: We can't verify the modeDeclarations list directly since it's not a public attribute
        # but we can verify the element was added to the parent's elements list

    def test_get_mode_declarations_empty(self):
        """Test getModeDeclarations method with empty list"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        
        declarations = mode_group.getModeDeclarations()
        assert declarations == []

    def test_get_mode_declarations(self):
        """Test getModeDeclarations method with multiple declarations"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        
        # Create mode declarations in reverse order to test sorting
        mode_group.createModeDeclaration("Mode2")
        mode_group.createModeDeclaration("Mode1")
        
        declarations = mode_group.getModeDeclarations()
        assert len(declarations) == 2
        assert declarations[0].getShortName() == "Mode1"
        assert declarations[1].getShortName() == "Mode2"

    def test_set_initial_mode_ref(self):
        """Test setInitialModeRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        
        test_value = RefType().setValue("InitialModeRef")
        result = mode_group.setInitialModeRef(test_value)
        assert result is mode_group  # Method chaining
        assert mode_group.getInitialModeRef() == test_value

    def test_get_initial_mode_ref(self):
        """Test getInitialModeRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        assert mode_group.getInitialModeRef() is None

    def test_set_on_transition_value(self):
        """Test setOnTransitionValue method with integer"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        
        result = mode_group.setOnTransitionValue(42)
        assert result is mode_group  # Method chaining
        # When an integer is passed, it should be converted to ARNumerical
        assert isinstance(mode_group.onTransitionValue, ARNumerical)
        assert mode_group.onTransitionValue.getValue() == 42

    def test_get_on_transition_value(self):
        """Test getOnTransitionValue method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        assert mode_group.getOnTransitionValue() is None


class TestModeDeclarationGroupPrototype:
    def test_initialization(self):
        """Test ModeDeclarationGroupPrototype initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        
        assert mode_group_proto is not None
        assert mode_group_proto.getShortName() == "TestModeGroupProto"
        assert mode_group_proto._swCalibrationAccess is None
        assert mode_group_proto.typeTRef is None

    def test_sw_calibration_access_property_getter(self):
        """Test sw_calibration_access property getter"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        
        # Initially None
        assert mode_group_proto.sw_calibration_access is None
        
        # Set a value
        mode_group_proto._swCalibrationAccess = "readOnly"
        assert mode_group_proto.sw_calibration_access == "readOnly"

    def test_sw_calibration_access_property_setter_valid_values(self):
        """Test sw_calibration_access property setter with valid values"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        
        # Test valid values
        mode_group_proto.sw_calibration_access = "notAccessible"
        assert mode_group_proto._swCalibrationAccess == "notAccessible"
        
        mode_group_proto.sw_calibration_access = "readOnly"
        assert mode_group_proto._swCalibrationAccess == "readOnly"
        
        mode_group_proto.sw_calibration_access = "readWrite"
        assert mode_group_proto._swCalibrationAccess == "readWrite"

    def test_sw_calibration_access_property_setter_invalid_value(self):
        """Test sw_calibration_access property setter with invalid value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        
        with pytest.raises(ValueError, match=r"Invalid SwCalibrationAccess <invalid> of ModeDeclarationGroupPrototype <TestModeGroupProto>"):
            mode_group_proto.sw_calibration_access = "invalid"

        def test_get_sw_calibration_access(self):
            """Test getSwCalibrationAccess method"""
            parent = AUTOSAR.getInstance()
            ar_root = parent.createARPackage("AUTOSAR")
            mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
            
            # Initially should return None
            assert mode_group_proto.getSwCalibrationAccess() is None
            
            # Set a value and check it's returned
            mode_group_proto.setSwCalibrationAccess("readOnly")
            assert mode_group_proto.getSwCalibrationAccess() == "readOnly"
    def test_set_sw_calibration_access(self):
        """Test setSwCalibrationAccess method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        
        # Test setting a valid value
        result = mode_group_proto.setSwCalibrationAccess("readOnly")
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getSwCalibrationAccess() == "readOnly"
        
        # Test setting another value
        mode_group_proto.setSwCalibrationAccess("readWrite")
        assert mode_group_proto.getSwCalibrationAccess() == "readWrite"

    def test_get_type_t_ref(self):
        """Test getTypeTRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        assert mode_group_proto.getTypeTRef() is None

    def test_set_type_t_ref(self):
        """Test setTypeTRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        test_value = TRefType().setValue("TypeTRefValue")
        result = mode_group_proto.setTypeTRef(test_value)
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getTypeTRef() == test_value

    def test_set_type_t_ref_none(self):
        """Test setTypeTRef with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        result = mode_group_proto.setTypeTRef(None)
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getTypeTRef() is None