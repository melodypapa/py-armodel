from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommConnectorPort,
    FibexElement,
    FramePort,
    FrameTriggering,
    IPduPort,
    ISignalPort,
    ISignalTriggering,
    PduTriggering,
)


class CommunicationCycle(ARObject, ABC):
    """
    Abstract base class for communication cycles, defining common
    properties for different types of communication timing cycles
    in the AUTOSAR communication system.
    """

    # CommunicationCycle method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is CommunicationCycle:
            raise TypeError("CommunicationCycle is an abstract class.")
        super().__init__()


class CycleCounter(CommunicationCycle):
    """
    Defines a counter for communication cycles, specifying the
    count value for cycle tracking in timed communication systems.
    """

    # CycleCounter method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCycleCounter              [x] impl  [ ] docstring  [ ] test
    # [ ] setCycleCounter              [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.CycleCounter: Integer = None

    def getCycleCounter(self):
        return self.CycleCounter

    def setCycleCounter(self, value):
        if value is not None:
            self.CycleCounter = value
        return self


class CycleRepetitionType(AREnum):
    """
    Enumeration defining types of cycle repetitions in communication
    scheduling, specifying how communication cycles are repeated
    over time.
    """

    # CycleRepetitionType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__([])


class CycleRepetition(CommunicationCycle):
    """
    Defines repetition properties for communication cycles,
    specifying base cycle and repetition pattern for cyclic
    communication scheduling.
    """

    # CycleRepetition method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseCycle                 [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseCycle                 [x] impl  [ ] docstring  [ ] test
    # [ ] getCycleRepetition           [x] impl  [ ] docstring  [ ] test
    # [ ] setCycleRepetition           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.BaseCycle: Integer = None
        self.CycleRepetition: CycleRepetitionType = None

    def getBaseCycle(self):
        return self.BaseCycle

    def setBaseCycle(self, value):
        if value is not None:
            self.BaseCycle = value
        return self

    def getCycleRepetition(self):
        return self.CycleRepetition

    def setCycleRepetition(self, value):
        if value is not None:
            self.CycleRepetition = value
        return self


class PhysicalChannel(Identifiable, ABC):
    """
    Abstract base class for physical communication channels,
    defining common properties for different types of physical
    communication media including connector references and
    frame triggering mechanisms.
    """

    # PhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommConnectorRefs         [x] impl  [ ] docstring  [ ] test
    # [ ] addCommConnectorRef          [x] impl  [ ] docstring  [ ] test
    # [ ] getFrameTriggerings          [x] impl  [ ] docstring  [ ] test
    # [ ] createCanFrameTriggering     [x] impl  [ ] docstring  [ ] test
    # [ ] createLinFrameTriggering     [x] impl  [ ] docstring  [ ] test
    # [ ] createFlexrayFrameTriggering [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalTriggerings        [x] impl  [ ] docstring  [ ] test
    # [ ] createISignalTriggering      [x] impl  [ ] docstring  [ ] test
    # [ ] getManagedPhysicalChannelRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addManagedPhysicalChannelRef [x] impl  [ ] docstring  [ ] test
    # [ ] getPduTriggerings            [x] impl  [ ] docstring  [ ] test
    # [ ] createPduTriggering          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PhysicalChannel:
            raise TypeError("PhysicalChannel is an abstract class.")

        super().__init__(parent, short_name)

        self.commConnectorRefs: List[RefType] = []
        self.frameTriggerings: List[FrameTriggering] = []
        self.managedPhysicalChannelRefs: List[RefType] = []

    def getCommConnectorRefs(self):
        return self.commConnectorRefs

    def addCommConnectorRef(self, value):
        self.commConnectorRefs.append(value)
        return self

    def getFrameTriggerings(self) -> List[FrameTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, FrameTriggering), self.elements), key=lambda o: o.getShortName()))

    def createCanFrameTriggering(self, short_name: str) -> CanFrameTriggering:
        if short_name not in self.elements:
            triggering = CanFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def createLinFrameTriggering(self, short_name: str) -> LinFrameTriggering:
        if short_name not in self.elements:
            triggering = LinFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def createFlexrayFrameTriggering(self, short_name: str) -> FlexrayFrameTriggering:
        if short_name not in self.elements:
            triggering = FlexrayFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def getISignalTriggerings(self) -> List[ISignalTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, ISignalTriggering), self.elements), key=lambda o: o.getShortName()))

    def createISignalTriggering(self, short_name: str):
        if short_name not in self.elements:
            triggering = ISignalTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)

    def getManagedPhysicalChannelRefs(self):
        return self.managedPhysicalChannelRefs

    def addManagedPhysicalChannelRef(self, value):
        self.managedPhysicalChannelRefs.append(value)
        return self

    def getPduTriggerings(self) -> List[PduTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, PduTriggering), self.elements), key=lambda o: o.getShortName()))

    def createPduTriggering(self, short_name: str):
        if short_name not in self.elements:
            triggering = PduTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)


