from abc import ABCMeta
from typing import List
from ....M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import RxIdentifierRange
from ....M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, Integer, PositiveInteger, RefType, ARBoolean, TimeValue
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class NmClusterCoupling(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == NmClusterCoupling:
            raise NotImplementedError("NmClusterCoupling is an abstract class.")
        
        super().__init__()

class CanNmClusterCoupling(NmClusterCoupling):
    def __init__(self):
        super().__init__()

        self.coupledClusterRefs = []
        self.nmBusloadReductionEnabled = None
        self.nmImmediateRestartEnabled = None

    def getCoupledClusterRefs(self):
        return self.coupledClusterRefs

    def addCoupledClusterRef(self, value):
        self.coupledClusterRefs.append(value)
        return self

    def getNmBusloadReductionEnabled(self):
        return self.nmBusloadReductionEnabled

    def setNmBusloadReductionEnabled(self, value):
        self.nmBusloadReductionEnabled = value
        return self

    def getNmImmediateRestartEnabled(self):
        return self.nmImmediateRestartEnabled

    def setNmImmediateRestartEnabled(self, value):
        self.nmImmediateRestartEnabled = value
        return self

class FlexrayNmClusterCoupling(NmClusterCoupling):
    def __init__(self):
        super().__init__()

        self.coupledClusterRefs = []
        self.nmScheduleVariant = None

    def getCoupledClusterRefs(self):
        return self.coupledClusterRefs

    def addCoupledClusterRef(self, value):
        self.coupledClusterRefs.append(value)
        return self

    def getNmScheduleVariant(self):
        return self.nmScheduleVariant

    def setNmScheduleVariant(self, value):
        self.nmScheduleVariant = value
        return self

class UdpNmClusterCoupling(NmClusterCoupling):
    def __init__(self):
        super().__init__()

class NmNode(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == NmNode:
            raise NotImplementedError("NmNode is an abstract class.")
        
        super().__init__(parent, short_name)

        self.controllerRef = None
        self.nmCoordCluster = None
        self.nmCoordinatorRole = None
        self.nmIfEcuRef = None
        self.nmNodeId = None
        self.nmPassiveModeEnabled = None
        self.rxNmPduRefs = []
        self.TxNmPduRefs = []

    def getControllerRef(self) -> RefType:
        return self.controllerRef

    def setControllerRef(self, value):
        self.controllerRef = value
        return self

    def getNmCoordCluster(self) -> ARNumerical:
        return self.nmCoordCluster

    def setNmCoordCluster(self, value: ARNumerical):
        self.nmCoordCluster = value
        return self

    def getNmCoordinatorRole(self) -> ARLiteral:
        return self.nmCoordinatorRole

    def setNmCoordinatorRole(self, value: ARLiteral):
        self.nmCoordinatorRole = value
        return self

    def getNmIfEcuRef(self) -> RefType:
        return self.nmIfEcuRef

    def setNmIfEcuRef(self, value):
        self.nmIfEcuRef = value
        return self

    def getNmNodeId(self) -> ARNumerical:
        return self.nmNodeId

    def setNmNodeId(self, value: ARNumerical):
        self.nmNodeId = value
        return self

    def getNmPassiveModeEnabled(self) -> ARBoolean:
        return self.nmPassiveModeEnabled

    def setNmPassiveModeEnabled(self, value: ARBoolean):
        self.nmPassiveModeEnabled = value
        return self

    def addRxNmPduRef(self, ref: RefType):
        self.rxNmPduRefs.append(ref)
        return self

    def getRxNmPduRefs(self) -> List[RefType]:
        return self.rxNmPduRefs

    def addTxNmPduRefs(self, ref: RefType):
        self.TxNmPduRefs.append(ref)
        return self

    def getTxNmPduRefs(self) -> List[RefType]:
        return self.TxNmPduRefs

class CanNmNode(NmNode):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allNmMessagesKeepAwake = None
        self.nmCarWakeUpFilterEnabled = None
        self.nmCarWakeUpRxEnabled = None
        self.nmMsgCycleOffset = None
        self.nmMsgReducedTime = None
        self.nmRangeConfig = None

    def getAllNmMessagesKeepAwake(self):
        return self.allNmMessagesKeepAwake

    def setAllNmMessagesKeepAwake(self, value):
        self.allNmMessagesKeepAwake = value
        return self

    def getNmCarWakeUpFilterEnabled(self):
        return self.nmCarWakeUpFilterEnabled

    def setNmCarWakeUpFilterEnabled(self, value):
        self.nmCarWakeUpFilterEnabled = value
        return self

    def getNmCarWakeUpRxEnabled(self):
        return self.nmCarWakeUpRxEnabled

    def setNmCarWakeUpRxEnabled(self, value):
        self.nmCarWakeUpRxEnabled = value
        return self

    def getNmMsgCycleOffset(self):
        return self.nmMsgCycleOffset

    def setNmMsgCycleOffset(self, value):
        self.nmMsgCycleOffset = value
        return self

    def getNmMsgReducedTime(self):
        return self.nmMsgReducedTime

    def setNmMsgReducedTime(self, value):
        self.nmMsgReducedTime = value
        return self
    
    def getNmRangeConfig(self) -> RxIdentifierRange:
        return self.nmRangeConfig

    def setNmRangeConfig(self, value: RxIdentifierRange):
        self.nmRangeConfig = value

class FlexrayNmNode(NmNode):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class J1939NmNode(NmNode):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class UdpNmNode(NmNode):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class NmCluster(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.communicationClusterRef = None
        self.nmChannelId = None
        self.nmChannelSleepMaster = None
        self.nmNodes = []                       # type: List[NmNode]
        self.nmNodeDetectionEnabled = None
        self.nmNodeIdEnabled = None
        self.nmPncParticipation = None
        self.nmRepeatMsgIndEnabled = None
        self._nmSynchronizingNetwork = None

    def getCommunicationClusterRef(self):
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value):
        self.communicationClusterRef = value
        return self

    def getNmChannelId(self):
        return self.nmChannelId

    def setNmChannelId(self, value):
        self.nmChannelId = value
        return self

    def getNmChannelSleepMaster(self):
        return self.nmChannelSleepMaster

    def setNmChannelSleepMaster(self, value):
        self.nmChannelSleepMaster = value
        return self

    def createCanNmNode(self, short_name: str) -> CanNmNode:
        if (short_name not in self.elements):
            node = CanNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name)
    
    def readUdpNmNode(self, short_name: str) -> UdpNmNode:
        if (short_name not in self.elements):
            node = UdpNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name)
    
    def getCanNmNodes(self) -> List[CanNmNode]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmNode), self.elements.values()), key= lambda o:o.short_name))
    
    def getUdpNmNodes(self) -> List[UdpNmNode]:
        return list(sorted(filter(lambda a: isinstance(a, UdpNmNode), self.elements.values()), key= lambda o:o.short_name))
    
    def getNmNodes(self) -> List[NmNode]:
        return list(sorted(filter(lambda a: isinstance(a, NmNode), self.elements.values()), key= lambda o:o.short_name))

    def getNmNodeDetectionEnabled(self):
        return self.nmNodeDetectionEnabled

    def setNmNodeDetectionEnabled(self, value):
        self.nmNodeDetectionEnabled = value
        return self

    def getNmNodeIdEnabled(self):
        return self.nmNodeIdEnabled

    def setNmNodeIdEnabled(self, value):
        self.nmNodeIdEnabled = value
        return self

    def getNmPncParticipation(self):
        return self.nmPncParticipation

    def setNmPncParticipation(self, value):
        self.nmPncParticipation = value
        return self

    def getNmRepeatMsgIndEnabled(self):
        return self.nmRepeatMsgIndEnabled

    def setNmRepeatMsgIndEnabled(self, value):
        self.nmRepeatMsgIndEnabled = value
        return self

    def getNmSynchronizingNetwork(self):
        return self._nmSynchronizingNetwork

    def setNmSynchronizingNetwork(self, value):
        self._nmSynchronizingNetwork = value
        return self

