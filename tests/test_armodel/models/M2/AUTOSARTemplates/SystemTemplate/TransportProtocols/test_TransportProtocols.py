import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddress,
    CanTpChannel,
    CanTpConfig,
    CanTpConnection,
    CanTpEcu,
    CanTpNode,
    DoIpLogicAddress,
    DoIpTpConfig,
    DoIpTpConnection,
    LinTpConfig,
    LinTpConnection,
    LinTpNode,
    TpAddress,
    TpConfig,
    TpConnection,
    TpConnectionIdent,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestTransportProtocols:
    """
    Test class for TransportProtocols module functionality.
    This class contains test methods for validating the behavior of
    transport protocol classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_tp_config_abstract(self):
        """
        Test TpConfig abstract class functionality.
        """
        with pytest.raises(TypeError):
            TpConfig(MockParent(), "test_tp_config")

    def test_can_tp_address(self):
        """
        Test CanTpAddress class functionality with method chaining and None handling.
        """
        parent = MockParent()
        address = CanTpAddress(parent, "test_can_tp_address")

        # Test constructor
        assert address is not None

        # Test default values
        assert address.getTpAddress() is None
        assert address.getTpAddressExtensionValue() is None

        # Test setter/getter methods with method chaining - with None values
        assert address == address.setTpAddress(None)
        assert address.getTpAddress() is None

        assert address == address.setTpAddressExtensionValue(None)
        assert address.getTpAddressExtensionValue() is None

        # Test setter/getter methods with method chaining - with actual values
        address.setTpAddress(100)
        assert address.getTpAddress() == 100
        assert address == address.setTpAddress(100)

        address.setTpAddressExtensionValue(50)
        assert address.getTpAddressExtensionValue() == 50
        assert address == address.setTpAddressExtensionValue(50)

    def test_can_tp_channel(self):
        """
        Test CanTpChannel class functionality with method chaining and None handling.
        """
        parent = MockParent()
        channel = CanTpChannel(parent, "test_can_tp_channel")

        # Test constructor
        assert channel is not None

        # Test default values
        assert channel.getChannelId() is None
        assert channel.getChannelMode() is None

        # Test setter/getter methods with method chaining - with None values
        assert channel == channel.setChannelId(None)
        assert channel.getChannelId() is None

        assert channel == channel.setChannelMode(None)
        assert channel.getChannelMode() is None

        # Test setter/getter methods with method chaining - with actual values
        channel.setChannelId(1)
        assert channel.getChannelId() == 1
        assert channel == channel.setChannelId(1)

        channel.setChannelMode("normal")
        assert channel.getChannelMode() == "normal"
        assert channel == channel.setChannelMode("normal")

    def test_tp_connection_ident(self):
        """
        Test TpConnectionIdent class functionality.
        """
        parent = MockParent()
        ident = TpConnectionIdent(parent, "test_tp_connection_ident")

        # Test constructor
        assert ident is not None

    def test_tp_connection_abstract(self):
        """
        Test TpConnection abstract class functionality.
        """
        with pytest.raises(TypeError):
            TpConnection()

    def test_can_tp_connection(self):
        """
        Test CanTpConnection class functionality with method chaining and None handling.
        """
        connection = CanTpConnection()

        # Test constructor
        assert connection is not None

        # Test default values
        assert connection.getIdent() is None
        assert connection.getAddressingFormat() is None
        assert connection.getCancellation() is None
        assert connection.getCanTpChannelRef() is None
        assert connection.getDataPduRef() is None
        assert connection.getFlowControlPduRef() is None
        assert connection.getMaxBlockSize() is None
        assert connection.getMulticastRef() is None
        assert connection.getPaddingActivation() is None
        assert connection.getReceiverRefs() == []
        assert connection.getTaType() is None
        assert connection.getTimeoutBr() is None
        assert connection.getTimeoutBs() is None
        assert connection.getTimeoutCr() is None
        assert connection.getTimeoutCs() is None
        assert connection.getTpSduRef() is None
        assert connection.getTransmitterRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert connection == connection.setAddressingFormat(None)
        assert connection.getAddressingFormat() is None

        assert connection == connection.setCancellation(None)
        assert connection.getCancellation() is None

        assert connection == connection.setCanTpChannelRef(None)
        assert connection.getCanTpChannelRef() is None

        assert connection == connection.setDataPduRef(None)
        assert connection.getDataPduRef() is None

        assert connection == connection.setFlowControlPduRef(None)
        assert connection.getFlowControlPduRef() is None

        assert connection == connection.setMaxBlockSize(None)
        assert connection.getMaxBlockSize() is None

        assert connection == connection.setMulticastRef(None)
        assert connection.getMulticastRef() is None

        assert connection == connection.setPaddingActivation(None)
        assert connection.getPaddingActivation() is None

        assert connection == connection.setTaType(None)
        assert connection.getTaType() is None

        assert connection == connection.setTimeoutBr(None)
        assert connection.getTimeoutBr() is None

        assert connection == connection.setTimeoutBs(None)
        assert connection.getTimeoutBs() is None

        assert connection == connection.setTimeoutCr(None)
        assert connection.getTimeoutCr() is None

        assert connection == connection.setTimeoutCs(None)
        assert connection.getTimeoutCs() is None

        assert connection == connection.setTpSduRef(None)
        assert connection.getTpSduRef() is None

        assert connection == connection.setTransmitterRef(None)
        assert connection.getTransmitterRef() is None

        # Test setter/getter methods with method chaining - with actual values
        connection.setAddressingFormat("format")
        assert connection.getAddressingFormat() == "format"
        assert connection == connection.setAddressingFormat("format")

        connection.setCancellation(True)
        assert connection.getCancellation() is True
        assert connection == connection.setCancellation(True)

        connection.setCanTpChannelRef("channel_ref")
        assert connection.getCanTpChannelRef() == "channel_ref"
        assert connection == connection.setCanTpChannelRef("channel_ref")

        connection.setDataPduRef("data_ref")
        assert connection.getDataPduRef() == "data_ref"
        assert connection == connection.setDataPduRef("data_ref")

        connection.setFlowControlPduRef("flow_ref")
        assert connection.getFlowControlPduRef() == "flow_ref"
        assert connection == connection.setFlowControlPduRef("flow_ref")

        connection.setMaxBlockSize(1024)
        assert connection.getMaxBlockSize() == 1024
        assert connection == connection.setMaxBlockSize(1024)

        connection.setMulticastRef("multicast_ref")
        assert connection.getMulticastRef() == "multicast_ref"
        assert connection == connection.setMulticastRef("multicast_ref")

        connection.setPaddingActivation(True)
        assert connection.getPaddingActivation() is True
        assert connection == connection.setPaddingActivation(True)

        connection.setTaType("type")
        assert connection.getTaType() == "type"
        assert connection == connection.setTaType("type")

        connection.setTimeoutBr(10)
        assert connection.getTimeoutBr() == 10
        assert connection == connection.setTimeoutBr(10)

        connection.setTimeoutBs(20)
        assert connection.getTimeoutBs() == 20
        assert connection == connection.setTimeoutBs(20)

        connection.setTimeoutCr(30)
        assert connection.getTimeoutCr() == 30
        assert connection == connection.setTimeoutCr(30)

        connection.setTimeoutCs(40)
        assert connection.getTimeoutCs() == 40
        assert connection == connection.setTimeoutCs(40)

        connection.setTpSduRef("sdu_ref")
        assert connection.getTpSduRef() == "sdu_ref"
        assert connection == connection.setTpSduRef("sdu_ref")

        connection.setTransmitterRef("transmitter_ref")
        assert connection.getTransmitterRef() == "transmitter_ref"
        assert connection == connection.setTransmitterRef("transmitter_ref")

        # Test addReceiverRef
        connection.addReceiverRef("receiver_ref")
        assert "receiver_ref" in connection.getReceiverRefs()
        assert connection == connection.addReceiverRef("receiver_ref2")

        # Test createTpConnectionIdent
        ident = connection.createTpConnectionIdent("ident_name")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() == ident

    def test_can_tp_ecu(self):
        """
        Test CanTpEcu class functionality with method chaining and None handling.
        """
        ecu = CanTpEcu()

        # Test constructor
        assert ecu is not None

        # Test default values
        assert ecu.getCycleTimeMainFunction() is None
        assert ecu.getEcuInstanceRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert ecu == ecu.setCycleTimeMainFunction(None)
        assert ecu.getCycleTimeMainFunction() is None

        assert ecu == ecu.setEcuInstanceRef(None)
        assert ecu.getEcuInstanceRef() is None

        # Test setter/getter methods with method chaining - with actual values
        ecu.setCycleTimeMainFunction(100)
        assert ecu.getCycleTimeMainFunction() == 100
        assert ecu == ecu.setCycleTimeMainFunction(100)

        ecu.setEcuInstanceRef("ecu_ref")
        assert ecu.getEcuInstanceRef() == "ecu_ref"
        assert ecu == ecu.setEcuInstanceRef("ecu_ref")

    def test_can_tp_node(self):
        """
        Test CanTpNode class functionality with method chaining and None handling.
        """
        parent = MockParent()
        node = CanTpNode(parent, "test_can_tp_node")

        # Test constructor
        assert node is not None

        # Test default values
        assert node.getConnectorRef() is None
        assert node.getMaxFcWait() is None
        assert node.getStMin() is None
        assert node.getTimeoutAr() is None
        assert node.getTimeoutAs() is None
        assert node.getTpAddressRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert node == node.setConnectorRef(None)
        assert node.getConnectorRef() is None

        assert node == node.setMaxFcWait(None)
        assert node.getMaxFcWait() is None

        assert node == node.setStMin(None)
        assert node.getStMin() is None

        assert node == node.setTimeoutAr(None)
        assert node.getTimeoutAr() is None

        assert node == node.setTimeoutAs(None)
        assert node.getTimeoutAs() is None

        assert node == node.setTpAddressRef(None)
        assert node.getTpAddressRef() is None

        # Test setter/getter methods with method chaining - with actual values
        node.setConnectorRef("connector_ref")
        assert node.getConnectorRef() == "connector_ref"
        assert node == node.setConnectorRef("connector_ref")

        node.setMaxFcWait(50)
        assert node.getMaxFcWait() == 50
        assert node == node.setMaxFcWait(50)

        node.setStMin(10)
        assert node.getStMin() == 10
        assert node == node.setStMin(10)

        node.setTimeoutAr(20)
        assert node.getTimeoutAr() == 20
        assert node == node.setTimeoutAr(20)

        node.setTimeoutAs(30)
        assert node.getTimeoutAs() == 30
        assert node == node.setTimeoutAs(30)

        node.setTpAddressRef("address_ref")
        assert node.getTpAddressRef() == "address_ref"
        assert node == node.setTpAddressRef("address_ref")

    def test_can_tp_config(self):
        """
        Test CanTpConfig class functionality.
        """
        parent = MockParent()
        config = CanTpConfig(parent, "test_can_tp_config")

        # Test constructor
        assert config is not None

        # Test default values
        assert config.getTpAddresses() == []
        assert config.getTpChannels() == []
        assert config.getTpConnections() == []
        assert config.getTpEcus() == []
        assert config.getTpNodes() == []

        # Test create methods
        address = config.createCanTpAddress("address_name")
        assert isinstance(address, CanTpAddress)
        assert address in config.getTpAddresses()

        channel = config.createCanTpChannel("channel_name")
        assert isinstance(channel, CanTpChannel)
        assert channel in config.getTpChannels()

        node = config.createCanTpNode("node_name")
        assert isinstance(node, CanTpNode)
        assert node in config.getTpNodes()

        # Test add methods
        connection = CanTpConnection()
        config.addTpConnection(connection)
        assert connection in config.getTpConnections()
        assert config == config.addTpConnection(connection)

        ecu = CanTpEcu()
        config.addTpEcu(ecu)
        assert ecu in config.getTpEcus()
        assert config == config.addTpEcu(ecu)

    def test_do_ip_logic_address(self):
        """
        Test DoIpLogicAddress class functionality with method chaining and None handling.
        """
        parent = MockParent()
        address = DoIpLogicAddress(parent, "test_do_ip_logic_address")

        # Test constructor
        assert address is not None

        # Test default values
        assert address.getAddress() is None
        assert address.getDoIpLogicAddressProps() is None

        # Test setter/getter methods with method chaining - with None values
        assert address == address.setAddress(None)
        assert address.getAddress() is None

        assert address == address.setDoIpLogicAddressProps(None)
        assert address.getDoIpLogicAddressProps() is None

        # Test setter/getter methods with method chaining - with actual values
        address.setAddress(1234)
        assert address.getAddress() == 1234
        assert address == address.setAddress(1234)

        # Note: We can't easily test setDoIpLogicAddressProps with an actual object
        # since AbstractDoIpLogicAddressProps is abstract, but we can test with None
        # which is already tested above

    def test_do_ip_tp_connection(self):
        """
        Test DoIpTpConnection class functionality with method chaining and None handling.
        """
        connection = DoIpTpConnection()

        # Test constructor
        assert connection is not None

        # Test default values
        assert connection.getIdent() is None
        assert connection.getDoIpSourceAddressRef() is None
        assert connection.getDoIpTargetAddressRef() is None
        assert connection.getTpSduRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert connection == connection.setDoIpSourceAddressRef(None)
        assert connection.getDoIpSourceAddressRef() is None

        assert connection == connection.setDoIpTargetAddressRef(None)
        assert connection.getDoIpTargetAddressRef() is None

        assert connection == connection.setTpSduRef(None)
        assert connection.getTpSduRef() is None

        # Test setter/getter methods with method chaining - with actual values
        connection.setDoIpSourceAddressRef("source_ref")
        assert connection.getDoIpSourceAddressRef() == "source_ref"
        assert connection == connection.setDoIpSourceAddressRef("source_ref")

        connection.setDoIpTargetAddressRef("target_ref")
        assert connection.getDoIpTargetAddressRef() == "target_ref"
        assert connection == connection.setDoIpTargetAddressRef("target_ref")

        connection.setTpSduRef("sdu_ref")
        assert connection.getTpSduRef() == "sdu_ref"
        assert connection == connection.setTpSduRef("sdu_ref")

    def test_do_ip_tp_config(self):
        """
        Test DoIpTpConfig class functionality.
        """
        parent = MockParent()
        config = DoIpTpConfig(parent, "test_do_ip_tp_config")

        # Test constructor
        assert config is not None

        # Test default values
        assert config.getDoIpLogicAddresses() == []
        assert config.getTpConnections() == []

        # Test create method
        address = config.createDoIpLogicAddress("address_name")
        assert isinstance(address, DoIpLogicAddress)
        assert address in config.getDoIpLogicAddresses()

        # Test addTpConnection
        connection = DoIpTpConnection()
        config.addTpConnection(connection)
        assert connection in config.getTpConnections()
        assert config == config.addTpConnection(connection)

    def test_tp_address(self):
        """
        Test TpAddress class functionality with method chaining and None handling.
        """
        parent = MockParent()
        address = TpAddress(parent, "test_tp_address")

        # Test constructor
        assert address is not None

        # Test default values
        assert address.getTpAddress() is None

        # Test setter/getter methods with method chaining - with None values
        assert address == address.setTpAddress(None)
        assert address.getTpAddress() is None

        # Test setter/getter methods with method chaining - with actual values
        address.setTpAddress(5678)
        assert address.getTpAddress() == 5678
        assert address == address.setTpAddress(5678)

    def test_lin_tp_connection(self):
        """
        Test LinTpConnection class functionality with method chaining and None handling.
        """
        connection = LinTpConnection()

        # Test constructor
        assert connection is not None

        # Test default values
        assert connection.getIdent() is None
        assert connection.getDataPduRef() is None
        assert connection.getFlowControlRef() is None
        assert connection.getLinTpNSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReceiverRefs() == []
        assert connection.getTimeoutAs() is None
        assert connection.getTimeoutCr() is None
        assert connection.getTimeoutCs() is None
        assert connection.getTransmitterRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert connection == connection.setDataPduRef(None)
        assert connection.getDataPduRef() is None

        assert connection == connection.setFlowControlRef(None)
        assert connection.getFlowControlRef() is None

        assert connection == connection.setLinTpNSduRef(None)
        assert connection.getLinTpNSduRef() is None

        assert connection == connection.setMulticastRef(None)
        assert connection.getMulticastRef() is None

        assert connection == connection.setTimeoutAs(None)
        assert connection.getTimeoutAs() is None

        assert connection == connection.setTimeoutCr(None)
        assert connection.getTimeoutCr() is None

        assert connection == connection.setTimeoutCs(None)
        assert connection.getTimeoutCs() is None

        assert connection == connection.setTransmitterRef(None)
        assert connection.getTransmitterRef() is None

        # Test setter/getter methods with method chaining - with actual values
        connection.setDataPduRef("data_ref")
        assert connection.getDataPduRef() == "data_ref"
        assert connection == connection.setDataPduRef("data_ref")

        connection.setFlowControlRef("flow_ref")
        assert connection.getFlowControlRef() == "flow_ref"
        assert connection == connection.setFlowControlRef("flow_ref")

        connection.setLinTpNSduRef("n_sdu_ref")
        assert connection.getLinTpNSduRef() == "n_sdu_ref"
        assert connection == connection.setLinTpNSduRef("n_sdu_ref")

        connection.setMulticastRef("multicast_ref")
        assert connection.getMulticastRef() == "multicast_ref"
        assert connection == connection.setMulticastRef("multicast_ref")

        connection.setTimeoutAs(10)
        assert connection.getTimeoutAs() == 10
        assert connection == connection.setTimeoutAs(10)

        connection.setTimeoutCr(20)
        assert connection.getTimeoutCr() == 20
        assert connection == connection.setTimeoutCr(20)

        connection.setTimeoutCs(30)
        assert connection.getTimeoutCs() == 30
        assert connection == connection.setTimeoutCs(30)

        connection.setTransmitterRef("transmitter_ref")
        assert connection.getTransmitterRef() == "transmitter_ref"
        assert connection == connection.setTransmitterRef("transmitter_ref")

        # Test addReceiverRef
        connection.addReceiverRef("receiver_ref")
        assert "receiver_ref" in connection.getReceiverRefs()
        assert connection == connection.addReceiverRef("receiver_ref2")

    def test_lin_tp_node(self):
        """
        Test LinTpNode class functionality with method chaining and None handling.
        """
        parent = MockParent()
        node = LinTpNode(parent, "test_lin_tp_node")

        # Test constructor
        assert node is not None

        # Test default values
        assert node.getConnectorRef() is None
        assert node.getDropNotRequestedNad() is None
        assert node.getMaxNumberOfRespPendingFrames() is None
        assert node.getP2Max() is None
        assert node.getP2Timing() is None
        assert node.getTpAddressRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert node == node.setConnectorRef(None)
        assert node.getConnectorRef() is None

        assert node == node.setDropNotRequestedNad(None)
        assert node.getDropNotRequestedNad() is None

        assert node == node.setMaxNumberOfRespPendingFrames(None)
        assert node.getMaxNumberOfRespPendingFrames() is None

        assert node == node.setP2Max(None)
        assert node.getP2Max() is None

        assert node == node.setP2Timing(None)
        assert node.getP2Timing() is None

        assert node == node.setTpAddressRef(None)
        assert node.getTpAddressRef() is None

        # Test setter/getter methods with method chaining - with actual values
        node.setConnectorRef("connector_ref")
        assert node.getConnectorRef() == "connector_ref"
        assert node == node.setConnectorRef("connector_ref")

        node.setDropNotRequestedNad(True)
        assert node.getDropNotRequestedNad() is True
        assert node == node.setDropNotRequestedNad(True)

        node.setMaxNumberOfRespPendingFrames(5)
        assert node.getMaxNumberOfRespPendingFrames() == 5
        assert node == node.setMaxNumberOfRespPendingFrames(5)

        node.setP2Max(100)
        assert node.getP2Max() == 100
        assert node == node.setP2Max(100)

        node.setP2Timing(200)
        assert node.getP2Timing() == 200
        assert node == node.setP2Timing(200)

        node.setTpAddressRef("address_ref")
        assert node.getTpAddressRef() == "address_ref"
        assert node == node.setTpAddressRef("address_ref")

    def test_lin_tp_config(self):
        """
        Test LinTpConfig class functionality.
        """
        parent = MockParent()
        config = LinTpConfig(parent, "test_lin_tp_config")

        # Test constructor
        assert config is not None

        # Test default values
        assert config.getTpAddresses() == []
        assert config.getTpConnections() == []
        assert config.getTpNodes() == []

        # Test create method
        address = config.createTpAddress("address_name")
        assert isinstance(address, TpAddress)
        assert address in config.getTpAddresses()

        node = config.createLinTpNode("node_name")
        assert isinstance(node, LinTpNode)
        assert node in config.getTpNodes()

        # Test addTpConnection
        connection = LinTpConnection()
        config.addTpConnection(connection)
        assert connection in config.getTpConnections()
        assert config == config.addTpConnection(connection)