class AbstractCanPhysicalChannel(PhysicalChannel, ABC):
    """
    Abstract base class for CAN physical channels, defining
    common properties for CAN-specific physical communication
    channels in the AUTOSAR system.
    """

    # AbstractCanPhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        if type(self) is AbstractCanPhysicalChannel:
            raise TypeError("AbstractCanPhysicalChannel is an abstract class.")

        super().__init__(parent, short_name)


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """
    Represents a CAN physical channel in the communication system,
    implementing specific properties for CAN bus communication
    including frame triggering and connector management.
    """

    # CanPhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class LinPhysicalChannel(PhysicalChannel):
    """
    Represents a LIN physical channel in the communication system,
    defining LIN-specific properties including bus idle timeout
    and schedule tables for LIN network communication.
    """

    # LinPhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBusIdleTimeoutPeriod      [x] impl  [ ] docstring  [ ] test
    # [ ] setBusIdleTimeoutPeriod      [x] impl  [ ] docstring  [ ] test
    # [ ] getScheduleTables            [x] impl  [ ] docstring  [ ] test
    # [ ] createLinScheduleTable       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.busIdleTimeoutPeriod: TimeValue = None
        self.scheduleTables: List[LinScheduleTable] = []

    def getBusIdleTimeoutPeriod(self):
        return self.busIdleTimeoutPeriod

    def setBusIdleTimeoutPeriod(self, value):
        if value is not None:
            self.busIdleTimeoutPeriod = value
        return self

    def getScheduleTables(self):
        return self.scheduleTables

    def createLinScheduleTable(self, short_name: str) -> LinScheduleTable:
        if short_name not in self.elements:
            end_point = LinScheduleTable(self, short_name)
            self.addElement(end_point)
            self.scheduleTables.append(end_point)
        return self.getElement(short_name)


class VlanConfig(Identifiable):
    """
    Defines Virtual LAN (VLAN) configuration properties,
    specifying VLAN identifiers for network segmentation
    and traffic management in Ethernet communication.
    """

    # VlanConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getVlanIdentifier            [x] impl  [ ] docstring  [ ] test
    # [ ] setVlanIdentifier            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.vlanIdentifier: PositiveInteger = None

    def getVlanIdentifier(self):
        return self.vlanIdentifier

    def setVlanIdentifier(self, value):
        if value is not None:
            self.vlanIdentifier = value
        return self


