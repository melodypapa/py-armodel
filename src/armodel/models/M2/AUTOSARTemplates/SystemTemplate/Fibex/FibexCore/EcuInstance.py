from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TimeValue
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector, EthernetCommunicationController
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector, CanCommunicationController
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector, FlexrayCommunicationController
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinMaster
from typing import List

class EcuInstance(FibexElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.associatedComIPduGroupRefs = []                                # type: List[RefType]
        self.associatedConsumedProvidedServiceInstanceGroupRefs = []        # type: List[RefType]
        self.associatedPdurIPduGroupRefs = []                               # type: List[RefType]
        self.channelSynchronousWakeup = None                                # type: Boolean
        self.clientIdRange = None                                           # type: ClientIdRange
        self.comConfigurationGwTimeBase = None                              # type: TimeValue
        self.comConfigurationRxTimeBase = None                              # type: TimeValue
        self.comConfigurationTxTimeBase = None                              # type: TimeValue
        self.comEnableMDTForCyclicTransmission = None                       # type: Boolean
        self.commControllers = []                                           # type: List[CommunicationController]
        self.connectors = []                                                # type: List[CommunicationConnector]
        self.diagnosticAddress = None                                       # type: Integer             ## Only AR 4.3.1
        self.dltConfig = None                                               # type: DltConfig
        self.doIpConfig = None                                              # type: DoIpConfig
        self.ecuTaskProxyRefs = []                                          # type: List[RefType]
        self.ethSwitchPortGroupDerivation = None                            # type: Boolean
        self.firewallRuleRef = None                                         # type: RefType
        self.partitions = []                                                # type: List[EcuPartition]
        self.pncNmRequest = None                                            # type: Boolean
        self.pncPrepareSleepTimer = None                                    # type: TimeValue
        self.pncSynchronousWakeup = None                                    # type: Boolean
        self.pnResetTime = None                                             # type: TimeValue
        self.sleepModeSupported = None                                      # type: Boolean
        self.tcpIpIcmpPropsRef = None                                       # type: RefType
        self.tcpIpPropsRef = None                                           # type: RefType
        self.v2xSupported = None                                            # type: V2xSupportEnum
        self.wakeUpOverBusSupported = None                                  # type: Boolean

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
        return list(sorted(filter(lambda a: isinstance(a, CommunicationController), self.elements), key= lambda o:o.short_name))

    def createCanCommunicationController(self, short_name: str) -> CanCommunicationController:
        if (not self.IsElementExists(short_name)):
            controller = CanCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)
    
    def createEthernetCommunicationController(self, short_name: str) -> EthernetCommunicationController:
        if (not self.IsElementExists(short_name)):
            controller = EthernetCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)
    
    def createLinMaster(self, short_name: str) -> LinMaster:
        if (not self.IsElementExists(short_name)):
            controller = LinMaster(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)
    
    def createFlexrayCommunicationController(self, short_name: str) -> FlexrayCommunicationController:
        if (not self.IsElementExists(short_name)):
            controller = FlexrayCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)

    def getConnectors(self):
        return list(sorted(filter(lambda a: isinstance(a, CommunicationConnector), self.elements), key= lambda o:o.short_name))

    def createCanCommunicationConnector(self, short_name: str) -> CanCommunicationConnector:
        if (not self.IsElementExists(short_name)):
            connector = CanCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def createEthernetCommunicationConnector(self, short_name: str) -> EthernetCommunicationConnector:
        if (not self.IsElementExists(short_name)):
            connector = EthernetCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def createLinCommunicationConnector(self, short_name: str) -> LinCommunicationConnector:
        if (not self.IsElementExists(short_name)):
            connector = LinCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def createFlexrayCommunicationConnector(self, short_name: str) -> FlexrayCommunicationConnector:
        if (not self.IsElementExists(short_name)):
            connector = FlexrayCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def getDiagnosticAddress(self):
        return self.diagnosticAddress

    def setDiagnosticAddress(self, value):
        if value is not None:
            self.diagnosticAddress = value
        return self

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

    def setEcuTaskProxyRefs(self, value):
        self.ecuTaskProxyRefs = value
        return self

    def getEthSwitchPortGroupDerivation(self):
        return self.ethSwitchPortGroupDerivation

    def setEthSwitchPortGroupDerivation(self, value):
        self.ethSwitchPortGroupDerivation = value
        return self

    def getFirewallRuleRef(self):
        return self.firewallRuleRef

    def setFirewallRuleRef(self, value):
        self.firewallRuleRef = value
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