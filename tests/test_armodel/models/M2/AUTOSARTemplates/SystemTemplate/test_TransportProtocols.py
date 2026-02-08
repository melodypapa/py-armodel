import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
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


class Test_TransportProtocols:
    """Test cases for TransportProtocols-related classes."""

    def test_TpConfig(self):
        """Test TpConfig abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            TpConfig(parent, "test_tp_config")

    def test_CanTpAddress(self):
        """Test CanTpAddress class functionality."""
        parent = MockParent()
        address = CanTpAddress(parent, "test_can_tp_address")

        assert isinstance(address, Identifiable)

        # Test default values
        assert address.getTpAddress() is None
        assert address.getTpAddressExtensionValue() is None

        # Test setter/getter methods
        address.setTpAddress(123)
        assert address.getTpAddress() == 123

        address.setTpAddressExtensionValue(456)
        assert address.getTpAddressExtensionValue() == 456

    def test_CanTpChannel(self):
        """Test CanTpChannel class functionality."""
        parent = MockParent()
        channel = CanTpChannel(parent, "test_can_tp_channel")

        assert isinstance(channel, Identifiable)

        # Test default values
        assert channel.getChannelId() is None
        assert channel.getChannelMode() is None

        # Test setter/getter methods
        channel.setChannelId(1)
        assert channel.getChannelId() == 1

        channel.setChannelMode("normal")
        assert channel.getChannelMode() == "normal"

    def test_TpConnectionIdent(self):
        """Test TpConnectionIdent class functionality."""
        parent = MockParent()
        ident = TpConnectionIdent(parent, "test_tp_connection_ident")

        assert isinstance(ident, Referrable)

    def test_TpConnection(self):
        """Test TpConnection abstract class instantiation."""
        with pytest.raises(TypeError):
            TpConnection()

    def test_CanTpConnection(self):
        """Test CanTpConnection class functionality."""
        connection = CanTpConnection()

        assert isinstance(connection, TpConnection)

        # Test default values
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

        # Test setter/getter methods
        connection.setAddressingFormat("extended")
        assert connection.getAddressingFormat() == "extended"

        connection.setCancellation(True)
        assert connection.getCancellation() is True

        # Test adding receiver refs
        mock_receiver_ref = "receiver_ref"
        connection.addReceiverRef(mock_receiver_ref)
        assert connection.getReceiverRefs() == [mock_receiver_ref]

        connection.setTaType("physical")
        assert connection.getTaType() == "physical"

    def test_CanTpEcu(self):
        """Test CanTpEcu class functionality."""
        ecu = CanTpEcu()

        assert isinstance(ecu, ARObject)

        # Test default values
        assert ecu.getCycleTimeMainFunction() is None
        assert ecu.getEcuInstanceRef() is None

        # Test setter/getter methods
        ecu.setCycleTimeMainFunction("10ms")
        assert ecu.getCycleTimeMainFunction() == "10ms"

        ecu.setEcuInstanceRef("ecu_ref")
        assert ecu.getEcuInstanceRef() == "ecu_ref"

    def test_CanTpNode(self):
        """Test CanTpNode class functionality."""
        parent = MockParent()
        node = CanTpNode(parent, "test_can_tp_node")

        assert isinstance(node, Identifiable)

        # Test default values
        assert node.getConnectorRef() is None
        assert node.getMaxFcWait() is None
        assert node.getStMin() is None
        assert node.getTimeoutAr() is None
        assert node.getTimeoutAs() is None
        assert node.getTpAddressRef() is None

        # Test setter/getter methods
        node.setConnectorRef("connector_ref")
        assert node.getConnectorRef() == "connector_ref"

        node.setMaxFcWait(10)
        assert node.getMaxFcWait() == 10

        node.setStMin("5ms")
        assert node.getStMin() == "5ms"

    def test_CanTpConfig(self):
        """Test CanTpConfig class functionality."""
        parent = MockParent()
        config = CanTpConfig(parent, "test_can_tp_config")

        assert isinstance(config, FibexElement)

        # Test default values
        assert config.getTpAddresses() == []
        assert config.getTpChannels() == []
        assert config.getTpConnections() == []
        assert config.getTpEcus() == []
        assert config.getTpNodes() == []

        # Test communicationClusterRef getter and setter to cover lines 28, 31-33
        assert config.getCommunicationClusterRef() is None

        result = config.setCommunicationClusterRef("cluster_ref")
        assert config.getCommunicationClusterRef() == "cluster_ref"
        assert result == config  # Test method chaining

        # Test setting None (should not change the value due to if value is not None check)
        result = config.setCommunicationClusterRef(None)
        assert config.getCommunicationClusterRef() == "cluster_ref"  # Value remains unchanged
        assert result == config  # Test method chaining

    def test_DoIpLogicAddress(self):
        """Test DoIpLogicAddress class functionality."""
        parent = MockParent()
        address = DoIpLogicAddress(parent, "test_doip_logic_address")

        assert isinstance(address, Identifiable)

        # Test default values
        assert address.getAddress() is None
        assert address.getDoIpLogicAddressProps() is None

        # Test setter/getter methods
        address.setAddress(123)
        assert address.getAddress() == 123

        # Note: Creating a mock for AbstractDoIpLogicAddressProps since it's also abstract
        class MockDoIpLogicAddressProps(AbstractDoIpLogicAddressProps):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        mock_props = MockDoIpLogicAddressProps(parent, "mock_props")
        address.setDoIpLogicAddressProps(mock_props)
        assert address.getDoIpLogicAddressProps() == mock_props

    def test_DoIpTpConnection(self):
        """Test DoIpTpConnection class functionality."""
        connection = DoIpTpConnection()

        assert isinstance(connection, TpConnection)

        # Test default values
        assert connection.getDoIpSourceAddressRef() is None
        assert connection.getDoIpTargetAddressRef() is None
        assert connection.getTpSduRef() is None

        # Test setter/getter methods
        connection.setDoIpSourceAddressRef("src_ref")
        assert connection.getDoIpSourceAddressRef() == "src_ref"

        connection.setDoIpTargetAddressRef("target_ref")
        assert connection.getDoIpTargetAddressRef() == "target_ref"

        connection.setTpSduRef("sdu_ref")
        assert connection.getTpSduRef() == "sdu_ref"

    def test_DoIpTpConfig(self):
        """Test DoIpTpConfig class functionality."""
        parent = MockParent()
        config = DoIpTpConfig(parent, "test_doip_tp_config")

        assert isinstance(config, FibexElement)

        # Test default values
        assert config.getDoIpLogicAddresses() == []
        assert config.getTpConnections() == []

    def test_TpAddress(self):
        """Test TpAddress class functionality."""
        parent = MockParent()
        address = TpAddress(parent, "test_tp_address")

        assert isinstance(address, Identifiable)

        # Test default values
        assert address.getTpAddress() is None

        # Test setter/getter methods
        address.setTpAddress(456)
        assert address.getTpAddress() == 456

    def test_LinTpConnection(self):
        """Test LinTpConnection class functionality."""
        connection = LinTpConnection()

        assert isinstance(connection, TpConnection)

        # Test default values
        assert connection.getDataPduRef() is None
        assert connection.getFlowControlRef() is None
        assert connection.getLinTpNSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReceiverRefs() == []
        assert connection.getTimeoutAs() is None
        assert connection.getTimeoutCr() is None
        assert connection.getTimeoutCs() is None
        assert connection.getTransmitterRef() is None

        # Test setter/getter methods
        connection.setDataPduRef("data_pdu_ref")
        assert connection.getDataPduRef() == "data_pdu_ref"

        # Test adding receiver refs
        mock_receiver_ref = "receiver_ref"
        connection.addReceiverRef(mock_receiver_ref)
        assert connection.getReceiverRefs() == [mock_receiver_ref]

    def test_LinTpNode(self):
        """Test LinTpNode class functionality."""
        parent = MockParent()
        node = LinTpNode(parent, "test_lin_tp_node")

        assert isinstance(node, Identifiable)

        # Test default values
        assert node.getConnectorRef() is None
        assert node.getDropNotRequestedNad() is None
        assert node.getMaxNumberOfRespPendingFrames() is None
        assert node.getP2Max() is None
        assert node.getP2Timing() is None
        assert node.getTpAddressRef() is None

        # Test setter/getter methods
        node.setConnectorRef("connector_ref")
        assert node.getConnectorRef() == "connector_ref"

        node.setDropNotRequestedNad(True)
        assert node.getDropNotRequestedNad() is True

        node.setMaxNumberOfRespPendingFrames(5)
        assert node.getMaxNumberOfRespPendingFrames() == 5

    def test_LinTpConfig(self):
        """Test LinTpConfig class functionality."""
        parent = MockParent()
        config = LinTpConfig(parent, "test_lin_tp_config")

        assert isinstance(config, FibexElement)

        # Test default values
        assert config.getTpAddresses() == []
        assert config.getTpConnections() == []
        assert config.getTpNodes() == []