class EthernetPhysicalChannel(PhysicalChannel):
    """
    Represents an Ethernet physical channel in the communication system,
    defining Ethernet-specific properties including network endpoints,
    Socket Adaptor (SoAd) configuration, and VLAN settings.
    """

    # EthernetPhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNetworkEndpoints          [x] impl  [ ] docstring  [ ] test
    # [ ] createNetworkEndPoint        [x] impl  [ ] docstring  [ ] test
    # [ ] getSoAdConfig                [x] impl  [ ] docstring  [ ] test
    # [ ] setSoAdConfig                [x] impl  [ ] docstring  [ ] test
    # [ ] getVlan                      [x] impl  [ ] docstring  [ ] test
    # [ ] createVlanConfig             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.networkEndpoints: List[NetworkEndpoint] = []
        self.soAdConfig = None
        self.vlan: VlanConfig = None

    def getNetworkEndpoints(self):
        return self.networkEndpoints

    def createNetworkEndPoint(self, short_name: str) -> NetworkEndpoint:
        if short_name not in self.elements:
            end_point = NetworkEndpoint(self, short_name)
            self.addElement(end_point)
            self.networkEndpoints.append(end_point)
        return self.getElement(short_name)

    def getSoAdConfig(self):
        return self.soAdConfig

    def setSoAdConfig(self, value):
        self.soAdConfig = value
        return self

    def getVlan(self):
        return self.vlan

    def createVlanConfig(self, short_name: str) -> VlanConfig:
        if short_name not in self.elements:
            config = VlanConfig(self, short_name)
            self.vlan = config
            self.addElement(config)
        return self.getElement(short_name)


class FlexrayChannelName(AREnum):
    """
    Enumeration defining names for FlexRay channels,
    specifying the available channel designations
    in FlexRay communication systems.
    """

    # FlexrayChannelName method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    CHANNEL_A = "channelA"
    channel_B = "channelB"

    def __init__(self):
        super().__init__([FlexrayChannelName.CHANNEL_A, FlexrayChannelName.channel_B])


class FlexrayPhysicalChannel(PhysicalChannel):
    """
    Represents a FlexRay physical channel in the communication system,
    defining FlexRay-specific properties including channel name
    designation for dual-channel FlexRay communication.
    """

    # FlexrayPhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getChannelName               [x] impl  [ ] docstring  [ ] test
    # [ ] setChannelName               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.channelName = None  # type: FlexrayChannelName

    def getChannelName(self):
        return self.channelName

    def setChannelName(self, value):
        if value is not None:
            self.channelName = value
        return self


class CommunicationCluster(FibexElement, ABC):
    """The CommunicationCluster is the main element to describe the topological connection of communicating ECUs. A cluster describes the ensemble of ECUs, which are linked by a communication medium of arbitrary topology (bus, star, ring, ...). The nodes within the cluster share the same communication protocol, which may be event-triggered, time-triggered or a combination of both. A CommunicationCluster aggregates one or more physical channels. Tags: vh.latestBindingTime=postBuild"""

    # CommunicationCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.6, p.57
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaudrate                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaudrate                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPhysicalChannels          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getCanPhysicalChannels       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getLinPhysicalChannels       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getEthernetPhysicalChannels  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCanPhysicalChannel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createLinPhysicalChannel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEthernetPhysicalChannel [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createFlexrayPhysicalChannel [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProtocolName              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProtocolName              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProtocolVersion           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProtocolVersion           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationCluster:
            raise TypeError("CommunicationCluster is an abstract class.")

        super().__init__(parent, short_name)

        # Channels speed in bits/s.
        self.baudrate: Optional[PositiveUnlimitedInteger] = None

        # This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        self.physicalChannel: List[PhysicalChannel] = []

        # The name of the protocol used.
        self.protocolName: Optional[String] = None

        # The version of the protocol used.
        self.protocolVersion: Optional[String] = None

    def getBaudrate(self) -> Optional[PositiveUnlimitedInteger]:
        """
        Channels speed in bits/s.
        """
        return self.baudrate

    def setBaudrate(self, value: Optional[PositiveUnlimitedInteger]) -> "CommunicationCluster":
        """
        Channels speed in bits/s.
        A None value is a no-op and does not overwrite an existing baudrate.
        """
        if value is not None:
            self.baudrate = value
        return self

    def getPhysicalChannels(self) -> List[PhysicalChannel]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        return list(sorted(self.physicalChannel, key=lambda o: o.getShortName()))

    def getCanPhysicalChannels(self) -> List[CanPhysicalChannel]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        return list(sorted(filter(lambda a: isinstance(a, CanPhysicalChannel), self.physicalChannel), key=lambda o: o.getShortName()))

    def getLinPhysicalChannels(self) -> List[LinPhysicalChannel]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        return list(sorted(filter(lambda a: isinstance(a, LinPhysicalChannel), self.physicalChannel), key=lambda o: o.getShortName()))

    def getEthernetPhysicalChannels(self) -> List[EthernetPhysicalChannel]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        return list(sorted(filter(lambda a: isinstance(a, EthernetPhysicalChannel), self.physicalChannel), key=lambda o: o.getShortName()))

    def createCanPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        if short_name not in self.elements:
            channel = CanPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)

    def createLinPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        if short_name not in self.elements:
            channel = LinPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)

    def createEthernetPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        if short_name not in self.elements:
            channel = EthernetPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)

    def createFlexrayPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        if short_name not in self.elements:
            channel = FlexrayPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)

    def getProtocolName(self) -> Optional[String]:
        """
        The name of the protocol used.
        """
        return self.protocolName

    def setProtocolName(self, value: Optional[String]) -> "CommunicationCluster":
        """
        The name of the protocol used.
        A None value is a no-op and does not overwrite an existing protocolName.
        """
        if value is not None:
            self.protocolName = value
        return self

    def getProtocolVersion(self) -> Optional[String]:
        """
        The version of the protocol used.
        """
        return self.protocolVersion

    def setProtocolVersion(self, value: Optional[String]) -> "CommunicationCluster":
        """
        The version of the protocol used.
        A None value is a no-op and does not overwrite an existing protocolVersion.
        """
        if value is not None:
            self.protocolVersion = value
        return self


