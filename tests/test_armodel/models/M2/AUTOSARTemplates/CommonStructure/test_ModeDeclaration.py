import inspect
from typing import Optional, get_type_hints

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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TRefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum


class TestModeDeclarationGroupPrototypeMapping:
    CLASS_NOTE = "Defines the mapping of two particular ModeDeclarationGroupPrototypes (in the given context) that are unequally named and/or require a reference to a ModeDeclarationMappingSet in order to become compatible by definition of ModeDeclarationMappings."
    MODE_GROUP_NOTE = "ModeDeclarationGroupPrototype to be mapped."
    MODE_DECL_MAPPING_SET_NOTE = "This represents the available mappings of Mode Declarations in the context ot this ModeDeclarationGroup Prototype."

    def test_initialization(self):
        """Test ModeDeclarationGroupPrototypeMapping initialization defaults (Table 4.27, all attrs 0..1)"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping is not None
        assert mapping.firstModeGroupRef is None
        assert mapping.modeDeclarationMappingSetRef is None
        assert mapping.secondModeGroupRef is None

    def test_base_shape(self):
        """ModeDeclarationGroupPrototypeMapping shall derive from ARObject (Table 4.27 Base row)"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert isinstance(mapping, ARObject)

    def test_get_set_first_mode_group_ref(self):
        """Test firstModeGroupRef round-trip, chaining and None no-op (Table 4.27 firstModeGroup)"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping.getFirstModeGroupRef() is None
        test_value = RefType().setValue("/ModeDeclarationGroups/ModeDeclarationGroup1")
        assert mapping.setFirstModeGroupRef(test_value) is mapping
        assert mapping.getFirstModeGroupRef() is test_value
        mapping.setFirstModeGroupRef(None)
        assert mapping.getFirstModeGroupRef() is test_value

    def test_get_set_mode_declaration_mapping_set_ref(self):
        """Test modeDeclarationMappingSetRef round-trip, chaining and None no-op (Table 4.27 modeDeclarationMappingSet)"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping.getModeDeclarationMappingSetRef() is None
        test_value = RefType().setValue("/PortInterfaceMappingSets/ModeDeclarationMappingSet1")
        assert mapping.setModeDeclarationMappingSetRef(test_value) is mapping
        assert mapping.getModeDeclarationMappingSetRef() is test_value
        mapping.setModeDeclarationMappingSetRef(None)
        assert mapping.getModeDeclarationMappingSetRef() is test_value

    def test_get_set_second_mode_group_ref(self):
        """Test secondModeGroupRef round-trip, chaining and None no-op (Table 4.27 secondModeGroup)"""
        mapping = ModeDeclarationGroupPrototypeMapping()
        assert mapping.getSecondModeGroupRef() is None
        test_value = RefType().setValue("/ModeDeclarationGroups/ModeDeclarationGroup2")
        assert mapping.setSecondModeGroupRef(test_value) is mapping
        assert mapping.getSecondModeGroupRef() is test_value
        mapping.setSecondModeGroupRef(None)
        assert mapping.getSecondModeGroupRef() is test_value

    def test_accessor_annotations(self):
        """Accessors shall carry Optional[RefType] hints; setters shall chain ModeDeclarationGroupPrototypeMapping (Table 4.27, 0..1 refs)"""
        for suffix in ("FirstModeGroupRef", "ModeDeclarationMappingSetRef", "SecondModeGroupRef"):
            getter_hints = get_type_hints(getattr(ModeDeclarationGroupPrototypeMapping, "get%s" % suffix))
            assert getter_hints["return"] == Optional[RefType]
            setter_hints = get_type_hints(getattr(ModeDeclarationGroupPrototypeMapping, "set%s" % suffix))
            assert setter_hints["value"] == Optional[RefType]
            assert setter_hints["return"] == ModeDeclarationGroupPrototypeMapping

    def test_spec_note(self):
        """Test the Table 4.27 class note and per-attribute notes (verbatim from the markdown)"""
        assert ModeDeclarationGroupPrototypeMapping.__doc__.strip() == self.CLASS_NOTE
        assert ModeDeclarationGroupPrototypeMapping.__init__.__doc__ is None
        init_source = inspect.getsource(ModeDeclarationGroupPrototypeMapping.__init__)
        assert self.MODE_GROUP_NOTE in init_source
        assert self.MODE_DECL_MAPPING_SET_NOTE in init_source
        for method, note in (
            ("getFirstModeGroupRef", self.MODE_GROUP_NOTE),
            ("setFirstModeGroupRef", self.MODE_GROUP_NOTE),
            ("getModeDeclarationMappingSetRef", self.MODE_DECL_MAPPING_SET_NOTE),
            ("setModeDeclarationMappingSetRef", self.MODE_DECL_MAPPING_SET_NOTE),
            ("getSecondModeGroupRef", self.MODE_GROUP_NOTE),
            ("setSecondModeGroupRef", self.MODE_GROUP_NOTE),
        ):
            doc = getattr(ModeDeclarationGroupPrototypeMapping, method).__doc__.strip()
            assert note in doc, "%s docstring must carry the spec Note verbatim" % method
            if method.startswith("set"):
                attr = method[3].lower() + method[4:]
                assert "A None value is a no-op and does not overwrite an existing %s." % attr in doc


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
    CLASS_NOTE = "Specifies a mapping between a ModeDeclarationGroup and an ImplementationDataType. This ImplementationDataType shall be used to implement the ModeDeclarationGroup."
    IMPL_DATA_TYPE_NOTE = 'This is the corresponding AbstractImplementationDataType. It shall be modeled along the idea of an "unsigned integer-like" data type.'
    MODE_GROUP_NOTE = "This is the corresponding ModeDeclarationGroup."

    def test_initialization(self):
        """Test ModeRequestTypeMap initialization defaults (Table 4.18, all attrs 0..1)"""
        map_obj = ModeRequestTypeMap()
        assert map_obj is not None
        assert map_obj.implementationDataTypeRef is None
        assert map_obj.modeGroupRef is None

    def test_base_shape(self):
        """ModeRequestTypeMap shall derive from ARObject (Table 4.18 Base row)"""
        map_obj = ModeRequestTypeMap()
        assert isinstance(map_obj, ARObject)

    def test_get_set_implementation_data_type_ref(self):
        """Test implementationDataTypeRef round-trip, chaining and None no-op (Table 4.18 implementationDataType)"""
        map_obj = ModeRequestTypeMap()
        assert map_obj.getImplementationDataTypeRef() is None
        test_value = RefType().setValue("/DataTypes/AbstractImplementationDataType1")
        assert map_obj.setImplementationDataTypeRef(test_value) is map_obj
        assert map_obj.getImplementationDataTypeRef() is test_value
        map_obj.setImplementationDataTypeRef(None)
        assert map_obj.getImplementationDataTypeRef() is test_value

    def test_get_set_mode_group_ref(self):
        """Test modeGroupRef round-trip, chaining and None no-op (Table 4.18 modeGroup)"""
        map_obj = ModeRequestTypeMap()
        assert map_obj.getModeGroupRef() is None
        test_value = RefType().setValue("/ModeDeclarationGroups/ModeDeclarationGroup1")
        assert map_obj.setModeGroupRef(test_value) is map_obj
        assert map_obj.getModeGroupRef() is test_value
        map_obj.setModeGroupRef(None)
        assert map_obj.getModeGroupRef() is test_value

    def test_accessor_annotations(self):
        """Accessors shall carry Optional[RefType] hints; setters shall chain ModeRequestTypeMap (Table 4.18, 0..1 refs)"""
        for suffix in ("ImplementationDataTypeRef", "ModeGroupRef"):
            getter_hints = get_type_hints(getattr(ModeRequestTypeMap, "get%s" % suffix))
            assert getter_hints["return"] == Optional[RefType]
            setter_hints = get_type_hints(getattr(ModeRequestTypeMap, "set%s" % suffix))
            assert setter_hints["value"] == Optional[RefType]
            assert setter_hints["return"] == ModeRequestTypeMap

    def test_spec_note(self):
        """Test the Table 4.18 class note and per-attribute notes (verbatim from the markdown)"""
        class_doc = ModeRequestTypeMap.__doc__.strip()
        assert self.CLASS_NOTE in class_doc
        assert "[constr_1166] Restrictions of ModeRequestTypeMap:" in class_doc
        assert "[constr_1871] Existence of attribute ModeRequestTypeMap.implementationDataType:" in class_doc
        assert "[constr_1872] Existence of attribute ModeRequestTypeMap.modeGroup:" in class_doc
        assert "[constr_1167] ImplementationDataTypes used as ModeRequestTypeMap.implementationDataType:" in class_doc
        assert ModeRequestTypeMap.__init__.__doc__ is None
        init_source = inspect.getsource(ModeRequestTypeMap.__init__)
        assert self.IMPL_DATA_TYPE_NOTE in init_source
        assert self.MODE_GROUP_NOTE in init_source
        for method, note in (
            ("getImplementationDataTypeRef", self.IMPL_DATA_TYPE_NOTE),
            ("setImplementationDataTypeRef", self.IMPL_DATA_TYPE_NOTE),
            ("getModeGroupRef", self.MODE_GROUP_NOTE),
            ("setModeGroupRef", self.MODE_GROUP_NOTE),
        ):
            doc = getattr(ModeRequestTypeMap, method).__doc__.strip()
            assert note in doc, "%s docstring must carry the spec Note verbatim" % method
            if method.startswith("set"):
                attr = method[3].lower() + method[4:]
                assert "A None value is a no-op and does not overwrite an existing %s." % attr in doc


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


