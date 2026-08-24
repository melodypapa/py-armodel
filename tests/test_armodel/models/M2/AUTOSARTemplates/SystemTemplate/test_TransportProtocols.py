import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection, TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIp import AbstractDoIpLogicAddressProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddress,
    CanTpAddressingFormatType,
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
    NetworkTargetAddressType,
    TpAddress,
    TpConfig,
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

    def test_CanTpAddress_initialization(self):
        """Test CanTpAddress default state (Table 6.255)."""
        parent = MockParent()
        address = CanTpAddress(parent, "CanTpAddress")

        assert isinstance(address, Identifiable)
        assert address.getTpAddress() is None
        assert address.getTpAddressExtensionValue() is None

    def test_CanTpAddress_get_set_tpAddress(self):
        """Test tpAddress getter/setter with None no-op (Table 6.255)."""
        parent = MockParent()
        address = CanTpAddress(parent, "CanTpAddress")

        assert address == address.setTpAddress(Integer().setValue(0x7FF))
        assert address.getTpAddress().getValue() == 0x7FF
        assert address == address.setTpAddress(None)
        assert address.getTpAddress().getValue() == 0x7FF

    def test_CanTpAddress_get_set_tpAddressExtensionValue(self):
        """Test tpAddressExtensionValue getter/setter with None no-op (Table 6.255)."""
        parent = MockParent()
        address = CanTpAddress(parent, "CanTpAddress")

        assert address == address.setTpAddressExtensionValue(Integer().setValue(6))
        assert address.getTpAddressExtensionValue().getValue() == 6
        assert address == address.setTpAddressExtensionValue(None)
        assert address.getTpAddressExtensionValue().getValue() == 6

    def test_CanTpChannel_initialization(self):
        """Test CanTpChannel default state (Table 6.252)."""
        parent = MockParent()
        channel = CanTpChannel(parent, "CanTpChannel")

        assert isinstance(channel, Identifiable)
        assert channel.getChannelId() is None

    def test_CanTpChannel_get_set_channelId(self):
        """Test channelId getter/setter with None no-op (Table 6.252)."""
        parent = MockParent()
        channel = CanTpChannel(parent, "CanTpChannel")

        assert channel == channel.setChannelId(PositiveInteger().setValue(1))
        assert channel.getChannelId().getValue() == 1
        assert channel == channel.setChannelId(None)
        assert channel.getChannelId().getValue() == 1

    def test_TpConnectionIdent_initialization(self):
        """Test TpConnectionIdent default state (Table 6.273)."""
        parent = MockParent()
        ident = TpConnectionIdent(parent, "TpConnectionIdent")

        assert isinstance(ident, Referrable)

    def test_TpConnection_abstract(self):
        """Test TpConnection abstract class instantiation (Table 6.272)."""
        with pytest.raises(TypeError):
            TpConnection()

    def test_TpConnection_create_ident(self):
        """Test TpConnection ident creation via concrete subclass (Table 6.272)."""
        connection = CanTpConnection()

        assert connection.getIdent() is None
        ident = connection.createTpConnectionIdent("connIdent")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() == ident
        assert connection.createTpConnectionIdent("other") == ident

    def test_CanTpAddressingFormatType(self):
        """Test CanTpAddressingFormatType enum (Table 6.254)."""
        enum = CanTpAddressingFormatType()
        assert enum is not None
        enum.setValue(CanTpAddressingFormatType.ENUM_STANDARD)
        assert enum.getValue() == "STANDARD"

        assert CanTpAddressingFormatType.ENUM_EXTENDED == "EXTENDED"
        assert CanTpAddressingFormatType.ENUM_MIXED == "MIXED"
        assert CanTpAddressingFormatType.ENUM_MIXED_29BIT == "MIXED-29-BIT"
        assert CanTpAddressingFormatType.ENUM_NORMALFIXED == "NORMALFIXED"
        assert CanTpAddressingFormatType.ENUM_STANDARD == "STANDARD"

        assert len(enum.getEnumValues()) == 5
        for literal in (
            CanTpAddressingFormatType.ENUM_EXTENDED,
            CanTpAddressingFormatType.ENUM_MIXED,
            CanTpAddressingFormatType.ENUM_MIXED_29BIT,
            CanTpAddressingFormatType.ENUM_NORMALFIXED,
            CanTpAddressingFormatType.ENUM_STANDARD,
        ):
            assert literal in enum.getEnumValues()

    def test_NetworkTargetAddressType(self):
        """Test NetworkTargetAddressType enum (Table 6.258)."""
        enum = NetworkTargetAddressType()
        assert enum is not None
        enum.setValue(NetworkTargetAddressType.ENUM_PHYSICAL)
        assert enum.getValue() == "PHYSICAL"

        assert NetworkTargetAddressType.ENUM_FUNCTIONAL == "FUNCTIONAL"
        assert NetworkTargetAddressType.ENUM_PHYSICAL == "PHYSICAL"

        assert len(enum.getEnumValues()) == 2
        for literal in (
            NetworkTargetAddressType.ENUM_FUNCTIONAL,
            NetworkTargetAddressType.ENUM_PHYSICAL,
        ):
            assert literal in enum.getEnumValues()

    def test_CanTpConnection_initialization(self):
        """Test CanTpConnection default state (Table 6.253)."""
        connection = CanTpConnection()

        assert isinstance(connection, TpConnection)
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

    def test_CanTpConnection_get_set_attributes(self):
        """Test CanTpConnection attribute getters/setters with None no-op (Table 6.253)."""
        connection = CanTpConnection()

        fmt = CanTpAddressingFormatType()
        fmt.setValue(CanTpAddressingFormatType.ENUM_STANDARD)
        assert connection == connection.setAddressingFormat(fmt)
        assert isinstance(connection.getAddressingFormat(), CanTpAddressingFormatType)
        assert connection.getAddressingFormat() == fmt
        assert connection == connection.setAddressingFormat(None)
        assert connection.getAddressingFormat() == fmt

        assert connection == connection.setCancellation(Boolean().setValue(True))
        assert connection.getCancellation().getValue() is True
        assert connection == connection.setCancellation(None)
        assert connection.getCancellation().getValue() is True

        assert connection == connection.setMaxBlockSize(Integer().setValue(8))
        assert connection.getMaxBlockSize().getValue() == 8
        assert connection == connection.setMaxBlockSize(None)
        assert connection.getMaxBlockSize().getValue() == 8

        assert connection == connection.setPaddingActivation(Boolean().setValue(False))
        assert connection.getPaddingActivation().getValue() is False
        assert connection == connection.setPaddingActivation(None)
        assert connection.getPaddingActivation().getValue() is False

        ta = ARLiteral()
        ta.setValue(NetworkTargetAddressType.ENUM_PHYSICAL)
        assert connection == connection.setTaType(ta)
        assert connection.getTaType() == ta
        assert connection == connection.setTaType(None)
        assert connection.getTaType() == ta

    def test_CanTpConnection_get_set_timeouts(self):
        """Test CanTpConnection timeout getters/setters with None no-op (Table 6.253)."""
        connection = CanTpConnection()

        for setter, getter in (
            ("setTimeoutBr", "getTimeoutBr"),
            ("setTimeoutBs", "getTimeoutBs"),
            ("setTimeoutCr", "getTimeoutCr"),
            ("setTimeoutCs", "getTimeoutCs"),
        ):
            value = TimeValue().setValue(0.1)
            assert getattr(connection, setter)(value) == connection
            assert getattr(connection, getter)().getValue() == 0.1
            getattr(connection, setter)(None)
            assert getattr(connection, getter)().getValue() == 0.1

    def test_CanTpConnection_get_set_refs(self):
        """Test CanTpConnection reference getters/setters with None no-op (Table 6.253)."""
        connection = CanTpConnection()

        channel_ref = RefType()
        channel_ref.setValue("/CanTpChannel")
        assert connection == connection.setCanTpChannelRef(channel_ref)
        assert connection.getCanTpChannelRef() == channel_ref
        assert connection == connection.setCanTpChannelRef(None)
        assert connection.getCanTpChannelRef() == channel_ref

        for setter, getter, path in (
            ("setDataPduRef", "getDataPduRef", "/DataPdu"),
            ("setFlowControlPduRef", "getFlowControlPduRef", "/FcPdu"),
            ("setMulticastRef", "getMulticastRef", "/Multicast"),
            ("setTpSduRef", "getTpSduRef", "/TpSdu"),
            ("setTransmitterRef", "getTransmitterRef", "/TxNode"),
        ):
            ref = RefType()
            ref.setValue(path)
            assert getattr(connection, setter)(ref) == connection
            assert getattr(connection, getter)() == ref
            getattr(connection, setter)(None)
            assert getattr(connection, getter)() == ref

    def test_CanTpConnection_receiver_refs(self):
        """Test receiverRefs add with None no-op (Table 6.253)."""
        connection = CanTpConnection()

        ref1 = RefType()
        ref1.setValue("/r1")
        assert connection == connection.addReceiverRef(ref1)
        assert connection.getReceiverRefs() == [ref1]
        assert connection == connection.addReceiverRef(None)
        assert connection.getReceiverRefs() == [ref1]

    def test_CanTpEcu_initialization(self):
        """Test CanTpEcu default state (Table 6.256)."""
        ecu = CanTpEcu()

        assert isinstance(ecu, ARObject)
        assert ecu.getCycleTimeMainFunction() is None
        assert ecu.getEcuInstanceRef() is None

    def test_CanTpEcu_get_set(self):
        """Test CanTpEcu getters/setters with None no-op (Table 6.256)."""
        ecu = CanTpEcu()

        assert ecu == ecu.setCycleTimeMainFunction(TimeValue().setValue(0.01))
        assert ecu.getCycleTimeMainFunction().getValue() == 0.01
        assert ecu == ecu.setCycleTimeMainFunction(None)
        assert ecu.getCycleTimeMainFunction().getValue() == 0.01

        ref = RefType()
        ref.setValue("/EcuInstance")
        assert ecu == ecu.setEcuInstanceRef(ref)
        assert ecu.getEcuInstanceRef() == ref
        assert ecu == ecu.setEcuInstanceRef(None)
        assert ecu.getEcuInstanceRef() == ref

    def test_CanTpNode_initialization(self):
        """Test CanTpNode default state (Table 6.257)."""
        parent = MockParent()
        node = CanTpNode(parent, "CanTpNode")

        assert isinstance(node, Identifiable)
        assert node.getConnectorRef() is None
        assert node.getMaxFcWait() is None
        assert node.getStMin() is None
        assert node.getTimeoutAr() is None
        assert node.getTimeoutAs() is None
        assert node.getTpAddressRef() is None

    def test_CanTpNode_get_set(self):
        """Test CanTpNode getters/setters with None no-op (Table 6.257)."""
        parent = MockParent()
        node = CanTpNode(parent, "CanTpNode")

        connector_ref = RefType()
        connector_ref.setValue("/Connector")
        assert node == node.setConnectorRef(connector_ref)
        assert node.getConnectorRef() == connector_ref
        assert node == node.setConnectorRef(None)
        assert node.getConnectorRef() == connector_ref

        assert node == node.setMaxFcWait(Integer().setValue(10))
        assert node.getMaxFcWait().getValue() == 10
        assert node == node.setMaxFcWait(None)
        assert node.getMaxFcWait().getValue() == 10

        assert node == node.setStMin(TimeValue().setValue(0.005))
        assert node.getStMin().getValue() == 0.005

        for setter, getter in (("setTimeoutAr", "getTimeoutAr"), ("setTimeoutAs", "getTimeoutAs")):
            value = TimeValue().setValue(0.075)
            getattr(node, setter)(value)
            assert getattr(node, getter)().getValue() == 0.075
            getattr(node, setter)(None)
            assert getattr(node, getter)().getValue() == 0.075

        address_ref = RefType()
        address_ref.setValue("/TpAddress")
        assert node == node.setTpAddressRef(address_ref)
        assert node.getTpAddressRef() == address_ref

    def test_CanTpConfig_initialization(self):
        """Test CanTpConfig default state (Table 6.251)."""
        parent = MockParent()
        config = CanTpConfig(parent, "CanTpConfig")

        assert isinstance(config, TpConfig)
        assert config.getTpAddresses() == []
        assert config.getTpChannels() == []
        assert config.getTpConnections() == []
        assert config.getTpEcus() == []
        assert config.getTpNodes() == []

    def test_CanTpConfig_create_address_duplicate_returns_existing(self):
        """Test tpAddress aggregation create (Table 6.251)."""
        parent = MockParent()
        config = CanTpConfig(parent, "CanTpConfig")

        addr = config.createCanTpAddress("Addr")
        assert isinstance(addr, CanTpAddress)
        assert config.getTpAddresses() == [addr]
        assert config.createCanTpAddress("Addr") == addr
        assert len(config.getTpAddresses()) == 1

    def test_CanTpConfig_create_channel_node_duplicate_returns_existing(self):
        """Test tpChannel/tpNode aggregation creates (Table 6.251)."""
        parent = MockParent()
        config = CanTpConfig(parent, "CanTpConfig")

        channel = config.createCanTpChannel("Ch")
        assert isinstance(channel, CanTpChannel)
        assert config.getTpChannels() == [channel]
        assert config.createCanTpChannel("Ch") == channel

        node = config.createCanTpNode("Node")
        assert isinstance(node, CanTpNode)
        assert config.getTpNodes() == [node]
        assert config.createCanTpNode("Node") == node

    def test_CanTpConfig_add_connection_ecu(self):
        """Test tpConnection/tpEcu aggregation adds with None no-op (Table 6.251)."""
        parent = MockParent()
        config = CanTpConfig(parent, "CanTpConfig")

        connection = CanTpConnection()
        assert config == config.addTpConnection(connection)
        assert config.getTpConnections() == [connection]
        assert config == config.addTpConnection(None)
        assert config.getTpConnections() == [connection]

        ecu = CanTpEcu()
        assert config == config.addTpEcu(ecu)
        assert config.getTpEcus() == [ecu]
        assert config == config.addTpEcu(None)
        assert config.getTpEcus() == [ecu]

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

        # Test remaining setters with chaining and round-trip
        assert node == node.setP2Max(TimeValue().setValue("0.05"))
        assert node.getP2Max().getValue() == 0.05

        assert node == node.setP2Timing(TimeValue().setValue("0.02"))
        assert node.getP2Timing().getValue() == 0.02

        ref = RefType()
        ref.setDest("COMMUNICATION-CONNECTOR")
        ref.setValue("/Cluster/Connector")
        assert node == node.setTpAddressRef(ref)
        assert node.getTpAddressRef().getValue() == "/Cluster/Connector"

        # Test None no-op behavior
        node.setP2Max(None)
        assert node.getP2Max().getValue() == 0.05
        node.setP2Timing(None)
        assert node.getP2Timing().getValue() == 0.02
        node.setTpAddressRef(None)
        assert node.getTpAddressRef().getValue() == "/Cluster/Connector"
        node.setConnectorRef(None)
        assert node.getConnectorRef() == "connector_ref"
        node.setDropNotRequestedNad(None)
        assert node.getDropNotRequestedNad() is True
        node.setMaxNumberOfRespPendingFrames(None)
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

        # Test createTpAddress: appends and duplicate returns existing
        address = config.createTpAddress("tpAddr1")
        assert len(config.getTpAddresses()) == 1
        assert config.createTpAddress("tpAddr1") is address
        assert len(config.getTpAddresses()) == 1
        assert isinstance(config.getTpAddresses()[0], TpAddress)

        # Test addTpConnection: appends, None no-op, chaining
        connection = LinTpConnection()
        assert config == config.addTpConnection(connection)
        assert config.getTpConnections() == [connection]
        assert config == config.addTpConnection(None)
        assert config.getTpConnections() == [connection]

        # Test createLinTpNode: appends and duplicate returns existing
        tp_node = config.createLinTpNode("tpNode1")
        assert len(config.getTpNodes()) == 1
        assert config.createLinTpNode("tpNode1") is tp_node
        assert len(config.getTpNodes()) == 1
        assert isinstance(config.getTpNodes()[0], LinTpNode)