class CanClusterBusOffRecovery(ARObject):
    """
    Defines bus off recovery properties for CAN clusters,
    specifying timing and counter configurations for
    CAN controller recovery after bus off conditions.
    """

    # CanClusterBusOffRecovery method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBorCounterL1ToL2          [x] impl  [ ] docstring  [ ] test
    # [ ] setBorCounterL1ToL2          [x] impl  [ ] docstring  [ ] test
    # [ ] getBorTimeL1                 [x] impl  [ ] docstring  [ ] test
    # [ ] setBorTimeL1                 [x] impl  [ ] docstring  [ ] test
    # [ ] getBorTimeL2                 [x] impl  [ ] docstring  [ ] test
    # [ ] setBorTimeL2                 [x] impl  [ ] docstring  [ ] test
    # [ ] getBorTimeTxEnsured          [x] impl  [ ] docstring  [ ] test
    # [ ] setBorTimeTxEnsured          [x] impl  [ ] docstring  [ ] test
    # [ ] getMainFunctionPeriod        [x] impl  [ ] docstring  [ ] test
    # [ ] setMainFunctionPeriod        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.borCounterL1ToL2: PositiveInteger = None
        self.borTimeL1: TimeValue = None
        self.borTimeL2: TimeValue = None
        self.borTimeTxEnsured: TimeValue = None
        self.mainFunctionPeriod: TimeValue = None

    def getBorCounterL1ToL2(self):
        return self.borCounterL1ToL2

    def setBorCounterL1ToL2(self, value):
        if value is not None:
            self.borCounterL1ToL2 = value
        return self

    def getBorTimeL1(self):
        return self.borTimeL1

    def setBorTimeL1(self, value):
        if value is not None:
            self.borTimeL1 = value
        return self

    def getBorTimeL2(self):
        return self.borTimeL2

    def setBorTimeL2(self, value):
        if value is not None:
            self.borTimeL2 = value
        return self

    def getBorTimeTxEnsured(self):
        return self.borTimeTxEnsured

    def setBorTimeTxEnsured(self, value):
        if value is not None:
            self.borTimeTxEnsured = value
        return self

    def getMainFunctionPeriod(self):
        return self.mainFunctionPeriod

    def setMainFunctionPeriod(self, value):
        if value is not None:
            self.mainFunctionPeriod = value
        return self


