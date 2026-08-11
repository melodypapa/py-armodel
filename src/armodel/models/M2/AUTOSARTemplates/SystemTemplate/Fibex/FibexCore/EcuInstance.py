from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector, EthernetCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector, CanCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector, FlexrayCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinMaster
from typing import List


class EcuInstance(FibexElement):
    """
    ECUInstances are used to define the ECUs used in the topology.
    The type of the ECU is defined by a reference to an ECU specified
    with the ECU resource description.
    """

    # EcuInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.1, pp.50-52
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAssociatedComIPduGroupRefs [x] impl  [x] docstring  [x] test
    # [x] addAssociatedComIPduGroupRef [x] impl  [x] docstring  [x] test
    # [x] getAssociatedConsumedProvidedServiceInstanceGroupRefs [x] impl  [x] docstring  [x] test
    # [x] addAssociatedConsumedProvidedServiceInstanceGroupRef [x] impl  [x] docstring  [x] test
    # [x] getAssociatedPdurIPduGroupRefs [x] impl  [x] docstring  [x] test
    # [x] addAssociatedPdurIPduGroupRef [x] impl  [x] docstring  [x] test
    # [x] getChannelSynchronousWakeup  [x] impl  [x] docstring  [x] test
    # [x] setChannelSynchronousWakeup  [x] impl  [x] docstring  [x] test
    # [x] getClientIdRange             [x] impl  [x] docstring  [x] test
    # [x] setClientIdRange             [x] impl  [x] docstring  [x] test
    # [x] getComConfigurationGwTimeBase [x] impl  [x] docstring  [x] test
    # [x] setComConfigurationGwTimeBase [x] impl  [x] docstring  [x] test
    # [x] getComConfigurationRxTimeBase [x] impl  [x] docstring  [x] test
    # [x] setComConfigurationRxTimeBase [x] impl  [x] docstring  [x] test
    # [x] getComConfigurationTxTimeBase [x] impl  [x] docstring  [x] test
    # [x] setComConfigurationTxTimeBase [x] impl  [x] docstring  [x] test
    # [x] getComEnableMDTForCyclicTransmission [x] impl  [x] docstring  [x] test
    # [x] setComEnableMDTForCyclicTransmission [x] impl  [x] docstring  [x] test
    # [x] getCommControllers           [x] impl  [x] docstring  [x] test
    # [x] createCanCommunicationController [x] impl  [x] docstring  [x] test
    # [x] createEthernetCommunicationController [x] impl  [x] docstring  [x] test
    # [x] createLinMaster              [x] impl  [x] docstring  [x] test
    # [x] createFlexrayCommunicationController [x] impl  [x] docstring  [x] test
    # [x] getConnectors                [x] impl  [x] docstring  [x] test
    # [x] createCanCommunicationConnector [x] impl  [x] docstring  [x] test
    # [x] createEthernetCommunicationConnector [x] impl  [x] docstring  [x] test
    # [x] createLinCommunicationConnector [x] impl  [x] docstring  [x] test
    # [x] createFlexrayCommunicationConnector [x] impl  [x] docstring  [x] test
    # [x] getDltConfig                 [x] impl  [x] docstring  [x] test
    # [x] setDltConfig                 [x] impl  [x] docstring  [x] test
    # [x] getDoIpConfig                [x] impl  [x] docstring  [x] test
    # [x] setDoIpConfig                [x] impl  [x] docstring  [x] test
    # [x] getEcuTaskProxyRefs          [x] impl  [x] docstring  [x] test
    # [x] addEcuTaskProxyRef           [x] impl  [x] docstring  [x] test
    # [x] getEthSwitchPortGroupDerivation [x] impl  [x] docstring  [x] test
    # [x] setEthSwitchPortGroupDerivation [x] impl  [x] docstring  [x] test
    # [x] getFirewallRuleRefs          [x] impl  [x] docstring  [x] test
    # [x] addFirewallRuleRef           [x] impl  [x] docstring  [x] test
    # [x] getPartitions                [x] impl  [x] docstring  [x] test
    # [x] addPartition                 [x] impl  [x] docstring  [x] test
    # [x] getPncNmRequest              [x] impl  [x] docstring  [x] test
    # [x] setPncNmRequest              [x] impl  [x] docstring  [x] test
    # [x] getPncPrepareSleepTimer      [x] impl  [x] docstring  [x] test
    # [x] setPncPrepareSleepTimer      [x] impl  [x] docstring  [x] test
    # [x] getPncSynchronousWakeup      [x] impl  [x] docstring  [x] test
    # [x] setPncSynchronousWakeup      [x] impl  [x] docstring  [x] test
    # [x] getPnResetTime               [x] impl  [x] docstring  [x] test
    # [x] setPnResetTime               [x] impl  [x] docstring  [x] test
    # [x] getSleepModeSupported        [x] impl  [x] docstring  [x] test
    # [x] setSleepModeSupported        [x] impl  [x] docstring  [x] test
    # [x] getTcpIpIcmpPropsRef         [x] impl  [x] docstring  [x] test
    # [x] setTcpIpIcmpPropsRef         [x] impl  [x] docstring  [x] test
    # [x] getTcpIpPropsRef             [x] impl  [x] docstring  [x] test
    # [x] setTcpIpPropsRef             [x] impl  [x] docstring  [x] test
    # [x] getV2xSupported              [x] impl  [x] docstring  [x] test
    # [x] setV2xSupported              [x] impl  [x] docstring  [x] test
    # [x] getWakeUpOverBusSupported    [x] impl  [x] docstring  [x] test
    # [x] setWakeUpOverBusSupported    [x] impl  [x] docstring  [x] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.associatedComIPduGroupRefs: List[RefType] = []
        self.associatedConsumedProvidedServiceInstanceGroupRefs: List[RefType] = []
        self.associatedPdurIPduGroupRefs: List[RefType] = []
        self.channelSynchronousWakeup: Boolean = None
        self.clientIdRange = None
        self.comConfigurationGwTimeBase: TimeValue = None
        self.comConfigurationRxTimeBase: TimeValue = None
        self.comConfigurationTxTimeBase: TimeValue = None
        self.comEnableMDTForCyclicTransmission: Boolean = None
        self.commControllers: List[CommunicationController] = []
        self.connectors: List[CommunicationConnector] = []
        self.dltConfig = None
        self.doIpConfig = None
        self.ecuTaskProxyRefs: List[RefType] = []
        self.ethSwitchPortGroupDerivation: Boolean = None
        self.firewallRuleRefs: List[RefType] = []
        self.partitions = []
        self.pncNmRequest: Boolean = None
        self.pncPrepareSleepTimer: TimeValue = None
        self.pncSynchronousWakeup: Boolean = None
        self.pnResetTime: TimeValue = None
        self.sleepModeSupported: Boolean = None
        self.tcpIpIcmpPropsRef: RefType = None
        self.tcpIpPropsRef: RefType = None
        self.v2xSupported = None
        self.wakeUpOverBusSupported: Boolean = None

    def getAssociatedComIPduGroupRefs(self):
        return self.associatedComIPduGroupRefs

    def addAssociatedComIPduGroupRef(self, value):
        self.associatedComIPduGroupRefs.append(value)
        return self

    def getAssociatedConsumedProvidedServiceInstanceGroupRefs(self):
        return self.associatedConsumedProvidedServiceInstanceGroupRefs

    def addAssociatedConsumedProvidedServiceInstanceGroupRef(self, value):
        self.associatedConsumedProvidedServiceInstanceGroupRefs.append(value)
        return self

    def getAssociatedPdurIPduGroupRefs(self):
        return self.associatedPdurIPduGroupRefs

    def addAssociatedPdurIPduGroupRef(self, value):
        self.associatedPdurIPduGroupRefs.append(value)
        return self

    def getChannelSynchronousWakeup(self):
        return self.channelSynchronousWakeup

    def setChannelSynchronousWakeup(self, value):
        self.channelSynchronousWakeup = value
        return self

    def getClientIdRange(self):
        return self.clientIdRange

    def setClientIdRange(self, value):
        self.clientIdRange = value
        return self

    def getComConfigurationGwTimeBase(self):
        return self.comConfigurationGwTimeBase

    def setComConfigurationGwTimeBase(self, value):
        self.comConfigurationGwTimeBase = value
        return self

    def getComConfigurationRxTimeBase(self):
        return self.comConfigurationRxTimeBase

    def setComConfigurationRxTimeBase(self, value):
        self.comConfigurationRxTimeBase = value
        return self

    def getComConfigurationTxTimeBase(self):
        return self.comConfigurationTxTimeBase

    def setComConfigurationTxTimeBase(self, value):
        self.comConfigurationTxTimeBase = value
        return self

    def getComEnableMDTForCyclicTransmission(self):
        return self.comEnableMDTForCyclicTransmission

    def setComEnableMDTForCyclicTransmission(self, value):
        self.comEnableMDTForCyclicTransmission = value
        return self

    def getCommControllers(self):
        return list(sorted(filter(lambda a: isinstance(a, CommunicationController), self.elements), key=lambda o: o.short_name))

    def createCanCommunicationController(self, short_name: str) -> CanCommunicationController:
        if not self.IsElementExists(short_name):
            controller = CanCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)

    def createEthernetCommunicationController(self, short_name: str) -> EthernetCommunicationController:
        if not self.IsElementExists(short_name):
            controller = EthernetCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)

    def createLinMaster(self, short_name: str) -> LinMaster:
        if not self.IsElementExists(short_name):
            controller = LinMaster(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)

    def createFlexrayCommunicationController(self, short_name: str) -> FlexrayCommunicationController:
        if not self.IsElementExists(short_name):
            controller = FlexrayCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)

    def getConnectors(self):
        return list(sorted(filter(lambda a: isinstance(a, CommunicationConnector), self.elements), key=lambda o: o.short_name))

    def createCanCommunicationConnector(self, short_name: str) -> CanCommunicationConnector:
        if not self.IsElementExists(short_name):
            connector = CanCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)

    def createEthernetCommunicationConnector(self, short_name: str) -> EthernetCommunicationConnector:
        if not self.IsElementExists(short_name):
            connector = EthernetCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)

    def createLinCommunicationConnector(self, short_name: str) -> LinCommunicationConnector:
        if not self.IsElementExists(short_name):
            connector = LinCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)

    def createFlexrayCommunicationConnector(self, short_name: str) -> FlexrayCommunicationConnector:
        if not self.IsElementExists(short_name):
            connector = FlexrayCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)

    def getDltConfig(self):
        return self.dltConfig

    def setDltConfig(self, value):
        self.dltConfig = value
        return self

    def getDoIpConfig(self):
        return self.doIpConfig

    def setDoIpConfig(self, value):
        self.doIpConfig = value
        return self

    def getEcuTaskProxyRefs(self):
        return self.ecuTaskProxyRefs

    def addEcuTaskProxyRef(self, value):
        self.ecuTaskProxyRefs.append(value)
        return self

    def getEthSwitchPortGroupDerivation(self):
        return self.ethSwitchPortGroupDerivation

    def setEthSwitchPortGroupDerivation(self, value):
        self.ethSwitchPortGroupDerivation = value
        return self

    def getFirewallRuleRefs(self):
        return self.firewallRuleRefs

    def addFirewallRuleRef(self, value):
        self.firewallRuleRefs.append(value)
        return self

    def getPartitions(self):
        return self.partitions

    def addPartition(self, value):
        self.partitions.append(value)
        return self

    def getPncNmRequest(self):
        return self.pncNmRequest

    def setPncNmRequest(self, value):
        self.pncNmRequest = value
        return self

    def getPncPrepareSleepTimer(self):
        return self.pncPrepareSleepTimer

    def setPncPrepareSleepTimer(self, value):
        self.pncPrepareSleepTimer = value
        return self

    def getPncSynchronousWakeup(self):
        return self.pncSynchronousWakeup

    def setPncSynchronousWakeup(self, value):
        self.pncSynchronousWakeup = value
        return self

    def getPnResetTime(self):
        return self.pnResetTime

    def setPnResetTime(self, value):
        self.pnResetTime = value
        return self

    def getSleepModeSupported(self):
        return self.sleepModeSupported

    def setSleepModeSupported(self, value):
        self.sleepModeSupported = value
        return self

    def getTcpIpIcmpPropsRef(self):
        return self.tcpIpIcmpPropsRef

    def setTcpIpIcmpPropsRef(self, value):
        self.tcpIpIcmpPropsRef = value
        return self

    def getTcpIpPropsRef(self):
        return self.tcpIpPropsRef

    def setTcpIpPropsRef(self, value):
        self.tcpIpPropsRef = value
        return self

    def getV2xSupported(self):
        return self.v2xSupported

    def setV2xSupported(self, value):
        self.v2xSupported = value
        return self

    def getWakeUpOverBusSupported(self):
        return self.wakeUpOverBusSupported

    def setWakeUpOverBusSupported(self, value):
        self.wakeUpOverBusSupported = value
        return self
