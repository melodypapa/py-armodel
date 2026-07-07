"""Tests for writer Ethernet/CAN controller and EcuInstance methods."""
import xml.etree.cElementTree as ET
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (  # noqa E501
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (  # noqa E501
    CouplingPortDetails,
    VlanMembership,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    Float,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
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


def _int(value):
    n = Integer()
    n.setValue(value)
    return n


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _float(value):
    f = Float()
    f.setValue(value)
    return f


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _make_ecu_instance():
    return _pkg().createEcuInstance("EcuInst")


def _make_ethernet_cluster():
    return _pkg().createEthernetCluster("EthCluster")


def _make_can_frame():
    return _pkg().createCanFrame("CanFrame")


def _make_can_communication_controller():
    instance = _make_ecu_instance()
    return instance.createCanCommunicationController("CanCtrl")


def _make_ethernet_communication_controller():
    instance = _make_ecu_instance()
    return instance.createEthernetCommunicationController("EthCtrl")


def _make_can_communication_connector():
    instance = _make_ecu_instance()
    return instance.createCanCommunicationConnector("CanConn")


class TestWriterMacMulticastGroup:
    def test_with_address(self, writer):
        cluster = _make_ethernet_cluster()
        group = cluster.createMacMulticastGroup("g1")
        group.setMacMulticastAddress(_literal("01:00:5E:00:00:01"))
        parent = _parent()
        writer.writeMacMulticastGroup(parent, group)
        assert parent[0].tag == "MAC-MULTICAST-GROUP"
        addr = parent[0].find("MAC-MULTICAST-ADDRESS")
        assert addr is not None
        assert addr.text == "01:00:5E:00:00:01"

    def test_none(self, writer):
        parent = _parent()
        writer.writeMacMulticastGroup(parent, None)
        assert len(parent) == 0


class TestWriterEthernetClusterMacMulticastGroups:
    def test_with_groups(self, writer):
        cluster = _make_ethernet_cluster()
        cluster.createMacMulticastGroup("g1").setMacMulticastAddress(
            _literal("addr1")
        )
        parent = _parent()
        writer.writeEthernetClusterMacMulticastGroups(parent, cluster)
        assert parent[0].tag == "MAC-MULTICAST-GROUPS"
        assert parent[0].find("MAC-MULTICAST-GROUP") is not None

    def test_empty(self, writer):
        cluster = _make_ethernet_cluster()
        parent = _parent()
        writer.writeEthernetClusterMacMulticastGroups(parent, cluster)
        assert len(parent) == 0


class TestWriterEthernetCluster:
    def test_full(self, writer):
        cluster = _make_ethernet_cluster()
        cluster.createMacMulticastGroup("g1")
        parent = _parent()
        writer.writeEthernetCluster(parent, cluster)
        assert parent[0].tag == "ETHERNET-CLUSTER"
        cond = parent[0].find(
            "ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL"
        )
        assert cond is not None
        assert cond.find("MAC-MULTICAST-GROUPS") is not None


class TestWriterCanFrame:
    def test_can_frame(self, writer):
        frame = _make_can_frame()
        parent = _parent()
        writer.writeCanFrame(parent, frame)
        assert parent[0].tag == "CAN-FRAME"
        assert parent[0].find("SHORT-NAME") is not None


class TestWriterCommConnectorPort:
    def test_comm_connector_port(self, writer):
        connector = _make_can_communication_connector()
        port = connector.createFramePort("fp")
        port.setCommunicationDirection(_literal("in"))
        parent = _parent()
        writer.writeCommConnectorPort(parent, port)
        assert parent.find("SHORT-NAME") is not None
        direction = parent.find("COMMUNICATION-DIRECTION")
        assert direction is not None
        assert direction.text == "in"


class TestWriterFramePort:
    def test_frame_port(self, writer):
        connector = _make_can_communication_connector()
        port = connector.createFramePort("fp")
        port.setCommunicationDirection(_literal("out"))
        parent = _parent()
        writer.writeFramePort(parent, port)
        assert parent[0].tag == "FRAME-PORT"
        assert parent[0].find("COMMUNICATION-DIRECTION").text == "out"


class TestWriterIPduPort:
    def test_ipdu_port(self, writer):
        connector = _make_can_communication_connector()
        port = connector.createIPduPort("ipp")
        port.setCommunicationDirection(_literal("in"))
        port.setKeyId(_posint(5))
        port.setRxSecurityVerification(_bool(True))
        port.setUseAuthDataFreshness(_bool(False))
        parent = _parent()
        writer.writeIPduPort(parent, port)
        assert parent[0].tag == "I-PDU-PORT"
        assert parent[0].find("KEY-ID") is not None
        assert parent[0].find("RX-SECURITY-VERIFICATION") is not None
        assert parent[0].find("USE-AUTH-DATA-FRESHNESS") is not None


class TestWriterISignalPort:
    def test_isignal_port(self, writer):
        connector = _make_can_communication_connector()
        port = connector.createISignalPort("isp")
        port.setCommunicationDirection(_literal("in"))
        port.setTimeout(_time(0.1))
        parent = _parent()
        writer.writeISignalPort(parent, port)
        assert parent[0].tag == "I-SIGNAL-PORT"
        assert parent[0].find("TIMEOUT") is not None


class TestWriterCommunicationConnectorEcuCommPortInstances:
    def test_dispatches_all_port_types(self, writer):
        connector = _make_can_communication_connector()
        connector.createFramePort("fp")
        connector.createIPduPort("ipp")
        connector.createISignalPort("isp")
        parent = _parent()
        writer.writeCommunicationConnectorEcuCommPortInstances(
            parent, connector
        )
        assert parent[0].tag == "ECU-COMM-PORT-INSTANCES"
        tags = {c.tag for c in parent[0]}
        assert "FRAME-PORT" in tags
        assert "I-PDU-PORT" in tags
        assert "I-SIGNAL-PORT" in tags

    def test_empty(self, writer):
        connector = _make_can_communication_connector()
        parent = _parent()
        writer.writeCommunicationConnectorEcuCommPortInstances(
            parent, connector
        )
        assert len(parent) == 0


class TestWriterCommunicationController:
    def test_write_communication_controller(self, writer):
        controller = _make_can_communication_controller()
        controller.setWakeUpByControllerSupported(_bool(True))
        parent = _parent()
        writer.writeCommunicationController(parent, controller)
        assert parent.find("WAKE-UP-BY-CONTROLLER-SUPPORTED") is not None


class TestWriterSetCanControllerFdConfiguration:
    def test_with_config(self, writer):
        config = CanControllerFdConfiguration()
        config.setTxBitRateSwitch(_bool(True))
        parent = _parent()
        writer.setCanControllerFdConfiguration(
            parent, "CAN-CONTROLLER-FD-CONFIGURATION", config
        )
        assert len(parent) == 0

    def test_none(self, writer):
        parent = _parent()
        writer.setCanControllerFdConfiguration(
            parent, "CAN-CONTROLLER-FD-CONFIGURATION", None
        )
        assert len(parent) == 0


class TestWriterSetCanControllerFdConfigurationRequirements:
    def test_with_requirements(self, writer):
        req = CanControllerFdConfigurationRequirements()
        req.setMaxNumberOfTimeQuantaPerBit(_int(32))
        req.setMaxSamplePoint(_float(0.8))
        req.setMaxSyncJumpWidth(_float(0.2))
        req.setMaxTrcvDelayCompensationOffset(_time(0.001))
        req.setMinNumberOfTimeQuantaPerBit(_int(16))
        req.setMinSamplePoint(_float(0.5))
        req.setMinSyncJumpWidth(_float(0.1))
        req.setMinTrcvDelayCompensationOffset(_time(0.0005))
        req.setTxBitRateSwitch(_bool(True))
        parent = _parent()
        writer.setCanControllerFdConfigurationRequirements(
            parent, "CAN-CONTROLLER-FD-REQUIREMENTS", req
        )
        assert parent[0].tag == "CAN-CONTROLLER-FD-REQUIREMENTS"
        assert parent[0].find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT") is not None
        assert parent[0].find("MAX-SAMPLE-POINT") is not None
        assert parent[0].find("MAX-SYNC-JUMP-WIDTH") is not None
        assert parent[0].find("MAX-TRCV-DELAY-COMPENSATION-OFFSET") is not None
        assert parent[0].find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT") is not None
        assert parent[0].find("MIN-SAMPLE-POINT") is not None
        assert parent[0].find("MIN-SYNC-JUMP-WIDTH") is not None
        assert parent[0].find("MIN-TRCV-DELAY-COMPENSATION-OFFSET") is not None
        assert parent[0].find("TX-BIT-RATE-SWITCH") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.setCanControllerFdConfigurationRequirements(
            parent, "CAN-CONTROLLER-FD-REQUIREMENTS", None
        )
        assert len(parent) == 0


class TestWriterAbstractCanCommunicationControllerAttributes:
    def test_with_attributes(self, writer):
        attrs = CanControllerConfigurationRequirements()
        attrs.setCanControllerFdAttributes(CanControllerFdConfiguration())
        req = CanControllerFdConfigurationRequirements()
        req.setTxBitRateSwitch(_bool(True))
        attrs.setCanControllerFdRequirements(req)
        parent = _parent()
        writer.writeAbstractCanCommunicationControllerAttributes(parent, attrs)
        assert parent.find("CAN-CONTROLLER-FD-REQUIREMENTS") is not None


class TestWriterCanControllerConfigurationRequirements:
    def test_with_requirements(self, writer):
        req = CanControllerConfigurationRequirements()
        req.setMaxNumberOfTimeQuantaPerBit(_int(32))
        req.setMaxSamplePoint(_float(0.8))
        req.setMaxSyncJumpWidth(_float(0.2))
        req.setMinNumberOfTimeQuantaPerBit(_int(16))
        req.setMinSamplePoint(_float(0.5))
        req.setMinSyncJumpWidth(_float(0.1))
        req.setCanControllerFdRequirements(
            CanControllerFdConfigurationRequirements()
        )
        parent = _parent()
        writer.writeCanControllerConfigurationRequirements(parent, req)
        assert parent[0].tag == "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS"
        assert parent[0].find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT") is not None
        assert parent[0].find("MAX-SAMPLE-POINT") is not None
        assert parent[0].find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT") is not None
        assert parent[0].find("CAN-CONTROLLER-FD-REQUIREMENTS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeCanControllerConfigurationRequirements(parent, None)
        assert len(parent) == 0


class TestWriterAbstractCanCommunicationControllerCanControllerAttributes:
    def test_with_requirements(self, writer):
        controller = _make_can_communication_controller()
        req = CanControllerConfigurationRequirements()
        req.setMaxSamplePoint(_float(0.8))
        controller.setCanControllerAttributes(req)
        parent = _parent()
        writer.writeAbstractCanCommunicationControllerCanControllerAttributes(
            parent, controller
        )
        assert parent[0].tag == "CAN-CONTROLLER-ATTRIBUTES"
        assert parent[0].find(
            "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS"
        ) is not None

    def test_no_attributes(self, writer):
        controller = _make_can_communication_controller()
        parent = _parent()
        writer.writeAbstractCanCommunicationControllerCanControllerAttributes(
            parent, controller
        )
        assert len(parent) == 0


class TestWriterAbstractCanCommunicationController:
    def test_full(self, writer):
        controller = _make_can_communication_controller()
        controller.setWakeUpByControllerSupported(_bool(True))
        req = CanControllerConfigurationRequirements()
        controller.setCanControllerAttributes(req)
        parent = _parent()
        writer.writeAbstractCanCommunicationController(parent, controller)
        assert parent.find("WAKE-UP-BY-CONTROLLER-SUPPORTED") is not None
        assert parent.find("CAN-CONTROLLER-ATTRIBUTES") is not None


class TestWriterCanCommunicationController:
    def test_full(self, writer):
        controller = _make_can_communication_controller()
        controller.setWakeUpByControllerSupported(_bool(True))
        req = CanControllerConfigurationRequirements()
        controller.setCanControllerAttributes(req)
        parent = _parent()
        writer.writeCanCommunicationController(parent, controller)
        assert parent[0].tag == "CAN-COMMUNICATION-CONTROLLER"
        cond = parent[0].find(
            "CAN-COMMUNICATION-CONTROLLER-VARIANTS"
            "/CAN-COMMUNICATION-CONTROLLER-CONDITIONAL"
        )
        assert cond is not None
        assert cond.find("WAKE-UP-BY-CONTROLLER-SUPPORTED") is not None
        assert cond.find("CAN-CONTROLLER-ATTRIBUTES") is not None


class TestWriterCouplingPortSchedulerCouplingPortStructuralElement:
    def test_structural_element(self, writer):
        details = CouplingPortDetails()
        fifo = details.createCouplingPortFifo("fifo")
        parent = _parent()
        writer.writeCouplingPortSchedulerCouplingPortStructuralElement(
            parent, fifo
        )
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("SHORT-NAME").text == "fifo"


class TestWriterCouplingPortFifo:
    def test_fifo(self, writer):
        details = CouplingPortDetails()
        fifo = details.createCouplingPortFifo("fifo")
        parent = _parent()
        writer.writeCouplingPortFifo(parent, fifo)
        assert parent[0].tag == "COUPLING-PORT-FIFO"
        assert parent[0].find("SHORT-NAME").text == "fifo"

    def test_none(self, writer):
        parent = _parent()
        writer.writeCouplingPortFifo(parent, None)
        assert len(parent) == 0


class TestWriterCouplingPortScheduler:
    def test_scheduler(self, writer):
        details = CouplingPortDetails()
        scheduler = details.createCouplingPortScheduler("sched")
        scheduler.setPortScheduler(_literal("scheduler1"))
        parent = _parent()
        writer.writeCouplingPortScheduler(parent, scheduler)
        assert parent[0].tag == "COUPLING-PORT-SCHEDULER"
        assert parent[0].find("PORT-SCHEDULER").text == "scheduler1"

    def test_none(self, writer):
        parent = _parent()
        writer.writeCouplingPortScheduler(parent, None)
        assert len(parent) == 0


class TestWriterCouplingPortDetailsStructuralElements:
    def test_dispatches_fifo_and_scheduler(self, writer):
        details = CouplingPortDetails()
        details.createCouplingPortFifo("fifo")
        details.createCouplingPortScheduler("sched")
        parent = _parent()
        writer.writeCouplingPortDetailsCouplingPortStructuralElements(
            parent, details
        )
        assert parent[0].tag == "COUPLING-PORT-STRUCTURAL-ELEMENTS"
        tags = {c.tag for c in parent[0]}
        assert "COUPLING-PORT-FIFO" in tags
        assert "COUPLING-PORT-SCHEDULER" in tags

    def test_empty(self, writer):
        details = CouplingPortDetails()
        parent = _parent()
        writer.writeCouplingPortDetailsCouplingPortStructuralElements(
            parent, details
        )
        assert len(parent) == 0


class TestWriterEthernetPriorityRegeneration:
    def test_regen(self, writer):
        details = CouplingPortDetails()
        regen = details.createEthernetPriorityRegeneration("regen")
        regen.setIngressPriority(_posint(1))
        regen.setRegeneratedPriority(_posint(2))
        parent = _parent()
        writer.writeEthernetPriorityRegeneration(parent, regen)
        assert parent[0].tag == "ETHERNET-PRIORITY-REGENERATION"
        assert parent[0].find("INGRESS-PRIORITY") is not None
        assert parent[0].find("REGENERATED-PRIORITY") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEthernetPriorityRegeneration(parent, None)
        assert len(parent) == 0


class TestWriterCouplingPortDetailsEthernetPriorityRegenerations:
    def test_with_regen(self, writer):
        details = CouplingPortDetails()
        details.createEthernetPriorityRegeneration("r1")
        parent = _parent()
        writer.writeCouplingPortDetailsEthernetPriorityRegenerations(
            parent, details
        )
        assert parent[0].tag == "ETHERNET-PRIORITY-REGENERATIONS"
        assert parent[0].find("ETHERNET-PRIORITY-REGENERATION") is not None

    def test_empty(self, writer):
        details = CouplingPortDetails()
        parent = _parent()
        writer.writeCouplingPortDetailsEthernetPriorityRegenerations(
            parent, details
        )
        assert len(parent) == 0


class TestWriterSetCouplingPortDetails:
    def test_with_details(self, writer):
        details = CouplingPortDetails()
        details.createCouplingPortFifo("fifo")
        details.createEthernetPriorityRegeneration("r1")
        details.setLastEgressSchedulerRef(
            _ref("/les", "COUPLING-PORT-SCHEDULER")
        )
        parent = _parent()
        writer.setCouplingPortDetails(
            parent, "COUPLING-PORT-DETAILS", details
        )
        assert parent[0].tag == "COUPLING-PORT-DETAILS"
        assert parent[0].find("COUPLING-PORT-STRUCTURAL-ELEMENTS") is not None
        assert parent[0].find("ETHERNET-PRIORITY-REGENERATIONS") is not None
        assert parent[0].find("LAST-EGRESS-SCHEDULER-REF") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.setCouplingPortDetails(
            parent, "COUPLING-PORT-DETAILS", None
        )
        assert len(parent) == 0


class TestWriterVlanMembership:
    def test_membership(self, writer):
        membership = VlanMembership()
        membership.setSendActivity(_literal("tagged"))
        membership.setVlanRef(_ref("/vlan", "VLAN-CONFIG"))
        parent = _parent()
        writer.writeVlanMembership(parent, membership)
        assert parent[0].tag == "VLAN-MEMBERSHIP"
        assert parent[0].find("SEND-ACTIVITY").text == "tagged"
        assert parent[0].find("VLAN-REF") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeVlanMembership(parent, None)
        assert len(parent) == 0


class TestWriterCouplingPortVlanMemberships:
    def test_with_memberships(self, writer):
        controller = _make_ethernet_communication_controller()
        port = controller.createCouplingPort("cp")
        port.addVlanMembership(VlanMembership())
        parent = _parent()
        writer.writeCouplingPortVlanMemberships(parent, port)
        assert parent[0].tag == "VLAN-MEMBERSHIPS"
        assert parent[0].find("VLAN-MEMBERSHIP") is not None

    def test_empty(self, writer):
        controller = _make_ethernet_communication_controller()
        port = controller.createCouplingPort("cp")
        parent = _parent()
        writer.writeCouplingPortVlanMemberships(parent, port)
        assert len(parent) == 0


class TestWriterCouplingPort:
    def test_full(self, writer):
        controller = _make_ethernet_communication_controller()
        port = controller.createCouplingPort("cp")
        details = CouplingPortDetails()
        details.createCouplingPortFifo("fifo")
        port.setCouplingPortDetails(details)
        port.setMacLayerType(_literal("ethernet"))
        port.addVlanMembership(VlanMembership())
        parent = _parent()
        writer.writeCouplingPort(parent, port)
        assert parent[0].tag == "COUPLING-PORT"
        assert parent[0].find("COUPLING-PORT-DETAILS") is not None
        assert parent[0].find("MAC-LAYER-TYPE").text == "ethernet"
        assert parent[0].find("VLAN-MEMBERSHIPS") is not None


class TestWriterEthernetCommunicationControllerCouplingPorts:
    def test_with_ports(self, writer):
        controller = _make_ethernet_communication_controller()
        controller.createCouplingPort("cp1")
        parent = _parent()
        writer.writeEthernetCommunicationControllerCouplingPorts(
            parent, controller
        )
        assert parent[0].tag == "COUPLING-PORTS"
        assert parent[0].find("COUPLING-PORT") is not None

    def test_empty(self, writer):
        controller = _make_ethernet_communication_controller()
        parent = _parent()
        writer.writeEthernetCommunicationControllerCouplingPorts(
            parent, controller
        )
        assert len(parent) == 0


class TestWriterEthernetCommunicationController:
    def test_full(self, writer):
        controller = _make_ethernet_communication_controller()
        controller.setWakeUpByControllerSupported(_bool(True))
        controller.createCouplingPort("cp")
        parent = _parent()
        writer.writeEthernetCommunicationController(parent, controller)
        assert parent[0].tag == "ETHERNET-COMMUNICATION-CONTROLLER"
        cond = parent[0].find(
            "ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS"
            "/ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL"
        )
        assert cond is not None
        assert cond.find("WAKE-UP-BY-CONTROLLER-SUPPORTED") is not None
        assert cond.find("COUPLING-PORTS") is not None


class TestWriterEcuInstanceCommControllers:
    def test_dispatches_all_controller_types(self, writer):
        instance = _make_ecu_instance()
        instance.createCanCommunicationController("can")
        instance.createEthernetCommunicationController("eth")
        instance.createLinMaster("lin")
        instance.createFlexrayCommunicationController("flex")
        parent = _parent()
        writer.writeEcuInstanceCommControllers(parent, instance)
        assert parent[0].tag == "COMM-CONTROLLERS"
        tags = {c.tag for c in parent[0]}
        assert "CAN-COMMUNICATION-CONTROLLER" in tags
        assert "ETHERNET-COMMUNICATION-CONTROLLER" in tags
        assert "LIN-MASTER" in tags
        assert "FLEXRAY-COMMUNICATION-CONTROLLER" in tags

    def test_empty(self, writer):
        instance = _make_ecu_instance()
        parent = _parent()
        writer.writeEcuInstanceCommControllers(parent, instance)
        assert len(parent) == 0


class TestWriterCommunicationConnector:
    def test_full(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createCanCommunicationConnector("cc")
        connector.setCommControllerRef(
            _ref("/ctrl", "CAN-COMMUNICATION-CONTROLLER")
        )
        connector.setPncGatewayType(_literal("active"))
        connector.createFramePort("fp")
        parent = _parent()
        writer.writeCommunicationConnector(parent, connector)
        assert parent.find("COMM-CONTROLLER-REF") is not None
        assert parent.find("ECU-COMM-PORT-INSTANCES") is not None
        assert parent.find("PNC-GATEWAY-TYPE").text == "active"


class TestWriterCanCommunicationConnector:
    def test_can_connector(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createCanCommunicationConnector("cc")
        connector.setCommControllerRef(
            _ref("/ctrl", "CAN-COMMUNICATION-CONTROLLER")
        )
        parent = _parent()
        writer.writeCanCommunicationConnector(parent, connector)
        assert parent.find("COMM-CONTROLLER-REF") is not None


class TestWriterEthernetCommunicationConnector:
    def test_full(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createEthernetCommunicationConnector("ec")
        connector.setCommControllerRef(
            _ref("/ctrl", "ETHERNET-COMMUNICATION-CONTROLLER")
        )
        connector.setMaximumTransmissionUnit(_posint(1500))
        connector.addNetworkEndpointRef(
            _ref("/ne", "NETWORK-ENDPOINT")
        )
        parent = _parent()
        writer.writeEthernetCommunicationConnector(parent, connector)
        assert parent.find("COMM-CONTROLLER-REF") is not None
        assert parent.find("MAXIMUM-TRANSMISSION-UNIT") is not None
        assert parent.find("NETWORK-ENDPOINT-REFS") is not None


class TestWriterEthernetCommunicationConnectorNetworkEndpointRefs:
    def test_with_refs(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createEthernetCommunicationConnector("ec")
        connector.addNetworkEndpointRef(
            _ref("/ne1", "NETWORK-ENDPOINT")
        )
        connector.addNetworkEndpointRef(
            _ref("/ne2", "NETWORK-ENDPOINT")
        )
        parent = _parent()
        writer.writeEthernetCommunicationConnectorNetworkEndpointRefs(
            parent, connector
        )
        assert parent[0].tag == "NETWORK-ENDPOINT-REFS"
        refs = parent[0].findall("NETWORK-ENDPOINT-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createEthernetCommunicationConnector("ec")
        parent = _parent()
        writer.writeEthernetCommunicationConnectorNetworkEndpointRefs(
            parent, connector
        )
        assert len(parent) == 0


class TestWriterLinCommunicationConnector:
    def test_lin_connector(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createLinCommunicationConnector("lc")
        connector.setCommControllerRef(_ref("/ctrl", "LIN-MASTER"))
        parent = _parent()
        writer.writeLinCommunicationConnector(parent, connector)
        assert parent.find("COMM-CONTROLLER-REF") is not None


class TestWriterFlexrayCommunicationConnector:
    def test_flexray_connector(self, writer):
        instance = _make_ecu_instance()
        connector = instance.createFlexrayCommunicationConnector("fc")
        connector.setCommControllerRef(
            _ref("/ctrl", "FLEXRAY-COMMUNICATION-CONTROLLER")
        )
        parent = _parent()
        writer.writeFlexrayCommunicationConnector(parent, connector)
        assert parent.find("COMM-CONTROLLER-REF") is not None


class TestWriterEcuInstanceConnectors:
    def test_dispatches_all_connector_types(self, writer):
        instance = _make_ecu_instance()
        instance.createCanCommunicationConnector("cc")
        instance.createEthernetCommunicationConnector("ec")
        instance.createLinCommunicationConnector("lc")
        instance.createFlexrayCommunicationConnector("fc")
        parent = _parent()
        writer.writeEcuInstanceConnectors(parent, instance)
        assert parent[0].tag == "CONNECTORS"
        tags = {c.tag for c in parent[0]}
        assert "CAN-COMMUNICATION-CONNECTOR" in tags
        assert "ETHERNET-COMMUNICATION-CONNECTOR" in tags
        assert "LIN-COMMUNICATION-CONNECTOR" in tags
        assert "FLEXRAY-COMMUNICATION-CONNECTOR" in tags

    def test_empty(self, writer):
        instance = _make_ecu_instance()
        parent = _parent()
        writer.writeEcuInstanceConnectors(parent, instance)
        assert len(parent) == 0


class TestWriterEcuInstanceAssociatedComIPduGroupRefs:
    def test_with_refs(self, writer):
        instance = _make_ecu_instance()
        instance.addAssociatedComIPduGroupRef(
            _ref("/g1", "I-SIGNAL-I-PDU-GROUP")
        )
        instance.addAssociatedComIPduGroupRef(
            _ref("/g2", "I-SIGNAL-I-PDU-GROUP")
        )
        parent = _parent()
        writer.writeEcuInstanceAssociatedComIPduGroupRefs(parent, instance)
        assert parent[0].tag == "ASSOCIATED-COM-I-PDU-GROUP-REFS"
        refs = parent[0].findall("ASSOCIATED-COM-I-PDU-GROUP-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        instance = _make_ecu_instance()
        parent = _parent()
        writer.writeEcuInstanceAssociatedComIPduGroupRefs(parent, instance)
        assert len(parent) == 0


class TestWriterEcuInstance:
    def test_full(self, writer):
        instance = _make_ecu_instance()
        instance.addAssociatedComIPduGroupRef(
            _ref("/g", "I-SIGNAL-I-PDU-GROUP")
        )
        instance.setComConfigurationGwTimeBase(_time(0.1))
        instance.setComConfigurationRxTimeBase(_time(0.2))
        instance.setComConfigurationTxTimeBase(_time(0.3))
        instance.setComEnableMDTForCyclicTransmission(_bool(True))
        instance.createCanCommunicationController("can")
        instance.createCanCommunicationConnector("cc")
        instance.setDiagnosticAddress(_int(1))
        instance.setSleepModeSupported(_bool(True))
        instance.setWakeUpOverBusSupported(_bool(False))
        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ei = parent[0]
        assert ei.tag == "ECU-INSTANCE"
        assert ei.find("ASSOCIATED-COM-I-PDU-GROUP-REFS") is not None
        assert ei.find("COM-CONFIGURATION-GW-TIME-BASE") is not None
        assert ei.find("COM-CONFIGURATION-RX-TIME-BASE") is not None
        assert ei.find("COM-CONFIGURATION-TX-TIME-BASE") is not None
        assert ei.find(
            "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION"
        ) is not None
        assert ei.find("COMM-CONTROLLERS") is not None
        assert ei.find("CONNECTORS") is not None
        assert ei.find("DIAGNOSTIC-ADDRESS") is not None
        assert ei.find("SLEEP-MODE-SUPPORTED") is not None
        assert ei.find("WAKE-UP-OVER-BUS-SUPPORTED") is not None
