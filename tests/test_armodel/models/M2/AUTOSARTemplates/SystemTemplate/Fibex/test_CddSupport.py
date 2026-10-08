"""Unit tests for the Fibex CddSupport module (UserDefinedCluster, UserDefinedPhysicalChannel, UserDefinedCommunicationConnector, UserDefinedCommunicationController).

Table 3.129 (p.179) is a page-split table whose fragment A renders the
Class/Package/Note/Base/Aggregated by rows before the caption and carries NO
Attribute rows — the class adds no own fields or accessors beyond its
CommunicationCluster base (Rule 0001.3); the XSD own group USER-DEFINED-CLUSTER
(AUTOSAR_00052.xsd lines 128516-128536) holds only the atpVariation
USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL wrapper.
Table 3.130 (p.179) is the page-split sibling whose fragment renders before its
caption and likewise carries NO Attribute rows — UserDefinedPhysicalChannel adds
no own fields or accessors beyond its PhysicalChannel base; the XSD own group
USER-DEFINED-PHYSICAL-CHANNEL (AUTOSAR_00052.xsd lines 128980-128988) is an empty
sequence (no atpVariation wrapper).
Table 3.131 (p.180) is the page-split sibling whose Class/Package/Note/Base
fragment renders before its caption and likewise carries NO Attribute rows —
UserDefinedCommunicationConnector adds no own fields or accessors beyond its
CommunicationConnector base; the XSD own group USER-DEFINED-COMMUNICATION-CONNECTOR
(AUTOSAR_00052.xsd lines 128603-128611) is an empty sequence (no atpVariation
wrapper).
Table 3.132 (p.180) is the atpVariation sibling whose table carries NO Attribute
rows — UserDefinedCommunicationController adds no own fields or accessors beyond
its CommunicationController base; the XSD own group USER-DEFINED-COMMUNICATION-
CONTROLLER (AUTOSAR_00052.xsd lines 128630-128650) holds only the atpVariation
USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS/USER-DEFINED-COMMUNICATION-
CONTROLLER-CONDITIONAL wrapper.
Spec placement per Rule 0007: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    PositiveInteger,
    PositiveUnlimitedInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster, UserDefinedCommunicationConnector, UserDefinedCommunicationController, UserDefinedPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FramePort, IPduPort, ISignalPort, ISignalTriggering, PduTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    EcuInstance,
    PhysicalChannel,
    PncGatewayTypeEnum,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


USER_DEFINED_CLUSTER_CLASS_NOTE = (
    "This element allows the modeling of arbitrary Communication Clusters (e.g. bus systems that are not supported by AUTOSAR). Tags: atp.recommendedPackage=CommunicationClusters"
)


class TestUserDefinedCluster:
    """Test cases for UserDefinedCluster (Table 3.129, p.179)."""

    def test_inheritance(self):
        assert issubclass(UserDefinedCluster, CommunicationCluster)
        assert issubclass(UserDefinedCluster, FibexElement)
        assert issubclass(UserDefinedCluster, ARObject)

    def test_concrete_instantiation(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")  # Table 3.129 carries no abstract stereotype

        assert isinstance(cluster, CommunicationCluster)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedCluster.__doc__) == USER_DEFINED_CLUSTER_CLASS_NOTE

    def test_init_docless(self):
        assert UserDefinedCluster.__init__.__doc__ is None

    def test_no_own_members(self):
        # Table 3.129's Attribute rows render none — UserDefinedCluster adds no fields or accessors beyond its bases (Rule 0001.3)
        own = [name for name, value in vars(UserDefinedCluster).items() if not name.startswith("_")]
        assert own == []

    def test_initialization_defaults(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")

        for getter in ["getBaudrate", "getProtocolName", "getProtocolVersion"]:
            assert getattr(cluster, getter)() is None, getter
        assert cluster.getPhysicalChannels() == []

    def test_inherited_accessors_round_trip(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")
        baudrate = PositiveUnlimitedInteger().setValue("500000")
        protocol_name = ARLiteral().setValue("USER-DEFINED")
        protocol_version = ARLiteral().setValue("1.0")

        assert cluster == cluster.setBaudrate(baudrate)
        assert cluster.getBaudrate() is baudrate
        assert cluster.getBaudrate().getValue() == 500000
        assert cluster == cluster.setBaudrate(None)  # None no-op
        assert cluster.getBaudrate() is baudrate  # unchanged

        assert cluster == cluster.setProtocolName(protocol_name)
        assert cluster.getProtocolName() is protocol_name
        assert cluster == cluster.setProtocolName(None)  # None no-op
        assert cluster.getProtocolName() is protocol_name  # unchanged

        assert cluster == cluster.setProtocolVersion(protocol_version)
        assert cluster.getProtocolVersion() is protocol_version
        assert cluster == cluster.setProtocolVersion(None)  # None no-op
        assert cluster.getProtocolVersion() is protocol_version  # unchanged

    def test_inherited_create_physical_channel(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")

        channel = cluster.createCanPhysicalChannel("Channel")
        assert isinstance(channel, CanPhysicalChannel)
        assert cluster.getPhysicalChannels() == [channel]

        duplicate = cluster.createCanPhysicalChannel("Channel")
        assert duplicate is channel
        assert len(cluster.getPhysicalChannels()) == 1


USER_DEFINED_PHYSICAL_CHANNEL_CLASS_NOTE = "This element allows the modeling of arbitrary Physical Channels."


class TestUserDefinedPhysicalChannel:
    """Test cases for UserDefinedPhysicalChannel (Table 3.130, p.179)."""

    def test_inheritance(self):
        assert issubclass(UserDefinedPhysicalChannel, PhysicalChannel)
        assert issubclass(UserDefinedPhysicalChannel, Identifiable)
        assert issubclass(UserDefinedPhysicalChannel, ARObject)

    def test_concrete_instantiation(self):
        channel = UserDefinedPhysicalChannel(MockParent(), "channel")  # Table 3.130 carries no abstract stereotype

        assert isinstance(channel, PhysicalChannel)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedPhysicalChannel.__doc__) == USER_DEFINED_PHYSICAL_CHANNEL_CLASS_NOTE

    def test_init_docless(self):
        assert UserDefinedPhysicalChannel.__init__.__doc__ is None

    def test_no_own_members(self):
        # Table 3.130's Attribute rows render none — UserDefinedPhysicalChannel adds no fields or accessors beyond its PhysicalChannel base (Rule 0001.3)
        own = [name for name, value in vars(UserDefinedPhysicalChannel).items() if not name.startswith("_")]
        assert own == []

    def test_initialization_defaults(self):
        channel = UserDefinedPhysicalChannel(MockParent(), "channel")

        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []

    def test_inherited_accessors_round_trip(self):
        channel = UserDefinedPhysicalChannel(MockParent(), "channel")
        comm_connector_ref = RefType()
        comm_connector_ref.setValue("/ECU/CONN")
        managed_channel_ref = RefType()
        managed_channel_ref.setValue("/CLUSTER/MANAGED_CH")

        assert channel == channel.addCommConnectorRef(comm_connector_ref)
        assert channel.getCommConnectorRefs() == [comm_connector_ref]
        assert channel == channel.addCommConnectorRef(None)  # None no-op
        assert channel.getCommConnectorRefs() == [comm_connector_ref]  # unchanged

        assert channel == channel.addManagedPhysicalChannelRef(managed_channel_ref)
        assert channel.getManagedPhysicalChannelRefs() == [managed_channel_ref]
        assert channel == channel.addManagedPhysicalChannelRef(None)  # None no-op
        assert channel.getManagedPhysicalChannelRefs() == [managed_channel_ref]  # unchanged

        triggering = channel.createISignalTriggering("ISignalTriggering")
        assert isinstance(triggering, ISignalTriggering)
        assert channel.getISignalTriggerings() == [triggering]

        pdu_triggering = channel.createPduTriggering("PduTriggering")
        assert isinstance(pdu_triggering, PduTriggering)
        assert channel.getPduTriggerings() == [pdu_triggering]
        assert channel.getFrameTriggerings() == []

        assert channel.createISignalTriggering("ISignalTriggering") is triggering
        assert channel.createPduTriggering("PduTriggering") is pdu_triggering
        assert len(channel.getISignalTriggerings()) == 1
        assert len(channel.getPduTriggerings()) == 1

    def test_cluster_factory_creates_and_appends(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")

        channel = cluster.createUserDefinedPhysicalChannel("Channel")
        assert isinstance(channel, UserDefinedPhysicalChannel)
        assert cluster.getPhysicalChannels() == [channel]

        duplicate = cluster.createUserDefinedPhysicalChannel("Channel")
        assert duplicate is channel
        assert len(cluster.getPhysicalChannels()) == 1


USER_DEFINED_COMMUNICATION_CONNECTOR_CLASS_NOTE = "This element allows the modeling of arbitrary Communication Connectors."


class TestUserDefinedCommunicationConnector:
    """Test cases for UserDefinedCommunicationConnector (Table 3.131, p.180)."""

    def test_inheritance(self):
        assert issubclass(UserDefinedCommunicationConnector, CommunicationConnector)
        assert issubclass(UserDefinedCommunicationConnector, Identifiable)
        assert issubclass(UserDefinedCommunicationConnector, ARObject)

    def test_concrete_instantiation(self):
        connector = UserDefinedCommunicationConnector(MockParent(), "connector")  # Table 3.131 carries no abstract stereotype

        assert isinstance(connector, CommunicationConnector)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedCommunicationConnector.__doc__) == USER_DEFINED_COMMUNICATION_CONNECTOR_CLASS_NOTE

    def test_init_docless(self):
        assert UserDefinedCommunicationConnector.__init__.__doc__ is None

    def test_no_own_members(self):
        # Table 3.131's Attribute rows render none — UserDefinedCommunicationConnector adds no fields or accessors beyond its CommunicationConnector base (Rule 0001.3)
        own = [name for name, value in vars(UserDefinedCommunicationConnector).items() if not name.startswith("_")]
        assert own == []

    def test_initialization_defaults(self):
        connector = UserDefinedCommunicationConnector(MockParent(), "connector")

        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None

    def test_inherited_accessors_round_trip(self):
        connector = UserDefinedCommunicationConnector(MockParent(), "connector")
        comm_controller_ref = RefType()
        comm_controller_ref.setValue("/EcuInst/Conn")
        wakeup_flag = Boolean()
        wakeup_flag.setValue(True)
        gateway_type = PncGatewayTypeEnum()
        gateway_type.setValue(PncGatewayTypeEnum.ACTIVE)

        assert connector == connector.setCommControllerRef(comm_controller_ref)
        assert connector.getCommControllerRef() is comm_controller_ref
        assert connector.getCommControllerRef().getValue() == "/EcuInst/Conn"
        assert connector == connector.setCommControllerRef(None)  # None no-op
        assert connector.getCommControllerRef() is comm_controller_ref  # unchanged

        assert connector == connector.setCreateEcuWakeupSource(wakeup_flag)
        assert connector.getCreateEcuWakeupSource() is wakeup_flag
        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector == connector.setCreateEcuWakeupSource(None)  # None no-op
        assert connector.getCreateEcuWakeupSource() is wakeup_flag  # unchanged

        assert connector == connector.setPncGatewayType(gateway_type)
        assert connector.getPncGatewayType() is gateway_type
        assert connector.getPncGatewayType().getValue() == "ACTIVE"
        assert connector == connector.setPncGatewayType(None)  # None no-op
        assert connector.getPncGatewayType() is gateway_type  # unchanged

    def test_inherited_port_factories_append(self):
        connector = UserDefinedCommunicationConnector(MockParent(), "connector")

        frame_port = connector.createFramePort("FramePort")
        assert isinstance(frame_port, FramePort)
        assert connector.getEcuCommPortInstances() == [frame_port]

        ipdu_port = connector.createIPduPort("IPduPort")
        assert isinstance(ipdu_port, IPduPort)
        assert connector.getEcuCommPortInstances() == [frame_port, ipdu_port]

        isignal_port = connector.createISignalPort("ISignalPort")
        assert isinstance(isignal_port, ISignalPort)
        assert connector.getEcuCommPortInstances() == [frame_port, ipdu_port, isignal_port]

        assert connector.createFramePort("FramePort") is frame_port
        assert connector.createIPduPort("IPduPort") is ipdu_port
        assert connector.createISignalPort("ISignalPort") is isignal_port
        assert len(connector.getEcuCommPortInstances()) == 3

    def test_inherited_pnc_filter_array_masks_append(self):
        connector = UserDefinedCommunicationConnector(MockParent(), "connector")
        mask = PositiveInteger()
        mask.setValue("255")

        assert connector == connector.addPncFilterArrayMask(mask)
        assert connector.getPncFilterArrayMasks() == [mask]
        assert connector.getPncFilterArrayMasks()[0].getValue() == 255
        assert connector == connector.addPncFilterArrayMask(None)  # None no-op
        assert connector.getPncFilterArrayMasks() == [mask]  # unchanged

    def test_ecu_factory_creates_and_appends(self):
        ecu = EcuInstance(MockParent(), "Ecu")

        connector = ecu.createUserDefinedCommunicationConnector("Connector")
        assert isinstance(connector, UserDefinedCommunicationConnector)
        assert ecu.getConnectors() == [connector]

        duplicate = ecu.createUserDefinedCommunicationConnector("Connector")
        assert duplicate is connector
        assert len(ecu.getConnectors()) == 1


USER_DEFINED_COMMUNICATION_CONTROLLER_CLASS_NOTE = "This element allows the modeling of arbitrary Communication Controllers."


class TestUserDefinedCommunicationController:
    """Test cases for UserDefinedCommunicationController (Table 3.132, p.180)."""

    def test_inheritance(self):
        assert issubclass(UserDefinedCommunicationController, CommunicationController)
        assert issubclass(UserDefinedCommunicationController, Identifiable)
        assert issubclass(UserDefinedCommunicationController, ARObject)

    def test_concrete_instantiation(self):
        controller = UserDefinedCommunicationController(MockParent(), "controller")  # Table 3.132 carries no abstract stereotype

        assert isinstance(controller, CommunicationController)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedCommunicationController.__doc__) == USER_DEFINED_COMMUNICATION_CONTROLLER_CLASS_NOTE

    def test_init_docless(self):
        assert UserDefinedCommunicationController.__init__.__doc__ is None

    def test_no_own_members(self):
        # Table 3.132's Attribute rows render none — UserDefinedCommunicationController adds no fields or accessors beyond its CommunicationController base (Rule 0001.3)
        own = [name for name, value in vars(UserDefinedCommunicationController).items() if not name.startswith("_")]
        assert own == []

    def test_initialization_defaults(self):
        controller = UserDefinedCommunicationController(MockParent(), "controller")

        assert controller.getWakeUpByControllerSupported() is None

    def test_inherited_accessors_round_trip(self):
        controller = UserDefinedCommunicationController(MockParent(), "controller")
        wakeup_flag = Boolean()
        wakeup_flag.setValue(True)

        assert controller == controller.setWakeUpByControllerSupported(wakeup_flag)
        assert controller.getWakeUpByControllerSupported() is wakeup_flag
        assert controller.getWakeUpByControllerSupported().getValue() is True
        assert controller == controller.setWakeUpByControllerSupported(None)  # None no-op
        assert controller.getWakeUpByControllerSupported() is wakeup_flag  # unchanged

    def test_ecu_factory_creates_and_appends(self):
        ecu = EcuInstance(MockParent(), "Ecu")

        controller = ecu.createUserDefinedCommunicationController("Controller")
        assert isinstance(controller, UserDefinedCommunicationController)
        assert ecu.getCommControllers() == [controller]

        duplicate = ecu.createUserDefinedCommunicationController("Controller")
        assert duplicate is controller
        assert len(ecu.getCommControllers()) == 1
