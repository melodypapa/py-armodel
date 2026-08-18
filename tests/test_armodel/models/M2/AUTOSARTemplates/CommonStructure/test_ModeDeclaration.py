from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
    ModeDeclaration,
    ModeDeclarationGroup,
    ModeDeclarationGroupPrototype,
    ModeDeclarationGroupPrototypeMapping,
    ModeErrorBehavior,
    ModeErrorReactionPolicyEnum,
    ModeRequestTypeMap,
    ModeTransition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TRefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum


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
        assert mode_decl.getValue() is None

    def test_get_set_value(self):
        """Test getValue and setValue methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_decl = ModeDeclaration(ar_root, "TestMode")

        test_value = PositiveInteger().setValue("4")
        result = mode_decl.setValue(test_value)
        assert result is mode_decl  # Method chaining
        assert mode_decl.getValue() == test_value

    def test_set_value_none_noop(self):
        """Test setValue with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_decl = ModeDeclaration(ar_root, "TestMode")

        test_value = PositiveInteger().setValue("4")
        mode_decl.setValue(test_value)
        result = mode_decl.setValue(None)
        assert result is mode_decl  # Method chaining
        assert mode_decl.getValue() == test_value


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
        assert mode_group.modeTransitions == []
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
        """Test setOnTransitionValue method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        result = mode_group.setOnTransitionValue(PositiveInteger().setValue("42"))
        assert result is mode_group  # Method chaining
        assert isinstance(mode_group.onTransitionValue, PositiveInteger)
        assert mode_group.onTransitionValue.getValue() == 42

    def test_get_on_transition_value(self):
        """Test getOnTransitionValue method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        assert mode_group.getOnTransitionValue() is None

    def test_set_initial_mode_ref_none(self):
        """Test setInitialModeRef with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        mode_group.setInitialModeRef(RefType().setValue("InitialModeRef"))
        result = mode_group.setInitialModeRef(None)
        assert result is mode_group  # Method chaining
        assert mode_group.getInitialModeRef() is not None

    def test_set_on_transition_value_none(self):
        """Test setOnTransitionValue with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        mode_group.setOnTransitionValue(PositiveInteger().setValue("42"))
        result = mode_group.setOnTransitionValue(None)
        assert result is mode_group  # Method chaining
        assert mode_group.getOnTransitionValue() is not None

    def test_create_mode_transition(self):
        """Test createModeTransition method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        transition = mode_group.createModeTransition("Transition1")
        assert transition is not None
        assert isinstance(transition, ModeTransition)
        assert transition.getShortName() == "Transition1"
        assert transition.getParent() is mode_group
        assert transition in mode_group.getModeTransitions()

    def test_create_mode_transition_duplicate(self):
        """Test createModeTransition returns existing instance for duplicate short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        first = mode_group.createModeTransition("Transition1")
        second = mode_group.createModeTransition("Transition1")
        assert second is first
        assert len(mode_group.getModeTransitions()) == 1

    def test_get_mode_transitions_empty(self):
        """Test getModeTransitions method with empty list"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        assert mode_group.getModeTransitions() == []

    def test_get_mode_manager_error_behavior(self):
        """Test getModeManagerErrorBehavior method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        assert mode_group.getModeManagerErrorBehavior() is None

    def test_set_mode_manager_error_behavior(self):
        """Test setModeManagerErrorBehavior method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        error_behavior = ModeErrorBehavior().setErrorReactionPolicy(ModeErrorReactionPolicyEnum().setValue(ModeErrorReactionPolicyEnum.DEFAULT_MODE))
        result = mode_group.setModeManagerErrorBehavior(error_behavior)
        assert result is mode_group  # Method chaining
        assert mode_group.getModeManagerErrorBehavior() == error_behavior

    def test_set_mode_manager_error_behavior_none(self):
        """Test setModeManagerErrorBehavior with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        error_behavior = ModeErrorBehavior().setErrorReactionPolicy(ModeErrorReactionPolicyEnum().setValue(ModeErrorReactionPolicyEnum.DEFAULT_MODE))
        mode_group.setModeManagerErrorBehavior(error_behavior)
        result = mode_group.setModeManagerErrorBehavior(None)
        assert result is mode_group  # Method chaining
        assert mode_group.getModeManagerErrorBehavior() is error_behavior

    def test_get_mode_user_error_behavior(self):
        """Test getModeUserErrorBehavior method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")
        assert mode_group.getModeUserErrorBehavior() is None

    def test_set_mode_user_error_behavior(self):
        """Test setModeUserErrorBehavior method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        error_behavior = ModeErrorBehavior().setErrorReactionPolicy(ModeErrorReactionPolicyEnum().setValue(ModeErrorReactionPolicyEnum.LAST_MODE))
        result = mode_group.setModeUserErrorBehavior(error_behavior)
        assert result is mode_group  # Method chaining
        assert mode_group.getModeUserErrorBehavior() == error_behavior

    def test_set_mode_user_error_behavior_none(self):
        """Test setModeUserErrorBehavior with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group = ModeDeclarationGroup(ar_root, "TestModeGroup")

        error_behavior = ModeErrorBehavior().setErrorReactionPolicy(ModeErrorReactionPolicyEnum().setValue(ModeErrorReactionPolicyEnum.LAST_MODE))
        mode_group.setModeUserErrorBehavior(error_behavior)
        result = mode_group.setModeUserErrorBehavior(None)
        assert result is mode_group  # Method chaining
        assert mode_group.getModeUserErrorBehavior() is error_behavior


class TestModeTransition:
    def test_initialization(self):
        """Test ModeTransition initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")

        assert transition is not None
        assert transition.getShortName() == "TestTransition"
        assert transition.enteredModeRef is None
        assert transition.exitedModeRef is None

    def test_get_entered_mode_ref(self):
        """Test getEnteredModeRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")
        assert transition.getEnteredModeRef() is None

    def test_set_entered_mode_ref(self):
        """Test setEnteredModeRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")

        test_value = RefType().setValue("EnteredModeRef")
        result = transition.setEnteredModeRef(test_value)
        assert result is transition  # Method chaining
        assert transition.getEnteredModeRef() == test_value

    def test_set_entered_mode_ref_none(self):
        """Test setEnteredModeRef with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")

        test_value = RefType().setValue("EnteredModeRef")
        transition.setEnteredModeRef(test_value)
        result = transition.setEnteredModeRef(None)
        assert result is transition  # Method chaining
        assert transition.getEnteredModeRef() is test_value

    def test_get_exited_mode_ref(self):
        """Test getExitedModeRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")
        assert transition.getExitedModeRef() is None

    def test_set_exited_mode_ref(self):
        """Test setExitedModeRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")

        test_value = RefType().setValue("ExitedModeRef")
        result = transition.setExitedModeRef(test_value)
        assert result is transition  # Method chaining
        assert transition.getExitedModeRef() == test_value

    def test_set_exited_mode_ref_none(self):
        """Test setExitedModeRef with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        transition = ModeTransition(ar_root, "TestTransition")

        test_value = RefType().setValue("ExitedModeRef")
        transition.setExitedModeRef(test_value)
        result = transition.setExitedModeRef(None)
        assert result is transition  # Method chaining
        assert transition.getExitedModeRef() is test_value


