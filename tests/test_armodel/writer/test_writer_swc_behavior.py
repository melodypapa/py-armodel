"""Tests for writer SWC internal behavior handlers."""
import xml.etree.cElementTree as ET
import pytest
from unittest.mock import MagicMock

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    CryptoServiceNeeds,
    DiagEventDebounceMonitorInternal,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticEventInfoNeeds,
    DiagnosticEventNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticValueNeeds,
    DltUserNeeds,
    DtcStatusChangeNotificationNeeds,
    EcuStateMgrUserNeeds,
    NvBlockNeeds,
    RoleBasedDataAssignment,
    RoleBasedDataTypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARLiteral,
    ARBoolean,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (  # noqa E501
    PModeGroupInAtomicSwcInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (  # noqa E501
    POperationInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef  # noqa E501
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (  # noqa E501
    ParameterAccess,
    VariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import (  # noqa E501
    AutosarParameterRef,
    ParameterInAtomicSWCTypeInstanceRef,
    VariableInAtomicSWCTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet  # noqa E501
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (  # noqa E501
    IncludedModeDeclarationGroupSet,
    ModeAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (  # noqa E501
    PortAPIOption,
    PortDefinedArgumentValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    RunnableEntityArgument,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (  # noqa E501
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification  # noqa E501


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


def _make_behavior():
    app = AUTOSAR.getInstance().createARPackage("Pkg").createApplicationSwComponentType("App")  # noqa E501
    return app.createSwcInternalBehavior("Behavior")


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


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _bool(value):
    b = ARBoolean()
    b.setValue(value)
    return b


def _int(value):
    i = Integer()
    i.setValue(str(value))
    return i


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


# ==================== RTE Event Writers ====================


class TestWriterRteEvents:
    def test_writeTimingEvent_full(self, writer):
        behavior = _make_behavior()
        event = behavior.createTimingEvent("te")
        event.setPeriod(_time(0.1))
        event.setOffset(_time(0.05))
        parent = _parent()
        writer.writeTimingEvent(parent, event)
        assert len(parent) == 1
        evt = parent[0]
        assert evt.tag == "TIMING-EVENT"
        assert evt.find("OFFSET").text == "0.05"
        assert evt.find("PERIOD").text == "0.1"

    def test_writeTimingEvent_none(self, writer):
        parent = _parent()
        writer.writeTimingEvent(parent, None)
        assert len(parent) == 0

    def test_writeOperationInvokedEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createOperationInvokedEvent("oe")
        iref = POperationInAtomicSwcInstanceRef()
        iref.setContextPPortRef(_ref("/p", "P-PORT-PROTOTYPE"))
        iref.setTargetProvidedOperationRef(_ref("/op", "CLIENT-SERVER-OPERATION"))
        event.setOperationIRef(iref)
        parent = _parent()
        writer.writeOperationInvokedEvent(parent, event)
        assert parent[0].tag == "OPERATION-INVOKED-EVENT"
        op_iref = parent[0].find("OPERATION-IREF")
        assert op_iref is not None

    def test_writeOperationInvokedEvent_none(self, writer):
        parent = _parent()
        writer.writeOperationInvokedEvent(parent, None)
        assert len(parent) == 0

    def test_writeSwcModeSwitchEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createSwcModeSwitchEvent("mse")
        event.setActivation(_literal("enable"))
        mode_iref = RModeInAtomicSwcInstanceRef()
        mode_iref.setContextPortRef(_ref("/p", "R-PORT-PROTOTYPE"))
        event.addModeIRef(mode_iref)
        parent = _parent()
        writer.writeSwcModeSwitchEvent(parent, event)
        evt = parent[0]
        assert evt.tag == "SWC-MODE-SWITCH-EVENT"
        assert evt.find("ACTIVATION").text == "enable"
        assert evt.find("MODE-IREFS") is not None

    def test_writeSwcModeSwitchEvent_none(self, writer):
        parent = _parent()
        writer.writeSwcModeSwitchEvent(parent, None)
        assert len(parent) == 0

    def test_writeDataReceivedEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createDataReceivedEvent("dre")
        iref = RVariableInAtomicSwcInstanceRef()
        iref.setContextRPortRef(_ref("/rp", "R-PORT-PROTOTYPE"))
        iref.setTargetDataElementRef(_ref("/de", "VARIABLE-DATA-PROTOTYPE"))
        event.setDataIRef(iref)
        parent = _parent()
        writer.writeDataReceivedEvent(parent, event)
        evt = parent[0]
        assert evt.tag == "DATA-RECEIVED-EVENT"
        assert evt.find("DATA-IREF") is not None

    def test_writeDataReceivedEvent_none(self, writer):
        parent = _parent()
        writer.writeDataReceivedEvent(parent, None)
        assert len(parent) == 0

    def test_writeInternalTriggerOccurredEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createInternalTriggerOccurredEvent("ito")
        parent = _parent()
        writer.writeInternalTriggerOccurredEvent(parent, event)
        assert len(parent) == 0

    def test_writeInitEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createInitEvent("ie")
        parent = _parent()
        writer.writeInitEvent(parent, event)
        assert parent[0].tag == "INIT-EVENT"

    def test_writeInitEvent_none(self, writer):
        parent = _parent()
        writer.writeInitEvent(parent, None)
        assert len(parent) == 0

    def test_writeAsynchronousServerCallReturnsEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createAsynchronousServerCallReturnsEvent("ascr")
        event.getActivationReasonRepresentationRef = MagicMock(
            return_value=_ref("/acp", "ASYNCHRONOUS-SERVER-CALL-POINT")
        )
        parent = _parent()
        writer.writeAsynchronousServerCallReturnsEvent(parent, event)
        evt = parent[0]
        assert evt.tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT"
        assert evt.find("EVENT-SOURCE-REF") is not None

    def test_writeAsynchronousServerCallReturnsEvent_none(self, writer):
        parent = _parent()
        writer.writeAsynchronousServerCallReturnsEvent(parent, None)
        assert len(parent) == 0

    def test_writeModeSwitchedAckEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createModeSwitchedAckEvent("msa")
        event.setEventSourceRef(_ref("/src", "MODE-SWITCH-POINT"))
        parent = _parent()
        writer.writeModeSwitchedAckEvent(parent, event)
        evt = parent[0]
        assert evt.tag == "MODE-SWITCHED-ACK-EVENT"
        assert evt.find("EVENT-SOURCE-REF") is not None

    def test_writeModeSwitchedAckEvent_none(self, writer):
        parent = _parent()
        writer.writeModeSwitchedAckEvent(parent, None)
        assert len(parent) == 0

    def test_writeBackgroundEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createBackgroundEvent("be")
        parent = _parent()
        writer.writeBackgroundEvent(parent, event)
        assert parent[0].tag == "BACKGROUND-EVENT"

    def test_writeBackgroundEvent_none(self, writer):
        parent = _parent()
        writer.writeBackgroundEvent(parent, None)
        assert len(parent) == 0

    def test_writeDataSendCompletedEvent(self, writer):
        behavior = _make_behavior()
        event = behavior.createDataSendCompletedEvent("dsc")
        event.setEventSourceRef(_ref("/src", "DATA-SEND-POINT"))
        parent = _parent()
        writer.writeDataSendCompletedEvent(parent, event)
        evt = parent[0]
        assert evt.tag == "DATA-SEND-COMPLETED-EVENT"
        assert evt.find("EVENT-SOURCE-REF") is not None

    def test_writeDataSendCompletedEvent_none(self, writer):
        parent = _parent()
        writer.writeDataSendCompletedEvent(parent, None)
        assert len(parent) == 0


class TestWriterSwcInternalBehaviorEventsDispatch:
    def test_dispatches_all_event_types(self, writer):
        behavior = _make_behavior()
        behavior.createTimingEvent("te")
        behavior.createInitEvent("ie")
        behavior.createBackgroundEvent("be")
        behavior.createModeSwitchedAckEvent("msa")
        behavior.createDataSendCompletedEvent("dsc")
        ascr = behavior.createAsynchronousServerCallReturnsEvent("ascr")
        ascr.getActivationReasonRepresentationRef = MagicMock(return_value=None)
        behavior.createInternalTriggerOccurredEvent("ito")
        parent = _parent()
        writer.writeSwcInternalBehaviorEvents(parent, behavior)
        events_tag = parent.find("EVENTS")
        assert events_tag is not None
        tags = {c.tag for c in events_tag}
        assert "TIMING-EVENT" in tags
        assert "INIT-EVENT" in tags
        assert "BACKGROUND-EVENT" in tags
        assert "MODE-SWITCHED-ACK-EVENT" in tags
        assert "DATA-SEND-COMPLETED-EVENT" in tags
        assert "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT" in tags

    def test_dispatches_operation_and_data_events(self, writer):
        behavior = _make_behavior()
        e1 = behavior.createOperationInvokedEvent("oe")
        iref = POperationInAtomicSwcInstanceRef()
        iref.setContextPPortRef(_ref("/p"))
        e1.setOperationIRef(iref)
        e2 = behavior.createDataReceivedEvent("dre")
        dref = RVariableInAtomicSwcInstanceRef()
        dref.setContextRPortRef(_ref("/rp"))
        e2.setDataIRef(dref)
        e3 = behavior.createSwcModeSwitchEvent("mse")
        e3.setActivation(_literal("enable"))
        parent = _parent()
        writer.writeSwcInternalBehaviorEvents(parent, behavior)
        tags = {c.tag for c in parent.find("EVENTS")}
        assert "OPERATION-INVOKED-EVENT" in tags
        assert "DATA-RECEIVED-EVENT" in tags
        assert "SWC-MODE-SWITCH-EVENT" in tags

    def test_no_events_no_tag(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorEvents(parent, behavior)
        assert parent.find("EVENTS") is None


# ==================== InternalBehavior writers ====================


class TestWriterInternalBehavior:
    def test_writeExclusiveAreas(self, writer):
        behavior = _make_behavior()
        behavior.createExclusiveArea("ea1")
        parent = _parent()
        writer.writeExclusiveAreas(parent, behavior)
        areas = parent.find("EXCLUSIVE-AREAS")
        assert areas is not None
        assert areas[0].tag == "EXCLUSIVE-AREA"

    def test_writeExclusiveAreas_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeExclusiveAreas(parent, behavior)
        assert parent.find("EXCLUSIVE-AREAS") is None

    def test_writeDataTypeMappingRefs(self, writer):
        behavior = _make_behavior()
        behavior.addDataTypeMappingRef(_ref("/dtm", "DATA-TYPE-MAPPING"))
        parent = _parent()
        writer.writeDataTypeMappingRefs(parent, behavior)
        refs = parent.find("DATA-TYPE-MAPPING-REFS")
        assert refs is not None
        assert refs[0].tag == "DATA-TYPE-MAPPING-REF"

    def test_writeDataTypeMappingRefs_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeDataTypeMappingRefs(parent, behavior)
        assert parent.find("DATA-TYPE-MAPPING-REFS") is None

    def test_writeInternalBehaviorStaticMemories(self, writer):
        behavior = _make_behavior()
        behavior.createStaticMemory("sm1")
        parent = _parent()
        writer.writeInternalBehaviorStaticMemories(parent, behavior)
        mem = parent.find("STATIC-MEMORYS")
        assert mem is not None
        assert mem[0].tag == "VARIABLE-DATA-PROTOTYPE"

    def test_writeInternalBehaviorStaticMemories_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeInternalBehaviorStaticMemories(parent, behavior)
        assert parent.find("STATIC-MEMORYS") is None

    def test_writeInternalBehavior(self, writer):
        behavior = _make_behavior()
        behavior.createConstantMemory("cm1")
        behavior.addDataTypeMappingRef(_ref("/dtm"))
        behavior.createExclusiveArea("ea1")
        behavior.createStaticMemory("sm1")
        parent = _parent()
        writer.writeInternalBehavior(parent, behavior)
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("CONSTANT-MEMORYS") is not None
        assert parent.find("DATA-TYPE-MAPPING-REFS") is not None
        assert parent.find("EXCLUSIVE-AREAS") is not None
        assert parent.find("STATIC-MEMORYS") is not None


# ==================== VariableAccess / ParameterAccess writers ====================


class TestWriterVariableAccess:
    def test_setVariableInAtomicSWCTypeInstanceRef(self, writer):
        iref = VariableInAtomicSWCTypeInstanceRef()
        iref.setPortPrototypeRef(_ref("/pp", "P-PORT-PROTOTYPE"))
        iref.setTargetDataPrototypeRef(_ref("/dp", "VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.setVariableInAtomicSWCTypeInstanceRef(parent, "VARIABLE-IREF", iref)
        assert parent[0].tag == "VARIABLE-IREF"
        assert parent[0].find("PORT-PROTOTYPE-REF") is not None

    def test_setVariableInAtomicSWCTypeInstanceRef_none(self, writer):
        parent = _parent()
        writer.setVariableInAtomicSWCTypeInstanceRef(parent, "VARIABLE-IREF", None)
        assert len(parent) == 0

    def test_setAutosarVariableRef(self, writer):
        ref = AutosarVariableRef()
        iref = VariableInAtomicSWCTypeInstanceRef()
        iref.setPortPrototypeRef(_ref("/pp"))
        ref.setAutosarVariableIRef(iref)
        ref.setLocalVariableRef(_ref("/lv"))
        parent = _parent()
        writer.setAutosarVariableRef(parent, "ACCESSED-VARIABLE", ref)
        av = parent.find("ACCESSED-VARIABLE")
        assert av is not None
        assert av.find("AUTOSAR-VARIABLE-IREF") is not None
        assert av.find("LOCAL-VARIABLE-REF") is not None

    def test_setAutosarVariableRef_none(self, writer):
        parent = _parent()
        writer.setAutosarVariableRef(parent, "ACCESSED-VARIABLE", None)
        assert len(parent) == 0

    def test_writeVariableAccess(self, writer):
        behavior = _make_behavior()
        runnable = behavior.createRunnableEntity("r1")
        access = runnable.createDataReadAccess("va")
        ref = AutosarVariableRef()
        iref = VariableInAtomicSWCTypeInstanceRef()
        iref.setPortPrototypeRef(_ref("/pp"))
        ref.setAutosarVariableIRef(iref)
        access.setAccessedVariableRef(ref)
        parent = _parent()
        writer.writeVariableAccess(parent, access)
        va = parent.find("VARIABLE-ACCESS")
        assert va is not None
        assert va.find("ACCESSED-VARIABLE") is not None


class TestWriterParameterAccess:
    def test_setParameterInAtomicSWCTypeInstanceRef(self, writer):
        iref = ParameterInAtomicSWCTypeInstanceRef()
        iref.setPortPrototypeRef(_ref("/pp"))
        iref.setTargetDataPrototypeRef(_ref("/dp"))
        parent = _parent()
        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "PARAM-IREF", iref)
        assert parent[0].tag == "PARAM-IREF"
        assert parent[0].find("PORT-PROTOTYPE-REF") is not None

    def test_setParameterInAtomicSWCTypeInstanceRef_none(self, writer):
        parent = _parent()
        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "PARAM-IREF", None)
        assert len(parent) == 0

    def test_setAutosarParameterRef(self, writer):
        pref = AutosarParameterRef()
        iref = ParameterInAtomicSWCTypeInstanceRef()
        iref.setPortPrototypeRef(_ref("/pp"))
        pref.setAutosarParameterIRef(iref)
        pref.setLocalParameterRef(_ref("/lp"))
        parent = _parent()
        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", pref)
        ap = parent.find("ACCESSED-PARAMETER")
        assert ap is not None
        assert ap.find("AUTOSAR-PARAMETER-IREF") is not None
        assert ap.find("LOCAL-PARAMETER-REF") is not None

    def test_setAutosarParameterRef_none(self, writer):
        parent = _parent()
        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", None)
        assert len(parent) == 0

    def test_writeParameterAccess(self, writer):
        behavior = _make_behavior()
        runnable = behavior.createRunnableEntity("r1")
        pa = runnable.createParameterAccess("pa1")
        pref = AutosarParameterRef()
        iref = ParameterInAtomicSWCTypeInstanceRef()
        iref.setPortPrototypeRef(_ref("/pp"))
        pref.setAutosarParameterIRef(iref)
        pa.setAccessedParameter(pref)
        parent = _parent()
        writer.writeParameterAccess(parent, pa)
        elem = parent.find("PARAMETER-ACCESS")
        assert elem is not None
        assert elem.find("ACCESSED-PARAMETER") is not None


# ==================== RunnableEntity writers ====================


class TestWriterRunnableEntity:
    def test_writeRunnableEntity_minimal(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        parent = _parent()
        writer.writeRunnableEntity(parent, entity)
        re_elem = parent.find("RUNNABLE-ENTITY")
        assert re_elem is not None
        assert re_elem.find("SHORT-NAME").text == "re1"

    def test_writeRunnableEntity_full(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.setCanBeInvokedConcurrently(_bool(True))
        entity.setSymbol(_literal("sym"))
        arg = RunnableEntityArgument()
        arg.setSymbol(_literal("argSym"))
        entity.addArgument(arg)
        entity.createDataReadAccess("dr1")
        entity.createDataWriteAccess("dw1")
        entity.createDataReceivePointByArgument("drp1")
        entity.createDataSendPoint("ds1")
        entity.createReadLocalVariable("rl1")
        entity.createWrittenLocalVariable("wl1")
        entity.createParameterAccess("pa1")
        sync = entity.createSynchronousServerCallPoint("scp1")
        rop = ROperationInAtomicSwcInstanceRef()
        rop.setContextRPortRef(_ref("/rp"))
        rop.setTargetRequiredOperationRef(_ref("/op"))
        sync.operationIRef = rop
        entity.createAsynchronousServerCallPoint("acp1")
        entity.createAsynchronousServerCallResultPoint("arp1")
        parent = _parent()
        writer.writeRunnableEntity(parent, entity)
        re_elem = parent.find("RUNNABLE-ENTITY")
        assert re_elem.find("CAN-BE-INVOKED-CONCURRENTLY").text == "true"
        assert re_elem.find("SYMBOL").text == "sym"
        assert re_elem.find("ARGUMENTS") is not None
        assert re_elem.find("DATA-READ-ACCESSS") is not None
        assert re_elem.find("DATA-WRITE-ACCESSS") is not None
        assert re_elem.find("DATA-RECEIVE-POINT-BY-ARGUMENTS") is not None
        assert re_elem.find("DATA-SEND-POINTS") is not None
        assert re_elem.find("READ-LOCAL-VARIABLES") is not None
        assert re_elem.find("WRITTEN-LOCAL-VARIABLES") is not None
        assert re_elem.find("PARAMETER-ACCESSS") is not None
        assert re_elem.find("SERVER-CALL-POINTS") is not None
        assert re_elem.find("ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS") is not None

    def test_writeRunnableEntity_none(self, writer):
        parent = _parent()
        writer.writeRunnableEntity(parent, None)
        assert len(parent) == 0

    def test_writeRunnableEntityModeAccessPoints_pmode(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        point = ModeAccessPoint()
        iref = PModeGroupInAtomicSwcInstanceRef()
        iref.setContextPPortRef(_ref("/pp"))
        iref.setTargetModeGroupRef(_ref("/mg"))
        point.setModeGroupIRef(iref)
        entity.addModeAccessPoint(point)
        parent = _parent()
        writer.writeRunnableEntityModeAccessPoints(parent, entity)
        assert parent.find("MODE-ACCESS-POINTS") is not None

    def test_writeRunnableEntityModeAccessPoints_rmode(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        point = ModeAccessPoint()
        iref = RModeGroupInAtomicSWCInstanceRef()
        iref.setContextRPortRef(_ref("/rp"))
        iref.setTargetModeGroupRef(_ref("/mg"))
        point.setModeGroupIRef(iref)
        entity.addModeAccessPoint(point)
        parent = _parent()
        writer.writeRunnableEntityModeAccessPoints(parent, entity)
        assert parent.find("MODE-ACCESS-POINTS") is not None

    def test_writeRunnableEntityModeAccessPoints_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        parent = _parent()
        writer.writeRunnableEntityModeAccessPoints(parent, entity)
        assert parent.find("MODE-ACCESS-POINTS") is None

    def test_writeRunnableEntityModeSwitchPoints(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        point = entity.createModeSwitchPoint("msp1")
        iref = PModeGroupInAtomicSwcInstanceRef()
        iref.setContextPPortRef(_ref("/pp"))
        iref.setTargetModeGroupRef(_ref("/mg"))
        point.setModeGroupIRef(iref)
        parent = _parent()
        writer.writeRunnableEntityModeSwitchPoints(parent, entity)
        pts = parent.find("MODE-SWITCH-POINTS")
        assert pts is not None
        assert pts[0].tag == "MODE-SWITCH-POINT"

    def test_writeRunnableEntityModeSwitchPoints_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        parent = _parent()
        writer.writeRunnableEntityModeSwitchPoints(parent, entity)
        assert parent.find("MODE-SWITCH-POINTS") is None

    def test_writeRunnableEntityServerCallPoints(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        sync = entity.createSynchronousServerCallPoint("sync1")
        rop = ROperationInAtomicSwcInstanceRef()
        rop.setContextRPortRef(_ref("/rp"))
        rop.setTargetRequiredOperationRef(_ref("/op"))
        sync.operationIRef = rop
        async_pt = entity.createAsynchronousServerCallPoint("async1")
        arop = ROperationInAtomicSwcInstanceRef()
        arop.setContextRPortRef(_ref("/rp2"))
        arop.setTargetRequiredOperationRef(_ref("/op2"))
        async_pt.operationIRef = arop
        parent = _parent()
        writer.writeRunnableEntityServerCallPoints(parent, entity)
        pts = parent.find("SERVER-CALL-POINTS")
        assert pts is not None
        tags = {c.tag for c in pts}
        assert "SYNCHRONOUS-SERVER-CALL-POINT" in tags
        assert "ASYNCHRONOUS-SERVER-CALL-POINT" in tags

    def test_writeRunnableEntityServerCallPoints_empty(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        parent = _parent()
        writer.writeRunnableEntityServerCallPoints(parent, entity)
        assert parent.find("SERVER-CALL-POINTS") is None

    def test_writeRunnableEntityArguments_invalid(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.addArgument(object())
        parent = _parent()
        with pytest.raises(NotImplementedError):
            writer.writeRunnableEntityArguments(parent, entity)

    def test_writeRunnableEntityDataReadAccesses(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createDataReadAccess("dr1")
        parent = _parent()
        writer.writeRunnableEntityDataReadAccesses(parent, entity)
        assert parent.find("DATA-READ-ACCESSS") is not None

    def test_writeRunnableEntityDataWriteAccesses(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createDataWriteAccess("dw1")
        parent = _parent()
        writer.writeRunnableEntityDataWriteAccesses(parent, entity)
        assert parent.find("DATA-WRITE-ACCESSS") is not None

    def test_writeRunnableEntityDataReceivePointByArguments(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createDataReceivePointByArgument("drp1")
        parent = _parent()
        writer.writeRunnableEntityDataReceivePointByArguments(parent, entity)
        assert parent.find("DATA-RECEIVE-POINT-BY-ARGUMENTS") is not None

    def test_writeRunnableEntityDataSendPoints(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createDataSendPoint("ds1")
        parent = _parent()
        writer.writeRunnableEntityDataSendPoints(parent, entity)
        assert parent.find("DATA-SEND-POINTS") is not None

    def test_writeRunnableEntityReadLocalVariables(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createReadLocalVariable("rl1")
        parent = _parent()
        writer.writeRunnableEntityReadLocalVariables(parent, entity)
        assert parent.find("READ-LOCAL-VARIABLES") is not None

    def test_writeRunnableEntityWrittenLocalVariable(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createWrittenLocalVariable("wl1")
        parent = _parent()
        writer.writeRunnableEntityWrittenLocalVariable(parent, entity)
        assert parent.find("WRITTEN-LOCAL-VARIABLES") is not None

    def test_writeRunnableEntityParameterAccesses(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createParameterAccess("pa1")
        parent = _parent()
        writer.writeRunnableEntityParameterAccesses(parent, entity)
        assert parent.find("PARAMETER-ACCESSS") is not None

    def test_writeRunnableEntityAsynchronousServerCallResultPoint(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        entity.createAsynchronousServerCallResultPoint("arp1")
        parent = _parent()
        writer.writeRunnableEntityAsynchronousServerCallResultPoint(parent, entity)
        assert parent.find("ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS") is not None


# ==================== SwcInternalBehavior collection writers ====================


class TestWriterSwcInternalBehaviorCollections:
    def test_writeSwcInternalBehaviorRunnables(self, writer):
        behavior = _make_behavior()
        behavior.createRunnableEntity("re1")
        parent = _parent()
        writer.writeSwcInternalBehaviorRunnables(parent, behavior)
        rs = parent.find("RUNNABLES")
        assert rs is not None
        assert rs[0].tag == "RUNNABLE-ENTITY"

    def test_writeSwcInternalBehaviorRunnables_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorRunnables(parent, behavior)
        assert parent.find("RUNNABLES") is None

    def test_writeSwcInternalBehaviorArTypedPerInstanceMemories(self, writer):
        behavior = _make_behavior()
        behavior.createArTypedPerInstanceMemory("ar1")
        parent = _parent()
        writer.writeSwcInternalBehaviorArTypedPerInstanceMemories(parent, behavior)
        m = parent.find("AR-TYPED-PER-INSTANCE-MEMORYS")
        assert m is not None
        assert m[0].tag == "VARIABLE-DATA-PROTOTYPE"

    def test_writeSwcInternalBehaviorArTypedPerInstanceMemories_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorArTypedPerInstanceMemories(parent, behavior)
        assert parent.find("AR-TYPED-PER-INSTANCE-MEMORYS") is None

    def test_writeSwcInternalBehaviorExplicitInterRunnableVariables(self, writer):
        behavior = _make_behavior()
        behavior.createExplicitInterRunnableVariable("eiv1")
        parent = _parent()
        writer.writeSwcInternalBehaviorExplicitInterRunnableVariables(parent, behavior)
        e = parent.find("EXPLICIT-INTER-RUNNABLE-VARIABLES")
        assert e is not None
        assert e[0].tag == "VARIABLE-DATA-PROTOTYPE"

    def test_writeSwcInternalBehaviorExplicitInterRunnableVariables_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorExplicitInterRunnableVariables(parent, behavior)
        assert parent.find("EXPLICIT-INTER-RUNNABLE-VARIABLES") is None

    def test_writeSwcInternalBehaviorPerInstanceMemories(self, writer):
        behavior = _make_behavior()
        mem = behavior.createPerInstanceMemory("pim1")
        mem.setInitValue(_literal("0"))
        mem.setType(_literal("uint8"))
        mem.setTypeDefinition(_literal("typedef"))
        parent = _parent()
        writer.writeSwcInternalBehaviorPerInstanceMemories(parent, behavior)
        m = parent.find("PER-INSTANCE-MEMORYS")
        assert m is not None
        assert m[0].tag == "PER-INSTANCE-MEMORY"
        assert m[0].find("INIT-VALUE").text == "0"
        assert m[0].find("TYPE").text == "uint8"

    def test_writeSwcInternalBehaviorPerInstanceMemories_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorPerInstanceMemories(parent, behavior)
        assert parent.find("PER-INSTANCE-MEMORYS") is None


# ==================== Parameter / PortAPIOption writers ====================


class TestWriterParameterAndPortApi:
    def test_writeParameterDataPrototype(self, writer):
        behavior = _make_behavior()
        proto = behavior.createPerInstanceParameter("pp1")
        parent = _parent()
        writer.writeParameterDataPrototype(parent, proto)
        assert parent[0].tag == "PARAMETER-DATA-PROTOTYPE"

    def test_writeSwcInternalBehaviorParameterDataPrototypes(self, writer):
        behavior = _make_behavior()
        behavior.createPerInstanceParameter("pp1")
        behavior.createPerInstanceParameter("pp2")
        parent = _parent()
        writer.writeSwcInternalBehaviorParameterDataPrototypes(
            parent, "PER-INSTANCE-PARAMETERS", behavior.getPerInstanceParameters()
        )
        assert parent[0].tag == "PER-INSTANCE-PARAMETERS"
        assert len(parent[0]) == 2

    def test_writeSwcInternalBehaviorParameterDataPrototypes_empty(self, writer):
        parent = _parent()
        writer.writeSwcInternalBehaviorParameterDataPrototypes(
            parent, "PER-INSTANCE-PARAMETERS", []
        )
        assert len(parent) == 0

    def test_writePortDefinedArgumentValues(self, writer):
        arg = PortDefinedArgumentValue()
        val = TextValueSpecification()
        val.setValue(_literal("v"))
        arg.setValue(val)
        arg.setValueTypeTRef(_ref("/vt", "DATA-TYPE"))
        parent = _parent()
        writer.writePortDefinedArgumentValues(parent, [arg])
        pav = parent.find("PORT-ARG-VALUES")
        assert pav is not None
        assert pav[0].tag == "PORT-DEFINED-ARGUMENT-VALUE"
        assert pav[0].find("VALUE") is not None
        assert pav[0].find("VALUE-TYPE-TREF") is not None

    def test_writePortDefinedArgumentValues_empty(self, writer):
        parent = _parent()
        writer.writePortDefinedArgumentValues(parent, [])
        assert len(parent) == 0

    def test_writeSwcInternalBehaviorPortAPIOptions(self, writer):
        behavior = _make_behavior()
        opt = PortAPIOption()
        opt.setEnableTakeAddress(_bool(True))
        opt.setErrorHandling(_literal("error"))
        opt.setIndirectAPI(_bool(False))
        opt.setPortRef(_ref("/port", "P-PORT-PROTOTYPE"))
        arg = PortDefinedArgumentValue()
        val = TextValueSpecification()
        val.setValue(_literal("v"))
        arg.setValue(val)
        opt.addPortArgValue(arg)
        behavior.addPortAPIOption(opt)
        parent = _parent()
        writer.writeSwcInternalBehaviorPortAPIOptions(parent, behavior)
        opts = parent.find("PORT-API-OPTIONS")
        assert opts is not None
        opt_elem = opts[0]
        assert opt_elem.find("ENABLE-TAKE-ADDRESS").text == "true"
        assert opt_elem.find("ERROR-HANDLING").text == "error"
        assert opt_elem.find("INDIRECT-API").text == "false"
        assert opt_elem.find("PORT-REF") is not None
        assert opt_elem.find("PORT-ARG-VALUES") is not None

    def test_writeSwcInternalBehaviorPortAPIOptions_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorPortAPIOptions(parent, behavior)
        assert parent.find("PORT-API-OPTIONS") is None


# ==================== Service Dependency writers ====================


class TestWriterServiceDependency:
    def test_writeRoleBasedDataTypeAssignment(self, writer):
        a = RoleBasedDataTypeAssignment()
        a.setRole(_literal("role1"))
        a.setUsedImplementationDataTypeRef(_ref("/idt", "IMPLEMENTATION-DATA-TYPE"))
        parent = _parent()
        writer.writeRoleBasedDataTypeAssignment(parent, a)
        elem = parent.find("ROLE-BASED-DATA-TYPE-ASSIGNMENT")
        assert elem is not None
        assert elem.find("ROLE").text == "role1"
        assert elem.find("USED-IMPLEMENTATION-DATA-TYPE-REF") is not None

    def test_writeServiceDependencyAssignedDataType(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        a = RoleBasedDataTypeAssignment()
        a.setRole(_literal("role1"))
        dep.addAssignedDataType(a)
        parent = _parent()
        writer.writeServiceDependencyAssignedDataType(parent, dep)
        adt = parent.find("ASSIGNED-DATA-TYPES")
        assert adt is not None
        assert adt[0].tag == "ROLE-BASED-DATA-TYPE-ASSIGNMENT"

    def test_writeServiceDependencyAssignedDataType_empty(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        parent = _parent()
        writer.writeServiceDependencyAssignedDataType(parent, dep)
        assert parent.find("ASSIGNED-DATA-TYPES") is None

    def test_writeServiceDependency(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        a = RoleBasedDataTypeAssignment()
        a.setRole(_literal("r1"))
        dep.addAssignedDataType(a)
        parent = _parent()
        writer.writeServiceDependency(parent, dep)
        assert parent.find("SHORT-NAME").text == "dep1"
        assert parent.find("ASSIGNED-DATA-TYPES") is not None

    def test_writeRoleBasedDataAssignment(self, writer):
        a = RoleBasedDataAssignment()
        a.setRole(_literal("r1"))
        vref = AutosarVariableRef()
        v_iref = VariableInAtomicSWCTypeInstanceRef()
        v_iref.setPortPrototypeRef(_ref("/pp"))
        vref.setAutosarVariableIRef(v_iref)
        a.setUsedDataElement(vref)
        pref = AutosarParameterRef()
        p_iref = ParameterInAtomicSWCTypeInstanceRef()
        p_iref.setPortPrototypeRef(_ref("/pp"))
        pref.setAutosarParameterIRef(p_iref)
        a.setUsedParameterElement(pref)
        a.setUsedPimRef(_ref("/pim"))
        parent = _parent()
        writer.writeRoleBasedDataAssignment(parent, a)
        elem = parent.find("ROLE-BASED-DATA-ASSIGNMENT")
        assert elem is not None
        assert elem.find("ROLE").text == "r1"
        assert elem.find("USED-DATA-ELEMENT") is not None
        assert elem.find("USED-PARAMETER-ELEMENT") is not None
        assert elem.find("USED-PIM-REF") is not None

    def test_writeRoleBasedPortAssignment(self, writer):
        a = RoleBasedPortAssignment()
        a.setPortPrototypeRef(_ref("/pp", "P-PORT-PROTOTYPE"))
        a.setRole(_literal("r1"))
        parent = _parent()
        writer.writeRoleBasedPortAssignment(parent, a)
        elem = parent.find("ROLE-BASED-PORT-ASSIGNMENT")
        assert elem is not None
        assert elem.find("PORT-PROTOTYPE-REF") is not None
        assert elem.find("ROLE").text == "r1"

    def test_writeSwcServiceDependencyAssignedData(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        a = RoleBasedDataAssignment()
        a.setRole(_literal("r1"))
        dep.AddAssignedData(a)
        parent = _parent()
        writer.writeSwcServiceDependencyAssignedData(parent, dep)
        ad = parent.find("ASSIGNED-DATAS")
        assert ad is not None
        assert ad[0].tag == "ROLE-BASED-DATA-ASSIGNMENT"

    def test_writeSwcServiceDependencyAssignedData_empty(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        parent = _parent()
        writer.writeSwcServiceDependencyAssignedData(parent, dep)
        assert parent.find("ASSIGNED-DATAS") is None

    def test_writeSwcServiceDependencyAssignedPorts(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        a = RoleBasedPortAssignment()
        a.setRole(_literal("r1"))
        dep.AddAssignedPort(a)
        parent = _parent()
        writer.writeSwcServiceDependencyAssignedPorts(parent, dep)
        ap = parent.find("ASSIGNED-PORTS")
        assert ap is not None
        assert ap[0].tag == "ROLE-BASED-PORT-ASSIGNMENT"

    def test_writeSwcServiceDependencyAssignedPorts_empty(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        parent = _parent()
        writer.writeSwcServiceDependencyAssignedPorts(parent, dep)
        assert parent.find("ASSIGNED-PORTS") is None

    def test_writeSwcServiceDependency(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        a = RoleBasedDataTypeAssignment()
        a.setRole(_literal("r1"))
        dep.addAssignedDataType(a)
        parent = _parent()
        writer.writeSwcServiceDependency(parent, dep)
        ssd = parent.find("SWC-SERVICE-DEPENDENCY")
        assert ssd is not None
        assert ssd.find("ASSIGNED-DATA-TYPES") is not None


# ==================== ServiceNeeds writers ====================


class TestWriterServiceNeeds:
    def test_writeServiceNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createEcuStateMgrUserNeeds("needs1")
        parent = _parent()
        writer.writeServiceNeeds(parent, needs)
        assert parent.find("SHORT-NAME").text == "needs1"

    def test_writeNvBlockNeeds_full(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createNvBlockNeeds("nv1")
        needs.setCalcRamBlockCrc(_bool(True))
        needs.setCheckStaticBlockId(_bool(False))
        needs.setNDataSets(_posint(2))
        needs.setNRomBlocks(_posint(3))
        needs.setRamBlockStatusControl(_literal("api"))
        needs.setReadonly(_bool(False))
        needs.setReliability(_literal("critical"))
        needs.setResistantToChangedSw(_bool(True))
        needs.setRestoreAtStart(_bool(False))
        needs.setStoreAtShutdown(_bool(True))
        needs.setStoreCyclic(_bool(False))
        needs.setStoreEmergency(_bool(True))
        needs.setStoreImmediate(_bool(False))
        needs.setUseAutoValidationAtShutDown(_bool(True))
        needs.setUseCRCCompMechanism(_bool(False))
        needs.setWriteOnlyOnce(_bool(True))
        needs.setWriteVerification(_bool(False))
        needs.setWritingFrequency(_posint(10))
        needs.setWritingPriority(_literal("high"))
        parent = _parent()
        writer.writeNvBlockNeeds(parent, needs)
        elem = parent.find("NV-BLOCK-NEEDS")
        assert elem is not None
        assert elem.find("CALC-RAM-BLOCK-CRC").text == "true"
        assert elem.find("CHECK-STATIC-BLOCK-ID").text == "false"
        assert elem.find("N-DATA-SETS").text == "2"
        assert elem.find("N-ROM-BLOCKS").text == "3"
        assert elem.find("RAM-BLOCK-STATUS-CONTROL").text == "api"
        assert elem.find("READONLY").text == "false"
        assert elem.find("RELIABILITY").text == "critical"
        assert elem.find("WRITING-FREQUENCY").text == "10"
        assert elem.find("WRITING-PRIORITY").text == "high"

    def test_writeDiagnosticCommunicationManagerNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDiagnosticCommunicationManagerNeeds("dcm1")
        needs.setServiceRequestCallbackType(_literal("requestCallbackTypeManufacturer"))
        parent = _parent()
        writer.writeDiagnosticCommunicationManagerNeeds(parent, needs)
        elem = parent.find("DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS")
        assert elem is not None
        assert elem.find("SERVICE-REQUEST-CALLBACK-TYPE") is not None

    def test_writeDiagnosticRoutineNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDiagnosticRoutineNeeds("drn1")
        needs.setDiagRoutineType(_literal("asynchronous"))
        needs.setRidNumber(_int("16"))
        parent = _parent()
        writer.writeDiagnosticRoutineNeeds(parent, needs)
        elem = parent.find("DIAGNOSTIC-ROUTINE-NEEDS")
        assert elem is not None
        assert elem.find("DIAG-ROUTINE-TYPE") is not None
        assert elem.find("RID-NUMBER").text == "16"

    def test_writeDiagnosticValueNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDiagnosticValueNeeds("dvn1")
        needs.setDataLength(_posint(8))
        needs.setDiagnosticValueAccess(_literal("read"))
        needs.setDidNumber(_int("32"))
        needs.setFixedLength(_bool(True))
        needs.setProcessingStyle(_literal("asynchronous"))
        parent = _parent()
        writer.writeDiagnosticValueNeeds(parent, needs)
        elem = parent.find("DIAGNOSTIC-VALUE-NEEDS")
        assert elem is not None
        assert elem.find("DATA-LENGTH").text == "8"
        assert elem.find("DIAGNOSTIC-VALUE-ACCESS").text == "read"
        assert elem.find("DID-NUMBER").text == "32"
        assert elem.find("FIXED-LENGTH").text == "true"
        assert elem.find("PROCESSING-STYLE").text == "asynchronous"

    def test_writeDiagnosticEventNeeds_with_algorithm(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDiagnosticEventNeeds("den1")
        algo = DiagEventDebounceMonitorInternal(behavior, "deb1")
        needs.diagEventDebounceAlgorithm = algo
        needs.setDtcKind(_literal("UDS_DTC"))
        needs.setUdsDtcNumber(_int("48"))
        parent = _parent()
        writer.writeDiagnosticEventNeeds(parent, needs)
        elem = parent.find("DIAGNOSTIC-EVENT-NEEDS")
        assert elem is not None
        algo_elem = elem.find("DIAG-EVENT-DEBOUNCE-ALGORITHM")
        assert algo_elem is not None
        assert algo_elem.find("DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL") is not None
        assert elem.find("DTC-KIND").text == "UDS_DTC"
        assert elem.find("UDS-DTC-NUMBER").text == "48"

    def test_writeDiagnosticEventNeeds_no_algorithm(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDiagnosticEventNeeds("den1")
        parent = _parent()
        writer.writeDiagnosticEventNeeds(parent, needs)
        elem = parent.find("DIAGNOSTIC-EVENT-NEEDS")
        assert elem is not None
        assert elem.find("DIAG-EVENT-DEBOUNCE-ALGORITHM") is None

    def test_writeDiagnosticEventInfoNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDiagnosticEventInfoNeeds("dei1")
        needs.setDtcKind(_literal("UDS_DTC"))
        needs.setUdsDtcNumber(_posint("64"))
        parent = _parent()
        writer.writeDiagnosticEventInfoNeeds(parent, needs)
        elem = parent.find("DIAGNOSTIC-EVENT-INFO-NEEDS")
        assert elem is not None
        assert elem.find("DTC-KIND").text == "UDS_DTC"
        assert elem.find("UDS-DTC-NUMBER").text == "64"

    def test_writeCryptoServiceNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createCryptoServiceNeeds("csn1")
        needs.setMaximumKeyLength(_posint("128"))
        parent = _parent()
        writer.writeCryptoServiceNeeds(parent, needs)
        elem = parent.find("CRYPTO-SERVICE-NEEDS")
        assert elem is not None
        assert elem.find("MAXIMUM-KEY-LENGTH").text == "128"

    def test_writeEcuStateMgrUserNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createEcuStateMgrUserNeeds("esm1")
        parent = _parent()
        writer.writeEcuStateMgrUserNeeds(parent, needs)
        elem = parent.find("ECU-STATE-MGR-USER-NEEDS")
        assert elem is not None

    def test_writeDtcStatusChangeNotificationNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDtcStatusChangeNotificationNeeds("dsc1")
        needs.setDtcFormatType(_literal("UDS"))
        parent = _parent()
        writer.writeDtcStatusChangeNotificationNeeds(parent, needs)
        elem = parent.find("DTC-STATUS-CHANGE-NOTIFICATION-NEEDS")
        assert elem is not None
        assert elem.find("DTC-FORMAT-TYPE") is not None

    def test_writeDltUserNeeds(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        needs = dep.createDltUserNeeds("dlt1")
        parent = _parent()
        writer.writeDltUserNeeds(parent, needs)
        elem = parent.find("DLT-USER-NEEDS")
        assert elem is not None


class TestWriterSwcServiceDependencyServiceNeeds:
    def test_dispatch_all_needs_types(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        dep.createNvBlockNeeds("nv")
        dep.createDiagnosticCommunicationManagerNeeds("dcm")
        dep.createDiagnosticRoutineNeeds("drn")
        dep.createDiagnosticValueNeeds("dvn")
        dep.createDiagnosticEventNeeds("den")
        dep.createDiagnosticEventInfoNeeds("dei")
        dep.createCryptoServiceNeeds("csn")
        dep.createEcuStateMgrUserNeeds("esm")
        dep.createDtcStatusChangeNotificationNeeds("dsc")
        dep.createDltUserNeeds("dlt")
        parent = _parent()
        writer.writeSwcServiceDependencyServiceNeeds(parent, dep)
        needs_tag = parent.find("SERVICE-NEEDS")
        assert needs_tag is not None
        tags = {c.tag for c in needs_tag}
        assert "NV-BLOCK-NEEDS" in tags
        assert "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS" in tags
        assert "DIAGNOSTIC-ROUTINE-NEEDS" in tags
        assert "DIAGNOSTIC-VALUE-NEEDS" in tags
        assert "DIAGNOSTIC-EVENT-NEEDS" in tags
        assert "DIAGNOSTIC-EVENT-INFO-NEEDS" in tags
        assert "CRYPTO-SERVICE-NEEDS" in tags
        assert "ECU-STATE-MGR-USER-NEEDS" in tags
        assert "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS" in tags
        assert "DLT-USER-NEEDS" in tags

    def test_no_needs_no_tag(self, writer):
        behavior = _make_behavior()
        dep = behavior.createSwcServiceDependency("dep1")
        parent = _parent()
        writer.writeSwcServiceDependencyServiceNeeds(parent, dep)
        assert parent.find("SERVICE-NEEDS") is None


# ==================== SwcInternalBehavior hub & helpers ====================


class TestWriterSwcInternalBehaviorHub:
    def test_writeSwcInternalBehavior_minimal(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehavior(parent, behavior)
        elem = parent.find("SWC-INTERNAL-BEHAVIOR")
        assert elem is not None
        assert elem.find("SHORT-NAME").text == "Behavior"

    def test_writeSwcInternalBehavior_full(self, writer):
        behavior = _make_behavior()
        behavior.setHandleTerminationAndRestart(_literal("KEEP-UNLESS-RESTARTED"))
        behavior.setSupportsMultipleInstantiation(_bool(True))
        behavior.createArTypedPerInstanceMemory("ar1")
        behavior.createTimingEvent("te")
        behavior.createExplicitInterRunnableVariable("eiv1")
        behavior.createPerInstanceMemory("pim1")
        behavior.createPerInstanceParameter("pp1")
        behavior.createSharedParameter("sp1")
        behavior.createRunnableEntity("re1")
        dep = behavior.createSwcServiceDependency("dep1")
        dep.createNvBlockNeeds("nv1")
        dt_set = IncludedDataTypeSet()
        dt_set.addDataTypeRef(_ref("/dt1", "DATA-TYPE"))
        behavior.addIncludedDataTypeSet(dt_set)
        mset = IncludedModeDeclarationGroupSet()
        mset.addModeDeclarationGroupRef(_ref("/mdg1", "MODE-DECLARATION-GROUP"))
        mset.setPrefix(_literal("p_"))
        behavior.addIncludedModeDeclarationGroupSet(mset)
        opt = PortAPIOption()
        opt.setEnableTakeAddress(_bool(True))
        behavior.addPortAPIOption(opt)
        parent = _parent()
        writer.writeSwcInternalBehavior(parent, behavior)
        elem = parent.find("SWC-INTERNAL-BEHAVIOR")
        assert elem is not None
        htr = elem.find("HANDLE-TERMINATION-AND-RESTART")
        assert htr.text == "KEEP-UNLESS-RESTARTED"
        smi = elem.find("SUPPORTS-MULTIPLE-INSTANTIATION")
        assert smi.text == "true"
        assert elem.find("AR-TYPED-PER-INSTANCE-MEMORYS") is not None
        assert elem.find("EVENTS") is not None
        assert elem.find("EXPLICIT-INTER-RUNNABLE-VARIABLES") is not None
        assert elem.find("INCLUDED-DATA-TYPE-SETS") is not None
        assert elem.find("INCLUDED-MODE-DECLARATION-GROUP-SETS") is not None
        assert elem.find("PER-INSTANCE-MEMORYS") is not None
        assert elem.find("PER-INSTANCE-PARAMETERS") is not None
        assert elem.find("PORT-API-OPTIONS") is not None
        assert elem.find("RUNNABLES") is not None
        assert elem.find("SERVICE-DEPENDENCYS") is not None
        assert elem.find("SHARED-PARAMETERS") is not None

    def test_writeAtomicSwComponentTypeInternalBehaviors_swc(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeAtomicSwComponentTypeInternalBehaviors(parent, behavior)
        assert parent.find("INTERNAL-BEHAVIORS") is not None
        assert parent[0][0].tag == "SWC-INTERNAL-BEHAVIOR"

    def test_writeAtomicSwComponentTypeInternalBehaviors_none(self, writer):
        parent = _parent()
        writer.writeAtomicSwComponentTypeInternalBehaviors(parent, None)
        assert len(parent) == 0


class TestWriterIncludedModeDeclarationGroupSet:
    def test_writeIncludedModeDeclarationGroupSet(self, writer):
        mset = IncludedModeDeclarationGroupSet()
        mset.addModeDeclarationGroupRef(_ref("/mdg1", "MODE-DECLARATION-GROUP"))
        mset.setPrefix(_literal("p_"))
        parent = _parent()
        writer.writeIncludedModeDeclarationGroupSet(parent, mset)
        elem = parent.find("INCLUDED-MODE-DECLARATION-GROUP-SET")
        assert elem is not None
        assert elem.find("MODE-DECLARATION-GROUP-REFS") is not None
        assert elem.find("PREFIX").text == "p_"

    def test_writeIncludedModeDeclarationGroupSet_none(self, writer):
        parent = _parent()
        writer.writeIncludedModeDeclarationGroupSet(parent, None)
        assert len(parent) == 0

    def test_writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(self, writer):
        behavior = _make_behavior()
        mset = IncludedModeDeclarationGroupSet()
        mset.addModeDeclarationGroupRef(_ref("/mdg1", "MODE-DECLARATION-GROUP"))
        behavior.addIncludedModeDeclarationGroupSet(mset)
        parent = _parent()
        writer.writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(parent, behavior)
        elem = parent.find("INCLUDED-MODE-DECLARATION-GROUP-SETS")
        assert elem is not None
        assert elem[0].tag == "INCLUDED-MODE-DECLARATION-GROUP-SET"

    def test_writeSwcInternalBehaviorIncludedModeDeclarationGroupSets_empty(self, writer):
        behavior = _make_behavior()
        parent = _parent()
        writer.writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(parent, behavior)
        assert parent.find("INCLUDED-MODE-DECLARATION-GROUP-SETS") is None


class TestWriterSetIncludedDataTypeSets:
    def test_setIncludedDataTypeSets(self, writer):
        dt_set = IncludedDataTypeSet()
        dt_set.addDataTypeRef(_ref("/dt1", "DATA-TYPE"))
        dt_set.addDataTypeRef(_ref("/dt2", "DATA-TYPE"))
        parent = _parent()
        writer.setIncludedDataTypeSets(parent, [dt_set])
        elem = parent.find("INCLUDED-DATA-TYPE-SETS")
        assert elem is not None
        assert elem[0].tag == "INCLUDED-DATA-TYPE-SET"
        refs = elem[0].find("DATA-TYPE-REFS")
        assert refs is not None
        assert len(refs) == 2

    def test_setIncludedDataTypeSets_empty(self, writer):
        parent = _parent()
        writer.setIncludedDataTypeSets(parent, [])
        assert parent.find("INCLUDED-DATA-TYPE-SETS") is None


class TestWriterModeAccessPointHelpers:
    def test_writeModeAccessPoint(self, writer):
        point = ModeAccessPoint()
        iref = PModeGroupInAtomicSwcInstanceRef()
        iref.setContextPPortRef(_ref("/pp"))
        iref.setTargetModeGroupRef(_ref("/mg"))
        point.setModeGroupIRef(iref)
        parent = _parent()
        writer.writeModeAccessPoint(parent, point)
        assert parent.find("MODE-ACCESS-POINT") is not None

    def test_writeModeAccessPoint_none(self, writer):
        parent = _parent()
        writer.writeModeAccessPoint(parent, None)
        assert len(parent) == 0

    def test_writeModeSwitchPoint(self, writer):
        behavior = _make_behavior()
        entity = behavior.createRunnableEntity("re1")
        point = entity.createModeSwitchPoint("msp1")
        iref = PModeGroupInAtomicSwcInstanceRef()
        iref.setContextPPortRef(_ref("/pp"))
        iref.setTargetModeGroupRef(_ref("/mg"))
        point.setModeGroupIRef(iref)
        parent = _parent()
        writer.writeModeSwitchPoint(parent, point)
        assert parent.find("MODE-SWITCH-POINT") is not None

    def test_writeModeSwitchPoint_none(self, writer):
        parent = _parent()
        writer.writeModeSwitchPoint(parent, None)
        assert len(parent) == 0


class TestWriterComponentInSystemInstanceRef:
    def test_setComponentInSystemInstanceRef(self, writer):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef  # noqa E501
        ref = ComponentInSystemInstanceRef()
        ref.setBaseRef(_ref("/base"))
        ref.setContextCompositionRef(_ref("/cc"))
        ref.setTargetComponentRef(_ref("/tc"))
        parent = _parent()
        writer.setComponentInSystemInstanceRef(parent, "CONTEXT-COMPONENT-IREF", ref)
        elem = parent.find("CONTEXT-COMPONENT-IREF")
        assert elem is not None
        assert elem.find("BASE-REF") is not None
        assert elem.find("CONTEXT-COMPOSITION-REF") is not None
        assert elem.find("TARGET-COMPONENT-REF") is not None

    def test_setComponentInSystemInstanceRef_none(self, writer):
        parent = _parent()
        writer.setComponentInSystemInstanceRef(parent, "CONTEXT-COMPONENT-IREF", None)
        assert len(parent) == 0
