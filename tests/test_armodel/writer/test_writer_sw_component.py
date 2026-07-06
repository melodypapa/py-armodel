"""Tests for writer SW component and communication handlers."""
import xml.etree.cElementTree as ET
import pytest
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec, CompositeNetworkRepresentation, ModeSwitchedAckRequest,
    ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec, NonqueuedSenderComSpec, NvProvideComSpec,
    NvRequireComSpec, PPortComSpec, ParameterRequireComSpec,
    QueuedReceiverComSpec, QueuedSenderComSpec, RPortComSpec, ServerComSpec,
    TransmissionAcknowledgementRequest, UserDefinedTransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PortGroup, PPortPrototype, PRPortPrototype, RPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector, CompositionSwComponentType, DelegationSwConnector,
    PassThroughSwConnector, SwComponentPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (  # noqa: E501
    PPortInCompositionInstanceRef, PortInCompositionTypeInstanceRef,
    RPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (  # noqa: E501
    InnerPortGroupInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (  # noqa: E501
    ApplicationCompositeElementInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ApplicationValueSpecification, ArrayValueSpecification,
    ConstantReference, NumericalValueSpecification,
    RecordValueSpecification, TextValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import (
    SwValueCont, SwValues,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps, ValueList,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    SwCalprmAxisSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARBoolean, ARFloat, ARLiteral, ARPositiveInteger, ARNumerical,
    PositiveInteger, RefType, TRefType, TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    TransformationComSpecProps,
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


def _ref(value="/Pkg/Elem", dest="VARIABLE-DATA-PROTOTYPE"):
    r = RefType()
    r.setValue(value)
    r.setDest(dest)
    return r


def _literal(text="val"):
    lit = ARLiteral()
    lit.setValue(text)
    return lit


def _boolean(val=True):
    b = ARBoolean()
    b.setValue(val)
    return b


def _positive_int(val=1):
    i = ARPositiveInteger()
    i.setValue(val)
    return i


def _time_value(val=1.0):
    t = TimeValue()
    t.setValue(val)
    return t


def _numerical(val=1):
    n = ARNumerical()
    n.setValue(val)
    return n


def _float(val=1.5):
    f = ARFloat()
    f.setValue(val)
    return f


class _FakeTransformationComSpecProps(TransformationComSpecProps):
    def __init__(self):
        super().__init__()


class _FakePPortComSpec(PPortComSpec):
    def __init__(self):
        super().__init__()


class _FakeRPortComSpec(RPortComSpec):
    def __init__(self):
        super().__init__()


class _FakePortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    def __init__(self):
        super().__init__()


class TestWriteTransmissionAcknowledgement:
    def test_none_acknowledge(self, writer):
        parent = _parent()
        writer.writeTransmissionAcknowledgementRequest(
            parent, None)
        assert len(parent) == 0

    def test_acknowledge_without_timeout(self, writer):
        parent = _parent()
        ack = TransmissionAcknowledgementRequest()
        writer.writeTransmissionAcknowledgementRequest(parent, ack)
        assert len(parent) == 1
        assert parent[0].tag == "TRANSMISSION-ACKNOWLEDGE"
        assert parent[0].find("TIMEOUT") is None

    def test_acknowledge_with_timeout(self, writer):
        parent = _parent()
        ack = TransmissionAcknowledgementRequest()
        ack.setTimeout(_time_value(2.5))
        writer.writeTransmissionAcknowledgementRequest(parent, ack)
        assert parent[0].tag == "TRANSMISSION-ACKNOWLEDGE"
        timeout = parent[0].find("TIMEOUT")
        assert timeout is not None


class TestWriteSenderComSpec:
    def test_write_sender_comspec_with_options(self, writer):
        com_spec = NonqueuedSenderComSpec()
        com_spec.setDataElementRef(_ref())
        props = SwDataDefProps()
        props.setSwCalprmAxisSet(SwCalprmAxisSet())
        com_spec.setNetworkRepresentation(props)
        com_spec.setHandleOutOfRange(_literal("keep"))
        com_spec.setTransmissionAcknowledge(
            TransmissionAcknowledgementRequest())
        com_spec.setUsesEndToEndProtection(_boolean(False))
        parent = _parent()
        writer.writeSenderComSpec(parent, com_spec)
        assert parent.find("DATA-ELEMENT-REF") is not None
        assert parent.find("NETWORK-REPRESENTATION") is not None
        assert parent.find("HANDLE-OUT-OF-RANGE") is not None
        assert parent.find("TRANSMISSION-ACKNOWLEDGE") is not None
        assert parent.find("USES-END-TO-END-PROTECTION") is not None

    def test_write_sender_comspec_with_composite_repr(self, writer):
        com_spec = NonqueuedSenderComSpec()
        repr = CompositeNetworkRepresentation()
        com_spec.addCompositeNetworkRepresentation(repr)
        parent = _parent()
        writer.writeSenderComSpec(parent, com_spec)
        assert parent.find("COMPOSITE-NETWORK-REPRESENTATIONS") is not None

    def test_write_nonqueued_sender_comspec(self, writer):
        com_spec = NonqueuedSenderComSpec()
        com_spec.setDataElementRef(_ref())
        com_spec.setInitValue(TextValueSpecification())
        parent = _parent()
        writer.writeNonqueuedSenderComSpec(parent, com_spec)
        assert parent[0].tag == "NONQUEUED-SENDER-COM-SPEC"
        assert parent[0].find("INIT-VALUE") is not None

    def test_write_queued_sender_comspec(self, writer):
        com_spec = QueuedSenderComSpec()
        com_spec.setDataElementRef(_ref())
        parent = _parent()
        writer.writeQueuedSenderComSpec(parent, com_spec)
        assert parent[0].tag == "QUEUED-SENDER-COM-SPEC"


class TestWriteTransformationComSpec:
    def test_write_transformation_comspec_props_none(self, writer):
        parent = _parent()
        writer.writeTransformationComSpecProps(parent, None)
        assert len(parent) == 0

    def test_write_transformation_comspec_props(self, writer):
        parent = _parent()
        prop = UserDefinedTransformationComSpecProps()
        writer.writeTransformationComSpecProps(parent, prop)
        assert len(parent) == 0

    def test_write_user_defined_transformation_props_none(self, writer):
        parent = _parent()
        writer.writeUserDefinedTransformationComSpecProps(parent, None)
        assert len(parent) == 0

    def test_write_user_defined_transformation_props(self, writer):
        parent = _parent()
        prop = UserDefinedTransformationComSpecProps()
        writer.writeUserDefinedTransformationComSpecProps(parent, prop)
        assert len(parent) == 1
        assert parent[0].tag == (
            "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS")

    def test_write_server_comspec_transformation_props_empty(
            self, writer):
        parent = _parent()
        com_spec = ServerComSpec()
        writer.writeServerComSpecTransformationComSpecProps(
            parent, com_spec)
        assert len(parent) == 0

    def test_write_server_comspec_transformation_props(self, writer):
        parent = _parent()
        com_spec = ServerComSpec()
        com_spec.addTransformationComSpecProps(
            UserDefinedTransformationComSpecProps())
        writer.writeServerComSpecTransformationComSpecProps(
            parent, com_spec)
        assert parent[0].tag == "TRANSFORMATION-COM-SPEC-PROPSS"


class TestWriteServerComSpec:
    def test_write_server_comspec(self, writer):
        com_spec = ServerComSpec()
        com_spec.setOperationRef(_ref(dest="CLIENT-SERVER-OPERATION"))
        com_spec.setQueueLength(_positive_int(3))
        com_spec.addTransformationComSpecProps(
            UserDefinedTransformationComSpecProps())
        parent = _parent()
        writer.writeServerComSpec(parent, com_spec)
        assert parent[0].tag == "SERVER-COM-SPEC"
        assert parent[0].find("OPERATION-REF") is not None
        assert parent[0].find("QUEUE-LENGTH") is not None
        assert parent[0].find("TRANSFORMATION-COM-SPEC-PROPSS") is not None


class TestWriteModeSwitchSenderComSpec:
    def test_set_mode_switched_ack_none(self, writer):
        parent = _parent()
        writer.setModeSwitchedAckRequest(parent, "MODE-SWITCHED-ACK", None)
        assert len(parent) == 0

    def test_set_mode_switched_ack(self, writer):
        parent = _parent()
        req = ModeSwitchedAckRequest()
        req.setTimeout(_time_value(1.0))
        writer.setModeSwitchedAckRequest(parent, "MODE-SWITCHED-ACK", req)
        assert len(parent) == 1
        assert parent[0].tag == "MODE-SWITCHED-ACK"
        assert parent[0].find("TIMEOUT") is not None

    def test_write_mode_switch_sender_comspec(self, writer):
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setModeGroupRef(_ref(dest="MODE-DECLARATION-GROUP"))
        com_spec.setModeSwitchedAck(ModeSwitchedAckRequest())
        com_spec.setQueueLength(_positive_int(2))
        parent = _parent()
        writer.writeModeSwitchSenderComSpec(parent, com_spec)
        assert parent[0].tag == "MODE-SWITCH-SENDER-COM-SPEC"
        assert parent[0].find("MODE-GROUP-REF") is not None
        assert parent[0].find("MODE-SWITCHED-ACK") is not None
        assert parent[0].find("QUEUE-LENGTH") is not None


class TestWriteNvProvideComSpec:
    def test_none(self, writer):
        parent = _parent()
        writer.writeNvProvideComSpec(parent, None)
        assert len(parent) == 0

    def test_with_options(self, writer):
        com_spec = NvProvideComSpec()
        com_spec.setRamBlockInitValue(TextValueSpecification())
        com_spec.setRomBlockInitValue(NumericalValueSpecification())
        com_spec.setVariableRef(_ref())
        parent = _parent()
        writer.writeNvProvideComSpec(parent, com_spec)
        assert parent[0].tag == "NV-PROVIDE-COM-SPEC"
        assert parent[0].find("RAM-BLOCK-INIT-VALUE") is not None
        assert parent[0].find("ROM-BLOCK-INIT-VALUE") is not None
        assert parent[0].find("VARIABLE-REF") is not None


class TestWritePPortComSpec:
    def _pkg_app(self):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        return pkg.createApplicationSwComponentType("App")

    def test_dispatches_nonqueued_sender(self, writer):
        com_spec = NonqueuedSenderComSpec()
        com_spec.setDataElementRef(_ref())
        parent = _parent()
        writer.writePPortComSpec(parent, com_spec)
        assert parent.find("NONQUEUED-SENDER-COM-SPEC") is not None

    def test_dispatches_server(self, writer):
        com_spec = ServerComSpec()
        parent = _parent()
        writer.writePPortComSpec(parent, com_spec)
        assert parent.find("SERVER-COM-SPEC") is not None

    def test_dispatches_queued_sender(self, writer):
        com_spec = QueuedSenderComSpec()
        com_spec.setDataElementRef(_ref())
        parent = _parent()
        writer.writePPortComSpec(parent, com_spec)
        assert parent.find("QUEUED-SENDER-COM-SPEC") is not None

    def test_dispatches_mode_switch_sender(self, writer):
        com_spec = ModeSwitchSenderComSpec()
        parent = _parent()
        writer.writePPortComSpec(parent, com_spec)
        assert parent.find("MODE-SWITCH-SENDER-COM-SPEC") is not None

    def test_dispatches_nv_provide(self, writer):
        com_spec = NvProvideComSpec()
        parent = _parent()
        writer.writePPortComSpec(parent, com_spec)
        assert parent.find("NV-PROVIDE-COM-SPEC") is not None


class TestWriteCompositeNetworkRepresentation:
    def test_none(self, writer):
        parent = _parent()
        writer.writeCompositeNetworkRepresentation(parent, None)
        assert len(parent) == 0

    def test_with_representation(self, writer):
        repr = CompositeNetworkRepresentation()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        iref.root_data_prototype_ref = _ref()
        iref.target_data_prototype_ref = _ref()
        repr.setLeafElementIRef(iref)
        props = SwDataDefProps()
        props.setSwCalprmAxisSet(SwCalprmAxisSet())
        repr.setNetworkRepresentation(props)
        parent = _parent()
        writer.writeCompositeNetworkRepresentation(parent, repr)
        assert parent[0].tag == "COMPOSITE-NETWORK-REPRESENTATION"
        assert parent[0].find("LEAF-ELEMENT-IREF") is not None
        assert parent[0].find("NETWORK-REPRESENTATION") is not None

    def test_set_app_composite_iref_none(self, writer):
        parent = _parent()
        writer.setApplicationCompositeElementInPortInterfaceInstanceRef(
            parent, "LEAF-ELEMENT-IREF", None)
        assert len(parent) == 0

    def test_set_app_composite_iref(self, writer):
        parent = _parent()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        iref.root_data_prototype_ref = _ref()
        iref.target_data_prototype_ref = _ref()
        writer.setApplicationCompositeElementInPortInterfaceInstanceRef(
            parent, "LEAF-ELEMENT-IREF", iref)
        assert parent[0].tag == "LEAF-ELEMENT-IREF"
        assert parent[0].find("ROOT-DATA-PROTOTYPE-REF") is not None
        assert parent[0].find("TARGET-DATA-PROTOTYPE-REF") is not None


class TestWriteReceiverComSpec:
    def test_write_receiver_comspec_with_options(self, writer):
        com_spec = NonqueuedReceiverComSpec()
        com_spec.setDataElementRef(_ref())
        props = SwDataDefProps()
        props.setSwCalprmAxisSet(SwCalprmAxisSet())
        com_spec.setNetworkRepresentation(props)
        com_spec.setHandleOutOfRange(_literal("keep"))
        com_spec.setHandleOutOfRangeStatus(_literal("set-status"))
        com_spec.setMaxDeltaCounterInit(_positive_int(1))
        com_spec.setMaxNoNewOrRepeatedData(_positive_int(2))
        com_spec.setUsesEndToEndProtection(_boolean(True))
        parent = _parent()
        writer.writeReceiverComSpec(parent, com_spec)
        assert parent.find("DATA-ELEMENT-REF") is not None
        assert parent.find("NETWORK-REPRESENTATION") is not None
        assert parent.find("HANDLE-OUT-OF-RANGE") is not None
        assert parent.find("HANDLE-OUT-OF-RANGE-STATUS") is not None
        assert parent.find("MAX-DELTA-COUNTER-INIT") is not None
        assert parent.find("MAX-NO-NEW-OR-REPEATED-DATA") is not None
        assert parent.find("USES-END-TO-END-PROTECTION") is not None

    def test_write_receiver_comspec_with_composite_repr(self, writer):
        com_spec = NonqueuedReceiverComSpec()
        com_spec.addCompositeNetworkRepresentation(
            CompositeNetworkRepresentation())
        parent = _parent()
        writer.writeReceiverComSpec(parent, com_spec)
        assert parent.find("COMPOSITE-NETWORK-REPRESENTATIONS") is not None

    def test_write_nonqueued_receiver_comspec(self, writer):
        com_spec = NonqueuedReceiverComSpec()
        com_spec.setDataElementRef(_ref())
        com_spec.setAliveTimeout(_time_value(0.5))
        com_spec.setEnableUpdated(_boolean(True))
        com_spec.setFilter(DataFilter())
        com_spec.setHandleNeverReceived(_boolean(False))
        com_spec.setHandleTimeoutType(_literal("keep-old-value"))
        com_spec.setInitValue(TextValueSpecification())
        parent = _parent()
        writer.writeNonqueuedReceiverComSpec(parent, com_spec)
        assert parent[0].tag == "NONQUEUED-RECEIVER-COM-SPEC"
        assert parent[0].find("ALIVE-TIMEOUT") is not None
        assert parent[0].find("ENABLE-UPDATE") is not None
        assert parent[0].find("FILTER") is not None
        assert parent[0].find("HANDLE-NEVER-RECEIVED") is not None
        assert parent[0].find("HANDLE-TIMEOUT-TYPE") is not None
        assert parent[0].find("INIT-VALUE") is not None

    def test_write_queued_receiver_comspec(self, writer):
        com_spec = QueuedReceiverComSpec()
        com_spec.setDataElementRef(_ref())
        com_spec.queueLength = _positive_int(5)
        parent = _parent()
        writer.writeQueuedReceiverComSpec(parent, com_spec)
        assert parent[0].tag == "QUEUED-RECEIVER-COM-SPEC"
        assert parent[0].find("QUEUE-LENGTH") is not None


class TestWriteClientParameterNvComSpec:
    def test_write_client_comspec(self, writer):
        com_spec = ClientComSpec()
        com_spec.setOperationRef(_ref(dest="CLIENT-SERVER-OPERATION"))
        parent = _parent()
        writer.writeClientComSpec(parent, com_spec)
        assert parent[0].tag == "CLIENT-COM-SPEC"
        assert parent[0].find("OPERATION-REF") is not None

    def test_write_parameter_require_comspec(self, writer):
        com_spec = ParameterRequireComSpec()
        com_spec.setInitValue(TextValueSpecification())
        com_spec.setParameterRef(
            _ref(dest="PARAMETER-DATA-PROTOTYPE"))
        parent = _parent()
        writer.writeParameterRequireComSpec(parent, com_spec)
        assert parent[0].tag == "PARAMETER-REQUIRE-COM-SPEC"
        assert parent[0].find("INIT-VALUE") is not None
        assert parent[0].find("PARAMETER-REF") is not None

    def test_write_nv_require_comspec(self, writer):
        com_spec = NvRequireComSpec()
        com_spec.setInitValue(TextValueSpecification())
        com_spec.setVariableRef(_ref())
        parent = _parent()
        writer.writeNvRequireComSpec(parent, com_spec)
        assert parent[0].tag == "NV-REQUIRE-COM-SPEC"
        assert parent[0].find("INIT-VALUE") is not None
        assert parent[0].find("VARIABLE-REF") is not None


class TestWriteModeSwitchReceiverComSpec:
    def test_write_mode_switch_receiver_comspec(self, writer):
        com_spec = ModeSwitchReceiverComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref(dest="MODE-DECLARATION-GROUP"))
        com_spec.setSupportsAsynchronousModeSwitch(_boolean(False))
        parent = _parent()
        writer.setModeSwitchReceiverComSpec(parent, com_spec)
        assert parent[0].tag == "MODE-SWITCH-RECEIVER-COM-SPEC"
        assert parent[0].find("ENHANCED-MODE-API") is not None
        assert parent[0].find("MODE-GROUP-REF") is not None
        assert parent[0].find(
            "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH") is not None


class TestWriteRPortComSpec:
    def test_dispatches_nonqueued_receiver(self, writer):
        com_spec = NonqueuedReceiverComSpec()
        com_spec.handleTimeoutType = None
        parent = _parent()
        writer.writeRPortComSpec(parent, com_spec)
        assert parent.find("NONQUEUED-RECEIVER-COM-SPEC") is not None

    def test_dispatches_queued_receiver(self, writer):
        com_spec = QueuedReceiverComSpec()
        parent = _parent()
        writer.writeRPortComSpec(parent, com_spec)
        assert parent.find("QUEUED-RECEIVER-COM-SPEC") is not None

    def test_dispatches_client(self, writer):
        com_spec = ClientComSpec()
        parent = _parent()
        writer.writeRPortComSpec(parent, com_spec)
        assert parent.find("CLIENT-COM-SPEC") is not None

    def test_dispatches_mode_switch_receiver(self, writer):
        com_spec = ModeSwitchReceiverComSpec()
        parent = _parent()
        writer.writeRPortComSpec(parent, com_spec)
        assert parent.find("MODE-SWITCH-RECEIVER-COM-SPEC") is not None

    def test_dispatches_parameter_require(self, writer):
        com_spec = ParameterRequireComSpec()
        parent = _parent()
        writer.writeRPortComSpec(parent, com_spec)
        assert parent.find("PARAMETER-REQUIRE-COM-SPEC") is not None

    def test_dispatches_nv_require(self, writer):
        com_spec = NvRequireComSpec()
        parent = _parent()
        writer.writeRPortComSpec(parent, com_spec)
        assert parent.find("NV-REQUIRE-COM-SPEC") is not None


class TestWritePortPrototypes:
    def _app(self):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        return pkg.createApplicationSwComponentType("App")

    def test_write_p_port_prototype(self, writer):
        app = self._app()
        port = app.createPPortPrototype("PPort")
        tref = TRefType()
        tref.setValue("/If/SR")
        port.setProvidedInterfaceTRef(tref)
        parent = _parent()
        writer.writePPortPrototype(parent, port)
        assert parent[0].tag == "P-PORT-PROTOTYPE"
        assert parent[0].find("SHORT-NAME") is not None
        assert parent[0].find("PROVIDED-INTERFACE-TREF") is not None

    def test_write_p_port_prototype_with_comspec(self, writer):
        app = self._app()
        port = app.createPPortPrototype("PPort")
        com_spec = NonqueuedSenderComSpec()
        com_spec.setDataElementRef(_ref())
        port.addProvidedComSpec(com_spec)
        parent = _parent()
        writer.writePPortPrototype(parent, port)
        assert parent[0].find("PROVIDED-COM-SPECS") is not None

    def test_write_r_port_prototype(self, writer):
        app = self._app()
        port = app.createRPortPrototype("RPort")
        tref = TRefType()
        port.setRequiredInterfaceTRef(tref)
        parent = _parent()
        writer.writeRPortPrototype(parent, port)
        assert parent[0].tag == "R-PORT-PROTOTYPE"
        assert parent[0].find("SHORT-NAME") is not None
        assert parent[0].find("REQUIRED-INTERFACE-TREF") is not None

    def test_write_r_port_prototype_with_comspec(self, writer):
        app = self._app()
        port = app.createRPortPrototype("RPort")
        com_spec = ClientComSpec()
        port.addRequiredComSpec(com_spec)
        parent = _parent()
        writer.writeRPortPrototype(parent, port)
        assert parent[0].find("REQUIRED-COM-SPECS") is not None

    def test_write_pr_port_prototype(self, writer):
        app = self._app()
        port = app.createPRPortPrototype("PRPort")
        port.setProvidedRequiredInterface(TRefType())
        parent = _parent()
        writer.writePRPortPrototype(parent, port)
        assert parent[0].tag == "PR-PORT-PROTOTYPE"
        assert parent[0].find("SHORT-NAME") is not None
        assert parent[0].find("PROVIDED-REQUIRED-INTERFACE-TREF") is not None

    def test_write_pr_port_prototype_with_comspecs(self, writer):
        app = self._app()
        port = app.createPRPortPrototype("PRPort")
        port.addProvidedComSpec(QueuedSenderComSpec())
        port.addRequiredComSpec(ClientComSpec())
        parent = _parent()
        writer.writePRPortPrototype(parent, port)
        assert parent[0].find("PROVIDED-COM-SPECS") is not None
        assert parent[0].find("REQUIRED-COM-SPECS") is not None


class TestWriteSwComponentTypePorts:
    def _app(self):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        return pkg.createApplicationSwComponentType("App")

    def test_no_ports(self, writer):
        app = self._app()
        parent = _parent()
        writer.writeSwComponentTypePorts(parent, app)
        assert parent.find("PORTS") is None

    def test_with_ports(self, writer):
        app = self._app()
        app.createPPortPrototype("PPort")
        app.createRPortPrototype("RPort")
        app.createPRPortPrototype("PRPort")
        parent = _parent()
        writer.writeSwComponentTypePorts(parent, app)
        ports = parent.find("PORTS")
        assert ports is not None
        assert len(ports) == 3
        tags = [p.tag for p in ports]
        assert "P-PORT-PROTOTYPE" in tags
        assert "R-PORT-PROTOTYPE" in tags
        assert "PR-PORT-PROTOTYPE" in tags


class TestWritePortGroup:
    def _comp(self):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        return pkg.createCompositionSwComponentType("Comp")

    def test_write_inner_group_iref(self, writer):
        iref = InnerPortGroupInCompositionInstanceRef()
        iref.setTargetRef(_ref())
        parent = _parent()
        writer.writeInnerGroupIRef(parent, iref)
        assert parent[0].tag == "INNER-GROUP-IREF"
        assert parent[0].find("TARGET-REF") is not None

    def test_write_port_group_inner_group_irefs_empty(self, writer):
        comp = self._comp()
        pg = comp.createPortGroup("PG")
        parent = _parent()
        writer.writePortGroupInnerGroupIRefs(parent, pg)
        assert len(parent) == 0

    def test_write_port_group_inner_group_irefs(self, writer):
        comp = self._comp()
        pg = comp.createPortGroup("PG")
        iref = InnerPortGroupInCompositionInstanceRef()
        iref.setTargetRef(_ref())
        pg.addInnerGroupIRef(iref)
        parent = _parent()
        writer.writePortGroupInnerGroupIRefs(parent, pg)
        assert parent[0].tag == "INNER-GROUP-IREFS"
        assert parent[0].find("INNER-GROUP-IREF") is not None

    def test_write_port_group_outer_port_refs_empty(self, writer):
        comp = self._comp()
        pg = comp.createPortGroup("PG")
        parent = _parent()
        writer.writePortGroupOuterPortRefs(parent, pg)
        assert len(parent) == 0

    def test_write_port_group_outer_port_refs(self, writer):
        comp = self._comp()
        pg = comp.createPortGroup("PG")
        pg.addOuterPortRef(_ref())
        parent = _parent()
        writer.writePortGroupOuterPortRefs(parent, pg)
        assert parent[0].tag == "OUTER-PORTS"
        assert parent[0].find(
            "PORT-PROTOTYPE-REF-CONDITIONAL") is not None

    def test_write_port_group(self, writer):
        comp = self._comp()
        pg = comp.createPortGroup("PG")
        iref = InnerPortGroupInCompositionInstanceRef()
        iref.setTargetRef(_ref())
        pg.addInnerGroupIRef(iref)
        pg.addOuterPortRef(_ref())
        parent = _parent()
        writer.writePortGroup(parent, pg)
        assert parent[0].tag == "PORT-GROUP"
        assert parent[0].find("SHORT-NAME") is not None
        assert parent[0].find("INNER-GROUP-IREFS") is not None
        assert parent[0].find("OUTER-PORTS") is not None


class TestWriteSwComponentType:
    def _app(self):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        return pkg.createApplicationSwComponentType("App")

    def test_write_sw_component_type_port_groups_empty(self, writer):
        app = self._app()
        parent = _parent()
        writer.writeSwComponentTypePortGroups(parent, app)
        assert parent.find("PORT-GROUPS") is None

    def test_write_sw_component_type_port_groups(self, writer):
        app = self._app()
        app.createPortGroup("PG1")
        parent = _parent()
        writer.writeSwComponentTypePortGroups(parent, app)
        assert parent.find("PORT-GROUPS") is not None
        assert parent.find("PORT-GROUPS").find("PORT-GROUP") is not None

    def test_write_sw_component_type(self, writer):
        app = self._app()
        app.createPPortPrototype("PPort")
        app.createPortGroup("PG1")
        parent = _parent()
        writer.writeSwComponentType(parent, app)
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("PORTS") is not None
        assert parent.find("PORT-GROUPS") is not None


class TestWriteSwComponentPrototype:
    def test_write_sw_component_prototype(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        comp = pkg.createCompositionSwComponentType("Comp")
        proto = comp.createSwComponentPrototype("Cmp")
        proto.setTypeTRef(TRefType())
        parent = _parent()
        writer.writeSwComponentPrototype(parent, proto)
        assert parent[0].tag == "SW-COMPONENT-PROTOTYPE"
        assert parent[0].find("SHORT-NAME") is not None
        assert parent[0].find("TYPE-TREF") is not None


class TestWriteCompositionSwComponentType:
    def _comp(self):
        autosar = AUTOSAR.getInstance()
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        return pkg.createCompositionSwComponentType("Comp")

    def test_write_components_empty(self, writer):
        comp = self._comp()
        parent = _parent()
        writer.writeCompositionSwComponentTypeComponents(parent, comp)
        assert parent.find("COMPONENTS") is None

    def test_write_components(self, writer):
        comp = self._comp()
        comp.createSwComponentPrototype("Cmp1")
        parent = _parent()
        writer.writeCompositionSwComponentTypeComponents(parent, comp)
        assert parent.find("COMPONENTS") is not None
        assert parent.find("COMPONENTS").find(
            "SW-COMPONENT-PROTOTYPE") is not None

    def test_write_assembly_sw_connector(self, writer):
        comp = self._comp()
        conn = comp.createAssemblySwConnector("AsmConn")
        provider = PPortInCompositionInstanceRef()
        provider.setContextComponentRef(_ref())
        provider.setTargetPPortRef(_ref())
        conn.setProviderIRef(provider)
        requester = RPortInCompositionInstanceRef()
        requester.setContextComponentRef(_ref())
        requester.setTargetRPortRef(_ref())
        conn.setRequesterIRef(requester)
        parent = _parent()
        writer.writeAssemblySwConnector(parent, conn)
        assert parent[0].tag == "ASSEMBLY-SW-CONNECTOR"
        assert parent[0].find("PROVIDER-IREF") is not None
        assert parent[0].find("REQUESTER-IREF") is not None

    def test_write_assembly_sw_connector_no_irefs(self, writer):
        comp = self._comp()
        conn = comp.createAssemblySwConnector("AsmConn")
        parent = _parent()
        writer.writeAssemblySwConnector(parent, conn)
        assert parent[0].tag == "ASSEMBLY-SW-CONNECTOR"
        assert parent[0].find("PROVIDER-IREF") is None
        assert parent[0].find("REQUESTER-IREF") is None

    def test_write_delegation_sw_connector_p_port(self, writer):
        comp = self._comp()
        conn = comp.createDelegationSwConnector("DelConn")
        inner = PPortInCompositionInstanceRef()
        inner.setContextComponentRef(_ref())
        inner.setTargetPPortRef(_ref())
        conn.setInnerPortIRref(inner)
        conn.setOuterPortRef(_ref())
        parent = _parent()
        writer.writeDelegationSwConnector(parent, conn)
        assert parent[0].tag == "DELEGATION-SW-CONNECTOR"
        assert parent[0].find("INNER-PORT-IREF") is not None
        assert parent[0].find(
            "INNER-PORT-IREF").find(
                "P-PORT-IN-COMPOSITION-INSTANCE-REF") is not None
        assert parent[0].find("OUTER-PORT-REF") is not None

    def test_write_delegation_sw_connector_r_port(self, writer):
        comp = self._comp()
        conn = comp.createDelegationSwConnector("DelConn")
        inner = RPortInCompositionInstanceRef()
        inner.setContextComponentRef(_ref())
        inner.setTargetRPortRef(_ref())
        conn.setInnerPortIRref(inner)
        parent = _parent()
        writer.writeDelegationSwConnector(parent, conn)
        assert parent[0].find(
            "INNER-PORT-IREF").find(
                "R-PORT-IN-COMPOSITION-INSTANCE-REF") is not None

    def test_write_delegation_sw_connector_no_inner(self, writer):
        comp = self._comp()
        conn = comp.createDelegationSwConnector("DelConn")
        conn.setOuterPortRef(_ref())
        parent = _parent()
        writer.writeDelegationSwConnector(parent, conn)
        assert parent[0].find("INNER-PORT-IREF") is None
        assert parent[0].find("OUTER-PORT-REF") is not None

    def test_write_sw_connector(self, writer):
        comp = self._comp()
        conn = comp.createAssemblySwConnector("AsmConn")
        conn.setMappingRef(_ref())
        parent = _parent()
        writer.writeSwConnector(parent, conn)
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("MAPPING-REF") is not None

    def test_write_sw_connectors_empty(self, writer):
        comp = self._comp()
        parent = _parent()
        writer.writeCompositionSwComponentTypeSwConnectors(parent, comp)
        assert parent.find("CONNECTORS") is None

    def test_write_sw_connectors(self, writer):
        comp = self._comp()
        comp.createAssemblySwConnector("AsmConn")
        comp.createDelegationSwConnector("DelConn")
        parent = _parent()
        writer.writeCompositionSwComponentTypeSwConnectors(parent, comp)
        connectors = parent.find("CONNECTORS")
        assert connectors is not None
        assert connectors.find("ASSEMBLY-SW-CONNECTOR") is not None
        assert connectors.find("DELEGATION-SW-CONNECTOR") is not None

    def test_write_data_type_mapping_empty(self, writer):
        comp = self._comp()
        parent = _parent()
        writer.writeCompositionSwComponentTypeDataTypeMappingSet(
            parent, comp)
        assert parent.find("DATA-TYPE-MAPPING-REFS") is None

    def test_write_data_type_mapping(self, writer):
        comp = self._comp()
        comp.addDataTypeMapping(_ref(dest="DATA-TYPE-MAPPING-SET"))
        parent = _parent()
        writer.writeCompositionSwComponentTypeDataTypeMappingSet(
            parent, comp)
        assert parent.find("DATA-TYPE-MAPPING-REFS") is not None
        assert parent.find(
            "DATA-TYPE-MAPPING-REFS").find(
                "DATA-TYPE-MAPPING-REF") is not None

    def test_write_composition_sw_component_type(self, writer):
        comp = self._comp()
        comp.createSwComponentPrototype("Cmp1")
        comp.createAssemblySwConnector("AsmConn")
        comp.addDataTypeMapping(_ref(dest="DATA-TYPE-MAPPING-SET"))
        comp.createPPortPrototype("PPort")
        parent = _parent()
        writer.writeCompositionSwComponentType(parent, comp)
        assert parent[0].tag == "COMPOSITION-SW-COMPONENT-TYPE"
        assert parent[0].find("SHORT-NAME") is not None
        assert parent[0].find("PORTS") is not None
        assert parent[0].find("COMPONENTS") is not None
        assert parent[0].find("CONNECTORS") is not None
        assert parent[0].find("DATA-TYPE-MAPPING-REFS") is not None

    def test_write_composition_sw_component_types(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        pkg.createCompositionSwComponentType("Comp1")
        pkg.createCompositionSwComponentType("Comp2")
        parent = _parent()
        writer.writeCompositionSwComponentTypes(parent, pkg)
        comps = parent.findall("COMPOSITION-SW-COMPONENT-TYPE")
        assert len(comps) == 2


class _FakeValueSpecification(ValueSpecification):
    def __init__(self):
        super().__init__()


class _FakePortPrototype:
    pass


class _FakeComponent:
    pass


class TestSetValueSpecifications:
    def test_set_sw_values_none(self, writer):
        parent = _parent()
        writer.setSwValues(parent, "SW-VALUES-PHYS", None)
        assert len(parent) == 0

    def test_set_sw_values_with_vs_and_vt(self, writer):
        sw_values = SwValues()
        sw_values.addV(_numerical(1))
        sw_values.addV(_numerical(2))
        sw_values.vt = _literal("vt")
        parent = _parent()
        writer.setSwValues(parent, "SW-VALUES-PHYS", sw_values)
        assert parent[0].tag == "SW-VALUES-PHYS"
        vs = parent[0].findall("V")
        assert len(vs) == 2
        assert parent[0].find("VT") is not None

    def test_set_value_list_none(self, writer):
        parent = _parent()
        writer.setValueList(parent, "SW-ARRAYSIZE", None)
        assert len(parent) == 0

    def test_set_value_list_with_v(self, writer):
        value_list = ValueList()
        value_list.setV(_float(2.5))
        parent = _parent()
        writer.setValueList(parent, "SW-ARRAYSIZE", value_list)
        assert parent[0].tag == "SW-ARRAYSIZE"
        assert parent[0].find("V") is not None

    def test_write_sw_value_cont_none(self, writer):
        parent = _parent()
        writer.writeSwValueCont(parent, None)
        assert len(parent) == 0

    def test_write_sw_value_cont_full(self, writer):
        cont = SwValueCont()
        cont.setUnitRef(_ref(dest="UNIT"))
        value_list = ValueList()
        value_list.setV(_float(3.0))
        cont.setSwArraysize(value_list)
        sw_values = SwValues()
        sw_values.addV(_numerical(5))
        cont.setSwValuesPhys(sw_values)
        parent = _parent()
        writer.writeSwValueCont(parent, cont)
        assert parent[0].tag == "SW-VALUE-CONT"
        assert parent[0].find("UNIT-REF") is not None
        assert parent[0].find("SW-ARRAYSIZE") is not None
        assert parent[0].find("SW-VALUES-PHYS") is not None

    def test_write_array_value_specification_empty(self, writer):
        spec = ArrayValueSpecification()
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        assert parent[0].tag == "ARRAY-VALUE-SPECIFICATION"
        assert parent[0].find("ELEMENTS") is None

    def test_write_array_value_specification_numerical(self, writer):
        spec = ArrayValueSpecification()
        spec.addElement(NumericalValueSpecification())
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        assert parent[0].find("ELEMENTS").find(
            "NUMERICAL-VALUE-SPECIFICATION") is not None

    def test_write_array_value_specification_application(self, writer):
        spec = ArrayValueSpecification()
        app = ApplicationValueSpecification()
        app.setSwValueCont(SwValueCont())
        spec.addElement(app)
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        assert parent[0].find("ELEMENTS").find(
            "APPLICATION-VALUE-SPECIFICATION") is not None

    def test_write_array_value_specification_text(self, writer):
        spec = ArrayValueSpecification()
        spec.addElement(TextValueSpecification())
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        assert parent[0].find("ELEMENTS").find(
            "TEXT-VALUE-SPECIFICATION") is not None

    def test_write_array_value_specification_nested_array(self, writer):
        spec = ArrayValueSpecification()
        spec.addElement(ArrayValueSpecification())
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        elements = parent[0].find("ELEMENTS")
        assert elements.find("ARRAY-VALUE-SPECIFICATION") is not None

    def test_write_array_value_specification_record(self, writer):
        spec = ArrayValueSpecification()
        spec.addElement(RecordValueSpecification())
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        assert parent[0].find("ELEMENTS").find(
            "RECORD-VALUE-SPECIFICATION") is not None

    def test_write_array_value_specification_unsupported_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        spec = ArrayValueSpecification()
        spec.addElement(_FakeValueSpecification())
        parent = _parent()
        writer.writeArrayValueSpecification(parent, spec)
        assert parent[0].tag == "ARRAY-VALUE-SPECIFICATION"

    def test_set_constant_reference(self, writer):
        spec = ConstantReference()
        spec.setConstantRef(_ref(dest="CONSTANT-SPECIFICATION"))
        parent = _parent()
        writer.setConstantReference(parent, spec)
        assert parent[0].tag == "CONSTANT-REFERENCE"
        assert parent[0].find("CONSTANT-REF") is not None

    def test_set_child_value_specification_application(self, writer):
        spec = ApplicationValueSpecification()
        spec.setSwValueCont(SwValueCont())
        parent = _parent()
        writer.setChildValueSpecification(parent, "INIT-VALUE", spec)
        assert parent[0].tag == "INIT-VALUE"
        assert parent[0].find(
            "APPLICATION-VALUE-SPECIFICATION") is not None

    def test_set_child_value_specification_constant(self, writer):
        spec = ConstantReference()
        spec.setConstantRef(_ref(dest="CONSTANT-SPECIFICATION"))
        parent = _parent()
        writer.setChildValueSpecification(parent, "INIT-VALUE", spec)
        assert parent[0].find("CONSTANT-REFERENCE") is not None

    def test_set_child_value_specification_numerical(self, writer):
        spec = NumericalValueSpecification()
        parent = _parent()
        writer.setChildValueSpecification(parent, "INIT-VALUE", spec)
        assert parent[0].find("NUMERICAL-VALUE-SPECIFICATION") is not None

    def test_set_child_value_specification_array(self, writer):
        spec = ArrayValueSpecification()
        parent = _parent()
        writer.setChildValueSpecification(parent, "INIT-VALUE", spec)
        assert parent[0].find("ARRAY-VALUE-SPECIFICATION") is not None

    def test_set_child_value_specification_record(self, writer):
        spec = RecordValueSpecification()
        parent = _parent()
        writer.setChildValueSpecification(parent, "INIT-VALUE", spec)
        assert parent[0].find("RECORD-VALUE-SPECIFICATION") is not None

    def test_set_child_value_specification_unsupported_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        parent = _parent()
        writer.setChildValueSpecification(
            parent, "INIT-VALUE", _FakeValueSpecification())
        assert parent[0].tag == "INIT-VALUE"


class TestWriteErrorBranches:
    def test_write_server_comspec_transformation_props_unsupported_warning(
            self):
        writer = ARXMLWriter(options={"warning": True})
        com_spec = ServerComSpec()
        com_spec.addTransformationComSpecProps(_FakeTransformationComSpecProps())
        parent = _parent()
        writer.writeServerComSpecTransformationComSpecProps(
            parent, com_spec)
        assert parent[0].tag == "TRANSFORMATION-COM-SPEC-PROPSS"

    def test_write_p_port_comspec_unsupported_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        parent = _parent()
        writer.writePPortComSpec(parent, _FakePPortComSpec())
        assert len(parent) == 0

    def test_write_sw_component_type_ports_unsupported_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        app = pkg.createApplicationSwComponentType("App")
        app.ports.append(_FakePortPrototype())
        parent = _parent()
        writer.writeSwComponentTypePorts(parent, app)
        assert parent.find("PORTS") is not None

    def test_write_composition_components_unsupported_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        comp = pkg.createCompositionSwComponentType("Comp")
        comp.components.append(_FakeComponent())
        parent = _parent()
        writer.writeCompositionSwComponentTypeComponents(parent, comp)
        assert parent.find("COMPONENTS") is not None

    def test_write_delegation_sw_connector_invalid_inner_port_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        comp = pkg.createCompositionSwComponentType("Comp")
        conn = comp.createDelegationSwConnector("DelConn")
        conn.setInnerPortIRref(_FakePortInCompositionInstanceRef())
        parent = _parent()
        writer.writeDelegationSwConnector(parent, conn)
        assert parent[0].tag == "DELEGATION-SW-CONNECTOR"

    def test_write_composition_sw_connectors_unsupported_warning(self):
        writer = ARXMLWriter(options={"warning": True})
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        comp = pkg.createCompositionSwComponentType("Comp")
        pass_through = PassThroughSwConnector(comp, "PassConn")
        comp.addElement(pass_through)
        parent = _parent()
        writer.writeCompositionSwComponentTypeSwConnectors(parent, comp)
        assert parent.find("CONNECTORS") is not None


class TestWriteRPortComSpecUnsupported:
    def test_raises_value_error(self, writer):
        parent = _parent()
        with pytest.raises(ValueError):
            writer.writeRPortComSpec(parent, _FakeRPortComSpec())

    def test_raises_value_error_warning_mode(self):
        writer = ARXMLWriter(options={"warning": True})
        parent = _parent()
        with pytest.raises(ValueError):
            writer.writeRPortComSpec(parent, _FakeRPortComSpec())


class TestWriteDelegationSwConnectorError:
    def test_raises_value_error_default(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        comp = pkg.createCompositionSwComponentType("Comp")
        conn = comp.createDelegationSwConnector("DelConn")
        conn.setInnerPortIRref(_FakePortInCompositionInstanceRef())
        parent = _parent()
        with pytest.raises(ValueError):
            writer.writeDelegationSwConnector(parent, conn)
