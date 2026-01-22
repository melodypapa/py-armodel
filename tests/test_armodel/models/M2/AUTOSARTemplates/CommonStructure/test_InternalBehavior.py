import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ReentrancyLevelEnum, ExclusiveArea, ExecutableEntity, InternalBehavior, AbstractEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, RefType


class TestReentrancyLevelEnum:
    def test_enum_values(self):
        """Test ReentrancyLevelEnum values"""
        assert ReentrancyLevelEnum.ENUM_MULTICORE_REENTRANT.value == "multicoreReentrant"
        assert ReentrancyLevelEnum.ENUM_NON_REENTRANT.value == "nonReentrant"
        assert ReentrancyLevelEnum.ENUM_SINGLE_CORE_REENTRANT.value == "singleCoreReentrant"

    def test_enum_usage(self):
        """Test using ReentrancyLevelEnum values"""
        reentrant_level = ReentrancyLevelEnum.ENUM_MULTICORE_REENTRANT
        assert reentrant_level.value == "multicoreReentrant"


class TestExclusiveArea:
    def test_initialization(self):
        """Test ExclusiveArea initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        exclusive_area = ExclusiveArea(ar_root, "TestExclusiveArea")
        
        assert exclusive_area is not None
        assert exclusive_area.getShortName() == "TestExclusiveArea"


class TestExecutableEntity:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ExecutableEntity abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError, match="ExecutableEntity is an abstract class."):
            ExecutableEntity(ar_root, "TestExecutableEntity")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of ExecutableEntity can be instantiated"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        assert exec_entity is not None
        assert exec_entity.getShortName() == "TestExecutableEntity"
        assert exec_entity.activationReasons == []
        assert exec_entity.canEnterExclusiveAreaRefs == []
        assert exec_entity.minimumStartInterval is None
        assert exec_entity.reentrancyLevel is None
        assert exec_entity.swAddrMethodRef is None

    def test_get_activation_reasons(self):
        """Test getActivationReasons method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        assert exec_entity.getActivationReasons() == []

    def test_add_activation_reason(self):
        """Test addActivationReason method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        
        # Create a mock activation reason for testing
        class MockActivationReason:
            pass
        reason = MockActivationReason()
        
        result = exec_entity.addActivationReason(reason)
        assert result is exec_entity  # Method chaining
        assert len(exec_entity.getActivationReasons()) == 1
        assert exec_entity.getActivationReasons()[0] == reason

    def test_get_minimum_start_interval(self):
        """Test getMinimumStartInterval method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        assert exec_entity.getMinimumStartInterval() is None

    def test_set_minimum_start_interval(self):
        """Test setMinimumStartInterval method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        test_value = ARFloat().setValue(0.001)  # 1ms
        result = exec_entity.setMinimumStartInterval(test_value)
        assert result is exec_entity  # Method chaining
        assert exec_entity.getMinimumStartInterval() == test_value

    def test_set_minimum_start_interval_none(self):
        """Test setMinimumStartInterval with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        result = exec_entity.setMinimumStartInterval(None)
        assert result is exec_entity  # Method chaining
        assert exec_entity.getMinimumStartInterval() is None

    def test_get_reentrancy_level(self):
        """Test getReentrancyLevel method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        assert exec_entity.getReentrancyLevel() is None

    def test_set_reentrancy_level(self):
        """Test setReentrancyLevel method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        test_value = ReentrancyLevelEnum.ENUM_MULTICORE_REENTRANT
        result = exec_entity.setReentrancyLevel(test_value)
        assert result is exec_entity  # Method chaining
        assert exec_entity.getReentrancyLevel() == test_value

    def test_get_sw_addr_method_ref(self):
        """Test getSwAddrMethodRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        assert exec_entity.getSwAddrMethodRef() is None

    def test_set_sw_addr_method_ref(self):
        """Test setSwAddrMethodRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        test_value = RefType().setValue("AddrMethodRef")
        result = exec_entity.setSwAddrMethodRef(test_value)
        assert result is exec_entity  # Method chaining
        assert exec_entity.getSwAddrMethodRef() == test_value

    def test_minimum_start_interval_ms_property(self):
        """Test minimumStartIntervalMs property"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        
        # Test with no minimum start interval
        assert exec_entity.minimumStartIntervalMs is None
        
        # Test with minimum start interval set
        interval = ARFloat().setValue(0.002)  # 0.002 seconds = 2ms
        exec_entity.setMinimumStartInterval(interval)
        assert exec_entity.minimumStartIntervalMs == 2

    def test_add_can_enter_exclusive_area_ref(self):
        """Test addCanEnterExclusiveAreaRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        
        ref1 = RefType().setValue("ExclusiveArea1")
        ref2 = RefType().setValue("ExclusiveArea2")
        
        exec_entity.addCanEnterExclusiveAreaRef(ref1)
        exec_entity.addCanEnterExclusiveAreaRef(ref2)
        
        refs = exec_entity.getCanEnterExclusiveAreaRefs()
        assert len(refs) == 2
        assert refs[0] == ref1
        assert refs[1] == ref2

    def test_get_can_enter_exclusive_area_refs(self):
        """Test getCanEnterExclusiveAreaRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteExecutableEntity(ExecutableEntity):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        exec_entity = ConcreteExecutableEntity(ar_root, "TestExecutableEntity")
        refs = exec_entity.getCanEnterExclusiveAreaRefs()
        assert refs == []


class TestInternalBehavior:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that InternalBehavior abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError, match="InternalBehavior is an abstract class."):
            InternalBehavior(ar_root, "TestInternalBehavior")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of InternalBehavior can be instantiated"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        assert internal_behavior is not None
        assert internal_behavior.getShortName() == "TestInternalBehavior"
        assert internal_behavior.constantMemories == []
        assert internal_behavior.constantValueMappingRefs == []
        assert internal_behavior.dataTypeMappingRefs == []
        assert internal_behavior.exclusiveAreas == []
        assert internal_behavior.exclusiveAreaNestingOrders == []
        assert internal_behavior.staticMemories == []

    def test_create_constant_memory(self):
        """Test createConstantMemory method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        constant_memory = internal_behavior.createConstantMemory("TestConstant")
        
        assert constant_memory is not None
        assert constant_memory.getShortName() == "TestConstant"
        assert len(internal_behavior.constantMemories) == 1
        assert internal_behavior.constantMemories[0] == constant_memory

    def test_get_constant_memories(self):
        """Test getConstantMemories method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        constant_memory1 = internal_behavior.createConstantMemory("TestConstant1")
        constant_memory2 = internal_behavior.createConstantMemory("TestConstant2")
    
        memories = internal_behavior.getConstantMemories()
        assert len(memories) == 2
        # Note: getConstantMemories returns elements in insertion order, not sorted by default
        assert memories[0] == constant_memory1
        assert memories[1] == constant_memory2

    def test_add_data_type_mapping_ref(self):
        """Test addDataTypeMappingRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
    
        ref1 = RefType().setValue("DataTypeRef1")
        ref2 = RefType().setValue("DataTypeRef2")
    
        internal_behavior.addDataTypeMappingRef(ref1)
        internal_behavior.addDataTypeMappingRef(ref2)
    
        refs = internal_behavior.getDataTypeMappingRefs()
        assert len(refs) == 2
        assert refs[0] == ref1
        assert refs[1] == ref2

    def test_get_data_type_mapping_refs(self):
        """Test getDataTypeMappingRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        refs = internal_behavior.getDataTypeMappingRefs()
        assert refs == []

    def test_create_exclusive_area(self):
        """Test createExclusiveArea method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        exclusive_area = internal_behavior.createExclusiveArea("TestArea")
    
        assert exclusive_area is not None
        assert exclusive_area.getShortName() == "TestArea"
        assert len(internal_behavior.exclusiveAreas) == 1
        assert internal_behavior.exclusiveAreas[0] == exclusive_area

    def test_get_exclusive_areas(self):
        """Test getExclusiveAreas method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        area1 = internal_behavior.createExclusiveArea("Area1")
        area2 = internal_behavior.createExclusiveArea("Area2")
    
        areas = internal_behavior.getExclusiveAreas()
        assert len(areas) == 2
        # getExclusiveAreas uses filter to return only ExclusiveArea instances
        area_names = [area.getShortName() for area in areas]
        assert "Area1" in area_names
        assert "Area2" in area_names

    def test_get_static_memories(self):
        """Test getStaticMemories method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        memories = internal_behavior.getStaticMemories()
        assert memories == []
        
    def test_create_static_memory(self):
        """Test createStaticMemory method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
    
        class ConcreteInternalBehavior(InternalBehavior):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
    
        internal_behavior = ConcreteInternalBehavior(ar_root, "TestInternalBehavior")
        static_memory = internal_behavior.createStaticMemory("TestStatic")
    
        assert static_memory is not None
        assert static_memory.getShortName() == "TestStatic"
        assert len(internal_behavior.staticMemories) == 1
        assert internal_behavior.staticMemories[0] == static_memory


class TestAbstractEvent:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractEvent abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AbstractEvent is an abstract class"):
            AbstractEvent(ar_root, "TestAbstractEvent")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of AbstractEvent can be instantiated"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Use BswEvent as a concrete subclass
        from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent

        class ConcreteBswEvent(BswEvent):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        abstract_event = ConcreteBswEvent(ar_root, "TestAbstractEvent")

        assert abstract_event is not None
        assert abstract_event.getShortName() == "TestAbstractEvent"
        assert abstract_event.activationReasonRepresentationRef is None

    def test_get_activation_reason_representation_ref(self):
        """Test getActivationReasonRepresentationRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent

        class ConcreteBswEvent(BswEvent):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        abstract_event = ConcreteBswEvent(ar_root, "TestAbstractEvent")
        assert abstract_event.getActivationReasonRepresentationRef() is None

    def test_set_activation_reason_representation_ref(self):
        """Test setActivationReasonRepresentationRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent

        class ConcreteBswEvent(BswEvent):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        abstract_event = ConcreteBswEvent(ar_root, "TestAbstractEvent")
        test_value = RefType().setValue("ActivationReasonRef")
        result = abstract_event.setActivationReasonRepresentationRef(test_value)
        assert result is abstract_event  # Method chaining
        assert abstract_event.getActivationReasonRepresentationRef() == test_value

    def test_set_activation_reason_representation_ref_none(self):
        """Test setActivationReasonRepresentationRef with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent

        class ConcreteBswEvent(BswEvent):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        abstract_event = ConcreteBswEvent(ar_root, "TestAbstractEvent")
        result = abstract_event.setActivationReasonRepresentationRef(None)
        assert result is abstract_event  # Method chaining
        assert abstract_event.getActivationReasonRepresentationRef() is None