class TestModeDeclarationGroupPrototype:
    def test_initialization(self):
        """Test ModeDeclarationGroupPrototype initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")

        assert mode_group_proto is not None
        assert mode_group_proto.getShortName() == "TestModeGroupProto"
        assert mode_group_proto.getSwCalibrationAccess() is None
        assert mode_group_proto.getTypeTRef() is None

    def test_get_sw_calibration_access(self):
        """Test getSwCalibrationAccess method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")

        assert mode_group_proto.getSwCalibrationAccess() is None

    def test_set_sw_calibration_access(self):
        """Test setSwCalibrationAccess method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")

        cal_access = SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_ONLY)
        result = mode_group_proto.setSwCalibrationAccess(cal_access)
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getSwCalibrationAccess() == cal_access

    def test_set_sw_calibration_access_none(self):
        """Test setSwCalibrationAccess with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")

        cal_access = SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_WRITE)
        mode_group_proto.setSwCalibrationAccess(cal_access)
        result = mode_group_proto.setSwCalibrationAccess(None)
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getSwCalibrationAccess() == cal_access

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
        """Test setTypeTRef with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mode_group_proto = ModeDeclarationGroupPrototype(ar_root, "TestModeGroupProto")
        result = mode_group_proto.setTypeTRef(None)
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getTypeTRef() is None

        test_value = TRefType().setValue("TypeTRefValue")
        mode_group_proto.setTypeTRef(test_value)
        result = mode_group_proto.setTypeTRef(None)
        assert result is mode_group_proto  # Method chaining
        assert mode_group_proto.getTypeTRef() == test_value


class TestModeErrorReactionPolicyEnum:
    def test_initialization(self):
        """Test ModeErrorReactionPolicyEnum member values"""
        enum = ModeErrorReactionPolicyEnum()
        assert enum.DEFAULT_MODE == "defaultMode"
        assert enum.LAST_MODE == "lastMode"
        assert "defaultMode" in enum.getEnumValues()
        assert "lastMode" in enum.getEnumValues()

    def test_enum_values(self):
        """Test ModeErrorReactionPolicyEnum literal values"""
        assert ModeErrorReactionPolicyEnum.DEFAULT_MODE == "defaultMode"
        assert ModeErrorReactionPolicyEnum.LAST_MODE == "lastMode"

    def test_valid_values(self):
        """Test ModeErrorReactionPolicyEnum valid values in __init__"""
        enum = ModeErrorReactionPolicyEnum()
        valid_values = [
            ModeErrorReactionPolicyEnum.DEFAULT_MODE,
            ModeErrorReactionPolicyEnum.LAST_MODE,
        ]
        for value in valid_values:
            enum.setValue(value)
            assert enum.getText() == value


class TestModeErrorBehavior:
    def test_initialization(self):
        """Test ModeErrorBehavior initialization"""
        error_behavior = ModeErrorBehavior()
        assert error_behavior is not None
        assert error_behavior.defaultModeRef is None
        assert error_behavior.errorReactionPolicy is None

    def test_get_set_default_mode_ref(self):
        """Test getDefaultModeRef and setDefaultModeRef methods"""
        error_behavior = ModeErrorBehavior()
        test_ref = RefType().setValue("TestModeRef")

        # Test setter returns self
        result = error_behavior.setDefaultModeRef(test_ref)
        assert result is error_behavior

        # Test value round-trips
        assert error_behavior.getDefaultModeRef() == test_ref

        # Test None is no-op
        error_behavior.setDefaultModeRef(None)
        assert error_behavior.getDefaultModeRef() == test_ref

    def test_get_set_error_reaction_policy(self):
        """Test getErrorReactionPolicy and setErrorReactionPolicy methods"""
        error_behavior = ModeErrorBehavior()
        test_policy = ModeErrorReactionPolicyEnum().setValue(ModeErrorReactionPolicyEnum.DEFAULT_MODE)

        # Test setter returns self
        result = error_behavior.setErrorReactionPolicy(test_policy)
        assert result is error_behavior

        # Test value round-trips as a ModeErrorReactionPolicyEnum instance
        assert error_behavior.getErrorReactionPolicy() == test_policy
        assert isinstance(error_behavior.getErrorReactionPolicy(), ModeErrorReactionPolicyEnum)
        assert error_behavior.getErrorReactionPolicy().getText() == "defaultMode"

        # Test None is no-op
        error_behavior.setErrorReactionPolicy(None)
        assert error_behavior.getErrorReactionPolicy() == test_policy

    def test_method_chaining(self):
        """Test method chaining with ModeErrorBehavior"""
        error_behavior = ModeErrorBehavior()
        test_ref = RefType().setValue("TestModeRef")
        test_policy = ModeErrorReactionPolicyEnum().setValue(ModeErrorReactionPolicyEnum.LAST_MODE)

        result = error_behavior.setDefaultModeRef(test_ref).setErrorReactionPolicy(test_policy)

        assert result is error_behavior
        assert error_behavior.getDefaultModeRef() == test_ref
        assert error_behavior.getErrorReactionPolicy() == test_policy


class TestModeActivationKind:
    def test_initialization(self):
        """Test ModeActivationKind initialization"""
        activation_kind = ModeActivationKind()
        assert activation_kind.ON_ENTRY == "onEntry"
        assert activation_kind.ON_EXIT == "onExit"
        assert activation_kind.ON_TRANSITION == "onTransition"
        assert "onEntry" in activation_kind.getEnumValues()
        assert "onExit" in activation_kind.getEnumValues()
        assert "onTransition" in activation_kind.getEnumValues()

    def test_enum_values(self):
        """Test ModeActivationKind literal values"""
        assert ModeActivationKind.ON_ENTRY == "onEntry"
        assert ModeActivationKind.ON_EXIT == "onExit"
        assert ModeActivationKind.ON_TRANSITION == "onTransition"

    def test_valid_values(self):
        """Test ModeActivationKind valid values in __init__"""
        enum = ModeActivationKind()
        valid_values = [ModeActivationKind.ON_ENTRY, ModeActivationKind.ON_EXIT, ModeActivationKind.ON_TRANSITION]
        for value in valid_values:
            enum.setValue(value)
            assert enum.getText() == value
