from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswRunnableMapping, SwcBswMapping, SwcBswSynchronizedModeGroupPrototype, SwcBswSynchronizedTrigger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestSwcBswRunnableMapping:
    def test_initialization(self):
        """Test SwcBswRunnableMapping initialization"""
        mapping = SwcBswRunnableMapping()

        assert mapping is not None
        assert mapping.bswEntityRef is None
        assert mapping.swcRunnableRef is None

    def test_get_bsw_entity_ref(self):
        """Test getBswEntityRef method"""
        mapping = SwcBswRunnableMapping()
        assert mapping.getBswEntityRef() is None

    def test_set_bsw_entity_ref(self):
        """Test setBswEntityRef method"""
        mapping = SwcBswRunnableMapping()
        test_value = RefType().setValue("BswEntityRef")
        result = mapping.setBswEntityRef(test_value)
        assert result is mapping
        assert mapping.getBswEntityRef() == test_value

    def test_get_swc_runnable_ref(self):
        """Test getSwcRunnableRef method"""
        mapping = SwcBswRunnableMapping()
        assert mapping.getSwcRunnableRef() is None

    def test_set_swc_runnable_ref(self):
        """Test setSwcRunnableRef method"""
        mapping = SwcBswRunnableMapping()
        test_value = RefType().setValue("SwcRunnableRef")
        result = mapping.setSwcRunnableRef(test_value)
        assert result is mapping
        assert mapping.getSwcRunnableRef() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        mapping = SwcBswRunnableMapping()

        bsw_ref = RefType().setValue("BswEntityRef")
        swc_ref = RefType().setValue("SwcRunnableRef")

        mapping.setBswEntityRef(bsw_ref)
        mapping.setSwcRunnableRef(swc_ref)

        assert mapping.getBswEntityRef() == bsw_ref
        assert mapping.getSwcRunnableRef() == swc_ref


