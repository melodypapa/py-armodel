# This module contains AUTOSAR System Template classes for network management
# It defines CAN, FlexRay, J1939, and UDP network management configurations

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    ARLiteral,
    ARNumerical,
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    RxIdentifierRange,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
)


class NmClusterCoupling(ARObject, ABC):
    """
    Abstract base class for network management cluster coupling,
    defining common properties for connecting different types of
    network management clusters for coordinated network management.
    """
    def __init__(self) -> None:
        if type(self) is NmClusterCoupling:
            raise TypeError("NmClusterCoupling is an abstract class.")

        super().__init__()

class CanNmClusterCoupling(NmClusterCoupling):
    """
    Defines coupling properties for CAN network management clusters,
    specifying coupled cluster references and CAN-specific NM features
    like busload reduction and immediate restart capabilities.
    """
    def __init__(self) -> None:
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
    """
    Defines coupling properties for FlexRay network management clusters,
    specifying coupled cluster references and FlexRay-specific NM
    schedule variant configurations.
    """
    def __init__(self) -> None:
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


class NmNode(Identifiable, ABC):
    """
    Abstract base class for network management nodes, defining
    common properties for different types of NM nodes including
    controller references, node IDs, and communication properties.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is NmNode:
            raise TypeError("NmNode is an abstract class.")

        super().__init__(parent, short_name)

        self.controllerRef: Union[Union[RefType, None] , None] = None
        self.nmCoordCluster: Union[Union[ARNumerical, None] , None] = None
        self.nmCoordinatorRole: Union[Union[ARLiteral, None] , None] = None
        self.nmIfEcuRef: Union[Union[RefType, None] , None] = None
        self.nmNodeId: Union[Union[ARNumerical, None] , None] = None
        self.nmPassiveModeEnabled: Union[Union[ARBoolean, None] , None] = None
        self.rxNmPduRefs: List[RefType] = []
        self.TxNmPduRefs: List[RefType] = []

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
    """
    Represents a CAN network management node in the system,
    defining CAN-specific NM properties including message
    cycle offsets, timing configurations, and range settings.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.allNmMessagesKeepAwake = None
        self.nmCarWakeUpFilterEnabled = None
        self.nmCarWakeUpRxEnabled = None
        self.nmMsgCycleOffset = None
        self.nmMsgReducedTime = None
        self.nmRangeConfig: Union[Union[RxIdentifierRange, None] , None] = None

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
    """
    Represents a FlexRay network management node in the system,
    defining FlexRay-specific NM properties for time-triggered
    network management communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

class J1939NmNode(NmNode):
    """
    Represents a J1939 network management node in the system,
    defining J1939-specific NM properties for heavy-duty
    vehicle network management communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

