from abc import ABCMeta
from typing import List

from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, MacAddressString, PositiveInteger, RefType, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController

class MacMulticastGroup(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.macMulticastAddress = None                                     # type: MacAddressString

    def getMacMulticastAddress(self):
        return self.macMulticastAddress

    def setMacMulticastAddress(self, value):
        if value is not None:
            self.macMulticastAddress = value
        return self
class EthernetCluster(CommunicationCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.couplingPorts = []                                             # type: List[CouplingPortConnection]
        self.couplingPortStartupActiveTime = None                           # type: TimeValue
        self.couplingPortSwitchoffDelay = None                              # type: TimeValue
        self.macMulticastGroups = []                                        # type: List[MacMulticastGroup]

    def getCouplingPorts(self):
        return self.couplingPorts

    def addCouplingPort(self, value):
        if value is not None:
            self.couplingPorts.append(value)
        return self

    def getCouplingPortStartupActiveTime(self):
        return self.couplingPortStartupActiveTime

    def setCouplingPortStartupActiveTime(self, value):
        if value is not None:
            self.couplingPortStartupActiveTime = value
        return self

    def getCouplingPortSwitchoffDelay(self):
        return self.couplingPortSwitchoffDelay

    def setCouplingPortSwitchoffDelay(self, value):
        if value is not None:
            self.couplingPortSwitchoffDelay = value
        return self

    def getMacMulticastGroups(self):
        return self.macMulticastGroups

    def createMacMulticastGroup(self, short_name: str) -> MacMulticastGroup:
        if (short_name not in self.elements):
            group = MacMulticastGroup(self, short_name)
            self.addElement(group)
            self.macMulticastGroups.append(group)
        return self.getElement(short_name)
    
class CouplingPortStructuralElement(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CouplingPortStructuralElement:
            raise NotImplementedError("CouplingPortStructuralElement is an abstract class.")
        
        super().__init__(parent, short_name)
        
class CouplingPortFifo(CouplingPortStructuralElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.assignedTrafficClasses = []                            # type: List[PositiveInteger]
        self.minimumFifoLength = None                               # type: PositiveInteger
        self.shaper = None                                          # type: CouplingPortAbstractShaper
        self.trafficClassPreemptionSupport = None                   # type: EthernetCouplingPortPreemptionEnum

    def getAssignedTrafficClasses(self):
        return self.assignedTrafficClasses

    def addAssignedTrafficClass(self, value):
        if value is not None:
            self.assignedTrafficClasses.append(value)
        return self

    def getMinimumFifoLength(self):
        return self.minimumFifoLength

    def setMinimumFifoLength(self, value):
        if value is not None:
            self.minimumFifoLength = value
        return self

    def getShaper(self):
        return self.shaper

    def setShaper(self, value):
        if value is not None:
            self.shaper = value
        return self

    def getTrafficClassPreemptionSupport(self):
        return self.trafficClassPreemptionSupport

    def setTrafficClassPreemptionSupport(self, value):
        if value is not None:
            self.trafficClassPreemptionSupport = value
        return self
        
class CouplingPortScheduler(CouplingPortStructuralElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.portScheduler = None                                   # type: EthernetCouplingPortSchedulerEnum
        self.predecessorRefs = []                                   # type: List[RefType]

    def getPortScheduler(self):
        return self.portScheduler

    def setPortScheduler(self, value):
        if value is not None:
            self.portScheduler = value
        return self

    def getPredecessorRefs(self):
        return self.predecessorRefs

    def addPredecessorRef(self, value):
        if value is not None:
            self.predecessorRefs.append(value)
        return self

class EthernetPriorityRegeneration(Referrable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.ingressPriority = None                                 # type: PositiveInteger
        self.regeneratedPriority = None                             # type: PositiveInteger

    def getIngressPriority(self):
        return self.ingressPriority

    def setIngressPriority(self, value):
        if value is not None:
            self.ingressPriority = value
        return self

    def getRegeneratedPriority(self):
        return self.regeneratedPriority

    def setRegeneratedPriority(self, value):
        if value is not None:
            self.regeneratedPriority = value
        return self


class CouplingPortDetails(ARObject):
    def __init__(self):
        super().__init__()

        self.couplingPortStructuralElements = []                    # type: List[CouplingPortStructuralElement]
        self.defaultTrafficClass = None                             # type: PositiveInteger
        self.ethernetPriorityRegenerations = []                     # type: List[EthernetPriorityRegeneration]
        self.ethernetTrafficClassAssignments = []                   # type: List[CouplingPortTrafficClassAssignment]
        self.framePreemptionSupport = None                          # type: Boolean
        self.globalTimeProps = None                                 # type: GlobalTimeCouplingPortProps
        self.lastEgressSchedulerRef = None                          # type: RefType
        self.ratePolicies = []                                      # type: List[CouplingPortRatePolicy]
        self.vlanTranslationTables = []                             # type: List[EthernetVlanTranslationTable]

    def getCouplingPortStructuralElements(self):
        return self.couplingPortStructuralElements

    def createCouplingPortFifo(self, short_name: str) -> CouplingPortFifo:
        fifo = CouplingPortFifo(self, short_name)
        self.couplingPortStructuralElements.append(fifo)
        return fifo
    
    def createCouplingPortScheduler(self, short_name: str) -> CouplingPortScheduler:
        scheduler = CouplingPortScheduler(self, short_name)
        self.couplingPortStructuralElements.append(scheduler)
        return scheduler
    
    def createEthernetPriorityRegeneration(self, short_name: str) -> EthernetPriorityRegeneration:
        regeneration = EthernetPriorityRegeneration(self, short_name)
        self.ethernetPriorityRegenerations.append(regeneration)
        return regeneration

    def getDefaultTrafficClass(self):
        return self.defaultTrafficClass

    def setDefaultTrafficClass(self, value):
        if value is not None:
            self.defaultTrafficClass = value
        return self

    def getEthernetPriorityRegenerations(self):
        return self.ethernetPriorityRegenerations

    def setEthernetPriorityRegenerations(self, value):
        if value is not None:
            self.ethernetPriorityRegenerations = value
        return self

    def getEthernetTrafficClassAssignments(self):
        return self.ethernetTrafficClassAssignments

    def setEthernetTrafficClassAssignments(self, value):
        if value is not None:
            self.ethernetTrafficClassAssignments = value
        return self

    def getFramePreemptionSupport(self):
        return self.framePreemptionSupport

    def setFramePreemptionSupport(self, value):
        if value is not None:
            self.framePreemptionSupport = value
        return self

    def getGlobalTimeProps(self):
        return self.globalTimeProps

    def setGlobalTimeProps(self, value):
        if value is not None:
            self.globalTimeProps = value
        return self

    def getLastEgressSchedulerRef(self):
        return self.lastEgressSchedulerRef

    def setLastEgressSchedulerRef(self, value):
        if value is not None:
            self.lastEgressSchedulerRef = value
        return self

    def getRatePolicies(self):
        return self.ratePolicies

    def setRatePolicies(self, value):
        if value is not None:
            self.ratePolicies = value
        return self

    def getVlanTranslationTables(self):
        return self.vlanTranslationTables

    def setVlanTranslationTables(self, value):
        if value is not None:
            self.vlanTranslationTables = value
        return self

class VlanMembership(ARObject):
    def __init__(self):
        super().__init__()

        self.defaultPriority = None                                 # type: PositiveInteger        
        self.dhcpAddressAssignment = None                           # type: DhcpServerConfiguration
        self.sendActivity = None                                    # type: EthernetSwitchVlanEgressTaggingEnum
        self.vlanRef = None                                         # type: RefType

    def getDefaultPriority(self):
        return self.defaultPriority

    def setDefaultPriority(self, value):
        if value is not None:
            self.defaultPriority = value
        return self

    def getDhcpAddressAssignment(self):
        return self.dhcpAddressAssignment

    def setDhcpAddressAssignment(self, value):
        if value is not None:
            self.dhcpAddressAssignment = value
        return self

    def getSendActivity(self):
        return self.sendActivity

    def setSendActivity(self, value):
        if value is not None:
            self.sendActivity = value
        return self

    def getVlanRef(self):
        return self.vlanRef

    def setVlanRef(self, value):
        if value is not None:
            self.vlanRef = value
        return self


class CouplingPort(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.connectionNegotiationBehavior = None                   # type: EthernetConnectionNegotiationEnum
        self.couplingPortDetails = None                             # type: CouplingPortDetails
        self.couplingPortRole = None                                # type: CouplingPortRoleEnum
        self.defaultVlanRef = None                                  # type: RefType
        self.macAddressVlanAssignments = []                         # type: List[MacAddressVlanMembership]
        self.macLayerType = None                                    # type: EthernetMacLayerTypeEnum
        self.macMulticastAddressRefs = []                           # type: List[RefType]
        self.macSecProps = []                                       # type: List[MacSecProps]
        self.physicalLayerType = None                               # type: EthernetPhysicalLayerTypeEnum
        self.plcaProps = None                                       # type: PlcaProps
        self.pncMappingRefs = []                                    # type: List[RefType]
        self.receiveActivity = None                                 # type: EthernetSwitchVlanIngressTagEnum
        self.vlanMemberships = []                                   # type: List[VlanMembership]
        self.wakeupSleepOnDatalineConfigRef = None                  # type: RefType

    def getConnectionNegotiationBehavior(self):
        return self.connectionNegotiationBehavior

    def setConnectionNegotiationBehavior(self, value):
        if value is not None:
            self.connectionNegotiationBehavior = value
        return self

    def getCouplingPortDetails(self):
        return self.couplingPortDetails

    def setCouplingPortDetails(self, value):
        if value is not None:
            self.couplingPortDetails = value
        return self

    def getCouplingPortRole(self):
        return self.couplingPortRole

    def setCouplingPortRole(self, value):
        if value is not None:
            self.couplingPortRole = value
        return self

    def getDefaultVlanRef(self):
        return self.defaultVlanRef

    def setDefaultVlanRef(self, value):
        if value is not None:
            self.defaultVlanRef = value
        return self

    def getMacAddressVlanAssignments(self):
        return self.macAddressVlanAssignments

    def setMacAddressVlanAssignments(self, value):
        if value is not None:
            self.macAddressVlanAssignments = value
        return self

    def getMacLayerType(self):
        return self.macLayerType

    def setMacLayerType(self, value):
        if value is not None:
            self.macLayerType = value
        return self

    def getMacMulticastAddressRefs(self):
        return self.macMulticastAddressRefs

    def setMacMulticastAddressRefs(self, value):
        if value is not None:
            self.macMulticastAddressRefs = value
        return self

    def getMacSecProps(self):
        return self.macSecProps

    def setMacSecProps(self, value):
        if value is not None:
            self.macSecProps = value
        return self

    def getPhysicalLayerType(self):
        return self.physicalLayerType

    def setPhysicalLayerType(self, value):
        if value is not None:
            self.physicalLayerType = value
        return self

    def getPlcaProps(self):
        return self.plcaProps

    def setPlcaProps(self, value):
        if value is not None:
            self.plcaProps = value
        return self

    def getPncMappingRefs(self):
        return self.pncMappingRefs

    def setPncMappingRefs(self, value):
        if value is not None:
            self.pncMappingRefs = value
        return self

    def getReceiveActivity(self):
        return self.receiveActivity

    def setReceiveActivity(self, value):
        if value is not None:
            self.receiveActivity = value
        return self

    def getVlanMemberships(self):
        return self.vlanMemberships

    def addVlanMembership(self, value):
        if value is not None:
            self.vlanMemberships.append(value)
        return self

    def getWakeupSleepOnDatalineConfigRef(self):
        return self.wakeupSleepOnDatalineConfigRef

    def setWakeupSleepOnDatalineConfigRef(self, value):
        if value is not None:
            self.wakeupSleepOnDatalineConfigRef = value
        return self



class EthernetCommunicationController(CommunicationController):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.canXlConfigRef = None                          # type: RefType
        self.couplingPorts = []                             # type: List[CouplingPort]
        self.macLayerType = None                            # type: EthernetMacLayerTypeEnum
        self.macUnicastAddress = None                       # type: MacAddressString
        self.maximumReceiveBufferLength = None              # type: Integer
        self.maximumTransmitBufferLength = None             # type: Integer
        self.slaveActAsPassiveCommunicationSlave = None     # type: Boolean
        self.slaveQualifiedUnexpectedLinkDownTime = None    # type: TimeValue

    def getCanXlConfigRef(self):
        return self.canXlConfigRef

    def setCanXlConfigRef(self, value):
        self.canXlConfigRef = value
        return self

    def getCouplingPorts(self):
        return self.couplingPorts

    def createCouplingPort(self, short_name: str) -> CouplingPort:
        if (short_name not in self.elements):
            group = CouplingPort(self, short_name)
            self.addElement(group)
            self.couplingPorts.append(group)
        return self.getElement(short_name)

    def getMacLayerType(self):
        return self.macLayerType

    def setMacLayerType(self, value):
        self.macLayerType = value
        return self

    def getMacUnicastAddress(self):
        return self.macUnicastAddress

    def setMacUnicastAddress(self, value):
        self.macUnicastAddress = value
        return self

    def getMaximumReceiveBufferLength(self):
        return self.maximumReceiveBufferLength

    def setMaximumReceiveBufferLength(self, value):
        self.maximumReceiveBufferLength = value
        return self

    def getMaximumTransmitBufferLength(self):
        return self.maximumTransmitBufferLength

    def setMaximumTransmitBufferLength(self, value):
        self.maximumTransmitBufferLength = value
        return self

    def getSlaveActAsPassiveCommunicationSlave(self):
        return self.slaveActAsPassiveCommunicationSlave

    def setSlaveActAsPassiveCommunicationSlave(self, value):
        self.slaveActAsPassiveCommunicationSlave = value
        return self

    def getSlaveQualifiedUnexpectedLinkDownTime(self):
        return self.slaveQualifiedUnexpectedLinkDownTime

    def setSlaveQualifiedUnexpectedLinkDownTime(self, value):
        self.slaveQualifiedUnexpectedLinkDownTime = value
        return self

class EthernetCommunicationConnector(CommunicationConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ethIpPropsRef = None                               # type: RefType
        self.maximumTransmissionUnit = None                     # type: PositiveInteger
        self.neighborCacheSize = None                           # type: PositiveInteger
        self.pathMtuEnabled = None                              # type: Boolean
        self.pathMtuTimeout = None                              # type: TimeValue

    def getEthIpPropsRef(self):
        return self.ethIpPropsRef

    def setEthIpPropsRef(self, value):
        self.ethIpPropsRef = value
        return self

    def getMaximumTransmissionUnit(self):
        return self.maximumTransmissionUnit

    def setMaximumTransmissionUnit(self, value):
        self.maximumTransmissionUnit = value
        return self

    def getNeighborCacheSize(self):
        return self.neighborCacheSize

    def setNeighborCacheSize(self, value):
        self.neighborCacheSize = value
        return self

    def getPathMtuEnabled(self):
        return self.pathMtuEnabled

    def setPathMtuEnabled(self, value):
        self.pathMtuEnabled = value
        return self

    def getPathMtuTimeout(self):
        return self.pathMtuTimeout

    def setPathMtuTimeout(self, value):
        self.pathMtuTimeout = value
        return self
    
class RequestResponseDelay(ARObject):
    def __init__(self):
        super().__init__()

        self.maxValue = None                                        # type: TimeValue
        self.minValue = None                                        # type: TimeValue

    def getMaxValue(self):
        return self.maxValue

    def setMaxValue(self, value):
        if value is not None:
            self.maxValue = value
        return self

    def getMinValue(self):
        return self.minValue

    def setMinValue(self, value):
        if value is not None:
            self.minValue = value
        return self

class InitialSdDelayConfig(ARObject):
    def __init__(self):
        super().__init__()

        self.initialDelayMaxValue = None                            # type: TimeValue
        self.initialDelayMinValue = None                            # type: TimeValue
        self.initialRepetitionsBaseDelay = None                     # type: TimeValue
        self.initialRepetitionsMax = None                           # type: PositiveInteger

    def getInitialDelayMaxValue(self):
        return self.initialDelayMaxValue

    def setInitialDelayMaxValue(self, value):
        if value is not None:
            self.initialDelayMaxValue = value
        return self

    def getInitialDelayMinValue(self):
        return self.initialDelayMinValue

    def setInitialDelayMinValue(self, value):
        if value is not None:
            self.initialDelayMinValue = value
        return self

    def getInitialRepetitionsBaseDelay(self):
        return self.initialRepetitionsBaseDelay

    def setInitialRepetitionsBaseDelay(self, value):
        if value is not None:
            self.initialRepetitionsBaseDelay = value
        return self

    def getInitialRepetitionsMax(self):
        return self.initialRepetitionsMax

    def setInitialRepetitionsMax(self, value):
        if value is not None:
            self.initialRepetitionsMax = value
        return self

    
class SdClientConfig(ARObject):
    def __init__(self):
        super().__init__()

        self.capabilityRecord = None                                # type: TagWithOptionalValue
        self.clientServiceMajorVersion = None                       # type: PositiveInteger
        self.clientServiceMinorVersion = None                       # type: PositiveInteger
        self.initialFindBehavior = None                             # type: InitialSdDelayConfig
        self.requestResponseDelay = None                            # type: RequestResponseDelay
        self.ttl = None                                             # type: PositiveInteger

    def getClientServiceMajorVersion(self):
        return self.clientServiceMajorVersion

    def setClientServiceMajorVersion(self, value):
        if value is not None:
            self.clientServiceMajorVersion = value
        return self

    def getClientServiceMinorVersion(self):
        return self.clientServiceMinorVersion

    def setClientServiceMinorVersion(self, value):
        if value is not None:
            self.clientServiceMinorVersion = value
        return self

    def getInitialFindBehavior(self):
        return self.initialFindBehavior

    def setInitialFindBehavior(self, value):
        if value is not None:
            self.initialFindBehavior = value
        return self

    def getRequestResponseDelay(self):
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value):
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getTtl(self):
        return self.ttl

    def setTtl(self, value):
        if value is not None:
            self.ttl = value
        return self


