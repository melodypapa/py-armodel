
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import (
    SwcBswMapping,
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