class UdpNmNode(NmNode):
    """
    Represents a UDP network management node in the system,
    defining UDP-specific NM properties including message
    timing and wake-up capabilities.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.allNmMessagesKeepAwake: Union[Union[Boolean, None] , None] = None
        self.nmMsgCycleOffset: Union[Union[TimeValue, None] , None] = None

    def getAllNmMessagesKeepAwake(self):
        return self.allNmMessagesKeepAwake

    def setAllNmMessagesKeepAwake(self, value):
        if value is not None:
            self.allNmMessagesKeepAwake = value
        return self

    def getNmMsgCycleOffset(self):
        return self.nmMsgCycleOffset

    def setNmMsgCycleOffset(self, value):
        if value is not None:
            self.nmMsgCycleOffset = value
        return self

class BusspecificNmEcu(ARObject, ABC):
    """
    Abstract base class for bus-specific network management ECU
    configurations, defining common properties for different
    types of bus-specific NM implementations.
    """
    def __init__(self) -> None:
        if type(self) is BusspecificNmEcu:
            raise TypeError("BusspecificNmEcu is an abstract class.")
        super().__init__()

class CanNmEcu(BusspecificNmEcu):
    """
    Defines CAN-specific network management ECU properties,
    implementing bus-specific NM features for CAN communication.
    """
    def __init__(self) -> None:
        super().__init__()

class FlexrayNmEcu(BusspecificNmEcu):
    """
    Defines FlexRay-specific network management ECU properties,
    implementing bus-specific NM features for FlexRay communication.
    """
    def __init__(self) -> None:
        super().__init__()

class J1939NmEcu(BusspecificNmEcu):
    """
    Defines J1939-specific network management ECU properties,
    implementing bus-specific NM features for J1939 communication.
    """
    def __init__(self) -> None:
        super().__init__()

class UdpNmEcu(BusspecificNmEcu):
    """
    Defines UDP-specific network management ECU properties,
    implementing bus-specific NM features for UDP communication
    including synchronization point capabilities.
    """
    def __init__(self) -> None:
        super().__init__()

        self.nmSynchronizationPointEnabled: Union[Union[Boolean, None] , None] = None

    def getNmSynchronizationPointEnabled(self):
        return self.nmSynchronizationPointEnabled

    def setNmSynchronizationPointEnabled(self, value):
        if value is not None:
            self.nmSynchronizationPointEnabled = value
        return self


class NmEcu(Identifiable):
    """
    Represents a network management ECU in the system,
    defining properties for NM coordination, node detection,
    and communication control across different bus types.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.busDependentNmEcus: List[BusspecificNmEcu] = []
        self.ecuInstanceRef: Union[Union[RefType, None] , None] = None
        self.nmBusSynchronizationEnabled: Union[Union[Boolean, None] , None] = None
        self.nmComControlEnabled: Union[Union[Boolean, None] , None] = None
        self.nmCoordinator = None
        self.nmCycletimeMainFunction: Union[Union[TimeValue, None] , None] = None
        self.nmNodeDetectionEnabled: Union[Union[Boolean, None] , None] = None
        self.nmNodeIdEnabled: Union[Union[Boolean, None] , None] = None
        self.nmPduRxIndicationEnabled: Union[Union[Boolean, None] , None] = None
        self.nmRemoteSleepIndEnabled: Union[Union[Boolean, None] , None] = None
        self.nmRepeatMsgIndEnabled: Union[Union[Boolean, None] , None] = None
        self.nmStateChangeIndEnabled: Union[Union[Boolean, None] , None] = None
        self.nmUserDataEnabled: Union[Union[Boolean, None] , None] = None

    def getBusDependentNmEcus(self):
        return self.busDependentNmEcus

    def addBusDependentNmEcu(self, value):
        if value is not None:
            self.busDependentNmEcus.append(value)
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getNmBusSynchronizationEnabled(self):
        return self.nmBusSynchronizationEnabled

    def setNmBusSynchronizationEnabled(self, value):
        if value is not None:
            self.nmBusSynchronizationEnabled = value
        return self

    def getNmComControlEnabled(self):
        return self.nmComControlEnabled

    def setNmComControlEnabled(self, value):
        if value is not None:
            self.nmComControlEnabled = value
        return self

    def getNmCoordinator(self):
        return self.nmCoordinator

    def setNmCoordinator(self, value):
        if value is not None:
            self.nmCoordinator = value
        return self

    def getNmCycletimeMainFunction(self):
        return self.nmCycletimeMainFunction

    def setNmCycletimeMainFunction(self, value):
        if value is not None:
            self.nmCycletimeMainFunction = value
        return self

    def getNmNodeDetectionEnabled(self):
        return self.nmNodeDetectionEnabled

    def setNmNodeDetectionEnabled(self, value):
        if value is not None:
            self.nmNodeDetectionEnabled = value
        return self

    def getNmNodeIdEnabled(self):
        return self.nmNodeIdEnabled

    def setNmNodeIdEnabled(self, value):
        if value is not None:
            self.nmNodeIdEnabled = value
        return self

    def getNmPduRxIndicationEnabled(self):
        return self.nmPduRxIndicationEnabled

    def setNmPduRxIndicationEnabled(self, value):
        if value is not None:
            self.nmPduRxIndicationEnabled = value
        return self

    def getNmRemoteSleepIndEnabled(self):
        return self.nmRemoteSleepIndEnabled

    def setNmRemoteSleepIndEnabled(self, value):
        if value is not None:
            self.nmRemoteSleepIndEnabled = value
        return self

    def getNmRepeatMsgIndEnabled(self):
        return self.nmRepeatMsgIndEnabled

    def setNmRepeatMsgIndEnabled(self, value):
        if value is not None:
            self.nmRepeatMsgIndEnabled = value
        return self

    def getNmStateChangeIndEnabled(self):
        return self.nmStateChangeIndEnabled

    def setNmStateChangeIndEnabled(self, value):
        if value is not None:
            self.nmStateChangeIndEnabled = value
        return self

    def getNmUserDataEnabled(self):
        return self.nmUserDataEnabled

    def setNmUserDataEnabled(self, value):
        if value is not None:
            self.nmUserDataEnabled = value
        return self