class TestModeDeclarationGroupPrototypeHeritage:
    def test_direct_base_is_atp_prototype(self):
        """ModeDeclarationGroupPrototype's direct base must be AtpPrototype (AtpPrototype re-parented AtpBlueprintable -> AtpFeature)."""
        assert ModeDeclarationGroupPrototype.__bases__[0] is AtpPrototype

    def test_atp_blueprintable_excluded_from_mro(self):
        """Spec Base closure (BSW Table 4.9) excludes AtpBlueprintable; losing it via the AtpPrototype re-parent is spec-correct."""
        assert AtpBlueprintable not in ModeDeclarationGroupPrototype.__mro__

    def test_mro_matches_spec_base_closure(self):
        """MRO must equal the spec Base closure: ARObject, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable."""
        mro = [c.__name__ for c in ModeDeclarationGroupPrototype.__mro__]
        assert mro == [
            "ModeDeclarationGroupPrototype",
            "AtpPrototype",
            "AtpFeature",
            "Identifiable",
            "MultilanguageReferrable",
            "Referrable",
            "ARObject",
            "VariationPointCapable",
            "ABC",
            "object",
        ]

    def test_is_subclass_identifiable_and_arobject(self):
        assert issubclass(ModeDeclarationGroupPrototype, Identifiable)
        assert issubclass(ModeDeclarationGroupPrototype, ARObject)

    def test_concrete_subclass_reaches_parent_and_short_name(self):
        """A concrete subclass constructed with (parent, short_name) must resolve parent/shortName through the AtpPrototype chain."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteModeGroupProto(ModeDeclarationGroupPrototype):
            pass

        proto = ConcreteModeGroupProto(ar_root, "ConcreteModeGroupProto")
        assert proto.getShortName() == "ConcreteModeGroupProto"
        assert proto.parent is ar_root


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
    def test_literals(self):
        """Test ModeActivationKind literal values per AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Table 5.34"""
        assert ModeActivationKind.ON_ENTRY == "onEntry"
        assert ModeActivationKind.ON_EXIT == "onExit"
        assert ModeActivationKind.ON_TRANSITION == "onTransition"

    def test_enum_values(self):
        """Test the valid enum value set in spec literal order (Table 5.34)"""
        enum = ModeActivationKind()
        assert enum.getEnumValues() == (
            ModeActivationKind.ON_ENTRY,
            ModeActivationKind.ON_EXIT,
            ModeActivationKind.ON_TRANSITION,
        )

    def test_instantiation_set_value(self):
        """Test enum instantiability and setValue/getValue round-trip per Rule 0011"""
        enum = ModeActivationKind()
        result = enum.setValue(ModeActivationKind.ON_TRANSITION)
        assert result is enum  # Method chaining
        assert enum.getValue() == "onTransition"

    def test_set_value_none_noop(self):
        """Test setValue(None) is a no-op"""
        enum = ModeActivationKind()
        assert enum.setValue(None) is enum
        assert enum.getValue() == ""  # ARLiteral's empty representation for an unset literal
        enum.setValue(ModeActivationKind.ON_ENTRY)
        enum.setValue(None)
        assert enum.getValue() == "onEntry"

    def test_validate_enum_value(self):
        """Test validateEnumValue accepts spec literals and rejects others"""
        enum = ModeActivationKind()
        assert enum.validateEnumValue("onEntry") is True
        assert enum.validateEnumValue("onTransition") is True
        assert enum.validateEnumValue("bogus") is False

    def test_spec_note(self):
        """Test the Table 5.34 class note."""
        assert ModeActivationKind.__doc__.strip() == "Kind of mode switch condition used for activation of an event, as further described for each enumeration field."
        assert ModeActivationKind.__init__.__doc__ is None