class AbstractCanCluster(CommunicationCluster, ABC):
    """Abstract class that is used to collect the common TtCAN, J1939 and CAN Cluster attributes."""

    # AbstractCanCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.8, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBusOffRecovery      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBusOffRecovery      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanFdBaudrate       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanFdBaudrate       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanXlBaudrate       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanXlBaudrate       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCluster:
            raise TypeError("AbstractCanCluster is an abstract class.")

        super().__init__(parent, short_name)

        # CAN bus off monitoring / recovery at system level.
        self.busOffRecovery: Optional[CanClusterBusOffRecovery] = None

        # Specifies the data segment baud rate of the controller in bits/s.
        self.canFdBaudrate: Optional[PositiveUnlimitedInteger] = None

        # Specifies the data segment baud rate of the CAN XL controller in bits/s.
        self.canXlBaudrate: Optional[PositiveUnlimitedInteger] = None

    def getBusOffRecovery(self) -> Optional[CanClusterBusOffRecovery]:
        """
        CAN bus off monitoring / recovery at system level.
        """
        return self.busOffRecovery

    def setBusOffRecovery(self, value: Optional[CanClusterBusOffRecovery]) -> "AbstractCanCluster":
        """
        CAN bus off monitoring / recovery at system level.
        A None value is a no-op and does not overwrite an existing busOffRecovery.
        """
        if value is not None:
            self.busOffRecovery = value
        return self

    def getCanFdBaudrate(self) -> Optional[PositiveUnlimitedInteger]:
        """
        Specifies the data segment baud rate of the controller in bits/s.
        """
        return self.canFdBaudrate

    def setCanFdBaudrate(self, value: Optional[PositiveUnlimitedInteger]) -> "AbstractCanCluster":
        """
        Specifies the data segment baud rate of the controller in bits/s.
        A None value is a no-op and does not overwrite an existing canFdBaudrate.
        """
        if value is not None:
            self.canFdBaudrate = value
        return self

    def getCanXlBaudrate(self) -> Optional[PositiveUnlimitedInteger]:
        """
        Specifies the data segment baud rate of the CAN XL controller in bits/s.
        """
        return self.canXlBaudrate

    def setCanXlBaudrate(self, value: Optional[PositiveUnlimitedInteger]) -> "AbstractCanCluster":
        """
        Specifies the data segment baud rate of the CAN XL controller in bits/s.
        A None value is a no-op and does not overwrite an existing canXlBaudrate.
        """
        if value is not None:
            self.canXlBaudrate = value
        return self


