from abc import ABC
from enum import Enum
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement, FrameTriggering, ISignalTriggering, PduTriggering


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
    A physical channel is the transmission medium that is used to send and receive information between communicating ECUs. Each CommunicationCluster has at least one physical channel. Bus systems like CAN and LIN only have exactly one PhysicalChannel. A FlexRay cluster may have more than one PhysicalChannels that may be used in parallel for redundant communication. An ECU is part of a cluster if it contains at least one controller that is connected to at least one channel of the cluster.
    """

    # PhysicalChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.7, p.59
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCommConnectorRefs            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addCommConnectorRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFrameTriggerings             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCanFrameTriggering        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createLinFrameTriggering        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createFlexrayFrameTriggering     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalTriggerings           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createISignalTriggering         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getManagedPhysicalChannelRefs   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addManagedPhysicalChannelRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduTriggerings               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createPduTriggering             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PhysicalChannel:
            raise TypeError("PhysicalChannel is an abstract class.")

        super().__init__(parent, short_name)

        # Reference to the ECUInstance via a Communication Connector to which the channel is connected. atpVariation: Variable assignment of Physical Channels to different CommunicationConnectors is expressed with this variation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=commConnector.communicationConnector, commConnector.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.commConnectorRefs: List[RefType] = []

        # One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.frameTriggerings: List[FrameTriggering] = []

        # One ISignalTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of ISignaltriggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.shortName, iSignal Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.iSignalTriggerings: List[ISignalTriggering] = []

        # Reference between a channel with role managing channel and a channel with role managed channel.
        self.managedPhysicalChannelRefs: List[RefType] = []

        # One PduTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of I-Pdu triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.shortName, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.pduTriggerings: List[PduTriggering] = []

    def getCommConnectorRefs(self) -> List[RefType]:
        """
        Reference to the ECUInstance via a Communication Connector to which the channel is connected. atpVariation: Variable assignment of Physical Channels to different CommunicationConnectors is expressed with this variation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=commConnector.communicationConnector, commConnector.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.commConnectorRefs

    def addCommConnectorRef(self, value: RefType) -> "PhysicalChannel":
        """
        Reference to the ECUInstance via a Communication Connector to which the channel is connected. atpVariation: Variable assignment of Physical Channels to different CommunicationConnectors is expressed with this variation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=commConnector.communicationConnector, commConnector.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and does not overwrite an existing commConnectorRefs.
        """
        if value is not None:
            self.commConnectorRefs.append(value)
        return self

    def getFrameTriggerings(self) -> List[FrameTriggering]:
        """
        One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return list(sorted(self.frameTriggerings, key=lambda o: o.getShortName()))

    def createCanFrameTriggering(self, short_name: str) -> CanFrameTriggering:
        """
        One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if short_name not in self.elements:
            triggering = CanFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def createLinFrameTriggering(self, short_name: str) -> LinFrameTriggering:
        """
        One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if short_name not in self.elements:
            triggering = LinFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def createFlexrayFrameTriggering(self, short_name: str) -> FlexrayFrameTriggering:
        """
        One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if short_name not in self.elements:
            triggering = FlexrayFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def getISignalTriggerings(self) -> List[ISignalTriggering]:
        """
        One ISignalTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of ISignaltriggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.shortName, iSignal Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return list(sorted(self.iSignalTriggerings, key=lambda o: o.getShortName()))

    def createISignalTriggering(self, short_name: str) -> ISignalTriggering:
        """
        One ISignalTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of ISignaltriggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.shortName, iSignal Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if short_name not in self.elements:
            triggering = ISignalTriggering(self, short_name)
            self.addElement(triggering)
            self.iSignalTriggerings.append(triggering)
        return self.getElement(short_name)

    def getManagedPhysicalChannelRefs(self) -> List[RefType]:
        """
        Reference between a channel with role managing channel and a channel with role managed channel.
        """
        return self.managedPhysicalChannelRefs

    def addManagedPhysicalChannelRef(self, value: RefType) -> "PhysicalChannel":
        """
        Reference between a channel with role managing channel and a channel with role managed channel.
        A None value is a no-op and does not overwrite an existing managedPhysicalChannelRefs.
        """
        if value is not None:
            self.managedPhysicalChannelRefs.append(value)
        return self

    def getPduTriggerings(self) -> List[PduTriggering]:
        """
        One PduTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of I-Pdu triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.shortName, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return list(sorted(self.pduTriggerings, key=lambda o: o.getShortName()))

    def createPduTriggering(self, short_name: str) -> PduTriggering:
        """
        One PduTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of I-Pdu triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.shortName, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if short_name not in self.elements:
            triggering = PduTriggering(self, short_name)
            self.addElement(triggering)
            self.pduTriggerings.append(triggering)
        return self.getElement(short_name)


