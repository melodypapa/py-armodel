"""
Comprehensive test suite for BSW (Basic Software) Behavior module classes.
This module tests all the classes in the BswBehavior.py file to ensure 100% coverage.
Tests verify initialization, getter/setter methods, and special functionality for each class.
"""
import pytest

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswModuleCallPoint,
    BswAsynchronousServerCallPoint,
    BswDirectCallPoint,
    BswSynchronousServerCallPoint,
    BswAsynchronousServerCallResultPoint,
    BswVariableAccess,
    BswDistinguishedPartition,
    BswModuleEntity,
    BswCalledEntity,
    BswSchedulableEntity,
    BswInterruptCategory,
    BswInterruptEntity,
    BswEvent,
    BswOperationInvokedEvent,
    BswScheduleEvent,
    BswModeSwitchEvent,
    BswTimingEvent,
    BswDataReceivedEvent,
    BswInternalTriggerOccurredEvent,
    BswModeSwitchAckRequest,
    BswModeSenderPolicy,
    BswBackgroundEvent,
    BswOsTaskExecutionEvent,
    BswExternalTriggerOccurredEvent,
    BswApiOptions,
    BswDataReceptionPolicy,
    BswQueuedDataReceptionPolicy,
    BswInternalTriggeringPoint,
    BswInternalBehavior
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType, ARFloat, ARNumerical, PositiveInteger, TimeValue
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel import AUTOSAR


class TestBswModuleCallPoint:
    """Test cases for BswModuleCallPoint class - represents a call point in a BSW module."""
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that BswModuleCallPoint is abstract and cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        
        with pytest.raises(TypeError, match="BswModuleCallPoint is an abstract class"):
            call_point = BswModuleCallPoint(ar_root, "test_call_point")
    
    def test_concrete_subclass_can_be_instantiated(self):
        """Test that concrete subclasses of BswModuleCallPoint can be instantiated."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        
        # Test with BswDirectCallPoint (a concrete subclass)
        call_point = BswDirectCallPoint(ar_root, "test_call_point")
        
        assert call_point.short_name == "test_call_point"
        assert call_point.getContextLimitationRefs() == []
        
    def test_add_context_limitation_ref(self):
        """Test adding a context limitation reference to a concrete subclass of BswModuleCallPoint."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = BswDirectCallPoint(ar_root, "test_call_point")
        
        ref = RefType()
        result = call_point.addContextLimitationRef(ref)
        
        assert result == call_point
        assert call_point.getContextLimitationRefs() == [ref]


class TestBswAsynchronousServerCallPoint:
    """Test cases for BswAsynchronousServerCallPoint class - represents an asynchronous server call point in a BSW module."""
    def test_initialization(self):
        """Test initialization of BswAsynchronousServerCallPoint with proper attributes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        async_call_point = BswAsynchronousServerCallPoint(ar_root, "test_async_call")
        
        assert async_call_point.short_name == "test_async_call"
        assert async_call_point.getCalledEntryRef() is None
        
    def test_set_called_entry_ref(self):
        """Test setting and getting the called entry reference for BswAsynchronousServerCallPoint, including behavior when setting None."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        async_call_point = BswAsynchronousServerCallPoint(ar_root, "test_async_call")
        
        ref = RefType()
        result = async_call_point.setCalledEntryRef(ref)
        
        assert result == async_call_point
        assert async_call_point.getCalledEntryRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = async_call_point.setCalledEntryRef(None)
        assert result == async_call_point
        assert async_call_point.getCalledEntryRef() == ref  # Value should remain unchanged