class CanNmCluster(NmCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmBusloadReductionActive = None
        self.nmCarWakeUpBitPosition = None
        self.nmCarWakeUpFilterNodeId = None
        self.nmCarWakeUpRxEnabled = None
        self.nmCbvPosition = None
        self.nmChannelActive = None
        self.nmImmediateNmCycleTime = None
        self.nmImmediateNmTransmissions = None
        self.nmMessageTimeoutTime = None
        self.nmMsgCycleTime = None
        self.nmNetworkTimeout = None
        self.nmNidPosition = None
        self.nmRemoteSleepIndicationTime = None
        self.nmRepeatMessageTime = None
        self.nmUserDataLength = None
        self.nmWaitBusSleepTime = None

    def getNmBusloadReductionActive(self):
        return self.nmBusloadReductionActive

    def setNmBusloadReductionActive(self, value):
        self.nmBusloadReductionActive = value
        return self

    def getNmCarWakeUpBitPosition(self):
        return self.nmCarWakeUpBitPosition

    def setNmCarWakeUpBitPosition(self, value):
        self.nmCarWakeUpBitPosition = value
        return self

    def getNmCarWakeUpFilterNodeId(self):
        return self.nmCarWakeUpFilterNodeId

    def setNmCarWakeUpFilterNodeId(self, value):
        self.nmCarWakeUpFilterNodeId = value
        return self
    
    def getNmCarWakeUpRxEnabled(self):
        return self.nmCarWakeUpRxEnabled

    def setNmCarWakeUpRxEnabled(self, value):
        self.nmCarWakeUpRxEnabled = value
        return self

    def getNmCbvPosition(self):
        return self.nmCbvPosition

    def setNmCbvPosition(self, value):
        self.nmCbvPosition = value
        return self
    
    def getNmChannelActive(self):
        return self.nmChannelActive

    def setNmChannelActive(self, value):
        self.nmChannelActive = value
        return self

    def getNmImmediateNmCycleTime(self):
        return self.nmImmediateNmCycleTime

    def setNmImmediateNmCycleTime(self, value):
        self.nmImmediateNmCycleTime = value
        return self

    def getNmImmediateNmTransmissions(self):
        return self.nmImmediateNmTransmissions

    def setNmImmediateNmTransmissions(self, value):
        self.nmImmediateNmTransmissions = value
        return self

    def getNmMessageTimeoutTime(self):
        return self.nmMessageTimeoutTime

    def setNmMessageTimeoutTime(self, value):
        self.nmMessageTimeoutTime = value
        return self

    def getNmMsgCycleTime(self):
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value):
        self.nmMsgCycleTime = value
        return self

    def getNmNetworkTimeout(self):
        return self.nmNetworkTimeout

    def setNmNetworkTimeout(self, value):
        self.nmNetworkTimeout = value
        return self

    def getNmNidPosition(self):
        return self.nmNidPosition

    def setNmNidPosition(self, value):
        self.nmNidPosition = value
        return self

    def getNmRemoteSleepIndicationTime(self):
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value):
        self.nmRemoteSleepIndicationTime = value
        return self

    def getNmRepeatMessageTime(self):
        return self.nmRepeatMessageTime

    def setNmRepeatMessageTime(self, value):
        self.nmRepeatMessageTime = value
        return self
    
    def getNmUserDataLength(self):
        return self.nmUserDataLength

    def setNmUserDataLength(self, value):
        self.nmUserDataLength = value
        return self

    def getNmWaitBusSleepTime(self):
        return self.nmWaitBusSleepTime

    def setNmWaitBusSleepTime(self, value):
        self.nmWaitBusSleepTime = value
        return self

