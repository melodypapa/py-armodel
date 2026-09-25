"""
Comprehensive test suite for BSW (Basic Software) Behavior module classes.
This module tests all the classes in the BswBehavior.py file to ensure 100% coverage.
Tests verify initialization, getter/setter methods, and special functionality for each class.
"""

import typing

import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswApiOptions,
    BswAsynchronousServerCallPoint,
    BswAsynchronousServerCallResultPoint,
    BswAsynchronousServerCallReturnsEvent,
    BswBackgroundEvent,
    BswCalledEntity,
    BswClientPolicy,
    BswDataReceivedEvent,
    BswDataReceptionPolicy,
    BswDataSendPolicy,
    BswDirectCallPoint,
    BswDistinguishedPartition,
    BswEvent,
    BswExclusiveAreaPolicy,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggeringPoint,
    BswInternalTriggeringPointPolicy,
    BswInternalTriggerOccurredEvent,
    BswInterruptCategory,
    BswInterruptEntity,
    BswModeManagerErrorEvent,
    BswModeReceiverPolicy,
    BswModeSenderPolicy,
    BswModeSwitchAckRequest,
    BswModeSwitchedAckEvent,
    BswModeSwitchEvent,
    BswModuleCallPoint,
    BswModuleEntity,
    BswOperationInvokedEvent,
    BswOsTaskExecutionEvent,
    BswParameterPolicy,
    BswPerInstanceMemoryPolicy,
    BswQueuedDataReceptionPolicy,
    BswReleasedTriggerPolicy,
    BswSchedulableEntity,
    BswScheduleEvent,
    BswServiceDependency,
    BswSynchronousServerCallPoint,
    BswTimingEvent,
    BswTriggerDirectImplementation,
    BswVariableAccess,
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import ModeInBswModuleDescriptionInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ApiPrincipleEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import BswMgrNeeds, RoleBasedDataAssignment, SymbolicNameProps
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping import BswServiceDependencyIdent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Boolean, Identifier, PositiveInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedDataTypeAssignment
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum


class TestBswModuleCallPoint:
    """Test cases for BswModuleCallPoint class - represents a call point in a BSW module."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that BswModuleCallPoint is abstract and cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        with pytest.raises(TypeError, match="BswModuleCallPoint is an abstract class"):
            _call_point = BswModuleCallPoint(ar_root, "test_call_point")

    def test_concrete_subclass_can_be_instantiated(self):
        """Test that concrete subclasses of BswModuleCallPoint can be instantiated."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        # Test with BswDirectCallPoint (a concrete subclass)
        call_point = BswDirectCallPoint(ar_root, "test_call_point")

        assert call_point.short_name == "test_call_point"

    def test_initialization(self):
        """Test that a concrete subclass initializes its fields with the spec defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = BswDirectCallPoint(ar_root, "test_call_point")

        assert call_point.getContextLimitationRefs() == []

    def test_get_context_limitation_refs(self):
        """Test that getContextLimitationRefs returns the field directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = BswDirectCallPoint(ar_root, "test_call_point")

        assert call_point.getContextLimitationRefs() == []

    def test_add_context_limitation_ref(self):
        """Test adding a context limitation reference to a concrete subclass of BswModuleCallPoint."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = BswDirectCallPoint(ar_root, "test_call_point")

        ref = RefType()
        ref.setValue("/Partition1")
        result = call_point.addContextLimitationRef(ref)

        assert result == call_point
        assert call_point.getContextLimitationRefs() == [ref]

    def test_add_context_limitation_ref_none_no_op(self):
        """Test that addContextLimitationRef is a no-op on None."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = BswDirectCallPoint(ar_root, "test_call_point")

        result = call_point.addContextLimitationRef(None)

        assert result == call_point
        assert call_point.getContextLimitationRefs() == []


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
        """Test initialization of BswDirectCallPoint with the spec defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        direct_call_point = BswDirectCallPoint(ar_root, "test_direct_call")

        assert direct_call_point.short_name == "test_direct_call"
        assert direct_call_point.getCalledEntryRef() is None
        assert direct_call_point.getCalledFromWithinExclusiveAreaRef() is None
        assert direct_call_point.getContextLimitationRefs() == []

    def test_get_set_called_entry_ref(self):
        """Test setting and getting the called entry reference, including the None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        direct_call_point = BswDirectCallPoint(ar_root, "test_direct_call")

        ref = RefType()
        ref.setValue("/mod/Entry")
        result = direct_call_point.setCalledEntryRef(ref)

        assert result == direct_call_point
        assert direct_call_point.getCalledEntryRef() == ref

        result = direct_call_point.setCalledEntryRef(None)
        assert result == direct_call_point
        assert direct_call_point.getCalledEntryRef() == ref

    def test_get_set_called_from_within_exclusive_area_ref(self):
        """Test setting and getting the exclusive area reference, including the None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        direct_call_point = BswDirectCallPoint(ar_root, "test_direct_call")

        ref = RefType()
        ref.setValue("/mod/AreaNesting")
        result = direct_call_point.setCalledFromWithinExclusiveAreaRef(ref)

        assert result == direct_call_point
        assert direct_call_point.getCalledFromWithinExclusiveAreaRef() == ref

        result = direct_call_point.setCalledFromWithinExclusiveAreaRef(None)
        assert result == direct_call_point
        assert direct_call_point.getCalledFromWithinExclusiveAreaRef() == ref

    def test_type_annotations(self):
        """Pin the spec 0..1 optional annotations on the accessors."""
        getter_hints = typing.get_type_hints(BswDirectCallPoint.getCalledEntryRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(BswDirectCallPoint.setCalledEntryRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is BswDirectCallPoint

        getter_hints = typing.get_type_hints(BswDirectCallPoint.getCalledFromWithinExclusiveAreaRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(BswDirectCallPoint.setCalledFromWithinExclusiveAreaRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is BswDirectCallPoint


class TestBswSynchronousServerCallPoint:
    """Test cases for BswSynchronousServerCallPoint class - represents a synchronous procedure call point via the BSW Scheduler."""

    def test_initialization(self):
        """Test initialization of BswSynchronousServerCallPoint with the spec defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sync_call_point = BswSynchronousServerCallPoint(ar_root, "test_sync_call")

        assert sync_call_point.short_name == "test_sync_call"
        assert sync_call_point.getCalledEntryRef() is None
        assert sync_call_point.getCalledFromWithinExclusiveAreaRef() is None
        assert sync_call_point.getContextLimitationRefs() == []

    def test_get_set_called_entry_ref(self):
        """Test setting and getting the called entry reference, including the None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sync_call_point = BswSynchronousServerCallPoint(ar_root, "test_sync_call")

        ref = RefType()
        ref.setValue("/mod/ClientServerEntry")
        result = sync_call_point.setCalledEntryRef(ref)

        assert result == sync_call_point
        assert sync_call_point.getCalledEntryRef() == ref

        result = sync_call_point.setCalledEntryRef(None)
        assert result == sync_call_point
        assert sync_call_point.getCalledEntryRef() == ref

    def test_get_set_called_from_within_exclusive_area_ref(self):
        """Test setting and getting the exclusive area reference, including the None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sync_call_point = BswSynchronousServerCallPoint(ar_root, "test_sync_call")

        ref = RefType()
        ref.setValue("/mod/AreaNesting")
        result = sync_call_point.setCalledFromWithinExclusiveAreaRef(ref)

        assert result == sync_call_point
        assert sync_call_point.getCalledFromWithinExclusiveAreaRef() == ref

        result = sync_call_point.setCalledFromWithinExclusiveAreaRef(None)
        assert result == sync_call_point
        assert sync_call_point.getCalledFromWithinExclusiveAreaRef() == ref

    def test_type_annotations(self):
        """Pin the spec 0..1 optional annotations on the accessors."""
        getter_hints = typing.get_type_hints(BswSynchronousServerCallPoint.getCalledEntryRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(BswSynchronousServerCallPoint.setCalledEntryRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is BswSynchronousServerCallPoint

        getter_hints = typing.get_type_hints(BswSynchronousServerCallPoint.getCalledFromWithinExclusiveAreaRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(BswSynchronousServerCallPoint.setCalledFromWithinExclusiveAreaRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is BswSynchronousServerCallPoint


class TestBswAsynchronousServerCallResultPoint:
    """Test cases for BswAsynchronousServerCallResultPoint class - represents an asynchronous server call result point in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        async_result_point = BswAsynchronousServerCallResultPoint(ar_root, "test_async_result")

        assert async_result_point.short_name == "test_async_result"
        assert async_result_point.getAsynchronousServerCallPointRef() is None

    def test_get_set_asynchronous_server_call_point_ref(self):
        """get/set round-trip, chaining, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        result_point = BswAsynchronousServerCallResultPoint(ar_root, "test_async_result")

        ref = RefType().setValue("/CP/async_call_point")
        ref.setDest("BSW-ASYNCHRONOUS-SERVER-CALL-POINT")
        result = result_point.setAsynchronousServerCallPointRef(ref)

        assert result is result_point
        assert result_point.getAsynchronousServerCallPointRef() == ref

        # None is a no-op
        result = result_point.setAsynchronousServerCallPointRef(None)
        assert result is result_point
        assert result_point.getAsynchronousServerCallPointRef() == ref


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

    def test_concrete_subclass_initialization(self):
        """Test that BswModuleEntity.__init__ defaults are applied to concrete subclasses."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_entity")

        assert entity.getAccessedModeGroupRefs() == []
        assert entity.getActivationPointRefs() == []
        assert entity.getCallPoints() == []
        assert entity.getDataReceivePoints() == []
        assert entity.getDataSendPoints() == []
        assert entity.getImplementedEntryRef() is None
        assert entity.getIssuedTriggerRefs() == []
        assert entity.getManagedModeGroupRefs() == []
        assert entity.getSchedulerNamePrefixRef() is None

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

        # Setting None should not change the value (based on implementation)
        result = entity.setSchedulerNamePrefixRef(None)
        assert result == entity
        assert entity.getSchedulerNamePrefixRef() == ref  # Value should remain unchanged


class TestBswCalledEntity:
    """Test cases for BswCalledEntity class - represents a called entity in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "test_called_entity")

        assert entity.short_name == "test_called_entity"
        assert entity.getShortName() == "test_called_entity"
        assert isinstance(entity, BswModuleEntity)
        assert entity.getParent() is ar_root


class TestBswSchedulableEntity:
    """Test cases for BswSchedulableEntity class - represents a schedulable entity in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswSchedulableEntity(ar_root, "test_schedulable_entity")

        assert entity.short_name == "test_schedulable_entity"
        assert entity.getShortName() == "test_schedulable_entity"
        assert isinstance(entity, BswModuleEntity)
        assert entity.getParent() is ar_root


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

    def test_get_set_interrupt_category(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswInterruptEntity(ar_root, "test_interrupt_entity")

        category = BswInterruptCategory().setValue(BswInterruptCategory.CAT2)
        result = entity.setInterruptCategory(category)

        assert result == entity
        assert entity.getInterruptCategory() == category

        # Setting None should not change the value (based on implementation)
        result = entity.setInterruptCategory(None)
        assert result == entity
        assert entity.getInterruptCategory() == category  # Value should remain unchanged

    def test_get_set_interrupt_source(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswInterruptEntity(ar_root, "test_interrupt_entity")

        source = String().setValue("CAN interrupt")
        result = entity.setInterruptSource(source)

        assert result == entity
        assert entity.getInterruptSource() == source
        assert entity.getInterruptSource().getValue() == "CAN interrupt"

        # Setting None should not change the value (based on implementation)
        result = entity.setInterruptSource(None)
        assert result == entity
        assert entity.getInterruptSource() == source  # Value should remain unchanged

    def test_type_annotations(self):
        """Pin the spec 0..1 optional annotations on the accessors."""
        getter_hints = typing.get_type_hints(BswInterruptEntity.getInterruptCategory)
        assert getter_hints.get("return") == typing.Optional[BswInterruptCategory]

        setter_hints = typing.get_type_hints(BswInterruptEntity.setInterruptCategory)
        assert setter_hints.get("value") == typing.Optional[BswInterruptCategory]
        assert setter_hints.get("return") is BswInterruptEntity

        getter_hints = typing.get_type_hints(BswInterruptEntity.getInterruptSource)
        assert getter_hints.get("return") == typing.Optional[String]

        setter_hints = typing.get_type_hints(BswInterruptEntity.setInterruptSource)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is BswInterruptEntity


class TestBswEvent:
    """Test cases for BswEvent class - abstract base class for BSW events."""

    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            BswEvent(ar_root, "BswEvent")
        assert str(err.value) == "BswEvent is an abstract class."

    def test_concrete_subclass_initialization(self):
        """Test that BswEvent.__init__ defaults are inherited by a concrete subclass."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_event")

        assert event.short_name == "test_event"
        assert event.getContextLimitationRefs() == []
        assert event.getDisabledInModeIRefs() == []
        assert event.getStartsOnEventRef() is None

    def test_get_set_starts_on_event_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_event")

        ref = RefType()
        result = event.setStartsOnEventRef(ref)

        assert result == event
        assert event.getStartsOnEventRef() == ref

        # Setting None should not change the value
        result = event.setStartsOnEventRef(None)
        assert result == event
        assert event.getStartsOnEventRef() == ref

    def test_add_context_limitation_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_event")

        ref = RefType()
        result = event.addContextLimitationRef(ref)

        assert result == event
        assert event.getContextLimitationRefs() == [ref]

        # Setting None should not append
        result = event.addContextLimitationRef(None)
        assert result == event
        assert event.getContextLimitationRefs() == [ref]

    def test_add_disabled_in_mode_iref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOperationInvokedEvent(ar_root, "test_event")

        iref = ModeInBswModuleDescriptionInstanceRef()
        result = event.addDisabledInModeIRef(iref)

        assert result == event
        assert event.getDisabledInModeIRefs() == [iref]

        # Setting None should not append
        result = event.addDisabledInModeIRef(None)
        assert result == event
        assert event.getDisabledInModeIRefs() == [iref]


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
        assert event.getModeIRefs() == []

    def test_set_activation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")

        activation = ModeActivationKind.ON_ENTRY
        result = event.setActivation(activation)

        assert result == event
        assert event.getActivation() == activation

    def test_set_activation_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")

        event.setActivation(ModeActivationKind.ON_EXIT)
        event.setActivation(None)

        assert event.getActivation() == ModeActivationKind.ON_EXIT

    def test_add_mode_iref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")

        iref = ModeInBswModuleDescriptionInstanceRef()
        result = event.addModeIRef(iref)

        assert result == event
        assert event.getModeIRefs() == [iref]

    def test_add_mode_iref_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")

        event.addModeIRef(None)

        assert event.getModeIRefs() == []

    def test_add_multiple_mode_irefs(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")

        iref1 = ModeInBswModuleDescriptionInstanceRef()
        iref2 = ModeInBswModuleDescriptionInstanceRef()
        event.addModeIRef(iref1).addModeIRef(iref2)

        assert event.getModeIRefs() == [iref1, iref2]

    def test_method_chaining(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchEvent(ar_root, "test_mode_switch_event")

        iref = ModeInBswModuleDescriptionInstanceRef()
        result = event.setActivation(ModeActivationKind.ON_TRANSITION).addModeIRef(iref)

        assert result is event
        assert event.getActivation() == ModeActivationKind.ON_TRANSITION
        assert event.getModeIRefs() == [iref]


class TestBswModeManagerErrorEvent:
    """Test cases for BswModeManagerErrorEvent class - represents a mode manager error event in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeManagerErrorEvent(ar_root, "test_mode_manager_error_event")

        assert event.short_name == "test_mode_manager_error_event"
        assert event.getModeGroupRef() is None

    def test_get_set_mode_group_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeManagerErrorEvent(ar_root, "test_mode_manager_error_event")

        ref = RefType()
        ref.setValue("/MG/ModeDeclarationGroupPrototype")
        ref.setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        result = event.setModeGroupRef(ref)

        assert result == event
        assert event.getModeGroupRef() == ref

    def test_set_mode_group_ref_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeManagerErrorEvent(ar_root, "test_mode_manager_error_event")

        ref = RefType()
        ref.setValue("/MG/ModeDeclarationGroupPrototype")
        event.setModeGroupRef(ref)
        event.setModeGroupRef(None)

        assert event.getModeGroupRef() == ref

    def test_method_chaining(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeManagerErrorEvent(ar_root, "test_mode_manager_error_event")

        ref = RefType()
        ref.setValue("/MG/ModeDeclarationGroupPrototype")
        result = event.setModeGroupRef(ref)

        assert result is event
        assert event.getModeGroupRef() == ref


class TestBswModeSwitchedAckEvent:
    """Test cases for BswModeSwitchedAckEvent class - represents a mode switched acknowledgement event in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchedAckEvent(ar_root, "test_mode_switched_ack_event")

        assert event.short_name == "test_mode_switched_ack_event"
        assert event.getModeGroupRef() is None

    def test_get_set_mode_group_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchedAckEvent(ar_root, "test_mode_switched_ack_event")

        ref = RefType()
        ref.setValue("/MG/ModeDeclarationGroupPrototype")
        ref.setDest("MODE-DECLARATION-GROUP-PROTOTYPE")
        result = event.setModeGroupRef(ref)

        assert result == event
        assert event.getModeGroupRef() == ref

    def test_set_mode_group_ref_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchedAckEvent(ar_root, "test_mode_switched_ack_event")

        ref = RefType()
        ref.setValue("/MG/ModeDeclarationGroupPrototype")
        event.setModeGroupRef(ref)
        event.setModeGroupRef(None)

        assert event.getModeGroupRef() == ref

    def test_method_chaining(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswModeSwitchedAckEvent(ar_root, "test_mode_switched_ack_event")

        ref = RefType()
        ref.setValue("/MG/ModeDeclarationGroupPrototype")
        result = event.setModeGroupRef(ref)

        assert result is event
        assert event.getModeGroupRef() == ref


class TestBswAsynchronousServerCallReturnsEvent:
    """Test cases for BswAsynchronousServerCallReturnsEvent class - represents the callback event for asynchronous Client-Server communication."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswAsynchronousServerCallReturnsEvent(ar_root, "test_async_server_call_returns_event")

        assert event.short_name == "test_async_server_call_returns_event"
        assert event.getEventSourceRef() is None

    def test_get_set_event_source_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswAsynchronousServerCallReturnsEvent(ar_root, "test_async_server_call_returns_event")

        ref = RefType()
        ref.setValue("/CP/BswAsynchronousServerCallResultPoint")
        ref.setDest("BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT")
        result = event.setEventSourceRef(ref)

        assert result == event
        assert event.getEventSourceRef() == ref

    def test_set_event_source_ref_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswAsynchronousServerCallReturnsEvent(ar_root, "test_async_server_call_returns_event")

        ref = RefType()
        ref.setValue("/CP/BswAsynchronousServerCallResultPoint")
        event.setEventSourceRef(ref)
        event.setEventSourceRef(None)

        assert event.getEventSourceRef() == ref

    def test_method_chaining(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswAsynchronousServerCallReturnsEvent(ar_root, "test_async_server_call_returns_event")

        ref = RefType()
        ref.setValue("/CP/BswAsynchronousServerCallResultPoint")
        result = event.setEventSourceRef(ref)

        assert result is event
        assert event.getEventSourceRef() == ref


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

    def test_period_ms(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswTimingEvent(ar_root, "test_timing_event")

        assert event.periodMs is None

        period = TimeValue()
        period.value = 2.5
        event.setPeriod(period)

        assert event.periodMs == 2500  # 2.5 * 1000


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

        timeout = TimeValue()
        timeout.setValue(5.0)
        result = ack_request.setTimeout(timeout)

        assert result == ack_request
        assert ack_request.getTimeout() == timeout
        assert ack_request.getTimeout().getValue() == 5.0

    def test_set_timeout_none_is_noop(self):
        ack_request = BswModeSwitchAckRequest()

        timeout = TimeValue()
        timeout.setValue(5.0)
        ack_request.setTimeout(timeout)
        result = ack_request.setTimeout(None)

        assert result == ack_request
        assert ack_request.getTimeout() == timeout

    def test_type_annotations(self):
        """Pin the spec 0..1 optional annotations on the accessors."""
        getter_hints = typing.get_type_hints(BswModeSwitchAckRequest.getTimeout)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(BswModeSwitchAckRequest.setTimeout)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is BswModeSwitchAckRequest


class TestBswModeSenderPolicy:
    """Test cases for BswModeSenderPolicy class - specifies the details for the sending of a mode switch for the referred mode group."""

    def test_initialization(self):
        policy = BswModeSenderPolicy()

        assert policy.getAckRequest() is None
        assert policy.getEnhancedModeApi() is None
        assert policy.getProvidedModeGroupRef() is None
        assert policy.getQueueLength() is None

    def test_get_set_ack_request(self):
        policy = BswModeSenderPolicy()

        request = BswModeSwitchAckRequest()
        result = policy.setAckRequest(request)

        assert result == policy
        assert policy.getAckRequest() == request

    def test_set_ack_request_none_is_noop(self):
        policy = BswModeSenderPolicy()

        request = BswModeSwitchAckRequest()
        policy.setAckRequest(request)
        policy.setAckRequest(None)

        assert policy.getAckRequest() == request

    def test_get_set_enhanced_mode_api(self):
        policy = BswModeSenderPolicy()

        result = policy.setEnhancedModeApi(True)

        assert result == policy
        assert policy.getEnhancedModeApi() is True

    def test_set_enhanced_mode_api_none_is_noop(self):
        policy = BswModeSenderPolicy()

        policy.setEnhancedModeApi(True)
        policy.setEnhancedModeApi(None)

        assert policy.getEnhancedModeApi() is True

    def test_get_set_provided_mode_group_ref(self):
        policy = BswModeSenderPolicy()

        ref = RefType()
        result = policy.setProvidedModeGroupRef(ref)

        assert result == policy
        assert policy.getProvidedModeGroupRef() == ref

    def test_set_provided_mode_group_ref_none_is_noop(self):
        policy = BswModeSenderPolicy()

        ref = RefType()
        policy.setProvidedModeGroupRef(ref)
        policy.setProvidedModeGroupRef(None)

        assert policy.getProvidedModeGroupRef() == ref

    def test_get_set_queue_length(self):
        policy = BswModeSenderPolicy()

        length = ARNumerical()
        length.setValue(10)
        result = policy.setQueueLength(length)

        assert result == policy
        assert policy.getQueueLength() == length

    def test_set_queue_length_none_is_noop(self):
        policy = BswModeSenderPolicy()

        length = ARNumerical()
        length.setValue(10)
        policy.setQueueLength(length)
        policy.setQueueLength(None)

        assert policy.getQueueLength() == length


class TestBswBackgroundEvent:
    """Test cases for BswBackgroundEvent class - represents a background event in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswBackgroundEvent(ar_root, "test_background_event")

        assert event.short_name == "test_background_event"
        assert event.getShortName() == "test_background_event"
        assert isinstance(event, BswScheduleEvent)
        assert event.getParent() is ar_root


class TestBswOsTaskExecutionEvent:
    """Test cases for BswOsTaskExecutionEvent class - represents an OS task execution event in a BSW module."""

    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BswOsTaskExecutionEvent(ar_root, "test_os_task_event")

        assert event.short_name == "test_os_task_event"
        assert event.getShortName() == "test_os_task_event"
        assert isinstance(event, BswScheduleEvent)
        assert event.getParent() is ar_root


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

    def test_initialization(self):
        policy = BswQueuedDataReceptionPolicy()
        assert policy.getEnableTakeAddress() is None

    def test_abstract_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError) as err:
            BswApiOptions()
        assert str(err.value) == "BswApiOptions is an abstract class."

    def test_get_set_enable_take_address(self):
        # BswApiOptions is abstract: exercise the base accessors through a concrete subclass
        policy = BswQueuedDataReceptionPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        getter_hints = typing.get_type_hints(BswApiOptions.getEnableTakeAddress)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(BswApiOptions.setEnableTakeAddress)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is BswApiOptions


class TestBswExclusiveAreaPolicy:
    """Test cases for BswExclusiveAreaPolicy class - BSW exclusive area policy."""

    def test_initialization(self):
        policy = BswExclusiveAreaPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getApiPrinciple() is None
        assert policy.getExclusiveAreaRef() is None

    def test_get_set_api_principle(self):
        policy = BswExclusiveAreaPolicy()

        result = policy.setApiPrinciple(ApiPrincipleEnum.COMMON)
        assert result == policy
        assert policy.getApiPrinciple() == ApiPrincipleEnum.COMMON

        # Setting None is a no-op: the existing value is preserved
        result = policy.setApiPrinciple(None)
        assert result == policy
        assert policy.getApiPrinciple() == ApiPrincipleEnum.COMMON

    def test_get_set_exclusive_area_ref(self):
        policy = BswExclusiveAreaPolicy()
        ref = RefType()

        result = policy.setExclusiveAreaRef(ref)
        assert result == policy
        assert policy.getExclusiveAreaRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setExclusiveAreaRef(None)
        assert result == policy
        assert policy.getExclusiveAreaRef() == ref


class TestBswPerInstanceMemoryPolicy:
    """Test cases for BswPerInstanceMemoryPolicy class - BSW per-instance memory policy (XSD-only class)."""

    def test_initialization(self):
        policy = BswPerInstanceMemoryPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getArTypedPerInstanceMemoryRef() is None
        assert policy.getVariationPoint() is None

    def test_get_set_ar_typed_per_instance_memory_ref(self):
        policy = BswPerInstanceMemoryPolicy()
        ref = RefType()

        result = policy.setArTypedPerInstanceMemoryRef(ref)
        assert result == policy
        assert policy.getArTypedPerInstanceMemoryRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setArTypedPerInstanceMemoryRef(None)
        assert result == policy
        assert policy.getArTypedPerInstanceMemoryRef() == ref

    def test_inherited_enable_take_address(self):
        policy = BswPerInstanceMemoryPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

    def test_inherited_variation_point(self):
        policy = BswPerInstanceMemoryPolicy()
        variation_point = VariationPoint()

        result = policy.setVariationPoint(variation_point)
        assert result == policy
        assert policy.getVariationPoint() is variation_point

        # Setting None is a no-op: the existing value is preserved
        policy.setVariationPoint(None)
        assert policy.getVariationPoint() is variation_point


class TestBswClientPolicy:
    """Test cases for BswClientPolicy class - BSW client policy (XSD-only class)."""

    def test_initialization(self):
        policy = BswClientPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getRequiredClientServerEntryRef() is None
        assert policy.getVariationPoint() is None

    def test_get_set_required_client_server_entry_ref(self):
        policy = BswClientPolicy()
        ref = RefType()

        result = policy.setRequiredClientServerEntryRef(ref)
        assert result == policy
        assert policy.getRequiredClientServerEntryRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setRequiredClientServerEntryRef(None)
        assert result == policy
        assert policy.getRequiredClientServerEntryRef() == ref

    def test_inherited_enable_take_address(self):
        policy = BswClientPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

    def test_inherited_variation_point(self):
        policy = BswClientPolicy()
        variation_point = VariationPoint()

        result = policy.setVariationPoint(variation_point)
        assert result == policy
        assert policy.getVariationPoint() is variation_point

        # Setting None is a no-op: the existing value is preserved
        policy.setVariationPoint(None)
        assert policy.getVariationPoint() is variation_point


class TestBswInternalTriggeringPointPolicy:
    """Test cases for BswInternalTriggeringPointPolicy class - BSW internal triggering point policy (XSD-only class)."""

    def test_initialization(self):
        policy = BswInternalTriggeringPointPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getBswInternalTriggeringPointRef() is None
        assert policy.getVariationPoint() is None

    def test_get_set_bsw_internal_triggering_point_ref(self):
        policy = BswInternalTriggeringPointPolicy()
        ref = RefType()

        result = policy.setBswInternalTriggeringPointRef(ref)
        assert result == policy
        assert policy.getBswInternalTriggeringPointRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setBswInternalTriggeringPointRef(None)
        assert result == policy
        assert policy.getBswInternalTriggeringPointRef() == ref

    def test_inherited_enable_take_address(self):
        policy = BswInternalTriggeringPointPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

    def test_inherited_variation_point(self):
        policy = BswInternalTriggeringPointPolicy()
        variation_point = VariationPoint()

        result = policy.setVariationPoint(variation_point)
        assert result == policy
        assert policy.getVariationPoint() is variation_point

        # Setting None is a no-op: the existing value is preserved
        policy.setVariationPoint(None)
        assert policy.getVariationPoint() is variation_point


class TestBswParameterPolicy:
    """Test cases for BswParameterPolicy class - BSW parameter policy (XSD-only class)."""

    def test_initialization(self):
        policy = BswParameterPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getPerInstanceParameterRef() is None
        assert policy.getVariationPoint() is None

    def test_get_set_per_instance_parameter_ref(self):
        policy = BswParameterPolicy()
        ref = RefType()

        result = policy.setPerInstanceParameterRef(ref)
        assert result == policy
        assert policy.getPerInstanceParameterRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setPerInstanceParameterRef(None)
        assert result == policy
        assert policy.getPerInstanceParameterRef() == ref

    def test_inherited_enable_take_address(self):
        policy = BswParameterPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

    def test_inherited_variation_point(self):
        policy = BswParameterPolicy()
        variation_point = VariationPoint()

        result = policy.setVariationPoint(variation_point)
        assert result == policy
        assert policy.getVariationPoint() is variation_point

        # Setting None is a no-op: the existing value is preserved
        policy.setVariationPoint(None)
        assert policy.getVariationPoint() is variation_point


class TestBswReleasedTriggerPolicy:
    """Test cases for BswReleasedTriggerPolicy class - BSW released trigger policy (XSD-only class)."""

    def test_initialization(self):
        policy = BswReleasedTriggerPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getReleasedTriggerRef() is None
        assert policy.getVariationPoint() is None

    def test_get_set_released_trigger_ref(self):
        policy = BswReleasedTriggerPolicy()
        ref = RefType()

        result = policy.setReleasedTriggerRef(ref)
        assert result == policy
        assert policy.getReleasedTriggerRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setReleasedTriggerRef(None)
        assert result == policy
        assert policy.getReleasedTriggerRef() == ref

    def test_inherited_enable_take_address(self):
        policy = BswReleasedTriggerPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

    def test_inherited_variation_point(self):
        policy = BswReleasedTriggerPolicy()
        variation_point = VariationPoint()

        result = policy.setVariationPoint(variation_point)
        assert result == policy
        assert policy.getVariationPoint() is variation_point

        # Setting None is a no-op: the existing value is preserved
        policy.setVariationPoint(None)
        assert policy.getVariationPoint() is variation_point


class TestBswDataSendPolicy:
    """Test cases for BswDataSendPolicy class - BSW data send policy (XSD-only class)."""

    def test_initialization(self):
        policy = BswDataSendPolicy()
        assert policy.getEnableTakeAddress() is None
        assert policy.getProvidedDataRef() is None
        assert policy.getProviedeDataRef() is None
        assert policy.getVariationPoint() is None

    def test_get_set_provided_data_ref(self):
        policy = BswDataSendPolicy()
        ref = RefType()

        result = policy.setProvidedDataRef(ref)
        assert result == policy
        assert policy.getProvidedDataRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setProvidedDataRef(None)
        assert result == policy
        assert policy.getProvidedDataRef() == ref

    def test_get_set_proviede_data_ref(self):
        policy = BswDataSendPolicy()
        ref = RefType()

        result = policy.setProviedeDataRef(ref)
        assert result == policy
        assert policy.getProviedeDataRef() == ref

        # Setting None is a no-op: the existing value is preserved
        result = policy.setProviedeDataRef(None)
        assert result == policy
        assert policy.getProviedeDataRef() == ref

    def test_inherited_enable_take_address(self):
        policy = BswDataSendPolicy()
        value = Boolean()
        value.setValue(True)

        result = policy.setEnableTakeAddress(value)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

        # Setting None is a no-op: the existing value is preserved
        result = policy.setEnableTakeAddress(None)
        assert result == policy
        assert policy.getEnableTakeAddress() == value

    def test_inherited_variation_point(self):
        policy = BswDataSendPolicy()
        variation_point = VariationPoint()

        result = policy.setVariationPoint(variation_point)
        assert result == policy
        assert policy.getVariationPoint() is variation_point

        # Setting None is a no-op: the existing value is preserved
        policy.setVariationPoint(None)
        assert policy.getVariationPoint() is variation_point


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
    """Test cases for BswInternalTriggeringPoint class - represents the activation point for one or more BswInternalTriggerOccurredEvents."""

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

        policy = SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED)
        result = point.setSwImplPolicy(policy)

        assert result == point
        assert point.getSwImplPolicy() == policy

        # Setting None should not change the value (based on implementation)
        result = point.setSwImplPolicy(None)
        assert result == point
        assert point.getSwImplPolicy() == policy  # Value should remain unchanged

    def test_type_annotations(self):
        """Pin the spec 0..1 optional annotations on the accessors."""
        getter_hints = typing.get_type_hints(BswInternalTriggeringPoint.getSwImplPolicy)
        assert getter_hints.get("return") == typing.Optional[SwImplPolicyEnum]

        setter_hints = typing.get_type_hints(BswInternalTriggeringPoint.setSwImplPolicy)
        assert setter_hints.get("value") == typing.Optional[SwImplPolicyEnum]
        assert setter_hints.get("return") is BswInternalTriggeringPoint


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

    def test_add_client_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        policy = BswClientPolicy()

        result = behavior.addClientPolicy(policy)

        assert result == behavior
        assert behavior.getClientPolicies() == [policy]

        # Adding None is a no-op: the list is unchanged
        behavior.addClientPolicy(None)
        assert behavior.getClientPolicies() == [policy]

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

    def test_add_internal_triggering_point_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        policy = BswInternalTriggeringPointPolicy()

        result = behavior.addInternalTriggeringPointPolicy(policy)

        assert result == behavior
        assert behavior.getInternalTriggeringPointPolicies() == [policy]

        # Adding None is a no-op: the list is unchanged
        behavior.addInternalTriggeringPointPolicy(None)
        assert behavior.getInternalTriggeringPointPolicies() == [policy]

    def test_get_set_parameter_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        result = behavior.setParameterPolicies([])
        assert result == behavior
        assert behavior.getParameterPolicies() == []

    def test_add_parameter_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        policy = BswParameterPolicy()

        result = behavior.addParameterPolicy(policy)

        assert result == behavior
        assert behavior.getParameterPolicies() == [policy]

        # Adding None is a no-op: the list is unchanged
        behavior.addParameterPolicy(None)
        assert behavior.getParameterPolicies() == [policy]

    def test_get_set_released_trigger_policies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        result = behavior.setReleasedTriggerPolicies([])
        assert result == behavior
        assert behavior.getReleasedTriggerPolicies() == []

    def test_add_released_trigger_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        policy = BswReleasedTriggerPolicy()

        result = behavior.addReleasedTriggerPolicy(policy)

        assert result == behavior
        assert behavior.getReleasedTriggerPolicies() == [policy]

        # Adding None is a no-op: the list is unchanged
        behavior.addReleasedTriggerPolicy(None)
        assert behavior.getReleasedTriggerPolicies() == [policy]

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

    def test_add_send_policy(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        policy = BswDataSendPolicy()

        result = behavior.addSendPolicy(policy)

        assert result == behavior
        assert behavior.getSendPolicies() == [policy]

        # Adding None is a no-op: the list is unchanged
        behavior.addSendPolicy(None)
        assert behavior.getSendPolicies() == [policy]

    def test_get_set_service_dependencies(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        result = behavior.setServiceDependencies([])
        assert result == behavior
        assert behavior.getServiceDependencies() == []

    def test_add_service_dependency(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")
        dependency = BswServiceDependency()

        result = behavior.addServiceDependency(dependency)

        assert result == behavior
        assert behavior.getServiceDependencies() == [dependency]

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

    def test_create_bsw_mode_manager_error_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        event = behavior.createBswModeManagerErrorEvent("test_mode_manager_error_event")

        assert event.short_name == "test_mode_manager_error_event"
        assert len(behavior.getBswModeManagerErrorEvents()) == 1

    def test_get_bsw_mode_manager_error_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        event = behavior.createBswModeManagerErrorEvent("test_mode_manager_error_event")

        mode_manager_error_events = behavior.getBswModeManagerErrorEvents()
        assert len(mode_manager_error_events) == 1
        assert mode_manager_error_events[0] == event

    def test_create_bsw_mode_switched_ack_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        event = behavior.createBswModeSwitchedAckEvent("test_mode_switched_ack_event")

        assert event.short_name == "test_mode_switched_ack_event"
        assert len(behavior.getBswModeSwitchedAckEvents()) == 1

    def test_get_bsw_mode_switched_ack_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        event = behavior.createBswModeSwitchedAckEvent("test_mode_switched_ack_event")

        mode_switched_ack_events = behavior.getBswModeSwitchedAckEvents()
        assert len(mode_switched_ack_events) == 1
        assert mode_switched_ack_events[0] == event

    def test_create_bsw_asynchronous_server_call_returns_event(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        event = behavior.createBswAsynchronousServerCallReturnsEvent("test_async_server_call_returns_event")

        assert event.short_name == "test_async_server_call_returns_event"
        assert len(behavior.getBswAsynchronousServerCallReturnsEvents()) == 1

    def test_get_bsw_asynchronous_server_call_returns_events(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = BswInternalBehavior(ar_root, "test_internal_behavior")

        event = behavior.createBswAsynchronousServerCallReturnsEvent("test_async_server_call_returns_event")

        async_events = behavior.getBswAsynchronousServerCallReturnsEvents()
        assert len(async_events) == 1
        assert async_events[0] == event

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

    def test_set_mode_sender_policies_none_noop(self):
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

        # This method adds to modeSenderPolicies
        assert len(behavior.getModeSenderPolicies()) == 1
        assert behavior.getModeSenderPolicies()[0] == policy


class TestBswInternalBehaviorFullSync:
    """Accessor coverage for the remaining Table 5.2 attributes (full sync 2026-09-17)."""

    def _make_behavior(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        return BswInternalBehavior(ar_root, "test_internal_behavior")

    def test_add_ar_typed_per_instance_memory(self):
        behavior = self._make_behavior()
        prototype = VariableDataPrototype(parent=behavior, short_name="mem")

        result = behavior.addArTypedPerInstanceMemory(prototype)

        assert result == behavior
        assert behavior.getArTypedPerInstanceMemories() == [prototype]

        # Adding None is a no-op: the list is unchanged
        behavior.addArTypedPerInstanceMemory(None)
        assert behavior.getArTypedPerInstanceMemories() == [prototype]

    def test_add_exclusive_area_policy(self):
        behavior = self._make_behavior()
        policy = BswExclusiveAreaPolicy()

        result = behavior.addExclusiveAreaPolicy(policy)

        assert result == behavior
        assert behavior.getExclusiveAreaPolicies() == [policy]

        behavior.addExclusiveAreaPolicy(None)
        assert behavior.getExclusiveAreaPolicies() == [policy]

    def test_add_mode_receiver_policy(self):
        behavior = self._make_behavior()
        policy = BswModeReceiverPolicy()

        result = behavior.addModeReceiverPolicy(policy)

        assert result == behavior
        assert behavior.getModeReceiverPolicies() == [policy]

        behavior.addModeReceiverPolicy(None)
        assert behavior.getModeReceiverPolicies() == [policy]

    def test_set_mode_receiver_policies(self):
        behavior = self._make_behavior()
        policy = BswModeReceiverPolicy()

        result = behavior.setModeReceiverPolicies([policy])
        assert result == behavior
        assert behavior.getModeReceiverPolicies() == [policy]

        result = behavior.setModeReceiverPolicies([])
        assert result == behavior
        assert behavior.getModeReceiverPolicies() == []

    def test_add_per_instance_parameter(self):
        behavior = self._make_behavior()
        prototype = ParameterDataPrototype(parent=behavior, short_name="pip")

        result = behavior.addPerInstanceParameter(prototype)

        assert result == behavior
        assert behavior.getPerInstanceParameters() == [prototype]

        behavior.addPerInstanceParameter(None)
        assert behavior.getPerInstanceParameters() == [prototype]

    def test_add_trigger_direct_implementation(self):
        behavior = self._make_behavior()
        implementation = BswTriggerDirectImplementation()

        result = behavior.addTriggerDirectImplementation(implementation)

        assert result == behavior
        assert behavior.getTriggerDirectImplementations() == [implementation]

        behavior.addTriggerDirectImplementation(None)
        assert behavior.getTriggerDirectImplementations() == [implementation]

    def test_add_variation_point_proxy(self):
        behavior = self._make_behavior()
        proxy = VariationPointProxy(parent=behavior, short_name="vp")

        result = behavior.addVariationPointProxy(proxy)

        assert result == behavior
        assert behavior.getVariationPointProxies() == [proxy]

        behavior.addVariationPointProxy(None)
        assert behavior.getVariationPointProxies() == [proxy]


class TestBswDistinguishedPartition:
    """Test cases for BswDistinguishedPartition class - represents an abstract partition in which context the code of the enclosing BswModuleBehavior can be executed."""

    def test_initialization(self):
        """Test BswDistinguishedPartition initialization with proper attributes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        partition = BswDistinguishedPartition(ar_root, "test_partition")

        assert partition.short_name == "test_partition"
        assert partition.getShortName() == "test_partition"
        assert partition.getParent() is ar_root

    def test_no_own_attributes_beyond_referrable(self):
        """BswDistinguishedPartition has no spec attributes of its own (Table 5.50)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        class ReferrableProbe(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        probe = ReferrableProbe(ar_root, "probe")
        partition = BswDistinguishedPartition(ar_root, "test_partition")

        own = set(vars(partition)) - set(vars(probe))
        assert own == set()


class TestRoleBasedBswModuleEntryAssignment:
    """Test cases for RoleBasedBswModuleEntryAssignment class - assigns a role to a particular BswModuleEntry."""

    def test_initialization(self):
        assignment = RoleBasedBswModuleEntryAssignment()

        assert assignment.getAssignedEntryRef() is None
        assert assignment.getRole() is None

    def test_get_set_assigned_entry_ref(self):
        assignment = RoleBasedBswModuleEntryAssignment()
        ref = RefType()

        result = assignment.setAssignedEntryRef(ref)

        assert result == assignment
        assert assignment.getAssignedEntryRef() == ref

        # Setting None should not change the value
        result = assignment.setAssignedEntryRef(None)
        assert result == assignment
        assert assignment.getAssignedEntryRef() == ref

    def test_get_set_role(self):
        assignment = RoleBasedBswModuleEntryAssignment()
        role = Identifier().setValue("errorNotification")

        result = assignment.setRole(role)

        assert result == assignment
        assert assignment.getRole() == role

        # Setting None should not change the value
        result = assignment.setRole(None)
        assert result == assignment
        assert assignment.getRole() == role


class TestBswServiceDependency:
    """Test cases for BswServiceDependency class - specialization of ServiceDependency in the context of a BswInternalBehavior."""

    def test_initialization(self):
        dependency = BswServiceDependency()

        assert dependency.getAssignedData() == []
        assert dependency.getAssignedEntryRole() == []
        assert dependency.getIdent() is None
        assert dependency.getServiceNeeds() is None

    def test_get_add_assigned_data(self):
        dependency = BswServiceDependency()
        data = RoleBasedDataAssignment()

        result = dependency.addAssignedData(data)

        assert result == dependency
        assert dependency.getAssignedData() == [data]

    def test_add_assigned_data_none_is_noop(self):
        dependency = BswServiceDependency()
        data = RoleBasedDataAssignment()
        dependency.addAssignedData(data)

        result = dependency.addAssignedData(None)

        assert result == dependency
        assert dependency.getAssignedData() == [data]

    def test_get_add_assigned_entry_role(self):
        dependency = BswServiceDependency()
        assignment = RoleBasedBswModuleEntryAssignment()

        result = dependency.addAssignedEntryRole(assignment)

        assert result == dependency
        assert dependency.getAssignedEntryRole() == [assignment]

    def test_add_assigned_entry_role_none_is_noop(self):
        dependency = BswServiceDependency()
        assignment = RoleBasedBswModuleEntryAssignment()
        dependency.addAssignedEntryRole(assignment)

        result = dependency.addAssignedEntryRole(None)

        assert result == dependency
        assert dependency.getAssignedEntryRole() == [assignment]

    def test_add_assigned_data_type_none_is_noop(self):
        dependency = BswServiceDependency()
        data_type = RoleBasedDataTypeAssignment()
        dependency.setAssignedDataType(data_type)

        result = dependency.setAssignedDataType(None)

        assert result == dependency
        assert dependency.getAssignedDataType() == data_type

    def test_get_set_ident(self):
        dependency = BswServiceDependency()
        ident = BswServiceDependencyIdent(dependency, "test_ident")

        result = dependency.setIdent(ident)

        assert result == dependency
        assert dependency.getIdent() == ident

        # Setting None should not change the value
        result = dependency.setIdent(None)
        assert result == dependency
        assert dependency.getIdent() == ident

    def test_get_set_service_needs(self):
        dependency = BswServiceDependency()
        needs = BswMgrNeeds(dependency, "test_needs")

        result = dependency.setServiceNeeds(needs)

        assert result == dependency
        assert dependency.getServiceNeeds() == needs

        # Setting None should not change the value
        result = dependency.setServiceNeeds(None)
        assert result == dependency
        assert dependency.getServiceNeeds() == needs

    def test_get_set_symbolic_name_props(self):
        dependency = BswServiceDependency()
        props = SymbolicNameProps(dependency, "symProps")

        result = dependency.setSymbolicNameProps(props)

        assert result == dependency
        assert dependency.getSymbolicNameProps() == props

        # Setting None should not change the value
        result = dependency.setSymbolicNameProps(None)
        assert result == dependency
        assert dependency.getSymbolicNameProps() == props


class TestSymbolicNameProps:
    def test_get_set_symbol(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier

        parent = BswServiceDependency()
        props = SymbolicNameProps(parent, "symProps")

        assert props.getShortName() == "symProps"
        assert props.getSymbol() is None

        value = CIdentifier().setValue("test_symbol")
        result = props.setSymbol(value)

        assert result == props
        assert props.getSymbol() == value

        # Setting None should not change the value
        result = props.setSymbol(None)
        assert result == props
        assert props.getSymbol() == value

    def test_inherits_implementation_props(self):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps

        assert issubclass(SymbolicNameProps, ImplementationProps)
