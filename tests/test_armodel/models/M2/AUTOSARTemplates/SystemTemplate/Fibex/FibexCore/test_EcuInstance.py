
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanCommunicationConnector,
    CanCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetCommunicationConnector,
    EthernetCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCommunicationConnector,
    LinMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    EcuInstance,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_FibexCoreEcuInstance:
    """Test cases for FibexCore EcuInstance class."""

    def test_EcuInstance(self):
        """Test EcuInstance class functionality."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        assert isinstance(ecu, FibexElement)

        # Test default values
        assert ecu.getAssociatedComIPduGroupRefs() == []
        assert ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs() == []
        assert ecu.getAssociatedPdurIPduGroupRefs() == []
        assert ecu.getChannelSynchronousWakeup() is None
        assert ecu.getClientIdRange() is None
        assert ecu.getComConfigurationGwTimeBase() is None
        assert ecu.getComConfigurationRxTimeBase() is None
        assert ecu.getComConfigurationTxTimeBase() is None
        assert ecu.getComEnableMDTForCyclicTransmission() is None
        assert ecu.getCommControllers() == []
        assert ecu.getConnectors() == []
        assert ecu.getDiagnosticAddress() is None
        assert ecu.getDltConfig() is None
        assert ecu.getDoIpConfig() is None
        assert ecu.getEcuTaskProxyRefs() == []
        assert ecu.getEthSwitchPortGroupDerivation() is None
        assert ecu.getFirewallRuleRef() is None
        assert ecu.getPartitions() == []
        assert ecu.getPncNmRequest() is None
        assert ecu.getPncPrepareSleepTimer() is None
        assert ecu.getPncSynchronousWakeup() is None
        assert ecu.getPnResetTime() is None
        assert ecu.getSleepModeSupported() is None
        assert ecu.getTcpIpIcmpPropsRef() is None
        assert ecu.getTcpIpPropsRef() is None
        assert ecu.getV2xSupported() is None
        assert ecu.getWakeUpOverBusSupported() is None

    def test_EcuInstance_setters_with_none_handling(self):
        """Test EcuInstance setter methods with None values and method chaining."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test setter/getter methods with method chaining - with None values
        # Note: Most setters will set the value to None, but setDiagnosticAddress doesn't change value when None is passed
        assert ecu == ecu.setChannelSynchronousWakeup(None)
        assert ecu.getChannelSynchronousWakeup() is None

        assert ecu == ecu.setClientIdRange(None)
        assert ecu.getClientIdRange() is None

        assert ecu == ecu.setComConfigurationGwTimeBase(None)
        assert ecu.getComConfigurationGwTimeBase() is None

        assert ecu == ecu.setComConfigurationRxTimeBase(None)
        assert ecu.getComConfigurationRxTimeBase() is None

        assert ecu == ecu.setComConfigurationTxTimeBase(None)
        assert ecu.getComConfigurationTxTimeBase() is None

        assert ecu == ecu.setComEnableMDTForCyclicTransmission(None)
        assert ecu.getComEnableMDTForCyclicTransmission() is None

        # Test setDiagnosticAddress with initial value first, then None (doesn't change when None)
        ecu.setDiagnosticAddress(123)
        assert ecu.getDiagnosticAddress() == 123
        assert ecu == ecu.setDiagnosticAddress(None)  # Method chaining still works
        assert ecu.getDiagnosticAddress() == 123  # Value should remain unchanged when None is passed

        assert ecu == ecu.setDltConfig(None)
        assert ecu.getDltConfig() is None

        assert ecu == ecu.setDoIpConfig(None)
        assert ecu.getDoIpConfig() is None

        assert ecu == ecu.setEcuTaskProxyRefs(None)
        assert ecu.getEcuTaskProxyRefs() is None

        assert ecu == ecu.setEthSwitchPortGroupDerivation(None)
        assert ecu.getEthSwitchPortGroupDerivation() is None

        assert ecu == ecu.setFirewallRuleRef(None)
        assert ecu.getFirewallRuleRef() is None

        assert ecu == ecu.setPncNmRequest(None)
        assert ecu.getPncNmRequest() is None

        assert ecu == ecu.setPncPrepareSleepTimer(None)
        assert ecu.getPncPrepareSleepTimer() is None

        assert ecu == ecu.setPncSynchronousWakeup(None)
        assert ecu.getPncSynchronousWakeup() is None

        assert ecu == ecu.setPnResetTime(None)
        assert ecu.getPnResetTime() is None

        assert ecu == ecu.setSleepModeSupported(None)
        assert ecu.getSleepModeSupported() is None

        assert ecu == ecu.setTcpIpIcmpPropsRef(None)
        assert ecu.getTcpIpIcmpPropsRef() is None

        assert ecu == ecu.setTcpIpPropsRef(None)
        assert ecu.getTcpIpPropsRef() is None

        assert ecu == ecu.setV2xSupported(None)
        assert ecu.getV2xSupported() is None

        assert ecu == ecu.setWakeUpOverBusSupported(None)
        assert ecu.getWakeUpOverBusSupported() is None

    def test_EcuInstance_setters_with_actual_values(self):
        """Test EcuInstance setter methods with actual values and method chaining."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test setter/getter methods with method chaining - with actual values
        ecu.setChannelSynchronousWakeup(True)
        assert ecu.getChannelSynchronousWakeup() is True
        assert ecu == ecu.setChannelSynchronousWakeup(True)

        ecu.setClientIdRange("client_range")
        assert ecu.getClientIdRange() == "client_range"
        assert ecu == ecu.setClientIdRange("client_range")

        ecu.setComConfigurationGwTimeBase(100)
        assert ecu.getComConfigurationGwTimeBase() == 100
        assert ecu == ecu.setComConfigurationGwTimeBase(100)

        ecu.setComConfigurationRxTimeBase(200)
        assert ecu.getComConfigurationRxTimeBase() == 200
        assert ecu == ecu.setComConfigurationRxTimeBase(200)

        ecu.setComConfigurationTxTimeBase(300)
        assert ecu.getComConfigurationTxTimeBase() == 300
        assert ecu == ecu.setComConfigurationTxTimeBase(300)

        ecu.setComEnableMDTForCyclicTransmission(False)
        assert ecu.getComEnableMDTForCyclicTransmission() is False
        assert ecu == ecu.setComEnableMDTForCyclicTransmission(False)

        ecu.setDiagnosticAddress(123)
        assert ecu.getDiagnosticAddress() == 123
        assert ecu == ecu.setDiagnosticAddress(123)

        ecu.setDltConfig("dlt_config_value")
        assert ecu.getDltConfig() == "dlt_config_value"
        assert ecu == ecu.setDltConfig("dlt_config_value")

        ecu.setDoIpConfig("doip_config_value")
        assert ecu.getDoIpConfig() == "doip_config_value"
        assert ecu == ecu.setDoIpConfig("doip_config_value")

        ecu.setEcuTaskProxyRefs(["task1", "task2"])
        assert ecu.getEcuTaskProxyRefs() == ["task1", "task2"]
        assert ecu == ecu.setEcuTaskProxyRefs(["task1", "task2"])

        ecu.setEthSwitchPortGroupDerivation(True)
        assert ecu.getEthSwitchPortGroupDerivation() is True
        assert ecu == ecu.setEthSwitchPortGroupDerivation(True)

        ecu.setFirewallRuleRef("firewall_rule")
        assert ecu.getFirewallRuleRef() == "firewall_rule"
        assert ecu == ecu.setFirewallRuleRef("firewall_rule")

        ecu.setPncNmRequest(True)
        assert ecu.getPncNmRequest() is True
        assert ecu == ecu.setPncNmRequest(True)

        ecu.setPncPrepareSleepTimer(500)
        assert ecu.getPncPrepareSleepTimer() == 500
        assert ecu == ecu.setPncPrepareSleepTimer(500)

        ecu.setPncSynchronousWakeup(False)
        assert ecu.getPncSynchronousWakeup() is False
        assert ecu == ecu.setPncSynchronousWakeup(False)

        ecu.setPnResetTime(600)
        assert ecu.getPnResetTime() == 600
        assert ecu == ecu.setPnResetTime(600)

        ecu.setSleepModeSupported(True)
        assert ecu.getSleepModeSupported() is True
        assert ecu == ecu.setSleepModeSupported(True)

        ecu.setTcpIpIcmpPropsRef("tcpip_icmp")
        assert ecu.getTcpIpIcmpPropsRef() == "tcpip_icmp"
        assert ecu == ecu.setTcpIpIcmpPropsRef("tcpip_icmp")

        ecu.setTcpIpPropsRef("tcpip")
        assert ecu.getTcpIpPropsRef() == "tcpip"
        assert ecu == ecu.setTcpIpPropsRef("tcpip")

        ecu.setV2xSupported(True)
        assert ecu.getV2xSupported() is True
        assert ecu == ecu.setV2xSupported(True)

        ecu.setWakeUpOverBusSupported(False)
        assert ecu.getWakeUpOverBusSupported() is False
        assert ecu == ecu.setWakeUpOverBusSupported(False)

    def test_EcuInstance_add_methods(self):
        """Test EcuInstance add methods with method chaining."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test addAssociatedComIPduGroupRef with method chaining
        ecu.addAssociatedComIPduGroupRef("com_ipdu_ref")
        assert "com_ipdu_ref" in ecu.getAssociatedComIPduGroupRefs()
        assert ecu == ecu.addAssociatedComIPduGroupRef("com_ipdu_ref2")
        assert len(ecu.getAssociatedComIPduGroupRefs()) == 2

        # Test addAssociatedConsumedProvidedServiceInstanceGroupRef with method chaining
        ecu.addAssociatedConsumedProvidedServiceInstanceGroupRef("service_instance_ref")
        assert "service_instance_ref" in ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs()
        assert ecu == ecu.addAssociatedConsumedProvidedServiceInstanceGroupRef("service_instance_ref2")
        assert len(ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs()) == 2

        # Test addAssociatedPdurIPduGroupRef with method chaining
        ecu.addAssociatedPdurIPduGroupRef("pdur_ipdu_ref")
        assert "pdur_ipdu_ref" in ecu.getAssociatedPdurIPduGroupRefs()
        assert ecu == ecu.addAssociatedPdurIPduGroupRef("pdur_ipdu_ref2")
        assert len(ecu.getAssociatedPdurIPduGroupRefs()) == 2

        # Test addPartition with method chaining
        ecu.addPartition("partition_value")
        assert "partition_value" in ecu.getPartitions()
        assert ecu == ecu.addPartition("partition_value2")
        assert len(ecu.getPartitions()) == 2

    def test_EcuInstance_create_methods(self):
        """Test EcuInstance create methods for communication controllers and connectors."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test createCanCommunicationController
        controller = ecu.createCanCommunicationController("can_controller_1")
        assert isinstance(controller, CanCommunicationController)
        assert controller.getShortName() == "can_controller_1"
        assert controller in ecu.getCommControllers()

        # Test createEthernetCommunicationController
        eth_controller = ecu.createEthernetCommunicationController("eth_controller_1")
        assert isinstance(eth_controller, EthernetCommunicationController)
        assert eth_controller.getShortName() == "eth_controller_1"
        assert eth_controller in ecu.getCommControllers()

        # Test createLinMaster
        lin_controller = ecu.createLinMaster("lin_controller_1")
        assert isinstance(lin_controller, LinMaster)
        assert lin_controller.getShortName() == "lin_controller_1"
        assert lin_controller in ecu.getCommControllers()

        # Test createFlexrayCommunicationController
        flex_controller = ecu.createFlexrayCommunicationController("flex_controller_1")
        assert isinstance(flex_controller, FlexrayCommunicationController)
        assert flex_controller.getShortName() == "flex_controller_1"
        assert flex_controller in ecu.getCommControllers()

        # Test createCanCommunicationConnector
        connector = ecu.createCanCommunicationConnector("can_connector_1")
        assert isinstance(connector, CanCommunicationConnector)
        assert connector.getShortName() == "can_connector_1"
        assert connector in ecu.getConnectors()

        # Test createEthernetCommunicationConnector
        eth_connector = ecu.createEthernetCommunicationConnector("eth_connector_1")
        assert isinstance(eth_connector, EthernetCommunicationConnector)
        assert eth_connector.getShortName() == "eth_connector_1"
        assert eth_connector in ecu.getConnectors()

        # Test createLinCommunicationConnector
        lin_connector = ecu.createLinCommunicationConnector("lin_connector_1")
        assert isinstance(lin_connector, LinCommunicationConnector)
        assert lin_connector.getShortName() == "lin_connector_1"
        assert lin_connector in ecu.getConnectors()

        # Test createFlexrayCommunicationConnector
        flex_connector = ecu.createFlexrayCommunicationConnector("flex_connector_1")
        assert isinstance(flex_connector, FlexrayCommunicationConnector)
        assert flex_connector.getShortName() == "flex_connector_1"
        assert flex_connector in ecu.getConnectors()