class TestBswDirectCallPoint:
    """Test cases for BswDirectCallPoint class - represents a direct call point in a BSW module."""
    def test_initialization(self):
        """Test initialization of BswDirectCallPoint with proper attributes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        direct_call_point = BswDirectCallPoint(ar_root, "test_direct_call")
        
        assert direct_call_point.short_name == "test_direct_call"
        assert direct_call_point.getCalledEntryRef() is None
        assert direct_call_point.getCalledFromWithinExclusiveAreaRef() is None
        
    def test_set_called_entry_ref(self):
        """Test setting and getting the called entry reference for BswDirectCallPoint, including behavior when setting None."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        direct_call_point = BswDirectCallPoint(ar_root, "test_direct_call")
        
        ref = RefType()
        result = direct_call_point.setCalledEntryRef(ref)
        
        assert result == direct_call_point
        assert direct_call_point.getCalledEntryRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = direct_call_point.setCalledEntryRef(None)
        assert result == direct_call_point
        assert direct_call_point.getCalledEntryRef() == ref  # Value should remain unchanged
        
    def test_set_called_from_within_exclusive_area_ref(self):
        """Test setting and getting the called from within exclusive area reference for BswDirectCallPoint, including behavior when setting None."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        direct_call_point = BswDirectCallPoint(ar_root, "test_direct_call")
        
        ref = RefType()
        result = direct_call_point.setCalledFromWithinExclusiveAreaRef(ref)
        
        assert result == direct_call_point
        assert direct_call_point.getCalledFromWithinExclusiveAreaRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = direct_call_point.setCalledFromWithinExclusiveAreaRef(None)
        assert result == direct_call_point
        assert direct_call_point.getCalledFromWithinExclusiveAreaRef() == ref  # Value should remain unchanged


class TestBswSynchronousServerCallPoint:
    """Test cases for BswSynchronousServerCallPoint class - represents a synchronous server call point in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sync_call_point = BswSynchronousServerCallPoint(ar_root, "test_sync_call")
        
        assert sync_call_point.short_name == "test_sync_call"
        assert sync_call_point.getCalledEntryRef() is None
        assert sync_call_point.getCalledFromWithinExclusiveAreaRef() is None
        
    def test_set_called_entry_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sync_call_point = BswSynchronousServerCallPoint(ar_root, "test_sync_call")
        
        ref = RefType()
        result = sync_call_point.setCalledEntryRef(ref)
        
        assert result == sync_call_point
        assert sync_call_point.getCalledEntryRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = sync_call_point.setCalledEntryRef(None)
        assert result == sync_call_point
        assert sync_call_point.getCalledEntryRef() == ref  # Value should remain unchanged
        
    def test_set_called_from_within_exclusive_area_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sync_call_point = BswSynchronousServerCallPoint(ar_root, "test_sync_call")
        
        ref = RefType()
        result = sync_call_point.setCalledFromWithinExclusiveAreaRef(ref)
        
        assert result == sync_call_point
        assert sync_call_point.getCalledFromWithinExclusiveAreaRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = sync_call_point.setCalledFromWithinExclusiveAreaRef(None)
        assert result == sync_call_point
        assert sync_call_point.getCalledFromWithinExclusiveAreaRef() == ref  # Value should remain unchanged


class TestBswAsynchronousServerCallResultPoint:
    """Test cases for BswAsynchronousServerCallResultPoint class - represents an asynchronous server call result point in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        async_result_point = BswAsynchronousServerCallResultPoint(ar_root, "test_async_result")
        
        assert async_result_point.short_name == "test_async_result"


class TestBswVariableAccess:
    """Test cases for BswVariableAccess class - represents access to a variable in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        variable_access = BswVariableAccess(ar_root, "test_variable_access")
        
        assert variable_access.short_name == "test_variable_access"
        assert variable_access.getAccessedVariableRef() is None
        assert variable_access.getContextLimitationRefs() == []
        
    def test_set_accessed_variable_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        variable_access = BswVariableAccess(ar_root, "test_variable_access")
        
        ref = RefType()
        result = variable_access.setAccessedVariableRef(ref)
        
        assert result == variable_access
        assert variable_access.getAccessedVariableRef() == ref
        
    def test_add_context_limitation_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        variable_access = BswVariableAccess(ar_root, "test_variable_access")
        
        ref = RefType()
        result = variable_access.addContextLimitationRef(ref)
        
        assert result == variable_access
        assert variable_access.getContextLimitationRefs() == [ref]