class FlexrayNmCluster(NmCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class J1939NmCluster(NmCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class UdpNmCluster(NmCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class NmEcu(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.busDependentNmEcus = []
        self.ecuInstance = None
        self.nmBusSynchronizationEnabled = None
        self.nmComControlEnabled = None
        self.nmCoordinator = None
        self.nmCycletimeMainFunction = None
        self.nmPduRxIndicationEnabled = None
        self.nmRemoteSleepIndEnabled = None
        self.nmStateChangeIndEnabled = None
        self.nmUserDataEnabled = None

    def getBusDependentNmEcus(self):
        return self.busDependentNmEcus

    def addBusDependentNmEcu(self, value):
        self.busDependentNmEcus.append(value)
        return self

    def getEcuInstance(self):
        return self.ecuInstance

    def setEcuInstance(self, value):
        self.ecuInstance = value
        return self

    def getNmBusSynchronizationEnabled(self):
        return self.nmBusSynchronizationEnabled

    def setNmBusSynchronizationEnabled(self, value):
        self.nmBusSynchronizationEnabled = value
        return self

    def getNmComControlEnabled(self):
        return self.nmComControlEnabled

    def setNmComControlEnabled(self, value):
        self.nmComControlEnabled = value
        return self

    def getNmCoordinator(self):
        return self.nmCoordinator

    def setNmCoordinator(self, value):
        self.nmCoordinator = value
        return self

    def getNmCycletimeMainFunction(self):
        return self.nmCycletimeMainFunction

    def setNmCycletimeMainFunction(self, value):
        self.nmCycletimeMainFunction = value
        return self

    def getNmPduRxIndicationEnabled(self):
        return self.nmPduRxIndicationEnabled

    def setNmPduRxIndicationEnabled(self, value):
        self.nmPduRxIndicationEnabled = value
        return self

    def getNmRemoteSleepIndEnabled(self):
        return self.nmRemoteSleepIndEnabled

    def setNmRemoteSleepIndEnabled(self, value):
        self.nmRemoteSleepIndEnabled = value
        return self

    def getNmStateChangeIndEnabled(self):
        return self.nmStateChangeIndEnabled

    def setNmStateChangeIndEnabled(self, value):
        self.nmStateChangeIndEnabled = value
        return self

    def getNmUserDataEnabled(self):
        return self.nmUserDataEnabled

    def setNmUserDataEnabled(self, value):
        self.nmUserDataEnabled = value
        return self   

class NmConfig(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmClusterCouplings = []                # type: List[NmClusterCoupling]
        self.nmIfEcus = []                          # type: List[NmEcu]

    def createCanNmCluster(self, short_name: str) -> CanNmCluster:
        if (short_name not in self.elements):
            cluster = CanNmCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)
    
    def createUdpNmCluster(self, short_name: str) -> UdpNmCluster:
        if (short_name not in self.elements):
            cluster = UdpNmCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def getCanNmClusters(self) -> List[CanNmCluster]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmCluster), self.elements.values()), key= lambda o:o.short_name))
    
    def getUdpNmClusters(self) -> List[UdpNmCluster]:
        return list(sorted(filter(lambda a: isinstance(a, UdpNmCluster), self.elements.values()), key= lambda o:o.short_name))
    
    def getNmClusters(self) -> List[NmCluster]:
        return list(sorted(filter(lambda a: isinstance(a, NmCluster), self.elements.values()), key= lambda o:o.short_name))
    
    def getNmClusterCouplings(self):
        return self.nmClusterCouplings

    def addNmClusterCouplings(self, value):
        self.nmClusterCouplings.append(value)
        return self

    def getNmIfEcus(self):
        return self.nmIfEcus

    def addNmIfEcus(self, value):
        self.nmIfEcus.append(value)
        return self
    