class CanCluster(AbstractCanCluster):
    """CAN bus specific cluster attributes. Tags: atp.recommendedPackage=CommunicationClusters"""

    # CanCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.9, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class CommunicationController(Identifiable, ABC):
    """The communication controller is a dedicated hardware device by means of which hosts are sending frames to and receiving frames from the communication medium. Tags: vh.latestBindingTime=postBuild"""

    # CommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.3, p.53
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getWakeUpByControllerSupported [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeUpByControllerSupported [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationController:
            raise TypeError("CommunicationController is an abstract class.")

        super().__init__(parent, short_name)

        # Defines whether the ECU shall be woken up by this CommunicationController. TRUE: wake up is possible FALSE: wake up is not supported Note: If wakeUpByControllerSupported is set to TRUE the feature shall be supported by both hardware and basic software.
        self.wakeUpByControllerSupported: Optional[Boolean] = None

    def getWakeUpByControllerSupported(self) -> Optional[Boolean]:
        """
        Defines whether the ECU shall be woken up by this CommunicationController. TRUE: wake up is possible FALSE: wake up is not supported Note: If wakeUpByControllerSupported is set to TRUE the feature shall be supported by both hardware and basic software.
        """
        return self.wakeUpByControllerSupported

    def setWakeUpByControllerSupported(self, value: Optional[Boolean]) -> "CommunicationController":
        """
        Defines whether the ECU shall be woken up by this CommunicationController. TRUE: wake up is possible FALSE: wake up is not supported Note: If wakeUpByControllerSupported is set to TRUE the feature shall be supported by both hardware and basic software.
        A None value is a no-op and does not overwrite an existing wakeUpByControllerSupported.
        """
        if value is not None:
            self.wakeUpByControllerSupported = value
        return self


class PncGatewayTypeEnum(AREnum):
    """
    Enumeration defining types of PNC (Partial Network Cluster)
    gateways, specifying the gateway behavior in partial
    network communication management.
    """

    # PncGatewayTypeEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    ENUM_ACTIVE = "active"
    ENUM_NONE = "none"
    ENUM_PASSIVE = "passive"

    def __init__(self):
        super().__init__([PncGatewayTypeEnum.ENUM_ACTIVE, PncGatewayTypeEnum.ENUM_NONE, PncGatewayTypeEnum.ENUM_PASSIVE])


class CommunicationConnector(Identifiable, ABC):
    """
    Abstract base class for communication connectors,
    defining common properties for connecting communication
    controllers to communication channels and managing
    port instances and gateway types.
    """

    # CommunicationConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommControllerRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setCommControllerRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getCreateEcuWakeupSource     [x] impl  [ ] docstring  [ ] test
    # [ ] setCreateEcuWakeupSource     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicPncToChannelMappingEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicPncToChannelMappingEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuCommPortInstances      [x] impl  [ ] docstring  [ ] test
    # [ ] createFramePort              [x] impl  [ ] docstring  [ ] test
    # [ ] createIPduPort               [x] impl  [ ] docstring  [ ] test
    # [ ] createISignalPort            [x] impl  [ ] docstring  [ ] test
    # [ ] getPncFilterArrayMasks       [x] impl  [ ] docstring  [ ] test
    # [ ] addPncFilterArrayMask        [x] impl  [ ] docstring  [ ] test
    # [ ] getPncGatewayType            [x] impl  [ ] docstring  [ ] test
    # [ ] setPncGatewayType            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationConnector:
            raise TypeError("CommunicationConnector is an abstract class.")

        super().__init__(parent, short_name)

        self.commControllerRef: RefType = None
        self.createEcuWakeupSource: Boolean = None
        self.dynamicPncToChannelMappingEnabled: Boolean = None
        self.ecuCommPortInstances: List[CommConnectorPort] = []
        self.pncFilterArrayMasks: List[PositiveInteger] = []
        self.pncGatewayType: PncGatewayTypeEnum = None

    def getCommControllerRef(self):
        return self.commControllerRef

    def setCommControllerRef(self, value):
        self.commControllerRef = value
        return self

    def getCreateEcuWakeupSource(self):
        return self.createEcuWakeupSource

    def setCreateEcuWakeupSource(self, value):
        self.createEcuWakeupSource = value
        return self

    def getDynamicPncToChannelMappingEnabled(self):
        return self.dynamicPncToChannelMappingEnabled

    def setDynamicPncToChannelMappingEnabled(self, value):
        self.dynamicPncToChannelMappingEnabled = value
        return self

    def getEcuCommPortInstances(self):
        return list(sorted(filter(lambda a: isinstance(a, CommConnectorPort), self.elements), key=lambda o: o.getShortName()))

    def createFramePort(self, short_name) -> FramePort:
        if short_name not in self.elements:
            port = FramePort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createIPduPort(self, short_name) -> IPduPort:
        if short_name not in self.elements:
            port = IPduPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createISignalPort(self, short_name) -> ISignalPort:
        if short_name not in self.elements:
            port = ISignalPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def getPncFilterArrayMasks(self):
        return self.pncFilterArrayMasks

    def addPncFilterArrayMask(self, value):
        self.pncFilterArrayMasks.append(value)
        return self

    def getPncGatewayType(self):
        return self.pncGatewayType

    def setPncGatewayType(self, value):
        self.pncGatewayType = value
        return self