class NmConfig(FibexElement):
    """
    Represents network management configuration in the system,
    defining cluster couplings and ECU configurations for
    comprehensive network management setup.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.nmClusterCouplings: List[NmClusterCoupling] = []
        self.nmIfEcus: List[NmEcu] = []

    def createCanNmCluster(self, short_name: str):          # type: (str) -> CanNmCluster
        if (short_name not in self.elements):
            cluster = CanNmCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def createUdpNmCluster(self, short_name: str):          # type: (str) -> UdpNmCluster
        if (short_name not in self.elements):
            cluster = UdpNmCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name)

    def getCanNmClusters(self):                             # type: () -> List[CanNmCluster]
        return sorted(filter(lambda a: isinstance(a, CanNmCluster), self.elements), key= lambda o:o.short_name)

    def getUdpNmClusters(self):                             # type: () -> List[UdpNmCluster]
        return sorted(filter(lambda a: isinstance(a, UdpNmCluster), self.elements), key= lambda o:o.short_name)

    def getNmClusters(self):                                # type: () -> List[NmCluster]
        return sorted(filter(lambda a: isinstance(a, NmCluster), self.elements), key= lambda o:o.short_name)

    def getNmClusterCouplings(self):
        return self.nmClusterCouplings

    def addNmClusterCouplings(self, value):
        self.nmClusterCouplings.append(value)
        return self

    def getNmIfEcus(self):
        return self.nmIfEcus

    def createNmEcu(self, short_name: str) -> NmEcu:
        if (short_name not in self.elements):
            cluster = NmEcu(self, short_name)
            self.addElement(cluster)
            self.nmIfEcus.append(cluster)
        return self.getElement(short_name)

class NmCluster(Identifiable, ABC):
    """
    Abstract base class for network management clusters,
    defining common properties for different types of
    NM clusters including communication cluster references
    and node management capabilities.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is NmCluster:
            raise TypeError("NmCluster is an abstract class.")
        super().__init__(parent, short_name)

        self.communicationClusterRef = None                              # type: RefType
        self.nmChannelId = None
        self.nmChannelSleepMaster = None
        self.nmNodes = []                                                 # type: List[NmNode]
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
        return sorted(filter(lambda a: isinstance(a, CanNmNode), self.elements), key= lambda o:o.short_name)

    def getUdpNmNodes(self) -> List[UdpNmNode]:
        return sorted(filter(lambda a: isinstance(a, UdpNmNode), self.elements), key= lambda o:o.short_name)

    def getNmNodes(self) -> List[NmNode]:
        return sorted(filter(lambda a: isinstance(a, NmNode), self.elements), key= lambda o:o.short_name)

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
    """
    Represents a CAN network management cluster in the system,
    defining CAN-specific NM properties including busload
    reduction, wake-up configurations, and message timing.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
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
    """
    Represents a FlexRay network management cluster in the system,
    defining FlexRay-specific NM properties for time-triggered
    network management in FlexRay communication networks.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

class J1939NmCluster(NmCluster):
    """
    Represents a J1939 network management cluster in the system,
    defining J1939-specific NM properties for heavy-duty vehicle
    network management communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

class UdpNmClusterCoupling(NmClusterCoupling):
    """
    Defines coupling properties for UDP network management clusters,
    specifying coupled cluster references and UDP-specific NM
    immediate restart capabilities.
    """
    def __init__(self) -> None:
        super().__init__()

        self.coupledClusterRefs: List[RefType] = []
        self.nmImmediateRestartEnabled: Union[Union[Boolean, None] , None] = None

    def getCoupledClusterRefs(self):
        return self.coupledClusterRefs

    def addCoupledClusterRef(self, value):
        if value is not None:
            self.coupledClusterRefs.append(value)
        return self

    def getNmImmediateRestartEnabled(self):
        return self.nmImmediateRestartEnabled

    def setNmImmediateRestartEnabled(self, value):
        if value is not None:
            self.nmImmediateRestartEnabled = value
        return self


class UdpNmCluster(NmCluster):
    """
    Represents a UDP network management cluster in the system,
    defining UDP-specific NM properties including message timing,
    CBV (Common Bit Vector) position, and VLAN references.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.nmCbvPosition: Union[Union[Integer, None] , None] = None
        self.nmChannelActive: Union[Union[Boolean, None] , None] = None
        self.nmImmediateNmCycleTime: Union[Union[TimeValue, None] , None] = None
        self.nmImmediateNmTransmissions: Union[Union[PositiveInteger, None] , None] = None
        self.nmMessageTimeoutTime: Union[Union[TimeValue, None] , None] = None
        self.nmMsgCycleTime: Union[Union[TimeValue, None] , None] = None
        self.nmNetworkTimeout: Union[Union[TimeValue, None] , None] = None
        self.nmNidPosition: Union[Union[Integer, None] , None] = None
        self.nmRemoteSleepIndicationTime: Union[Union[TimeValue, None] , None] = None
        self.nmRepeatMessageTime: Union[Union[TimeValue, None] , None] = None
        self.nmWaitBusSleepTime: Union[Union[TimeValue, None] , None] = None
        self.vlanRef: Union[Union[RefType, None] , None] = None

    def getNmCbvPosition(self):
        return self.nmCbvPosition

    def setNmCbvPosition(self, value):
        if value is not None:
            self.nmCbvPosition = value
        return self

    def getNmChannelActive(self):
        return self.nmChannelActive

    def setNmChannelActive(self, value):
        if value is not None:
            self.nmChannelActive = value
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
