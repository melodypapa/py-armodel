"""
Test suite for the BswInternalBehavior model class.

Covers the aggregation members of BswInternalBehavior (BSWMDT Table 5.2, p.68):
entities, events, internal triggering points and the policy lists, plus the
mode-sender-policy regression (addModeSenderPolicy/getModeSenderPolicies must
operate on modeSenderPolicies, not modeReceiverPolicies).
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswAsynchronousServerCallReturnsEvent,
    BswBackgroundEvent,
    BswDataReceivedEvent,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggerOccurredEvent,
    BswModeManagerErrorEvent,
    BswModeSenderPolicy,
    BswModeSwitchedAckEvent,
    BswModeSwitchEvent,
    BswOperationInvokedEvent,
    BswTimingEvent,
    IncludedDataTypeSet,
    IncludedModeDeclarationGroupSet,
)


@pytest.fixture
def behavior():
    parent = AUTOSAR.getInstance()
    ar_root = parent.createARPackage("AUTOSAR")
    return BswInternalBehavior(ar_root, "TestBehavior")


class TestBswInternalBehaviorInitialization:
    def test_initialization_defaults(self, behavior):
        assert behavior is not None
        assert behavior.getShortName() == "TestBehavior"
        assert behavior.arTypedPerInstanceMemories == []
        assert behavior.bswPerInstanceMemoryPolicies == []
        assert behavior.clientPolicies == []
        assert behavior.distinguishedPartitions == []
        assert behavior.entities == []
        assert behavior.events == []
        assert behavior.exclusiveAreaPolicies == []
        assert behavior.includedDataTypeSets == []
        assert behavior.includedModeDeclarationGroupSets == []
        assert behavior.internalTriggeringPoints == []
        assert behavior.internalTriggeringPointPolicies == []
        assert behavior.modeReceiverPolicies == []
        assert behavior.modeSenderPolicies == []
        assert behavior.parameterPolicies == []
        assert behavior.perInstanceParameters == []
        assert behavior.receptionPolicies == []
        assert behavior.releasedTriggerPolicies == []
        assert behavior.schedulerNamePrefixes == []
        assert behavior.sendPolicies == []
        assert behavior.serviceDependencies == []
        assert behavior.triggerDirectImplementations == []
        assert behavior.variationPointProxies == []


class TestBswInternalBehaviorPolicyLists:
    @pytest.mark.parametrize(
        "getter,setter,attr",
        [
            ("getArTypedPerInstanceMemories", "setArTypedPerInstanceMemories", "arTypedPerInstanceMemories"),
            ("getBswPerInstanceMemoryPolicies", "setBswPerInstanceMemoryPolicies", "bswPerInstanceMemoryPolicies"),
            ("getClientPolicies", "setClientPolicies", "clientPolicies"),
            ("getDistinguishedPartitions", "setDistinguishedPartitions", "distinguishedPartitions"),
            ("getExclusiveAreaPolicies", "setExclusiveAreaPolicies", "exclusiveAreaPolicies"),
            ("getInternalTriggeringPointPolicies", "setInternalTriggeringPointPolicies", "internalTriggeringPointPolicies"),
            ("getParameterPolicies", "setParameterPolicies", "parameterPolicies"),
            ("getPerInstanceParameters", "setPerInstanceParameters", "perInstanceParameters"),
            ("getReleasedTriggerPolicies", "setReleasedTriggerPolicies", "releasedTriggerPolicies"),
            ("getSchedulerNamePrefixes", "setSchedulerNamePrefixes", "schedulerNamePrefixes"),
            ("getSendPolicies", "setSendPolicies", "sendPolicies"),
            ("getServiceDependencies", "setServiceDependencies", "serviceDependencies"),
            ("getTriggerDirectImplementations", "setTriggerDirectImplementations", "triggerDirectImplementations"),
            ("getVariationPointProxies", "setVariationPointProxies", "variationPointProxies"),
        ],
    )
    def test_get_set_roundtrip(self, behavior, getter, setter, attr):
        sentinel = [object()]
        result = getattr(behavior, setter)(sentinel)
        assert result is behavior
        assert getattr(behavior, getter)() == sentinel

    @pytest.mark.parametrize(
        "getter,setter",
        [
            ("getArTypedPerInstanceMemories", "setArTypedPerInstanceMemories"),
            ("getBswPerInstanceMemoryPolicies", "setBswPerInstanceMemoryPolicies"),
            ("getClientPolicies", "setClientPolicies"),
            ("getDistinguishedPartitions", "setDistinguishedPartitions"),
            ("getExclusiveAreaPolicies", "setExclusiveAreaPolicies"),
            ("getInternalTriggeringPointPolicies", "setInternalTriggeringPointPolicies"),
            ("getParameterPolicies", "setParameterPolicies"),
            ("getPerInstanceParameters", "setPerInstanceParameters"),
            ("getReleasedTriggerPolicies", "setReleasedTriggerPolicies"),
            ("getSchedulerNamePrefixes", "setSchedulerNamePrefixes"),
            ("getSendPolicies", "setSendPolicies"),
            ("getServiceDependencies", "setServiceDependencies"),
            ("getTriggerDirectImplementations", "setTriggerDirectImplementations"),
            ("getVariationPointProxies", "setVariationPointProxies"),
        ],
    )
    def test_set_none_is_noop(self, behavior, getter, setter):
        sentinel = [object()]
        getattr(behavior, setter)(sentinel)
        getattr(behavior, setter)(None)
        assert getattr(behavior, getter)() == sentinel

    def test_get_mode_sender_policies_default(self, behavior):
        assert behavior.getModeSenderPolicies() == []
        assert behavior.modeSenderPolicies == []

    def test_set_mode_sender_policies(self, behavior):
        policy = BswModeSenderPolicy()
        result = behavior.setModeSenderPolicies([policy])
        assert result is behavior
        assert behavior.getModeSenderPolicies() == [policy]

    def test_add_mode_sender_policy_uses_mode_sender_policies(self, behavior):
        policy = BswModeSenderPolicy()
        behavior.addModeSenderPolicy(policy)
        assert behavior.getModeSenderPolicies() == [policy]
        assert policy in behavior.modeSenderPolicies
        assert behavior.modeReceiverPolicies == []

    def test_get_mode_receiver_policies_default(self, behavior):
        assert behavior.getModeReceiverPolicies() == []

    def test_add_reception_policy_none_is_noop(self, behavior):
        result = behavior.addReceptionPolicy(None)
        assert result is behavior
        assert behavior.receptionPolicies == []

    def test_add_service_dependency(self, behavior):
        dependency = object()
        result = behavior.addServiceDependency(dependency)
        assert result is behavior
        assert behavior.serviceDependencies == [dependency]


class TestBswInternalBehaviorEntities:
    def test_create_bsw_called_entity(self, behavior):
        entity = behavior.createBswCalledEntity("Called")
        assert entity is not None
        assert entity.getShortName() == "Called"
        assert behavior.getBswCalledEntities() == [entity]
        assert behavior.getBswModuleEntities() == [entity]

    def test_create_bsw_schedulable_entity(self, behavior):
        entity = behavior.createBswSchedulableEntity("Schedulable")
        assert entity is not None
        assert entity.getShortName() == "Schedulable"
        assert behavior.getBswSchedulableEntities() == [entity]

    def test_create_bsw_interrupt_entity(self, behavior):
        entity = behavior.createBswInterruptEntity("Interrupt")
        assert entity is not None
        assert entity.getShortName() == "Interrupt"
        assert behavior.getBswInterruptEntities() == [entity]

    def test_create_duplicate_entity_returns_existing(self, behavior):
        first = behavior.createBswCalledEntity("Called")
        second = behavior.createBswCalledEntity("Called")
        assert first is second
        assert len(behavior.getBswCalledEntities()) == 1

    def test_get_bsw_module_entities_empty(self, behavior):
        assert behavior.getBswModuleEntities() == []

    def test_create_bsw_internal_triggering_point(self, behavior):
        point = behavior.createBswInternalTriggeringPoint("TriggerPoint")
        assert point is not None
        assert point.getShortName() == "TriggerPoint"
        assert behavior.getInternalTriggeringPoints() == [point]


class TestBswInternalBehaviorEvents:
    @pytest.mark.parametrize(
        "create,getter,cls",
        [
            ("createBswModeSwitchEvent", "getBswModeSwitchEvents", BswModeSwitchEvent),
            ("createBswTimingEvent", "getBswTimingEvents", BswTimingEvent),
            ("createBswDataReceivedEvent", "getBswDataReceivedEvents", BswDataReceivedEvent),
            ("createBswInternalTriggerOccurredEvent", "getBswInternalTriggerOccurredEvents", BswInternalTriggerOccurredEvent),
            ("createBswExternalTriggerOccurredEvent", "getBswExternalTriggerOccurredEvents", BswExternalTriggerOccurredEvent),
            ("createBswOperationInvokedEvent", "getBswOperationInvokedEvents", BswOperationInvokedEvent),
            ("createBswBackgroundEvent", "getBswBackgroundEvents", BswBackgroundEvent),
            ("createBswModeManagerErrorEvent", "getBswModeManagerErrorEvents", BswModeManagerErrorEvent),
            ("createBswModeSwitchedAckEvent", "getBswModeSwitchedAckEvents", BswModeSwitchedAckEvent),
            ("createBswAsynchronousServerCallReturnsEvent", "getBswAsynchronousServerCallReturnsEvents", BswAsynchronousServerCallReturnsEvent),
        ],
    )
    def test_create_and_get(self, behavior, create, getter, cls):
        event = getattr(behavior, create)("Event1")
        assert isinstance(event, cls)
        assert event.getShortName() == "Event1"
        assert getattr(behavior, getter)() == [event]
        assert behavior.getBswEvents() == [event]
        assert event in behavior.events

    def test_create_duplicate_event_returns_existing(self, behavior):
        first = behavior.createBswTimingEvent("Event1")
        second = behavior.createBswTimingEvent("Event1")
        assert first is second
        assert len(behavior.getBswTimingEvents()) == 1

    def test_get_bsw_events_empty(self, behavior):
        assert behavior.getBswEvents() == []


class TestBswInternalBehaviorTypeSets:
    def test_add_included_mode_declaration_group_set(self, behavior):
        group_set = IncludedModeDeclarationGroupSet()
        behavior.addIncludedModeDeclarationGroupSet(group_set)
        assert behavior.getIncludedModeDeclarationGroupSets() == [group_set]

    def test_add_included_data_type_set(self, behavior):
        type_set = IncludedDataTypeSet()
        behavior.addIncludedDataTypeSet(type_set)
        assert behavior.getIncludedDataTypeSets() == [type_set]
