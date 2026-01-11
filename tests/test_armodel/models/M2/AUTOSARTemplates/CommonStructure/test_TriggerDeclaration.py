import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestTrigger:
    def test_initialization(self):
        """Test Trigger initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        
        assert trigger is not None
        assert trigger.getShortName() == "TestTrigger"
        assert trigger.swImplPolicy is None
        assert trigger.triggerPeriod is None

    def test_get_sw_impl_policy(self):
        """Test getSwImplPolicy method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        assert trigger.getSwImplPolicy() is None

    def test_set_sw_impl_policy(self):
        """Test setSwImplPolicy method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        # Create mock SwImplPolicyEnum value for testing
        class MockSwImplPolicy:
            pass
        test_value = MockSwImplPolicy()
        result = trigger.setSwImplPolicy(test_value)
        assert result is trigger
        assert trigger.getSwImplPolicy() == test_value

    def test_set_sw_impl_policy_none(self):
        """Test setSwImplPolicy with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        result = trigger.setSwImplPolicy(None)
        assert result is trigger
        assert trigger.getSwImplPolicy() is None

    def test_get_trigger_period(self):
        """Test getTriggerPeriod method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        assert trigger.getTriggerPeriod() is None

    def test_set_trigger_period(self):
        """Test setTriggerPeriod method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        # Create mock MultidimensionalTime value for testing
        class MockMultidimensionalTime:
            pass
        test_value = MockMultidimensionalTime()
        result = trigger.setTriggerPeriod(test_value)
        assert result is trigger
        assert trigger.getTriggerPeriod() == test_value

    def test_set_trigger_period_none(self):
        """Test setTriggerPeriod with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        result = trigger.setTriggerPeriod(None)
        assert result is trigger
        assert trigger.getTriggerPeriod() is None

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        
        class MockSwImplPolicy:
            pass
        class MockMultidimensionalTime:
            pass
        
        sw_policy = MockSwImplPolicy()
        period = MockMultidimensionalTime()
        
        trigger.setSwImplPolicy(sw_policy)
        trigger.setTriggerPeriod(period)
        
        assert trigger.getSwImplPolicy() == sw_policy
        assert trigger.getTriggerPeriod() == period


class TestTriggerMapping:
    def test_initialization(self):
        """Test TriggerMapping initialization"""
        mapping = TriggerMapping()
        
        assert mapping is not None
        assert mapping.firstTriggerRef is None
        assert mapping.secondTriggerRef is None

    def test_get_first_trigger_ref(self):
        """Test getFirstTriggerRef method"""
        mapping = TriggerMapping()
        assert mapping.getFirstTriggerRef() is None

    def test_set_first_trigger_ref(self):
        """Test setFirstTriggerRef method"""
        mapping = TriggerMapping()
        test_value = RefType().setValue("FirstTriggerRef")
        result = mapping.setFirstTriggerRef(test_value)
        assert result is mapping
        assert mapping.getFirstTriggerRef() == test_value

    def test_set_first_trigger_ref_none(self):
        """Test setFirstTriggerRef with None value"""
        mapping = TriggerMapping()
        result = mapping.setFirstTriggerRef(None)
        assert result is mapping
        assert mapping.getFirstTriggerRef() is None

    def test_get_second_trigger_ref(self):
        """Test getSecondTriggerRef method"""
        mapping = TriggerMapping()
        assert mapping.getSecondTriggerRef() is None

    def test_set_second_trigger_ref(self):
        """Test setSecondTriggerRef method"""
        mapping = TriggerMapping()
        test_value = RefType().setValue("SecondTriggerRef")
        result = mapping.setSecondTriggerRef(test_value)
        assert result is mapping
        assert mapping.getSecondTriggerRef() == test_value

    def test_set_second_trigger_ref_none(self):
        """Test setSecondTriggerRef with None value"""
        mapping = TriggerMapping()
        result = mapping.setSecondTriggerRef(None)
        assert result is mapping
        assert mapping.getSecondTriggerRef() is None

    def test_all_properties(self):
        """Test setting all properties"""
        mapping = TriggerMapping()
        
        ref1 = RefType().setValue("FirstTriggerRef")
        ref2 = RefType().setValue("SecondTriggerRef")
        
        mapping.setFirstTriggerRef(ref1)
        mapping.setSecondTriggerRef(ref2)
        
        assert mapping.getFirstTriggerRef() == ref1
        assert mapping.getSecondTriggerRef() == ref2