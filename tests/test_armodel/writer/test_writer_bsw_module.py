"""Tests for writer BSW module template handlers."""
import xml.etree.cElementTree as ET
import pytest
from unittest.mock import MagicMock

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswModeSenderPolicy,
    BswQueuedDataReceptionPolicy,
    BswVariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswModuleClientServerEntry,
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    ARNumerical,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (  # noqa E501
    IncludedModeDeclarationGroupSet,
)


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
        desc.createProvidedModeGroup("pmg").setTypeTRef(
            _ref("/t", "MODE-DECLARATION-GROUP")
        )
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
        desc.createRequiredModeGroup("rmg").setTypeTRef(
            _ref("/t", "MODE-DECLARATION-GROUP")
        )
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
        entity.addCanEnterExclusiveAreaRef(_ref("/ea1", "EXCLUSIVE-AREA"))
        entity.addCanEnterExclusiveAreaRef(_ref("/ea2", "EXCLUSIVE-AREA"))
        parent = _parent()
        writer.writeCanEnterExclusiveAreaRefs(parent, entity)
        assert parent[0].tag == "CAN-ENTER-EXCLUSIVE-AREA-REFS"
        refs = parent[0].findall("CAN-ENTER-EXCLUSIVE-AREA-REF")
        assert len(refs) == 2

    def test_can_enter_exclusive_area_refs_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeCanEnterExclusiveAreaRefs(parent, entity)
        assert len(parent) == 0

    def test_writeExecutableEntity_full(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addCanEnterExclusiveAreaRef(_ref("/ea", "EXCLUSIVE-AREA"))
        entity.setMinimumStartInterval(_time(0.1))
        entity.setSwAddrMethodRef(_ref("/am", "SW-ADDR-METHOD"))
        parent = _parent()
        writer.writeExecutableEntity(parent, entity)
        assert parent.find("CAN-ENTER-EXCLUSIVE-AREA-REFS") is not None
        assert parent.find("MINIMUM-START-INTERVAL").text == "0.1"
        assert parent.find("SW-ADDR-METHOD-REF") is not None


class TestWriterBswModuleEntityFamily:
    def test_managed_mode_groups(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        entity.addManagedModeGroupRef(
            _ref("/mg1", "MODE-DECLARATION-GROUP-PROTOTYPE")
        )
        parent = _parent()
        writer.writeBswModuleEntityManagedModeGroups(parent, entity)
        assert parent[0].tag == "MANAGED-MODE-GROUPS"
        cond = parent[0].find(
            "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"
        )
        assert cond is not None

    def test_managed_mode_groups_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeBswModuleEntityManagedModeGroups(parent, entity)
        assert len(parent) == 0

    def test_bsw_variable_access_with_data(self, writer):
        behavior = _make_behavior()
        access = BswVariableAccess(behavior, "va")
        access.setAccessedVariableRef(
            _ref("/v", "VARIABLE-DATA-PROTOTYPE")
        )
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
        entity.addActivationPointRef(
            _ref("/ap", "BSW-INTERNAL-TRIGGERING-POINT")
        )
        parent = _parent()
        writer.writeBswModuleEntityActivationPointRefs(parent, entity)
        assert parent[0].tag == "ACTIVATION-POINTS"
        cond = parent[0].find(
            "BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL"
        )
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
        entity.createBswAsynchronousServerCallPoint("acp").setCalledEntryRef(
            _ref("/e1", "BSW-MODULE-ENTRY")
        )
        entity.createBswSynchronousServerCallPoint("scp").setCalledEntryRef(
            _ref("/e2", "BSW-MODULE-ENTRY")
        )
        parent = _parent()
        writer.writeBswModuleEntityCallPoints(parent, entity)
        assert parent[0].tag == "CALL-POINTS"
        tags = {c.tag for c in parent[0]}
        assert "BSW-ASYNCHRONOUS-SERVER-CALL-POINT" in tags
        assert "BSW-SYNCHRONOUS-SERVER-CALL-POINT" in tags

    def test_entity_call_points_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("ent")
        parent = _parent()
        writer.writeBswModuleEntityCallPoints(parent, entity)
        assert len(parent) == 0


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
        entity.addActivationPointRef(
            _ref("/ap", "BSW-INTERNAL-TRIGGERING-POINT")
        )
        entity.createBswSynchronousServerCallPoint("scp").setCalledEntryRef(
            _ref("/ce", "BSW-MODULE-ENTRY")
        )
        entity.createDataSendPoint("dsp")
        entity.createDataReceivePoint("drp")
        entity.addManagedModeGroupRef(
            _ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE")
        )
        entity.addIssuedTriggerRef(_ref("/t", "TRIGGER"))
        parent = _parent()
        writer.writeBswModuleEntity(parent, entity)
        assert parent.find("IMPLEMENTED-ENTRY-REF") is not None
        assert parent.find("ACTIVATION-POINTS") is not None
        assert parent.find("CALL-POINTS") is not None
        assert parent.find("DATA-SEND-POINTS") is not None
        assert parent.find("DATA-RECEIVE-POINTS") is not None
        assert parent.find("MANAGED-MODE-GROUPS") is not None
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

    def test_background_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswBackgroundEvent("be")
        parent = _parent()
        writer.writeBswBackgroundEvent(parent, event)
        assert parent[0].tag == "BSW-BACKGROUND-EVENT"

    def test_internal_trigger_occurred_event(self, writer):
        behavior = _make_behavior()
        event = behavior.createBswInternalTriggerOccurredEvent("ito")
        event.setEventSourceRef(
            _ref("/src", "BSW-INTERNAL-TRIGGERING-POINT")
        )
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

    def test_dispatches_all_event_types(self, writer):
        behavior = _make_behavior()
        behavior.createBswTimingEvent("te").setPeriod(_time(0.1))
        behavior.createBswBackgroundEvent("be")
        behavior.createBswInternalTriggerOccurredEvent("ito")
        behavior.createBswExternalTriggerOccurredEvent("eto")
        behavior.createBswDataReceivedEvent("dre")
        behavior.createBswOperationInvokedEvent("oie")
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

    def test_events_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorEvents(parent, behavior)
        assert len(parent) == 0


class TestWriterBswModeSenderPolicy:
    def test_set_bsw_mode_sender_policy(self, writer):
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(
            _ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE")
        )
        policy.setQueueLength(5)
        parent = _parent()
        writer.setBswModeSenderPolicy(parent, policy)
        assert parent[0].tag == "BSW-MODE-SENDER-POLICY"
        assert parent[0].find("PROVIDED-MODE-GROUP-REF") is not None
        assert parent[0].find("QUEUE-LENGTH") is not None

    def test_behavior_mode_sender_policy(self, writer):
        behavior = _make_behavior()
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(
            _ref("/mg", "MODE-DECLARATION-GROUP-PROTOTYPE")
        )
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
        group_set.addModeDeclarationGroupRef(
            _ref("/g", "MODE-DECLARATION-GROUP")
        )
        group_set.setPrefix(_literal("px"))
        behavior.addIncludedModeDeclarationGroupSet(group_set)
        parent = _parent()
        writer.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(
            parent, behavior
        )
        assert parent[0].tag == "INCLUDED-MODE-DECLARATION-GROUP-SETS"
        gs = parent[0].find("INCLUDED-MODE-DECLARATION-GROUP-SET")
        assert gs is not None
        assert gs.find("PREFIX").text == "px"

    def test_included_mode_declaration_group_sets_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(
            parent, behavior
        )
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
        writer.writeBswModuleDescriptionProvidedClientServerEntries(
            parent, desc
        )
        assert parent[0].tag == "PROVIDED-CLIENT-SERVER-ENTRYS"
        assert parent[0].find("BSW-MODULE-CLIENT-SERVER-ENTRY") is not None

    def test_provided_client_server_entries_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionProvidedClientServerEntries(
            parent, desc
        )
        assert len(parent) == 0

    def test_required_client_server_entries(self, writer):
        desc = _make_desc()
        desc.createRequiredClientServerEntry("cs1")
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredClientServerEntries(
            parent, desc
        )
        assert parent[0].tag == "REQUIRED-CLIENT-SERVER-ENTRYS"
        assert parent[0].find("BSW-MODULE-CLIENT-SERVER-ENTRY") is not None

    def test_required_client_server_entries_empty(self, writer):
        desc = _make_desc()
        parent = _parent()
        writer.writeBswModuleDescriptionRequiredClientServerEntries(
            parent, desc
        )
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
        entry.setServiceId(_numerical(42))
        entry.setIsReentrant(_bool(True))
        entry.setIsSynchronous(_bool(False))
        entry.setCallType(_literal("scheduled"))
        entry.setExecutionContext(_literal("task"))
        entry.setSwServiceImplPolicy(_literal("inline"))
        entry.setBswEntryKind(_literal("function"))
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
        assert e.find("RETURN-TYPE") is not None
        assert e.find("ARGUMENTS") is not None