class TestBswModuleEntity:
    """Test cases for BswModuleEntity class - abstract base class for BSW module entities."""
    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            BswModuleEntity(ar_root, "BswModuleEntity")
        assert str(err.value) == "BswModuleEntity is an abstract class."
    
    def test_get_set_accessed_mode_group_refs(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        ref = RefType()
        result = entity.addAccessedModeGroupRef(ref)
        
        assert result == entity
        assert entity.getAccessedModeGroupRefs() == [ref]
        
        result = entity.addAccessedModeGroupRef(None)
        assert result == entity
        assert len(entity.getAccessedModeGroupRefs()) == 1  # None should not be added
    
    def test_get_set_activation_point_refs(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        ref = RefType()
        result = entity.addActivationPointRef(ref)
        
        assert result == entity
        assert entity.getActivationPointRefs() == [ref]
        
        result = entity.addActivationPointRef(None)
        assert result == entity
        assert len(entity.getActivationPointRefs()) == 1  # None should not be added
    
    def test_get_call_points(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getCallPoints() == []
    
    def test_create_bsw_asynchronous_server_call_point(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        call_point = entity.createBswAsynchronousServerCallPoint("test_async_call_point")
        
        assert call_point.short_name == "test_async_call_point"
        assert len(entity.getCallPoints()) == 1
    
    def test_create_bsw_synchronous_server_call_point(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        call_point = entity.createBswSynchronousServerCallPoint("test_sync_call_point")
        
        assert call_point.short_name == "test_sync_call_point"
        assert len(entity.getCallPoints()) == 1
    
    def test_get_data_receive_points(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getDataReceivePoints() == []
    
    def test_create_data_receive_point(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        data_point = entity.createDataReceivePoint("test_data_receive_point")
        
        assert data_point.short_name == "test_data_receive_point"
        assert len(entity.getDataReceivePoints()) == 1
    
    def test_get_data_send_points(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getDataSendPoints() == []
    
    def test_create_data_send_point(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        data_point = entity.createDataSendPoint("test_data_send_point")
        
        assert data_point.short_name == "test_data_send_point"
        assert len(entity.getDataSendPoints()) == 1
    
    def test_get_implemented_entry_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getImplementedEntryRef() is None
    
    def test_set_implemented_entry_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        ref = RefType()
        result = entity.setImplementedEntryRef(ref)
        
        assert result == entity
        assert entity.getImplementedEntryRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = entity.setImplementedEntryRef(None)
        assert result == entity
        assert entity.getImplementedEntryRef() == ref  # Value should remain unchanged
    
    def test_get_issued_trigger_refs(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getIssuedTriggerRefs() == []
    
    def test_add_issued_trigger_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        ref = RefType()
        result = entity.addIssuedTriggerRef(ref)
        
        assert result == entity
        assert entity.getIssuedTriggerRefs() == [ref]
        
        result = entity.addIssuedTriggerRef(None)
        assert result == entity
        assert len(entity.getIssuedTriggerRefs()) == 1  # None should not be added
    
    def test_get_managed_mode_group_refs(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getManagedModeGroupRefs() == []
    
    def test_add_managed_mode_group_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        ref = RefType()
        result = entity.addManagedModeGroupRef(ref)
        
        assert result == entity
        assert entity.getManagedModeGroupRefs() == [ref]
        
        result = entity.addManagedModeGroupRef(None)
        assert result == entity
        assert len(entity.getManagedModeGroupRefs()) == 1  # None should not be added
    
    def test_get_scheduler_name_prefix_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        assert entity.getSchedulerNamePrefixRef() is None
    
    def test_set_scheduler_name_prefix_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")
        
        ref = RefType()
        result = entity.setSchedulerNamePrefixRef(ref)
        
        assert result == entity
        assert entity.getSchedulerNamePrefixRef() == ref


class TestBswCalledEntity:
    """Test cases for BswCalledEntity class - represents a called entity in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_called_entity")
        
        assert entity.short_name == "test_called_entity"


class TestBswSchedulableEntity:
    """Test cases for BswSchedulableEntity class - represents a schedulable entity in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswSchedulableEntity(ar_root, "test_schedulable_entity")
        
        assert entity.short_name == "test_schedulable_entity"


class TestBswInterruptCategory:
    """Test cases for BswInterruptCategory enum class - represents interrupt categories for BSW modules."""
    def test_initialization(self):
        category = BswInterruptCategory()
        assert category.CAT1 == "cat1"
        assert category.CAT2 == "cat2"
        # Check if the enum values are in the internal enumValues list
        assert "cat1" in category.getEnumValues()
        assert "cat2" in category.getEnumValues()


class TestBswInterruptEntity:
    """Test cases for BswInterruptEntity class - represents an interrupt entity in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswInterruptEntity(ar_root, "test_interrupt_entity")
        
        assert entity.short_name == "test_interrupt_entity"
        assert entity.getInterruptCategory() is None
        assert entity.getInterruptSource() is None
        
    def test_set_interrupt_category(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswInterruptEntity(ar_root, "test_interrupt_entity")
        
        category = BswInterruptCategory()
        result = entity.setInterruptCategory(category)
        
        assert result == entity
        assert entity.getInterruptCategory() == category
        
    def test_set_interrupt_source(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswInterruptEntity(ar_root, "test_interrupt_entity")
        
        source = "test_source"
        result = entity.setInterruptSource(source)
        
        assert result == entity
        assert entity.getInterruptSource() == source


class TestBswEvent:
    """Test cases for BswEvent class - abstract base class for BSW events."""
    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            BswEvent(ar_root, "BswEvent")
        assert str(err.value) == "BswEvent is an abstract class."
    
    def test_get_set_starts_on_event_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_event")
        
        ref = RefType()
        result = event.setStartsOnEventRef(ref)
        
        assert result == event
        assert event.getStartsOnEventRef() == ref


class TestBswOperationInvokedEvent:
    """Test cases for BswOperationInvokedEvent class - represents an operation invoked event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_operation_invoked_event")
        
        assert event.short_name == "test_operation_invoked_event"
        assert event.getEntryRef() is None
        
    def test_set_entry_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_operation_invoked_event")
        
        ref = RefType()
        result = event.setEntryRef(ref)
        
        assert result == event
        assert event.getEntryRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = event.setEntryRef(None)
        assert result == event
        assert event.getEntryRef() == ref  # Value should remain unchanged


class TestBswScheduleEvent:
    """Test cases for BswScheduleEvent class - abstract base class for scheduled BSW events."""
    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            BswScheduleEvent(ar_root, "BswScheduleEvent")
        assert str(err.value) == "BswScheduleEvent is an abstract class."


class TestBswModeSwitchEvent:
    """Test cases for BswModeSwitchEvent class - represents a mode switch event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")
        
        assert event.short_name == "test_mode_switch_event"
        assert event.getActivation() is None
        
    def test_set_activation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")
        
        activation = "test_activation"
        result = event.setActivation(activation)
        
        assert result == event
        assert event.getActivation() == activation


class TestBswTimingEvent:
    """Test cases for BswTimingEvent class - represents a timing event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswTimingEvent(ar_root, "test_timing_event")
        
        assert event.short_name == "test_timing_event"
        assert event.getPeriod() is None
        assert event.periodMs is None
        
    def test_set_period(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswTimingEvent(ar_root, "test_timing_event")
        
        period = TimeValue()
        period.value = 5.0
        result = event.setPeriod(period)
        
        assert result == event
        assert event.getPeriod() == period
        assert event.periodMs == 5000  # 5.0 * 1000
        
    def test_set_period_none_handling(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswTimingEvent(ar_root, "test_timing_event")
        
        # Set an initial period
        initial_period = TimeValue()
        initial_period.value = 2.0
        event.setPeriod(initial_period)
        
        # Try to set to None when current is not None (should not update)
        result = event.setPeriod(None)
        assert result == event
        assert event.getPeriod() == initial_period  # Should remain unchanged


class TestBswDataReceivedEvent:
    """Test cases for BswDataReceivedEvent class - represents a data received event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswDataReceivedEvent(ar_root, "test_data_received_event")
        
        assert event.short_name == "test_data_received_event"
        assert event.getDataRef() is None
        
    def test_set_data_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswDataReceivedEvent(ar_root, "test_data_received_event")
        
        ref = RefType()
        result = event.setDataRef(ref)
        
        assert result == event
        assert event.getDataRef() == ref


class TestBswInternalTriggerOccurredEvent:
    """Test cases for BswInternalTriggerOccurredEvent class - represents an internal trigger occurred event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswInternalTriggerOccurredEvent(ar_root, "test_internal_trigger_event")
        
        assert event.short_name == "test_internal_trigger_event"
        assert event.getEventSourceRef() is None
        
    def test_set_event_source_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswInternalTriggerOccurredEvent(ar_root, "test_internal_trigger_event")
        
        ref = RefType()
        result = event.setEventSourceRef(ref)
        
        assert result == event
        assert event.getEventSourceRef() == ref


class TestBswModeSwitchAckRequest:
    """Test cases for BswModeSwitchAckRequest class - represents a mode switch acknowledgment request in a BSW module."""
    def test_initialization(self):
        ack_request = BswModeSwitchAckRequest()
        
        assert ack_request.getTimeout() is None
        
    def test_set_timeout(self):
        ack_request = BswModeSwitchAckRequest()
        
        timeout = ARFloat()
        timeout.setValue(5.0)
        result = ack_request.setTimeout(timeout)
        
        assert result == ack_request
        assert ack_request.getTimeout() == timeout


class TestBswModeSenderPolicy:
    """Test cases for BswModeSenderPolicy class - represents a mode sender policy in a BSW module."""
    def test_initialization(self):
        policy = BswModeSenderPolicy()
        
        assert policy.getProvidedModeGroupRef() is None
        assert policy.getQueueLength() is None
        
    def test_set_get_provided_mode_group_ref(self):
        policy = BswModeSenderPolicy()
        
        ref = RefType()
        result = policy.setProvidedModeGroupRef(ref)
        
        assert result == policy
        assert policy.getProvidedModeGroupRef() == ref
    
    def test_set_get_queue_length_with_numerical(self):
        policy = BswModeSenderPolicy()
        
        length = ARNumerical()
        length.setValue(10)
        result = policy.setQueueLength(length)
        
        assert result is None  # setQueueLength doesn't return self
        assert policy.getQueueLength() == length
    
    def test_set_get_queue_length_with_int(self):
        policy = BswModeSenderPolicy()
        
        result = policy.setQueueLength(5)
        
        assert result is None  # setQueueLength doesn't return self
        queue_length = policy.getQueueLength()
        assert isinstance(queue_length, ARNumerical)
        assert queue_length.getValue() == 5
    
    def test_set_queue_length_with_invalid_type(self):
        policy = BswModeSenderPolicy()
        
        with pytest.raises(ValueError) as err:
            policy.setQueueLength("invalid")
        assert "Unsupported type" in str(err.value)


class TestBswBackgroundEvent:
    """Test cases for BswBackgroundEvent class - represents a background event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswBackgroundEvent(ar_root, "test_background_event")
        
        assert event.short_name == "test_background_event"


class TestBswOsTaskExecutionEvent:
    """Test cases for BswOsTaskExecutionEvent class - represents an OS task execution event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOsTaskExecutionEvent(ar_root, "test_os_task_event")
        
        assert event.short_name == "test_os_task_event"


class TestBswExternalTriggerOccurredEvent:
    """Test cases for BswExternalTriggerOccurredEvent class - represents an external trigger occurred event in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswExternalTriggerOccurredEvent(ar_root, "test_external_trigger_event")
        
        assert event.short_name == "test_external_trigger_event"
        assert event.getTriggerRef() is None
        
    def test_set_trigger_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswExternalTriggerOccurredEvent(ar_root, "test_external_trigger_event")
        
        ref = RefType()
        result = event.setTriggerRef(ref)
        
        assert result == event
        assert event.getTriggerRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = event.setTriggerRef(None)
        assert result == event
        assert event.getTriggerRef() == ref  # Value should remain unchanged


class TestBswApiOptions:
    """Test cases for BswApiOptions class - abstract base class for BSW API options."""
    def test_abstract_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError) as err:
            BswApiOptions()
        assert str(err.value) == "BswApiOptions is an abstract class."
    
    def test_get_set_enable_take_address(self):
        # Test with a concrete implementation that inherits from BswApiOptions
        # Since BswApiOptions is abstract, we need to use a concrete implementation
        policy = BswQueuedDataReceptionPolicy()
        
        # Initially, enableTakeAddress should be None
        # (Based on the actual behavior, it might have a default value)
        initial_value = policy.getEnableTakeAddress()
        
        result = policy.setEnableTakeAddress(True)
        
        assert result == policy
        assert policy.getEnableTakeAddress() is True
        
        # Now test setting to None (but it will only update if not None)
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        # Since the setter only updates if value is not None, it should still be True
        assert policy.getEnableTakeAddress() is True


class TestBswDataReceptionPolicy:
    """Test cases for BswDataReceptionPolicy class - abstract base class for BSW data reception policies."""
    def test_abstract_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError) as err:
            BswDataReceptionPolicy()
        assert str(err.value) == "BswDataReceptionPolicy is an abstract class."
    
    def test_get_set_received_data_ref(self):
        policy = BswQueuedDataReceptionPolicy()
        
        ref = RefType()
        result = policy.setReceivedDataRef(ref)
        
        assert result == policy
        assert policy.getReceivedDataRef() == ref
        
        # Setting None should not change the value (based on implementation)
        result = policy.setReceivedDataRef(None)
        assert result == policy
        assert policy.getReceivedDataRef() == ref  # Value should remain unchanged


class TestBswQueuedDataReceptionPolicy:
    """Test cases for BswQueuedDataReceptionPolicy class - represents a queued data reception policy in a BSW module."""
    def test_initialization(self):
        policy = BswQueuedDataReceptionPolicy()
        
        assert policy.getQueueLength() is None
        
    def test_set_queue_length(self):
        policy = BswQueuedDataReceptionPolicy()
        
        queue_length = PositiveInteger()
        queue_length.setValue(5)
        result = policy.setQueueLength(queue_length)
        
        assert result == policy
        assert policy.getQueueLength() == queue_length


class TestBswInternalTriggeringPoint:
    """Test cases for BswInternalTriggeringPoint class - represents an internal triggering point in a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = BswInternalTriggeringPoint(ar_root, "test_internal_triggering_point")
        
        assert point.short_name == "test_internal_triggering_point"
        assert point.getSwImplPolicy() is None
        
    def test_set_sw_impl_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = BswInternalTriggeringPoint(ar_root, "test_internal_triggering_point")
        
        policy = SwImplPolicyEnum()
        result = point.setSwImplPolicy(policy)
        
        assert result == point
        assert point.getSwImplPolicy() == policy
        
        # Setting None should not change the value (based on implementation)
        result = point.setSwImplPolicy(None)
        assert result == point
        assert point.getSwImplPolicy() == policy  # Value should remain unchanged


class TestBswInternalBehavior:
    """Test cases for BswInternalBehavior class - represents the internal behavior of a BSW module."""
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        assert behavior.short_name == "test_internal_behavior"
        
    def test_get_set_ar_typed_per_instance_memories(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setArTypedPerInstanceMemories([])
        assert result == behavior
        assert behavior.getArTypedPerInstanceMemories() == []
        
    def test_get_set_bsw_per_instance_memory_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setBswPerInstanceMemoryPolicies([])
        assert result == behavior
        assert behavior.getBswPerInstanceMemoryPolicies() == []
        
    def test_get_set_client_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setClientPolicies([])
        assert result == behavior
        assert behavior.getClientPolicies() == []
        
    def test_get_set_distinguished_partitions(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setDistinguishedPartitions([])
        assert result == behavior
        assert behavior.getDistinguishedPartitions() == []
        
    def test_get_set_exclusive_area_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setExclusiveAreaPolicies([])
        assert result == behavior
        assert behavior.getExclusiveAreaPolicies() == []
        
    def test_get_set_internal_triggering_point_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setInternalTriggeringPointPolicies([])
        assert result == behavior
        assert behavior.getInternalTriggeringPointPolicies() == []
        
    def test_get_set_parameter_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setParameterPolicies([])
        assert result == behavior
        assert behavior.getParameterPolicies() == []
        
    def test_get_set_released_trigger_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setReleasedTriggerPolicies([])
        assert result == behavior
        assert behavior.getReleasedTriggerPolicies() == []
        
    def test_get_set_scheduler_name_prefixes(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setSchedulerNamePrefixes([])
        assert result == behavior
        assert behavior.getSchedulerNamePrefixes() == []
        
    def test_get_set_send_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setSendPolicies([])
        assert result == behavior
        assert behavior.getSendPolicies() == []
        
    def test_get_set_service_dependencies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setServiceDependencies([])
        assert result == behavior
        assert behavior.getServiceDependencies() == []
        
    def test_get_set_trigger_direct_implementations(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setTriggerDirectImplementations([])
        assert result == behavior
        assert behavior.getTriggerDirectImplementations() == []
        
    def test_get_set_variation_point_proxies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setVariationPointProxies([])
        assert result == behavior
        assert behavior.getVariationPointProxies() == []
        
    def test_get_set_mode_sender_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setModeSenderPolicies([])
        assert result == behavior
        assert behavior.getModeSenderPolicies() == []
        
    def test_get_set_per_instance_parameters(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        result = behavior.setPerInstanceParameters([])
        assert result == behavior
        assert behavior.getPerInstanceParameters() == []
        
    def test_add_reception_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        # We'll use a concrete implementation of BswDataReceptionPolicy
        policy = BswQueuedDataReceptionPolicy()
        result = behavior.addReceptionPolicy(policy)
        
        assert result == behavior
        assert behavior.getReceptionPolicies() == [policy]
        
        result = behavior.addReceptionPolicy(None)
        assert result == behavior
        assert len(behavior.getReceptionPolicies()) == 1  # None should not be added
        
    def test_create_bsw_internal_triggering_point(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        point = behavior.createBswInternalTriggeringPoint("test_point")
        
        assert point.short_name == "test_point"
        assert len(behavior.getInternalTriggeringPoints()) == 1
        
    def test_create_bsw_called_entity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswCalledEntity("test_called_entity")
        
        assert entity.short_name == "test_called_entity"
        assert len(behavior.getBswCalledEntities()) == 1
        
    def test_get_bsw_called_entities(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswCalledEntity("test_called_entity")
        
        called_entities = behavior.getBswCalledEntities()
        assert len(called_entities) == 1
        assert called_entities[0] == entity
        
    def test_create_bsw_schedulable_entity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswSchedulableEntity("test_schedulable_entity")
        
        assert entity.short_name == "test_schedulable_entity"
        assert len(behavior.getBswSchedulableEntities()) == 1
        
    def test_get_bsw_schedulable_entities(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswSchedulableEntity("test_schedulable_entity")
        
        schedulable_entities = behavior.getBswSchedulableEntities()
        assert len(schedulable_entities) == 1
        assert schedulable_entities[0] == entity
        
    def test_create_bsw_interrupt_entity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswInterruptEntity("test_interrupt_entity")
        
        assert entity.short_name == "test_interrupt_entity"
        assert len(behavior.getBswInterruptEntities()) == 1
        
    def test_get_bsw_interrupt_entities(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswInterruptEntity("test_interrupt_entity")
        
        interrupt_entities = behavior.getBswInterruptEntities()
        assert len(interrupt_entities) == 1
        assert interrupt_entities[0] == entity
        
    def test_get_bsw_module_entities(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        entity = behavior.createBswCalledEntity("test_called_entity")
        
        module_entities = behavior.getBswModuleEntities()
        assert len(module_entities) == 1
        assert module_entities[0] == entity
        
    def test_create_bsw_mode_switch_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswModeSwitchEvent("test_mode_switch_event")
        
        assert event.short_name == "test_mode_switch_event"
        assert len(behavior.getBswModeSwitchEvents()) == 1
        
    def test_get_bsw_mode_switch_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswModeSwitchEvent("test_mode_switch_event")
        
        mode_switch_events = behavior.getBswModeSwitchEvents()
        assert len(mode_switch_events) == 1
        assert mode_switch_events[0] == event
        
    def test_create_bsw_timing_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswTimingEvent("test_timing_event")
        
        assert event.short_name == "test_timing_event"
        assert len(behavior.getBswTimingEvents()) == 1
        
    def test_get_bsw_timing_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswTimingEvent("test_timing_event")
        
        timing_events = behavior.getBswTimingEvents()
        assert len(timing_events) == 1
        assert timing_events[0] == event
        
    def test_create_bsw_data_received_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswDataReceivedEvent("test_data_received_event")
        
        assert event.short_name == "test_data_received_event"
        assert len(behavior.getBswDataReceivedEvents()) == 1
        
    def test_get_bsw_data_received_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswDataReceivedEvent("test_data_received_event")
        
        data_received_events = behavior.getBswDataReceivedEvents()
        assert len(data_received_events) == 1
        assert data_received_events[0] == event
        
    def test_create_bsw_internal_trigger_occurred_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswInternalTriggerOccurredEvent("test_internal_trigger_occurred_event")
        
        assert event.short_name == "test_internal_trigger_occurred_event"
        assert len(behavior.getBswInternalTriggerOccurredEvents()) == 1
        
    def test_get_bsw_internal_trigger_occurred_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswInternalTriggerOccurredEvent("test_internal_trigger_occurred_event")
        
        internal_trigger_occurred_events = behavior.getBswInternalTriggerOccurredEvents()
        assert len(internal_trigger_occurred_events) == 1
        assert internal_trigger_occurred_events[0] == event
        
    def test_create_bsw_external_trigger_occurred_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswExternalTriggerOccurredEvent("test_external_trigger_occurred_event")
        
        assert event.short_name == "test_external_trigger_occurred_event"
        assert len(behavior.getBswExternalTriggerOccurredEvents()) == 1
        
    def test_get_bsw_external_trigger_occurred_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswExternalTriggerOccurredEvent("test_external_trigger_occurred_event")
        
        external_trigger_occurred_events = behavior.getBswExternalTriggerOccurredEvents()
        assert len(external_trigger_occurred_events) == 1
        assert external_trigger_occurred_events[0] == event
        
    def test_create_bsw_operation_invoked_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswOperationInvokedEvent("test_operation_invoked_event")
        
        assert event.short_name == "test_operation_invoked_event"
        assert len(behavior.getBswOperationInvokedEvents()) == 1
        
    def test_get_bsw_operation_invoked_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswOperationInvokedEvent("test_operation_invoked_event")
        
        operation_invoked_events = behavior.getBswOperationInvokedEvents()
        assert len(operation_invoked_events) == 1
        assert operation_invoked_events[0] == event
        
    def test_create_bsw_background_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswBackgroundEvent("test_background_event")
        
        assert event.short_name == "test_background_event"
        assert len(behavior.getBswBackgroundEvents()) == 1
        
    def test_get_bsw_background_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswBackgroundEvent("test_background_event")
        
        background_events = behavior.getBswBackgroundEvents()
        assert len(background_events) == 1
        assert background_events[0] == event
        
    def test_get_bsw_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        event = behavior.createBswOperationInvokedEvent("test_operation_invoked_event")
        
        events = behavior.getBswEvents()
        assert len(events) == 1
        assert events[0] == event
        
    def test_add_included_mode_declaration_group_set(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet
        
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        group_set = IncludedModeDeclarationGroupSet()
        behavior.addIncludedModeDeclarationGroupSet(group_set)
        
        assert len(behavior.getIncludedModeDeclarationGroupSets()) == 1
        assert behavior.getIncludedModeDeclarationGroupSets()[0] == group_set
        
    def test_get_included_mode_declaration_group_sets(self):
        
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        assert behavior.getIncludedModeDeclarationGroupSets() == []
        
    def test_add_included_data_type_set(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
        
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        type_set = IncludedDataTypeSet()
        behavior.addIncludedDataTypeSet(type_set)
        
        assert len(behavior.getIncludedDataTypeSets()) == 1
        assert behavior.getIncludedDataTypeSets()[0] == type_set
        
    def test_get_included_data_type_sets(self):
        
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        assert behavior.getIncludedDataTypeSets() == []
        
    def test_get_mode_receiver_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        # Initially should be an empty list
        assert behavior.getModeReceiverPolicies() == []
        
    def test_get_set_mode_sender_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        policies = []
        result = behavior.setModeSenderPolicies(policies)
        
        assert result == behavior
        assert behavior.getModeSenderPolicies() == policies
        
        # Setting None should not change the value (based on implementation)
        result = behavior.setModeSenderPolicies(None)
        assert result == behavior
        assert behavior.getModeSenderPolicies() == policies  # Value should remain unchanged
        
    def test_add_mode_sender_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        
        policy = BswModeSenderPolicy()
        behavior.addModeSenderPolicy(policy)
        
        # This method adds to modeReceiverPolicies, not modeSenderPolicies
        assert len(behavior.getModeReceiverPolicies()) == 1
        assert behavior.getModeReceiverPolicies()[0] == policy


class TestBswDistinguishedPartition:
    """Test cases for BswDistinguishedPartition class - represents an abstract partition in which context the code of the enclosing BswModuleBehavior can be executed."""
    def test_initialization(self):
        """Test BswDistinguishedPartition initialization with proper attributes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        partition = BswDistinguishedPartition(ar_root, "test_partition")
        
        assert partition.short_name == "test_partition"