class AbstractCanPhysicalChannel(PhysicalChannel, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN PhysicalChannel attributes.
    """

    # AbstractCanPhysicalChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.20, p.73
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (no own attributes; Base = ARObject, Identifiable, MultilanguageReferrable, PhysicalChannel, Referrable)

    def __init__(self, parent, short_name):
        if type(self) is AbstractCanPhysicalChannel:
            raise TypeError("AbstractCanPhysicalChannel is an abstract class.")

        super().__init__(parent, short_name)


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """
    CAN bus specific physical channel attributes.
    """

    # CanPhysicalChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.21, p.73
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # (no own attributes; Base = ARObject, AbstractCanPhysicalChannel, Identifiable, MultilanguageReferrable, PhysicalChannel, Referrable)

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


class CommunicationDirectionType(AREnum):
    """
    Enumeration defining communication direction types,
    specifying whether communication is inbound or outbound.
    """

    # CommunicationDirectionType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    ENUM_IN = "in"
    ENUM_OUT = "out"

    def __init__(self):
        super().__init__([CommunicationDirectionType.ENUM_IN, CommunicationDirectionType.ENUM_OUT])


class CommConnectorPort(Identifiable, ABC):
    """
    Abstract base class for communication connector ports,
    defining common properties for different types of
    communication ports including direction and processing.
    """

    # CommConnectorPort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationDirection    [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommConnectorPort:
            raise TypeError("CommConnectorPort is an abstract class.")

        super().__init__(parent, short_name)

        self.communicationDirection: CommunicationDirectionType = None

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value):
        if value is not None:
            self.communicationDirection = value
        return self


class FramePort(CommConnectorPort):
    """
    Represents a frame port for communication connectors,
    handling frame-based communication at the connector level.
    """

    # FramePort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IPduSignalProcessingEnum(Enum):
    """
    Enumeration defining types of IPDU signal processing,
    specifying whether signal processing is deferred or immediate.
    """

    # IPduSignalProcessingEnum method parity checklist:
    # (no methods)

    ENUM_DEFERRED = "deferred"
    ENUM_IMMEDIATE = "immediate"


class IPduPort(CommConnectorPort):
    """
    Represents an IPDU port for communication connectors,
    handling Interaction Protocol Data Unit communication
    with specific processing and security properties.
    """

    # IPduPort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduSignalProcessing      [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduSignalProcessing      [x] impl  [ ] docstring  [ ] test
    # [ ] getKeyId                     [x] impl  [ ] docstring  [ ] test
    # [ ] setKeyId                     [x] impl  [ ] docstring  [ ] test
    # [ ] getRxSecurityVerification    [x] impl  [ ] docstring  [ ] test
    # [ ] setRxSecurityVerification    [x] impl  [ ] docstring  [ ] test
    # [ ] getTimestampRxAcceptanceWindow [x] impl  [ ] docstring  [ ] test
    # [ ] setTimestampRxAcceptanceWindow [x] impl  [ ] docstring  [ ] test
    # [ ] getUseAuthDataFreshness      [x] impl  [ ] docstring  [ ] test
    # [ ] setUseAuthDataFreshness      [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.iPduSignalProcessing: IPduSignalProcessingEnum = None
        self.keyId: PositiveInteger = None
        self.rxSecurityVerification: Boolean = None
        self.timestampRxAcceptanceWindow: TimeValue = None
        self.useAuthDataFreshness: Boolean = None

    def getIPduSignalProcessing(self):
        return self.iPduSignalProcessing

    def setIPduSignalProcessing(self, value):
        if value is not None:
            self.iPduSignalProcessing = value
        return self

    def getKeyId(self):
        return self.keyId

    def setKeyId(self, value):
        if value is not None:
            self.keyId = value
        return self

    def getRxSecurityVerification(self):
        return self.rxSecurityVerification

    def setRxSecurityVerification(self, value):
        if value is not None:
            self.rxSecurityVerification = value
        return self

    def getTimestampRxAcceptanceWindow(self):
        return self.timestampRxAcceptanceWindow

    def setTimestampRxAcceptanceWindow(self, value):
        if value is not None:
            self.timestampRxAcceptanceWindow = value
        return self

    def getUseAuthDataFreshness(self):
        return self.useAuthDataFreshness

    def setUseAuthDataFreshness(self, value):
        if value is not None:
            self.useAuthDataFreshness = value
        return self


class ISignalPort(CommConnectorPort):
    """
    Represents an interaction signal port for communication connectors,
    handling interaction signal communication with filtering,
    timeout, and validity handling properties.
    """

    # ISignalPort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataFilter                [x] impl  [ ] docstring  [ ] test
    # [ ] setDataFilter                [x] impl  [ ] docstring  [ ] test
    # [ ] getDdsQosProfileRef          [x] impl  [ ] docstring  [ ] test
    # [ ] setDdsQosProfileRef          [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstTimeout              [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstTimeout              [x] impl  [ ] docstring  [ ] test
    # [ ] getHandleInvalid             [x] impl  [ ] docstring  [ ] test
    # [ ] setHandleInvalid             [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeout                   [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeout                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataFilter: DataFilter = None
        self.ddsQosProfileRef: RefType = None
        self.firstTimeout: TimeValue = None
        self.handleInvalid = None
        self.timeout: TimeValue = None

    def getDataFilter(self):
        return self.dataFilter

    def setDataFilter(self, value):
        if value is not None:
            self.dataFilter = value
        return self

    def getDdsQosProfileRef(self):
        return self.ddsQosProfileRef

    def setDdsQosProfileRef(self, value):
        if value is not None:
            self.ddsQosProfileRef = value
        return self

    def getFirstTimeout(self):
        return self.firstTimeout

    def setFirstTimeout(self, value):
        if value is not None:
            self.firstTimeout = value
        return self

    def getHandleInvalid(self):
        return self.handleInvalid

    def setHandleInvalid(self, value):
        if value is not None:
            self.handleInvalid = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        if value is not None:
            self.timeout = value
        return self


class CommunicationConnector(Identifiable, ABC):
    """
    The connection between the referencing ECU and the referenced channel via the referenced controller. Connectors are used to describe the bus interfaces of the ECUs and to specify the sending/receiving behavior. Each CommunicationConnector has a reference to exactly one communicationController. Note: Several CommunicationConnectors can be assigned to one PhysicalChannel in the scope of one ECU Instance.
    """

    # CommunicationConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.4, p.54
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCommControllerRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCommControllerRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCreateEcuWakeupSource                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCreateEcuWakeupSource                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDynamicPncToChannelMappingEnabled    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDynamicPncToChannelMappingEnabled    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEcuCommPortInstances                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createFramePort                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createIPduPort                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createISignalPort                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPncFilterArrayMasks                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPncFilterArrayMask                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPncGatewayType                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPncGatewayType                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationConnector:
            raise TypeError("CommunicationConnector is an abstract class.")

        super().__init__(parent, short_name)

        # Reference to the communication controller. The CommunicationConnector and referenced CommunicationController shall be aggregated by the same ECUInstance. The communicationController can be referenced by several CommunicationConnector elements. This is important for the FlexRay Bus. FlexRay communicates via two physical channels. But only one controller in an ECU is responsible for both channels. Thus, two connectors (for channel A and for channel B) shall reference to the same controller.
        self.commControllerRef: Optional[RefType] = None

        # If this parameter is available and set to true then a channel wakeup source shall be created for the Physical Channel referencing this CommunicationConnector.
        self.createEcuWakeupSource: Optional[Boolean] = None

        # Defines if this EcuInstance shall implement the dynamic PNC-to-channel-mapping functionality on this CommunicationConnector and its respective Physical Channel. Tags: atp.Status=draft
        self.dynamicPncToChannelMappingEnabled: Optional[Boolean] = None

        # An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.ecuCommPortInstances: List[CommConnectorPort] = []

        # Bit mask for NM-Pdu Payload used to configure the NM filter mask for the Network Management.
        self.pncFilterArrayMasks: List[PositiveInteger] = []

        # Defines if this EcuInstance shall implement the Pnc Gateway functionality on this CommunicationConnector and its respective PhysicalChannel. Several Ecu Instances on the same PhysicalChannel can have the PncGateway functionality enabled, but only one of them shall have the pncGatewayType "active".
        self.pncGatewayType: Optional[PncGatewayTypeEnum] = None

    def getCommControllerRef(self) -> Optional[RefType]:
        """
        Reference to the communication controller. The CommunicationConnector and referenced CommunicationController shall be aggregated by the same ECUInstance. The communicationController can be referenced by several CommunicationConnector elements. This is important for the FlexRay Bus. FlexRay communicates via two physical channels. But only one controller in an ECU is responsible for both channels. Thus, two connectors (for channel A and for channel B) shall reference to the same controller.
        """
        return self.commControllerRef

    def setCommControllerRef(self, value: Optional[RefType]) -> "CommunicationConnector":
        """
        Reference to the communication controller. The CommunicationConnector and referenced CommunicationController shall be aggregated by the same ECUInstance. The communicationController can be referenced by several CommunicationConnector elements. This is important for the FlexRay Bus. FlexRay communicates via two physical channels. But only one controller in an ECU is responsible for both channels. Thus, two connectors (for channel A and for channel B) shall reference to the same controller.
        A None value is a no-op and does not overwrite an existing commControllerRef.
        """
        if value is not None:
            self.commControllerRef = value
        return self

    def getCreateEcuWakeupSource(self) -> Optional[Boolean]:
        """
        If this parameter is available and set to true then a channel wakeup source shall be created for the Physical Channel referencing this CommunicationConnector.
        """
        return self.createEcuWakeupSource

    def setCreateEcuWakeupSource(self, value: Optional[Boolean]) -> "CommunicationConnector":
        """
        If this parameter is available and set to true then a channel wakeup source shall be created for the Physical Channel referencing this CommunicationConnector.
        A None value is a no-op and does not overwrite an existing createEcuWakeupSource.
        """
        if value is not None:
            if not isinstance(value, Boolean):
                boolean = Boolean()
                boolean.setValue(value)
                value = boolean
            self.createEcuWakeupSource = value
        return self

    def getDynamicPncToChannelMappingEnabled(self) -> Optional[Boolean]:
        """
        Defines if this EcuInstance shall implement the dynamic PNC-to-channel-mapping functionality on this CommunicationConnector and its respective Physical Channel. Tags: atp.Status=draft
        """
        return self.dynamicPncToChannelMappingEnabled

    def setDynamicPncToChannelMappingEnabled(self, value: Optional[Boolean]) -> "CommunicationConnector":
        """
        Defines if this EcuInstance shall implement the dynamic PNC-to-channel-mapping functionality on this CommunicationConnector and its respective Physical Channel. Tags: atp.Status=draft
        A None value is a no-op and does not overwrite an existing dynamicPncToChannelMappingEnabled.
        """
        if value is not None:
            if not isinstance(value, Boolean):
                boolean = Boolean()
                boolean.setValue(value)
                value = boolean
            self.dynamicPncToChannelMappingEnabled = value
        return self

    def getEcuCommPortInstances(self) -> List[CommConnectorPort]:
        """
        An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return list(sorted(self.ecuCommPortInstances, key=lambda o: o.getShortName()))

    def createFramePort(self, short_name) -> FramePort:
        """
        An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if self.getElement(short_name) is None:
            port = FramePort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createIPduPort(self, short_name) -> IPduPort:
        """
        An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if self.getElement(short_name) is None:
            port = IPduPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createISignalPort(self, short_name) -> ISignalPort:
        """
        An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if self.getElement(short_name) is None:
            port = ISignalPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def getPncFilterArrayMasks(self) -> List[PositiveInteger]:
        """
        Bit mask for NM-Pdu Payload used to configure the NM filter mask for the Network Management.
        """
        return self.pncFilterArrayMasks

    def addPncFilterArrayMask(self, value: Optional[PositiveInteger]) -> "CommunicationConnector":
        """
        Bit mask for NM-Pdu Payload used to configure the NM filter mask for the Network Management.
        A None value is a no-op and does not overwrite an existing pncFilterArrayMasks.
        """
        if value is not None:
            self.pncFilterArrayMasks.append(value)
        return self

    def getPncGatewayType(self) -> Optional[PncGatewayTypeEnum]:
        """
        Defines if this EcuInstance shall implement the Pnc Gateway functionality on this CommunicationConnector and its respective PhysicalChannel. Several Ecu Instances on the same PhysicalChannel can have the PncGateway functionality enabled, but only one of them shall have the pncGatewayType "active".
        """
        return self.pncGatewayType

    def setPncGatewayType(self, value: Optional[PncGatewayTypeEnum]) -> "CommunicationConnector":
        """
        Defines if this EcuInstance shall implement the Pnc Gateway functionality on this CommunicationConnector and its respective PhysicalChannel. Several Ecu Instances on the same PhysicalChannel can have the PncGateway functionality enabled, but only one of them shall have the pncGatewayType "active".
        A None value is a no-op and does not overwrite an existing pncGatewayType.
        """
        if value is not None:
            self.pncGatewayType = value
        return self
