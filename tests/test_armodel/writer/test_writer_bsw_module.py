"""Tests for writer BSW module template handlers."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswModeSenderPolicy,
    BswModeSwitchAckRequest,
    BswModeSwitchEvent,
    BswQueuedDataReceptionPolicy,
    BswServiceDependency,
    BswServiceDependencyIdent,
    BswVariableAccess,
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import (
    ModeInBswModuleDescriptionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    BswMgrNeeds,
    RoleBasedDataAssignment,
    SymbolicNameProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    ARNumerical,
    CIdentifier,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (  # noqa E501
    IncludedModeDeclarationGroupSet,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _literal(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _bool(value):
    b = ARBoolean()
    b.setValue(value)
    return b


def _numerical(value):
    n = ARNumerical()
    n.setValue(str(value))
    return n


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _make_desc():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createBswModuleDescription("BswMd")


def _make_behavior():
    desc = _make_desc()
    return desc.createBswInternalBehavior("Beh")


def _make_entry():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createBswModuleEntry("Entry")


class TestWriterBswImplementedEntryRefs:
    def test_with_refs(self, writer):
        desc = _make_desc()
        desc.addImplementedEntryRef(_ref("/e1", "BSW-MODULE-ENTRY"))
        desc.addImplementedEntryRef(_ref("/e2", "BSW-MODULE-ENTRY"))
        parent = _parent()
        writer.writeBswModuleDescriptionImplementedEntryRefs(parent, desc)
        assert len(parent) == 1
        entries = parent[0]
        assert entries.tag == "PROVIDED-ENTRYS"
        refs = entries.findall("BSW-MODULE-ENTRY-REF-CONDITIONAL")
        assert len(refs) == 2

    def test_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionImplementedEntryRefs(parent, desc)
        assert len(parent) == 0


class TestWriterBswModuleDescriptionModeGroups:
    def test_provided_mode_groups(self, writer):
        desc = _make_desc()
        desc.createProvidedModeGroup("pmg").setTypeTRef(_ref("/t", "MODE-DECLARATION-GROUP"))
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedModeGroups(parent, desc)
        assert parent[0].tag == "PROVIDED-MODE-GROUPS"
        assert parent[0].find("MODE-DECLARATION-GROUP-PROTOTYPE") is not None

    def test_provided_mode_groups_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedModeGroups(parent, desc)
        assert len(parent) == 0

    def test_required_mode_groups(self, writer):
        desc = _make_desc()
        desc.createRequiredModeGroup("rmg").setTypeTRef(_ref("/t", "MODE-DECLARATION-GROUP"))
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredModeGroups(parent, desc)
        assert parent[0].tag == "REQUIRED-MODE-GROUPS"
        assert parent[0].find("MODE-DECLARATION-GROUP-PROTOTYPE") is not None

    def test_required_mode_groups_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredModeGroups(parent, desc)
        assert len(parent) == 0


class TestWriterExecutableEntity:
    def test_can_enter_exclusive_area_refs_with_refs(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addCanEnterRef(_ref("/ea1", "EXCLUSIVE-AREA"))
        entity.addCanEnterRef(_ref("/ea2", "EXCLUSIVE-AREA"))
        parent = _parent()
        writer.writeCanEnterRefs(parent, entity)
        assert parent[0].tag == "CAN-ENTER-EXCLUSIVE-AREA-REFS"
        refs = parent[0].findall("CAN-ENTER-EXCLUSIVE-AREA-REF")
        assert len(refs) == 2

    def test_can_enter_exclusive_area_refs_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeCanEnterRefs(parent, entity)
        assert len(parent) == 0

    def test_writeExecutableEntity_full(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addCanEnterRef(_ref("/ea", "EXCLUSIVE-AREA"))
        entity.setMinimumStartInterval(_time(0.1))
        entity.setSwAddrMethodRef(_ref("/am", "SW-ADDR-METHOD"))
        entity.addExclusiveAreaNestingOrderRef(_ref("/o1", "EXCLUSIVE-AREA-NESTING-ORDER"))
        entity.addRunsInsideRef(_ref("/ea1", "EXCLUSIVE-AREA"))
        entity.setReentrancyLevel(_literal("multicoreReentrant"))
        parent = _parent()
        writer.writeExecutableEntity(parent, entity)
        assert parent.find("CAN-ENTER-EXCLUSIVE-AREA-REFS") is not None
        assert parent.find("MINIMUM-START-INTERVAL").text == "0.1"
        assert parent.find("SW-ADDR-METHOD-REF") is not None
        assert parent.find("EXCLUSIVE-AREA-NESTING-ORDER-REFS") is not None
        assert parent.find("RUNS-INSIDE-EXCLUSIVE-AREA-REFS") is not None
        assert parent.find("REENTRANCY-LEVEL") is not None
        assert parent.find("REENTRANCY-LEVEL").text == "multicoreReentrant"

    def test_exclusive_area_nesting_order_refs_with_refs(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addExclusiveAreaNestingOrderRef(_ref("/o1", "EXCLUSIVE-AREA-NESTING-ORDER"))
        entity.addExclusiveAreaNestingOrderRef(_ref("/o2", "EXCLUSIVE-AREA-NESTING-ORDER"))
        parent = _parent()
        writer.writeExecutableEntity(parent, entity)
        assert parent.find("EXCLUSIVE-AREA-NESTING-ORDER-REFS") is not None
        refs = parent.find("EXCLUSIVE-AREA-NESTING-ORDER-REFS").findall("EXCLUSIVE-AREA-NESTING-ORDER-REF")
        assert len(refs) == 2

    def test_runs_inside_refs_with_refs(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addRunsInsideRef(_ref("/ea1", "EXCLUSIVE-AREA"))
        parent = _parent()
        writer.writeExecutableEntity(parent, entity)
        assert parent.find("RUNS-INSIDE-EXCLUSIVE-AREA-REFS") is not None

    def test_reentrancy_level(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.setReentrancyLevel(_literal("multicoreReentrant"))
        parent = _parent()
        writer.writeExecutableEntity(parent, entity)
        assert parent.find("REENTRANCY-LEVEL") is not None
        assert parent.find("REENTRANCY-LEVEL").text == "multicoreReentrant"


class TestWriterBswModuleEntityFamily:
    def test_managed_mode_groups(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addManagedModeGroupRef(_ref("/mg1", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        parent = _parent()
        writer.writeBswModuleEntityManagedModeGroups(parent, entity)
        assert parent[0].tag == "MANAGED-MODE-GROUPS"
        cond = parent[0].find("MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
        assert cond is not None

    def test_managed_mode_groups_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeBswModuleEntityManagedModeGroups(parent, entity)
        assert len(parent) == 0

    def test_accessed_mode_groups(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addAccessedModeGroupRef(_ref("/amg1", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        parent = _parent()
        writer.writeBswModuleEntityAccessedModeGroups(parent, entity)
        assert parent[0].tag == "ACCESSED-MODE-GROUPS"
        cond = parent[0].find("MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
        assert cond is not None

    def test_accessed_mode_groups_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeBswModuleEntityAccessedModeGroups(parent, entity)
        assert len(parent) == 0

    def test_bsw_variable_access_with_data(self, writer):
        behavior = _make_behavior()
        access = BswVariableAccess(behavior, "va")
        access.setAccessedVariableRef(_ref("/v", "VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.writeBswVariableAccess(parent, access)
        assert parent[0].tag == "BSW-VARIABLE-ACCESS"
        assert parent[0].find("ACCESSED-VARIABLE-REF") is not None

    def test_bsw_variable_access_none(self, writer):
        parent = _parent()
        writer.writeBswVariableAccess(parent, None)
        assert len(parent) == 0

    def test_data_send_points(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.createDataSendPoint("dsp")
        parent = _parent()
        writer.writeBswModuleEntityDataSendPoints(parent, entity)
        assert parent[0].tag == "DATA-SEND-POINTS"

    def test_data_receive_points(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.createDataReceivePoint("drp")
        parent = _parent()
        writer.writeBswModuleEntityDataReceivePoints(parent, entity)
        assert parent[0].tag == "DATA-RECEIVE-POINTS"

    def test_issued_trigger_refs(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addIssuedTriggerRef(_ref("/t", "TRIGGER"))
        parent = _parent()
        writer.writeBswModuleEntityIssuedTriggerRefs(parent, entity)
        assert parent[0].tag == "ISSUED-TRIGGERS"
        assert parent[0].find("TRIGGER-REF-CONDITIONAL") is not None

    def test_activation_point_refs(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addActivationPointRef(_ref("/ap", "BSW-INTERNAL-TRIGGERING-POINT"))
        parent = _parent()
        writer.writeBswModuleEntityActivationPointRefs(parent, entity)
        assert parent[0].tag == "ACTIVATION-POINTS"
        cond = parent[0].find("BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL")
        assert cond is not None


class TestWriterBswModuleCallPoints:
    def test_async_call_point(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        point = entity.createBswAsynchronousServerCallPoint("acp")
        point.setCalledEntryRef(_ref("/e", "BSW-MODULE-ENTRY"))
        parent = _parent()
        writer.writeBswAsynchronousServerCallPoint(parent, point)
        assert parent[0].tag == "BSW-ASYNCHRONOUS-SERVER-CALL-POINT"
        assert parent[0].find("CALLED-ENTRY-REF") is not None

    def test_sync_call_point(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        point = entity.createBswSynchronousServerCallPoint("scp")
        point.setCalledEntryRef(_ref("/e", "BSW-MODULE-ENTRY"))
        parent = _parent()
        writer.writeBswSynchronousServerCallPoint(parent, point)
        assert parent[0].tag == "BSW-SYNCHRONOUS-SERVER-CALL-POINT"
        assert parent[0].find("CALLED-ENTRY-REF") is not None

    def test_entity_call_points_async_and_sync(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.createBswAsynchronousServerCallPoint("acp").setCalledEntryRef(_ref("/e1", "BSW-MODULE-ENTRY"))
        entity.createBswSynchronousServerCallPoint("scp").setCalledEntryRef(_ref("/e2", "BSW-MODULE-ENTRY"))
        parent = _parent()
        writer.writeBswModuleEntityCallPoints(parent, entity)
        assert parent[0].tag == "CALL-POINTS"
        tags = {c.tag for c in parent[0]}
        assert "BSW-ASYNCHRONOUS-SERVER-CALL-POINT" in tags
        assert "BSW-SYNCHRONOUS-SERVER-CALL-POINT" in tags

    def test_result_point(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        point = entity.createBswAsynchronousServerCallResultPoint("rp")
        point.setAsynchronousServerCallPointRef(_ref("/acp", "BSW-ASYNCHRONOUS-SERVER-CALL-POINT"))
        parent = _parent()
        writer.writeBswAsynchronousServerCallResultPoint(parent, point)
        assert parent[0].tag == "BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"
        ref_elem = parent[0].find("ASYNCHRONOUS-SERVER-CALL-POINT-REF")
        assert ref_elem is not None
        assert ref_elem.text == "/acp"
        assert ref_elem.get("DEST") == "BSW-ASYNCHRONOUS-SERVER-CALL-POINT"

    def test_entity_call_points_result_point_dispatch(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        rp = entity.createBswAsynchronousServerCallResultPoint("rp")
        rp.setAsynchronousServerCallPointRef(_ref("/acp", "BSW-ASYNCHRONOUS-SERVER-CALL-POINT"))
        parent = _parent()
        writer.writeBswModuleEntityCallPoints(parent, entity)
        child_tags = [c.tag for c in parent[0]]
        assert child_tags == ["BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"]

    def test_entity_call_points_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeBswModuleEntityCallPoints(parent, entity)
        assert len(parent) == 0


class TestWriterBswInternalBehaviorSchedulerNamePrefixes:
    def test_scheduler_name_prefixes(self, writer):
        behavior = _make_behavior()
        prefix = behavior.createSchedulerNamePrefix("p1")
        symbol = CIdentifier()
        symbol.setValue("SchM_pre_")
        prefix.setSymbol(symbol)
        parent = _parent()
        writer.writeBswInternalBehaviorSchedulerNamePrefixes(parent, behavior)
        wrapper = parent.find("SCHEDULER-NAME-PREFIXS")
        assert wrapper is not None
        prefixes = wrapper.findall("BSW-SCHEDULER-NAME-PREFIX")
        assert len(prefixes) == 1
        assert prefixes[0].find("SHORT-NAME").text == "p1"
        assert prefixes[0].find("SYMBOL").text == "SchM_pre_"

    def test_scheduler_name_prefixes_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorSchedulerNamePrefixes(parent, behavior)
        assert parent.find("SCHEDULER-NAME-PREFIXS") is None

    def test_distinguished_partitions(self, writer):
        behavior = _make_behavior()
        behavior.createDistinguishedPartition("master")
        behavior.createDistinguishedPartition("satellite")
        parent = _parent()
        writer.writeBswInternalBehaviorDistinguishedPartitions(parent, behavior)
        wrapper = parent.find("DISTINGUISHED-PARTITIONS")
        assert wrapper is not None
        partitions = wrapper.findall("BSW-DISTINGUISHED-PARTITION")
        names = [p.find("SHORT-NAME").text for p in partitions]
        assert names == ["master", "satellite"]

    def test_distinguished_partitions_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorDistinguishedPartitions(parent, behavior)
        assert parent.find("DISTINGUISHED-PARTITIONS") is None

    def test_interrupt_event(self, writer):
        behavior = _make_behavior()
        behavior.createBswInterruptEvent("ie1")
        parent = _parent()
        writer.writeBswInternalBehaviorEvents(parent, behavior)
        wrapper = parent.find("EVENTS")
        assert wrapper is not None
        assert wrapper[0].tag == "BSW-INTERRUPT-EVENT"
        assert wrapper[0].find("SHORT-NAME").text == "ie1"

    def test_os_task_execution_event(self, writer):
        behavior = _make_behavior()
        behavior.createBswOsTaskExecutionEvent("ote1")
        parent = _parent()
        writer.writeBswInternalBehaviorEvents(parent, behavior)
        wrapper = parent.find("EVENTS")
        assert wrapper is not None
        assert wrapper[0].tag == "BSW-OS-TASK-EXECUTION-EVENT"
        assert wrapper[0].find("SHORT-NAME").text == "ote1"


class TestWriterBswInternalBehaviorEntities:
    def test_called_entity(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswCalledEntity("ce")
        parent = _parent()
        writer.writeBswCalledEntity(parent, entity)
        assert parent[0].tag == "BSW-CALLED-ENTITY"

    def test_schedulable_entity(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("se")
        parent = _parent()
        writer.writeBswSchedulableEntity(parent, entity)
        assert parent[0].tag == "BSW-SCHEDULABLE-ENTITY"

    def test_interrupt_entity(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswInterruptEntity("ie")
        entity.setInterruptCategory(_literal("cat1"))
        entity.setInterruptSource(_literal("src"))
        parent = _parent()
        writer.setBswInterruptEntity(parent, entity)
        assert parent[0].tag == "BSW-INTERRUPT-ENTITY"
        assert parent[0].find("INTERRUPT-CATEGORY").text == "cat1"
        assert parent[0].find("INTERRUPT-SOURCE").text == "src"

    def test_dispatches_all_entity_types(self, writer):
        behavior = _make_behavior()
        behavior.createBswCalledEntity("ce")
        behavior.createBswSchedulableEntity("se")
        behavior.createBswInterruptEntity("ie")
        parent = _parent()
        writer.writeBswInternalBehaviorEntities(parent, behavior)
        assert parent[0].tag == "ENTITYS"
        tags = {c.tag for c in parent[0]}
        assert "BSW-CALLED-ENTITY" in tags
        assert "BSW-SCHEDULABLE-ENTITY" in tags
        assert "BSW-INTERRUPT-ENTITY" in tags

    def test_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorEntities(parent, behavior)
        assert len(parent) == 0

    def test_writeBswModuleEntity_full(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.setImplementedEntryRef(_ref("/e", "BSW-MODULE-ENTRY"))
        entity.addActivationPointRef(_ref("/ap", "BSW-INTERNAL-TRIGGERING-POINT"))
        entity.createBswSynchronousServerCallPoint("scp").setCalledEntryRef(_ref("/ce", "BSW-MODULE-ENTRY"))
        entity.createDataSendPoint("dsp")
        entity.createDataReceivePoint("drp")
        entity.addManagedModeGroupRef(_ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        entity.addAccessedModeGroupRef(_ref("/amg", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        entity.addIssuedTriggerRef(_ref("/t", "TRIGGER"))
        parent = _parent()
        writer.writeBswModuleEntity(parent, entity)
        assert parent.find("IMPLEMENTED-ENTRY-REF") is not None
        assert parent.find("ACTIVATION-POINTS") is not None
        assert parent.find("CALL-POINTS") is not None
        assert parent.find("DATA-SEND-POINTS") is not None
        assert parent.find("DATA-RECEIVE-POINTS") is not None
        assert parent.find("MANAGED-MODE-GROUPS") is not None
        assert parent.find("ACCESSED-MODE-GROUPS") is not None
        assert parent.find("ISSUED-TRIGGERS") is not None


class TestWriterBswEvents:
    def test_timing_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswTimingEvent("te")
        event.setPeriod(_time(0.1))
        parent = _parent()
        writer.writeBswTimingEvent(parent, event)
        assert parent[0].tag == "BSW-TIMING-EVENT"
        assert parent[0].find("PERIOD").text == "0.1"

    def test_timing_event_activation_reason_representation(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswTimingEvent("te")
        event.setActivationReasonRepresentationRef(_ref("/ar", "EXECUTABLE-ENTITY-ACTIVATION-REASON"))
        parent = _parent()
        writer.writeBswTimingEvent(parent, event)
        assert parent[0].tag == "BSW-TIMING-EVENT"
        assert parent[0].find("ACTIVATION-REASON-REPRESENTATION-REF") is not None

    def test_background_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswBackgroundEvent("be")
        parent = _parent()
        writer.writeBswBackgroundEvent(parent, event)
        assert parent[0].tag == "BSW-BACKGROUND-EVENT"

    def test_internal_trigger_occurred_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswInternalTriggerOccurredEvent("ito")
        event.setEventSourceRef(_ref("/src", "BSW-INTERNAL-TRIGGERING-POINT"))
        parent = _parent()
        writer.writeBswInternalTriggerOccurredEvent(parent, event)
        assert parent[0].tag == "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT"
        assert parent[0].find("EVENT-SOURCE-REF") is not None

    def test_external_trigger_occurred_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswExternalTriggerOccurredEvent("eto")
        event.setTriggerRef(_ref("/t", "TRIGGER"))
        parent = _parent()
        writer.writeBswExternalTriggerOccurredEvent(parent, event)
        assert parent[0].tag == "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT"
        assert parent[0].find("TRIGGER-REF") is not None

    def test_data_received_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswDataReceivedEvent("dre")
        event.setDataRef(_ref("/d", "VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.writeBswDataReceivedEvent(parent, event)
        assert parent[0].tag == "BSW-DATA-RECEIVED-EVENT"
        assert parent[0].find("DATA-REF") is not None

    def test_operation_invoked_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswOperationInvokedEvent("oie")
        event.setEntryRef(_ref("/e", "BSW-MODULE-ENTRY"))
        parent = _parent()
        writer.writeBswOperationInvokedEvent(parent, event)
        assert parent[0].tag == "BSW-OPERATION-INVOKED-EVENT"
        assert parent[0].find("ENTRY-REF") is not None

    def test_mode_switch_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswModeSwitchEvent("mse")
        activation = ARLiteral()
        activation.setValue("onTransition")
        event.setActivation(activation)
        parent = _parent()
        writer.writeBswModeSwitchEvent(parent, event)
        assert parent[0].tag == "BSW-MODE-SWITCH-EVENT"
        assert parent[0].find("ACTIVATION").text == "onTransition"

    def test_mode_manager_error_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswModeManagerErrorEvent("mmee")
        event.setModeGroupRef(_ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        parent = _parent()
        writer.writeBswModeManagerErrorEvent(parent, event)
        assert parent[0].tag == "BSW-MODE-MANAGER-ERROR-EVENT"
        assert parent[0].find("MODE-GROUP-REF") is not None

    def test_mode_switched_ack_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswModeSwitchedAckEvent("msae")
        event.setModeGroupRef(_ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        parent = _parent()
        writer.writeBswModeSwitchedAckEvent(parent, event)
        assert parent[0].tag == "BSW-MODE-SWITCHED-ACK-EVENT"
        assert parent[0].find("MODE-GROUP-REF") is not None

    def test_asynchronous_server_call_returns_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswAsynchronousServerCallReturnsEvent("ascr")
        event.setEventSourceRef(_ref("/cp", "BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"))
        parent = _parent()
        writer.writeBswAsynchronousServerCallReturnsEvent(parent, event)
        assert parent[0].tag == "BSW-ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT"
        assert parent[0].find("EVENT-SOURCE-REF") is not None

    def test_dispatches_all_event_types(self, writer):
        behavior = _make_behavior()
        behavior.createBswTimingEvent("te").setPeriod(_time(0.1))
        behavior.createBswBackgroundEvent("be")
        behavior.createBswInternalTriggerOccurredEvent("ito")
        behavior.createBswExternalTriggerOccurredEvent("eto")
        behavior.createBswDataReceivedEvent("dre")
        behavior.createBswOperationInvokedEvent("oie")
        behavior.createBswModeSwitchEvent("mse")
        behavior.createBswModeManagerErrorEvent("mmee")
        behavior.createBswModeSwitchedAckEvent("msae")
        behavior.createBswAsynchronousServerCallReturnsEvent("ascr")
        parent = _parent()
        writer.writeBswInternalBehaviorEvents(parent, behavior)
        assert parent[0].tag == "EVENTS"
        tags = {c.tag for c in parent[0]}
        assert "BSW-TIMING-EVENT" in tags
        assert "BSW-BACKGROUND-EVENT" in tags
        assert "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT" in tags
        assert "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT" in tags
        assert "BSW-DATA-RECEIVED-EVENT" in tags
        assert "BSW-OPERATION-INVOKED-EVENT" in tags
        assert "BSW-MODE-SWITCH-EVENT" in tags
        assert "BSW-MODE-MANAGER-ERROR-EVENT" in tags
        assert "BSW-MODE-SWITCHED-ACK-EVENT" in tags
        assert "BSW-ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT" in tags

    def test_events_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorEvents(parent, behavior)
        assert len(parent) == 0


class TestWriterBswModeSenderPolicy:
    def test_set_bsw_mode_sender_policy(self, writer):
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(_ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        policy.setQueueLength(_posint(5))
        policy.setEnhancedModeApi(_bool(True))
        ack = BswModeSwitchAckRequest()
        ack.setTimeout(_time(5.0))
        policy.setAckRequest(ack)
        parent = _parent()
        writer.setBswModeSenderPolicy(parent, policy)
        assert parent[0].tag == "BSW-MODE-SENDER-POLICY"
        assert parent[0].find("PROVIDED-MODE-GROUP-REF") is not None
        assert parent[0].find("QUEUE-LENGTH") is not None
        assert parent[0].find("ENHANCED-MODE-API") is not None
        assert parent[0].find("ACK-REQUEST") is not None

    def test_behavior_mode_sender_policy(self, writer):
        behavior = _make_behavior()
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(_ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        behavior.addModeSenderPolicy(policy)
        parent = _parent()
        writer.writeBswInternalBehaviorModeSenderPolicy(parent, behavior)
        assert parent[0].tag == "MODE-SENDER-POLICYS"
        assert parent[0].find("BSW-MODE-SENDER-POLICY") is not None

    def test_behavior_mode_sender_policy_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorModeSenderPolicy(parent, behavior)
        assert len(parent) == 0

    def test_included_mode_declaration_group_sets(self, writer):
        behavior = _make_behavior()
        group_set = IncludedModeDeclarationGroupSet()
        group_set.addModeDeclarationGroupRef(_ref("/g", "MODE-DECLARATION-GROUP"))
        group_set.setPrefix(_literal("px"))
        behavior.addIncludedModeDeclarationGroupSet(group_set)
        parent = _parent()
        writer.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(parent, behavior)
        assert parent[0].tag == "INCLUDED-MODE-DECLARATION-GROUP-SETS"
        gs = parent[0].find("INCLUDED-MODE-DECLARATION-GROUP-SET")
        assert gs is not None
        assert gs.find("PREFIX").text == "px"

    def test_included_mode_declaration_group_sets_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(parent, behavior)
        assert len(parent) == 0


class TestWriterBswReceptionPolicies:
    def test_queued_data_reception_policy(self, writer):
        policy = BswQueuedDataReceptionPolicy()
        policy.setEnableTakeAddress(_bool(True))
        policy.setReceivedDataRef(_ref("/d", "VARIABLE-DATA-PROTOTYPE"))
        policy.setQueueLength(_posint(3))
        parent = _parent()
        writer.writeBswQueuedDataReceptionPolicy(parent, policy)
        assert parent[0].tag == "BSW-QUEUED-DATA-RECEPTION-POLICY"
        assert parent[0].find("ENABLE-TAKE-ADDRESS") is not None
        assert parent[0].find("RECEIVED-DATA-REF") is not None
        assert parent[0].find("QUEUE-LENGTH") is not None

    def test_behavior_reception_policies(self, writer):
        behavior = _make_behavior()
        policy = BswQueuedDataReceptionPolicy()
        policy.setReceivedDataRef(_ref("/d", "VARIABLE-DATA-PROTOTYPE"))
        behavior.addReceptionPolicy(policy)
        parent = _parent()
        writer.writeBswInternalBehaviorReceptionPolicies(parent, behavior)
        assert parent[0].tag == "RECEPTION-POLICYS"
        assert parent[0].find("BSW-QUEUED-DATA-RECEPTION-POLICY") is not None

    def test_behavior_reception_policies_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorReceptionPolicies(parent, behavior)
        assert len(parent) == 0

    def test_writeBswDataReceptionPolicy_direct(self, writer):
        policy = BswQueuedDataReceptionPolicy()
        policy.setEnableTakeAddress(_bool(True))
        policy.setReceivedDataRef(_ref("/d", "VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.writeBswDataReceptionPolicy(parent, policy)
        assert parent.find("ENABLE-TAKE-ADDRESS") is not None
        assert parent.find("RECEIVED-DATA-REF") is not None


class TestWriterBswInternalTriggeringPoints:
    def test_internal_triggering_point(self, writer):
        behavior = _make_behavior()
        point = behavior.createBswInternalTriggeringPoint("itp")
        parent = _parent()
        writer.writeBswInternalTriggeringPoint(parent, point)
        assert parent[0].tag == "BSW-INTERNAL-TRIGGERING-POINT"

    def test_behavior_internal_triggering_points(self, writer):
        behavior = _make_behavior()
        behavior.createBswInternalTriggeringPoint("itp1")
        behavior.createBswInternalTriggeringPoint("itp2")
        parent = _parent()
        writer.writeBswInternalBehaviorInternalTriggeringPoints(parent, behavior)
        assert parent[0].tag == "INTERNAL-TRIGGERING-POINTS"
        points = parent[0].findall("BSW-INTERNAL-TRIGGERING-POINT")
        assert len(points) == 2

    def test_behavior_internal_triggering_points_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorInternalTriggeringPoints(parent, behavior)
        assert len(parent) == 0

    def test_writeBswInternalBehavior(self, writer):
        behavior = _make_behavior()
        behavior.createBswInternalTriggeringPoint("itp")
        behavior.createBswSchedulableEntity("se")
        behavior.createBswTimingEvent("te").setPeriod(_time(0.1))
        parent = _parent()
        writer.writeBswInternalBehavior(parent, behavior)
        assert parent[0].tag == "BSW-INTERNAL-BEHAVIOR"
        bh = parent[0]
        assert bh.find("INTERNAL-TRIGGERING-POINTS") is not None
        assert bh.find("ENTITYS") is not None
        assert bh.find("EVENTS") is not None

    def test_writeBswModuleDescriptionInternalBehaviors(self, writer):
        desc = _make_desc()
        desc.createBswInternalBehavior("beh")
        parent = _parent()
        writer.writeBswModuleDescriptionInternalBehaviors(parent, desc)
        assert parent[0].tag == "INTERNAL-BEHAVIORS"
        assert parent[0].find("BSW-INTERNAL-BEHAVIOR") is not None

    def test_writeBswModuleDescriptionInternalBehaviors_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionInternalBehaviors(parent, desc)
        assert len(parent) == 0


class TestWriterBswServiceDependency:
    def test_writeBswServiceDependency_full(self, writer):
        dependency = BswServiceDependency()
        dependency.setIdent(BswServiceDependencyIdent(dependency, "ident"))
        data = RoleBasedDataAssignment()
        data.setRole(ARLiteral().setValue("theRole"))
        dependency.addAssignedData(data)
        entry = RoleBasedBswModuleEntryAssignment()
        entry.setRole(ARLiteral().setValue("errorNotification"))
        dependency.addAssignedEntryRole(entry)
        needs = BswMgrNeeds(dependency, "needs")
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("IDENT/SHORT-NAME").text == "ident"
        assert dep_element.find("ASSIGNED-DATAS/ROLE-BASED-DATA-ASSIGNMENT/ROLE").text == "theRole"
        assert dep_element.find("ASSIGNED-ENTRY-ROLES/ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT/ROLE").text == "errorNotification"
        assert dep_element.find("SERVICE-NEEDS/BSW-MGR-NEEDS/SHORT-NAME").text == "needs"

    def test_writeBswServiceDependency_com_mgr_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ComMgrUserNeeds, MaxCommModeEnum

        dependency = BswServiceDependency()
        needs = ComMgrUserNeeds(dependency, "needs")
        needs.setMaxCommMode(MaxCommModeEnum().setValue(MaxCommModeEnum.SILENT))
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/COM-MGR-USER-NEEDS/SHORT-NAME").text == "needs"
        assert dep_element.find("SERVICE-NEEDS/COM-MGR-USER-NEEDS/MAX-COMM-MODE").text == "silent"

    def test_writeBswServiceDependency_io_control_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIoControlNeeds

        dependency = BswServiceDependency()
        needs = DiagnosticIoControlNeeds(dependency, "needs")
        needs.setFreezeCurrentStateSupported(ARBoolean().setValue(True))
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-IO-CONTROL-NEEDS/SHORT-NAME").text == "needs"
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-IO-CONTROL-NEEDS/FREEZE-CURRENT-STATE-SUPPORTED").text == "true"

    def test_writeBswServiceDependency_diagnostic_enable_condition_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEnableConditionNeeds, EventAcceptanceStatusEnum

        dependency = BswServiceDependency()
        needs = DiagnosticEnableConditionNeeds(dependency, "needs")
        needs.setInitialStatus(EventAcceptanceStatusEnum().setValue(EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_DISABLED))
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-ENABLE-CONDITION-NEEDS/SHORT-NAME").text == "needs"
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-ENABLE-CONDITION-NEEDS/INITIAL-STATUS").text == "eventAcceptanceDisabled"

    def test_writeBswServiceDependency_diagnostic_operation_cycle_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticOperationCycleNeeds, OperationCycleTypeEnum

        dependency = BswServiceDependency()
        needs = DiagnosticOperationCycleNeeds(dependency, "needs")
        needs.setOperationCycle(OperationCycleTypeEnum().setValue(OperationCycleTypeEnum.WARMUP))
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-OPERATION-CYCLE-NEEDS/SHORT-NAME").text == "needs"
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-OPERATION-CYCLE-NEEDS/OPERATION-CYCLE").text == "warmup"

    def test_writeBswServiceDependency_diagnostic_storage_condition_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticStorageConditionNeeds, StorageConditionStatusEnum

        dependency = BswServiceDependency()
        needs = DiagnosticStorageConditionNeeds(dependency, "needs")
        needs.setInitialStatus(StorageConditionStatusEnum().setValue(StorageConditionStatusEnum.EVENT_STORAGE_ENABLE))
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-STORAGE-CONDITION-NEEDS/SHORT-NAME").text == "needs"
        assert dep_element.find("SERVICE-NEEDS/DIAGNOSTIC-STORAGE-CONDITION-NEEDS/INITIAL-STATUS").text == "eventStorageEnabled"

    def test_writeBswServiceDependency_indicator_status_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIndicatorTypeEnum, IndicatorStatusNeeds

        dependency = BswServiceDependency()
        needs = IndicatorStatusNeeds(dependency, "needs")
        needs.setType(DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION))
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/INDICATOR-STATUS-NEEDS/SHORT-NAME").text == "needs"
        assert dep_element.find("SERVICE-NEEDS/INDICATOR-STATUS-NEEDS/TYPE").text == "malfunction"

    def test_writeBswServiceDependency_function_inhibition_availability_needs(self, writer):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import FunctionInhibitionAvailabilityNeeds
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        dependency = BswServiceDependency()
        needs = FunctionInhibitionAvailabilityNeeds(dependency, "needs")
        ref = RefType()
        ref.setValue("/Fim/Controlled")
        ref.setDest("FUNCTION-INHIBITION-NEEDS")
        needs.setControlledFidRef(ref)
        dependency.setServiceNeeds(needs)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("SERVICE-NEEDS/FUNCTION-INHIBITION-AVAILABILITY-NEEDS/SHORT-NAME").text == "needs"
        ref_element = dep_element.find("SERVICE-NEEDS/FUNCTION-INHIBITION-AVAILABILITY-NEEDS/CONTROLLED-FID-REF")
        assert ref_element is not None
        assert ref_element.text == "/Fim/Controlled"
        assert ref_element.get("DEST") == "FUNCTION-INHIBITION-NEEDS"

    def test_writeBswServiceDependency_minimal(self, writer):
        dependency = BswServiceDependency()
        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        dep_element = parent.find("BSW-SERVICE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("IDENT") is None
        assert dep_element.find("ASSIGNED-DATAS") is None
        assert dep_element.find("ASSIGNED-ENTRY-ROLES") is None
        assert dep_element.find("SERVICE-NEEDS") is None

    def test_writeBswServiceDependency_symbolic_name_props(self, writer):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier

        dependency = BswServiceDependency()
        props = SymbolicNameProps(dependency, "symProps")
        props.setSymbol(CIdentifier().setValue("mySymbol"))
        dependency.setSymbolicNameProps(props)

        parent = _parent()
        writer.writeBswServiceDependency(parent, dependency)

        props_element = parent.find("BSW-SERVICE-DEPENDENCY/SYMBOLIC-NAME-PROPS")
        assert props_element is not None
        assert props_element.find("SHORT-NAME").text == "symProps"
        symbol_element = props_element.find("SYMBOL")
        assert symbol_element is not None
        assert symbol_element.text == "mySymbol"

    def test_writeBswInternalBehaviorServiceDependencies(self, writer):
        behavior = _make_behavior()
        dependency = BswServiceDependency()
        behavior.addServiceDependency(dependency)
        parent = _parent()
        writer.writeBswInternalBehaviorServiceDependencies(parent, behavior)
        assert parent[0].tag == "SERVICE-DEPENDENCYS"
        assert parent[0].find("BSW-SERVICE-DEPENDENCY") is not None

    def test_writeBswInternalBehaviorServiceDependencies_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorServiceDependencies(parent, behavior)
        assert len(parent) == 0

    def test_writeBswInternalBehavior_includes_service_dependencies(self, writer):
        behavior = _make_behavior()
        behavior.addServiceDependency(BswServiceDependency())
        parent = _parent()
        writer.writeBswInternalBehavior(parent, behavior)
        bh = parent[0]
        assert bh.find("SERVICE-DEPENDENCYS") is not None


class TestWriterBswModuleDescriptionTriggersAndDatas:
    def test_writeTrigger(self, writer):
        desc = _make_desc()
        trigger = desc.createReleasedTrigger("trig")
        parent = _parent()
        writer.writeTrigger(parent, trigger)
        assert parent[0].tag == "TRIGGER"

    def test_released_triggers(self, writer):
        desc = _make_desc()
        desc.createReleasedTrigger("rt1")
        parent = _parent()
        writer.writeBswModuleDescriptionReleasedTriggers(parent, desc)
        assert parent[0].tag == "RELEASED-TRIGGERS"
        assert parent[0].find("TRIGGER") is not None

    def test_released_triggers_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionReleasedTriggers(parent, desc)
        assert len(parent) == 0

    def test_required_triggers(self, writer):
        desc = _make_desc()
        desc.createRequiredTrigger("rt1")
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredTriggers(parent, desc)
        assert parent[0].tag == "REQUIRED-TRIGGERS"
        assert parent[0].find("TRIGGER") is not None

    def test_required_triggers_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredTriggers(parent, desc)
        assert len(parent) == 0

    def test_provided_datas(self, writer):
        desc = _make_desc()
        desc.createProvidedData("pd")
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedDatas(parent, desc)
        assert parent[0].tag == "PROVIDED-DATAS"
        assert parent[0].find("VARIABLE-DATA-PROTOTYPE") is not None

    def test_provided_datas_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedDatas(parent, desc)
        assert len(parent) == 0

    def test_required_datas(self, writer):
        desc = _make_desc()
        desc.createRequiredData("rd")
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredDatas(parent, desc)
        assert parent[0].tag == "REQUIRED-DATAS"
        assert parent[0].find("VARIABLE-DATA-PROTOTYPE") is not None

    def test_required_datas_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredDatas(parent, desc)
        assert len(parent) == 0


class TestWriterBswModuleClientServerEntries:
    def test_entry_full(self, writer):
        desc = _make_desc()
        entry = desc.createProvidedClientServerEntry("cs")
        entry.setEncapsulatedEntryRef(_ref("/e", "BSW-MODULE-ENTRY"))
        entry.setIsReentrant(_bool(True))
        entry.setIsSynchronous(_bool(False))
        parent = _parent()
        writer.writeBswModuleClientServerEntry(parent, entry)
        assert parent[0].tag == "BSW-MODULE-CLIENT-SERVER-ENTRY"
        assert parent[0].find("ENCAPSULATED-ENTRY-REF") is not None
        assert parent[0].find("IS-REENTRANT") is not None
        assert parent[0].find("IS-SYNCHRONOUS") is not None

    def test_entry_none(self, writer):
        parent = _parent()
        writer.writeBswModuleClientServerEntry(parent, None)
        assert len(parent) == 0

    def test_provided_client_server_entries(self, writer):
        desc = _make_desc()
        desc.createProvidedClientServerEntry("cs1")
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedClientServerEntries(parent, desc)
        assert parent[0].tag == "PROVIDED-CLIENT-SERVER-ENTRYS"
        assert parent[0].find("BSW-MODULE-CLIENT-SERVER-ENTRY") is not None

    def test_provided_client_server_entries_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedClientServerEntries(parent, desc)
        assert len(parent) == 0

    def test_required_client_server_entries(self, writer):
        desc = _make_desc()
        desc.createRequiredClientServerEntry("cs1")
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredClientServerEntries(parent, desc)
        assert parent[0].tag == "REQUIRED-CLIENT-SERVER-ENTRYS"
        assert parent[0].find("BSW-MODULE-CLIENT-SERVER-ENTRY") is not None

    def test_required_client_server_entries_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredClientServerEntries(parent, desc)
        assert len(parent) == 0

    def test_writeBswModuleDescription_full(self, writer):
        desc = _make_desc()
        desc.setModuleId(_posint(1))
        desc.addImplementedEntryRef(_ref("/e", "BSW-MODULE-ENTRY"))
        desc.createProvidedModeGroup("pmg")
        desc.createRequiredModeGroup("rmg")
        desc.createProvidedClientServerEntry("pcs")
        desc.createRequiredClientServerEntry("rcs")
        desc.createProvidedData("pd")
        desc.createRequiredData("rd")
        desc.createBswInternalBehavior("beh")
        desc.createReleasedTrigger("rt")
        parent = _parent()
        writer.writeBswModuleDescription(parent, desc)
        bmd = parent[0]
        assert bmd.tag == "BSW-MODULE-DESCRIPTION"
        assert bmd.find("MODULE-ID") is not None
        assert bmd.find("PROVIDED-ENTRYS") is not None
        assert bmd.find("PROVIDED-MODE-GROUPS") is not None
        assert bmd.find("REQUIRED-MODE-GROUPS") is not None
        assert bmd.find("PROVIDED-CLIENT-SERVER-ENTRYS") is not None
        assert bmd.find("REQUIRED-CLIENT-SERVER-ENTRYS") is not None
        assert bmd.find("PROVIDED-DATAS") is not None
        assert bmd.find("REQUIRED-DATAS") is not None
        assert bmd.find("INTERNAL-BEHAVIORS") is not None
        assert bmd.find("RELEASED-TRIGGERS") is not None


class TestWriterBswModuleEntry:
    def test_set_sw_service_arg(self, writer):
        entry = _make_entry()
        arg = entry.createArgument("arg")
        arg.setDirection(_literal("in"))
        parent = _parent()
        writer.setSwServiceArg(parent, "SW-SERVICE-ARG", arg)
        assert parent[0].tag == "SW-SERVICE-ARG"
        assert parent[0].find("DIRECTION") is not None

    def test_arguments(self, writer):
        entry = _make_entry()
        entry.createArgument("arg1")
        entry.createArgument("arg2")
        parent = _parent()
        writer.writeBswModuleEntryArguments(parent, entry)
        assert parent[0].tag == "ARGUMENTS"
        args = parent[0].findall("SW-SERVICE-ARG")
        assert len(args) == 2

    def test_arguments_empty(self, writer):
        entry = _make_entry()
        parent = _parent()
        writer.writeBswModuleEntryArguments(parent, entry)
        assert len(parent) == 0

    def test_return_type_with_return(self, writer):
        entry = _make_entry()
        entry.createReturnType("ret")
        parent = _parent()
        writer.writeBswModuleEntryReturnType(parent, entry)
        assert parent[0].tag == "RETURN-TYPE"

    def test_return_type_none(self, writer):
        entry = _make_entry()
        parent = _parent()
        writer.writeBswModuleEntryReturnType(parent, entry)
        assert len(parent) == 0

    def test_writeBswModuleEntry_full(self, writer):
        entry = _make_entry()
        entry.setServiceId(_posint(42))
        entry.setIsReentrant(_bool(True))
        entry.setIsSynchronous(_bool(False))
        entry.setCallType(_literal("scheduled"))
        entry.setExecutionContext(_literal("task"))
        entry.setSwServiceImplPolicy(_literal("inline"))
        entry.setBswEntryKind(_literal("concrete"))
        entry.setRole(_literal("theRole"))
        entry.setFunctionPrototypeEmitter(_literal("RTE"))
        entry.createReturnType("ret")
        entry.createArgument("arg")
        parent = _parent()
        writer.writeBswModuleEntry(parent, entry)
        e = parent[0]
        assert e.tag == "BSW-MODULE-ENTRY"
        assert e.find("SERVICE-ID") is not None
        assert e.find("IS-REENTRANT") is not None
        assert e.find("IS-SYNCHRONOUS") is not None
        assert e.find("CALL-TYPE") is not None
        assert e.find("EXECUTION-CONTEXT") is not None
        assert e.find("SW-SERVICE-IMPL-POLICY") is not None
        assert e.find("BSW-ENTRY-KIND") is not None
        assert e.find("ROLE").text == "theRole"
        assert e.find("FUNCTION-PROTOTYPE-EMITTER").text == "RTE"
        assert e.find("RETURN-TYPE") is not None
        assert e.find("ARGUMENTS") is not None


class TestWriterModeInBswModuleDescriptionInstanceRefRoundTrip:
    def test_round_trip_mode_irefs(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        desc = pkg.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        event = behavior.createBswModeSwitchEvent("Ev")
        iref = ModeInBswModuleDescriptionInstanceRef()
        iref.setContextModeDeclarationGroupRef(_ref("/g", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        iref.setTargetModeRef(_ref("/m", "MODE-DECLARATION"))
        event.addModeIRef(iref)

        out_file = tmp_path / "mode_iref_out.arxml"
        ARXMLWriter().save(str(out_file), document)

        reloaded = AUTOSAR.getInstance()
        reloaded.clear()
        reloaded.setARRelease("R23-11")
        ARXMLParser().load(str(out_file), reloaded)

        desc_2 = reloaded.getARPackages()[0].getBswModuleDescriptions()[0]
        event_2 = desc_2.getInternalBehaviors()[0].getBswEvents()[0]
        assert isinstance(event_2, BswModeSwitchEvent)
        mode_irefs = event_2.getModeIRefs()
        assert len(mode_irefs) == 1
        assert mode_irefs[0].getContextModeDeclarationGroupRef().getValue() == "/g"
        assert mode_irefs[0].getTargetModeRef().getValue() == "/m"

    def test_round_trip_empty_mode_irefs(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        desc = pkg.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        behavior.createBswModeSwitchEvent("Ev")

        out_file = tmp_path / "mode_iref_empty_out.arxml"
        ARXMLWriter().save(str(out_file), document)

        reloaded = AUTOSAR.getInstance()
        reloaded.clear()
        reloaded.setARRelease("R23-11")
        ARXMLParser().load(str(out_file), reloaded)

        desc_2 = reloaded.getARPackages()[0].getBswModuleDescriptions()[0]
        event_2 = desc_2.getInternalBehaviors()[0].getBswEvents()[0]
        assert event_2.getModeIRefs() == []


class TestSwServiceArgRoundTrip:
    def _build(self, document):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ArgumentDirectionEnum
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwImplPolicyEnum, ValueList

        pkg = document.createARPackage("AUTOSAR")
        entry = pkg.createBswModuleEntry("entry1")

        argument = entry.createArgument("arg1")
        argument.setDirection(ArgumentDirectionEnum().setValue(ArgumentDirectionEnum.IN))
        array_size = ValueList()
        array_size.setV(ARNumerical().setValue("4"))
        argument.setSwArraysize(array_size)
        props = SwDataDefProps()
        props.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.STANDARD))
        argument.setSwDataDefProps(props)

        return_type = entry.createReturnType("ret1")
        return_type.setDirection(ArgumentDirectionEnum().setValue(ArgumentDirectionEnum.OUT))
        return entry

    def test_round_trip_sw_service_arg(self):
        import os
        import tempfile

        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as _AUTOSAR
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        _AUTOSAR.getInstance().setARRelease("R23-11")
        document = _AUTOSAR.getInstance()
        document.clear()
        self._build(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = _AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            entry_2 = document_2.getARPackages()[0].getBswModuleEntries()[0]
            arguments = entry_2.getArguments()
            assert len(arguments) == 1
            argument_2 = arguments[0]
            assert argument_2.getShortName() == "arg1"
            assert argument_2.getDirection().getValue() == "in"
            assert argument_2.getSwArraysize().getV().getValue() == "4"
            assert argument_2.getSwDataDefProps().getSwImplPolicy().getValue() == "standard"
            return_type_2 = entry_2.getReturnType()
            assert return_type_2 is not None
            assert return_type_2.getShortName() == "ret1"
            assert return_type_2.getDirection().getValue() == "out"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