class UdpNmCluster(NmCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmCbvPosition = None                           # type: Integer
        self.nmImmediateNmCycleTime = None                  # type: TimeValue
        self.nmImmediateNmTransmissions = None              # type: PositiveInteger
        self.nmMessageTimeoutTime = None                    # type: TimeValue
        self.nmMsgCycleTime = None                          # type: TimeValue
        self.nmNetworkTimeout = None                        # type: TimeValue
        self.nmNidPosition = None                           # type: Integer
        self.nmRemoteSleepIndicationTime = None             # type: TimeValue
        self.nmRepeatMessageTime = None                     # type: TimeValue
        self.nmWaitBusSleepTime = None                      # type: TimeValue
        self.vlanRef = None                                 # type: RefType

    def getNmCbvPosition(self):
        return self.nmCbvPosition

    def setNmCbvPosition(self, value):
        if value is not None:
            self.nmCbvPosition = value
        return self

    def getNmImmediateNmCycleTime(self):
        return self.nmImmediateNmCycleTime

    def setNmImmediateNmCycleTime(self, value):
        if value is not None:
            self.nmImmediateNmCycleTime = value
        return self

    def getNmImmediateNmTransmissions(self):
        return self.nmImmediateNmTransmissions

    def setNmImmediateNmTransmissions(self, value):
        if value is not None:
            self.nmImmediateNmTransmissions = value
        return self

    def getNmMessageTimeoutTime(self):
        return self.nmMessageTimeoutTime

    def setNmMessageTimeoutTime(self, value):
        if value is not None:
            self.nmMessageTimeoutTime = value
        return self

    def getNmMsgCycleTime(self):
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value):
        if value is not None:
            self.nmMsgCycleTime = value
        return self

    def getNmNetworkTimeout(self):
        return self.nmNetworkTimeout

    def setNmNetworkTimeout(self, value):
        if value is not None:
            self.nmNetworkTimeout = value
        return self

    def getNmNidPosition(self):
        return self.nmNidPosition

    def setNmNidPosition(self, value):
        if value is not None:
            self.nmNidPosition = value
        return self

    def getNmRemoteSleepIndicationTime(self):
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value):
        if value is not None:
            self.nmRemoteSleepIndicationTime = value
        return self

    def getNmRepeatMessageTime(self):
        return self.nmRepeatMessageTime

    def setNmRepeatMessageTime(self, value):
        if value is not None:
            self.nmRepeatMessageTime = value
        return self

    def getNmWaitBusSleepTime(self):
        return self.nmWaitBusSleepTime

    def setNmWaitBusSleepTime(self, value):
        if value is not None:
            self.nmWaitBusSleepTime = value
        return self

    def getVlanRef(self):
        return self.vlanRef

    def setVlanRef(self, value):
        if value is not None:
            self.vlanRef = value
        return self

        