class TestSwcBswMapping:
    def test_initialization(self):
        """Test SwcBswMapping initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")

        assert swc_bsw_mapping is not None
        assert swc_bsw_mapping.getShortName() == "TestSwcBswMapping"
        assert swc_bsw_mapping.bswBehaviorRef is None
        assert swc_bsw_mapping.runnableMappings == []
        assert swc_bsw_mapping.swcBehaviorRef is None
        assert swc_bsw_mapping.synchronizedModeGroups == []
        assert swc_bsw_mapping.synchronizedTriggers == []

    def test_get_bsw_behavior_ref(self):
        """Test getBswBehaviorRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        assert swc_bsw_mapping.getBswBehaviorRef() is None

    def test_set_bsw_behavior_ref(self):
        """Test setBswBehaviorRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        test_value = RefType().setValue("BswBehaviorRef")
        result = swc_bsw_mapping.setBswBehaviorRef(test_value)
        assert result is swc_bsw_mapping
        assert swc_bsw_mapping.getBswBehaviorRef() == test_value

    def test_get_runnable_mappings(self):
        """Test getRunnableMappings method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        assert swc_bsw_mapping.getRunnableMappings() == []

    def test_add_runnable_mapping(self):
        """Test addRunnableMapping method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        mapping = SwcBswRunnableMapping()
        result = swc_bsw_mapping.addRunnableMapping(mapping)
        assert result is swc_bsw_mapping
        assert len(swc_bsw_mapping.getRunnableMappings()) == 1
        assert swc_bsw_mapping.getRunnableMappings()[0] == mapping

    def test_get_swc_behavior_ref(self):
        """Test getSwcBehaviorRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        assert swc_bsw_mapping.getSwcBehaviorRef() is None

    def test_set_swc_behavior_ref(self):
        """Test setSwcBehaviorRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        test_value = RefType().setValue("SwcBehaviorRef")
        result = swc_bsw_mapping.setSwcBehaviorRef(test_value)
        assert result is swc_bsw_mapping
        assert swc_bsw_mapping.getSwcBehaviorRef() == test_value

    def test_get_synchronized_mode_groups(self):
        """Test getSynchronizedModeGroups method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        groups = swc_bsw_mapping.getSynchronizedModeGroups()
        assert groups == []

    def test_set_synchronized_mode_groups(self):
        """Test setSynchronizedModeGroups method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        test_groups = ["Group1", "Group2"]
        result = swc_bsw_mapping.setSynchronizedModeGroups(test_groups)
        assert result is swc_bsw_mapping
        assert swc_bsw_mapping.getSynchronizedModeGroups() == test_groups

    def test_get_synchronized_triggers(self):
        """Test getSynchronizedTriggers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        triggers = swc_bsw_mapping.getSynchronizedTriggers()
        assert triggers == []

    def test_set_synchronized_triggers(self):
        """Test setSynchronizedTriggers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_bsw_mapping = SwcBswMapping(ar_root, "TestSwcBswMapping")
        test_triggers = ["Trigger1", "Trigger2"]
        result = swc_bsw_mapping.setSynchronizedTriggers(test_triggers)
        assert result is swc_bsw_mapping
        assert swc_bsw_mapping.getSynchronizedTriggers() == test_triggers


class TestSwcBswSynchronizedModeGroupPrototype:
    def test_initialization(self):
        """Test SwcBswSynchronizedModeGroupPrototype initialization"""
        prototype = SwcBswSynchronizedModeGroupPrototype()

        assert prototype is not None
        assert prototype.bswModeGroupRef is None
        assert prototype.swcModeGroupIRef is None

    def test_get_bsw_mode_group_ref(self):
        """Test getBswModeGroupRef method"""
        prototype = SwcBswSynchronizedModeGroupPrototype()
        assert prototype.getBswModeGroupRef() is None

    def test_set_bsw_mode_group_ref(self):
        """Test setBswModeGroupRef method"""
        prototype = SwcBswSynchronizedModeGroupPrototype()
        test_value = RefType().setValue("BswModeGroupRef")
        result = prototype.setBswModeGroupRef(test_value)
        assert result is prototype
        assert prototype.getBswModeGroupRef() == test_value

    def test_set_bsw_mode_group_ref_none_is_noop(self):
        """Test setBswModeGroupRef with None is a no-op"""
        prototype = SwcBswSynchronizedModeGroupPrototype()
        initial_value = RefType().setValue("BswModeGroupRef")
        prototype.setBswModeGroupRef(initial_value)
        prototype.setBswModeGroupRef(None)
        assert prototype.getBswModeGroupRef() == initial_value

    def test_get_swc_mode_group_iref(self):
        """Test getSwcModeGroupIRef method"""
        prototype = SwcBswSynchronizedModeGroupPrototype()
        assert prototype.getSwcModeGroupIRef() is None

    def test_set_swc_mode_group_iref(self):
        """Test setSwcModeGroupIRef method"""
        prototype = SwcBswSynchronizedModeGroupPrototype()
        test_value = RefType().setValue("SwcModeGroupRef")
        result = prototype.setSwcModeGroupIRef(test_value)
        assert result is prototype
        assert prototype.getSwcModeGroupIRef() == test_value

    def test_set_swc_mode_group_iref_none_is_noop(self):
        """Test setSwcModeGroupIRef with None is a no-op"""
        prototype = SwcBswSynchronizedModeGroupPrototype()
        initial_value = RefType().setValue("SwcModeGroupRef")
        prototype.setSwcModeGroupIRef(initial_value)
        prototype.setSwcModeGroupIRef(None)
        assert prototype.getSwcModeGroupIRef() == initial_value

    def test_all_properties(self):
        """Test setting all properties"""
        prototype = SwcBswSynchronizedModeGroupPrototype()

        bsw_ref = RefType().setValue("BswModeGroupRef")
        swc_ref = RefType().setValue("SwcModeGroupRef")

        prototype.setBswModeGroupRef(bsw_ref)
        prototype.setSwcModeGroupIRef(swc_ref)

        assert prototype.getBswModeGroupRef() == bsw_ref
        assert prototype.getSwcModeGroupIRef() == swc_ref

    def test_method_chaining(self):
        """Test method chaining for setters"""
        prototype = SwcBswSynchronizedModeGroupPrototype()

        bsw_ref = RefType().setValue("BswModeGroupRef")
        swc_ref = RefType().setValue("SwcModeGroupRef")

        result = prototype.setBswModeGroupRef(bsw_ref).setSwcModeGroupIRef(swc_ref)
        assert result is prototype
        assert prototype.getBswModeGroupRef() == bsw_ref
        assert prototype.getSwcModeGroupIRef() == swc_ref


class TestSwcBswSynchronizedTrigger:
    def test_initialization(self):
        """Test SwcBswSynchronizedTrigger initialization"""
        trigger = SwcBswSynchronizedTrigger()

        assert trigger is not None
        assert trigger.bswTriggerRef is None
        assert trigger.swcTriggerIRef is None

    def test_get_bsw_trigger_ref(self):
        """Test getBswTriggerRef method"""
        trigger = SwcBswSynchronizedTrigger()
        assert trigger.getBswTriggerRef() is None

    def test_set_bsw_trigger_ref(self):
        """Test setBswTriggerRef method"""
        trigger = SwcBswSynchronizedTrigger()
        test_value = RefType().setValue("BswTriggerRef")
        result = trigger.setBswTriggerRef(test_value)
        assert result is trigger
        assert trigger.getBswTriggerRef() == test_value

    def test_set_bsw_trigger_ref_none_is_noop(self):
        """Test setBswTriggerRef with None is a no-op"""
        trigger = SwcBswSynchronizedTrigger()
        initial_value = RefType().setValue("BswTriggerRef")
        trigger.setBswTriggerRef(initial_value)
        trigger.setBswTriggerRef(None)
        assert trigger.getBswTriggerRef() == initial_value

    def test_get_swc_trigger_iref(self):
        """Test getSwcTriggerIRef method"""
        trigger = SwcBswSynchronizedTrigger()
        assert trigger.getSwcTriggerIRef() is None

    def test_set_swc_trigger_iref(self):
        """Test setSwcTriggerIRef method"""
        trigger = SwcBswSynchronizedTrigger()
        test_value = RefType().setValue("SwcTriggerRef")
        result = trigger.setSwcTriggerIRef(test_value)
        assert result is trigger
        assert trigger.getSwcTriggerIRef() == test_value

    def test_set_swc_trigger_iref_none_is_noop(self):
        """Test setSwcTriggerIRef with None is a no-op"""
        trigger = SwcBswSynchronizedTrigger()
        initial_value = RefType().setValue("SwcTriggerRef")
        trigger.setSwcTriggerIRef(initial_value)
        trigger.setSwcTriggerIRef(None)
        assert trigger.getSwcTriggerIRef() == initial_value

    def test_all_properties(self):
        """Test setting all properties"""
        trigger = SwcBswSynchronizedTrigger()

        bsw_ref = RefType().setValue("BswTriggerRef")
        swc_ref = RefType().setValue("SwcTriggerRef")

        trigger.setBswTriggerRef(bsw_ref)
        trigger.setSwcTriggerIRef(swc_ref)

        assert trigger.getBswTriggerRef() == bsw_ref
        assert trigger.getSwcTriggerIRef() == swc_ref

    def test_method_chaining(self):
        """Test method chaining for setters"""
        trigger = SwcBswSynchronizedTrigger()

        bsw_ref = RefType().setValue("BswTriggerRef")
        swc_ref = RefType().setValue("SwcTriggerRef")

        result = trigger.setBswTriggerRef(bsw_ref).setSwcTriggerIRef(swc_ref)
        assert result is trigger
        assert trigger.getBswTriggerRef() == bsw_ref
        assert trigger.getSwcTriggerIRef() == swc_ref
