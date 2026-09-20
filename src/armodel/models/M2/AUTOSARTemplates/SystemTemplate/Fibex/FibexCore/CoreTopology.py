from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
        CanClusterBusOffRecovery,
        CanCommunicationConnector,
        CanCommunicationController,
        CanPhysicalChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
        EthernetCommunicationConnector,
        EthernetCommunicationController,
        EthernetPhysicalChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
        FlexrayCommunicationConnector,
        FlexrayCommunicationController,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
        LinCommunicationConnector,
        LinMaster,
        LinPhysicalChannel,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
        CommunicationDirectionType,
        FramePort,
        FrameTriggering,
        IPduPort,
        ISignalPort,
        ISignalTriggering,
        PduTriggering,
    )

    # Rule 0001.10 placeholders - referenced classes not yet implemented; TYPE_CHECKING imports
    # satisfy the forward annotations and are never executed at runtime.
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate import V2xSupportEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import DltConfig
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpConfig
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import ClientIdRange
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuPartition

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


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


class PhysicalChannel(Identifiable, VariationPointCapable, ABC):
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
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering

        if not self.IsElementExists(short_name, CanFrameTriggering):
            triggering = CanFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name, CanFrameTriggering)

    def createLinFrameTriggering(self, short_name: str) -> LinFrameTriggering:
        """
        One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering

        if not self.IsElementExists(short_name, LinFrameTriggering):
            triggering = LinFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name, LinFrameTriggering)

    def createFlexrayFrameTriggering(self, short_name: str) -> FlexrayFrameTriggering:
        """
        One frame triggering is defined for exactly one channel. Channels may have assigned an arbitrary number of frame triggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=frameTriggering.shortName, frame Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering

        if not self.IsElementExists(short_name, FlexrayFrameTriggering):
            triggering = FlexrayFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name, FlexrayFrameTriggering)

    def getISignalTriggerings(self) -> List[ISignalTriggering]:
        """
        One ISignalTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of ISignaltriggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.shortName, iSignal Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return list(sorted(self.iSignalTriggerings, key=lambda o: o.getShortName()))

    def createISignalTriggering(self, short_name: str) -> ISignalTriggering:
        """
        One ISignalTriggering is defined for exactly one channel. Channels may have assigned an arbitrary number of ISignaltriggerings. atpVariation: If signals/PDUs/frames are variable, the corresponding triggerings shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.shortName, iSignal Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering

        if not self.IsElementExists(short_name, ISignalTriggering):
            triggering = ISignalTriggering(self, short_name)
            self.addElement(triggering)
            self.iSignalTriggerings.append(triggering)
        return self.getElement(short_name, ISignalTriggering)

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
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PduTriggering

        if not self.IsElementExists(short_name, PduTriggering):
            triggering = PduTriggering(self, short_name)
            self.addElement(triggering)
            self.pduTriggerings.append(triggering)
        return self.getElement(short_name, PduTriggering)


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

    def getCanPhysicalChannels(self) -> List["CanPhysicalChannel"]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel

        return list(sorted(filter(lambda a: isinstance(a, CanPhysicalChannel), self.physicalChannel), key=lambda o: o.getShortName()))

    def getLinPhysicalChannels(self) -> List[LinPhysicalChannel]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinPhysicalChannel

        return list(sorted(filter(lambda a: isinstance(a, LinPhysicalChannel), self.physicalChannel), key=lambda o: o.getShortName()))

    def getEthernetPhysicalChannels(self) -> List[EthernetPhysicalChannel]:
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetPhysicalChannel

        return list(sorted(filter(lambda a: isinstance(a, EthernetPhysicalChannel), self.physicalChannel), key=lambda o: o.getShortName()))

    def createCanPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel

        if not self.IsElementExists(short_name, CanPhysicalChannel):
            channel = CanPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name, CanPhysicalChannel)

    def createLinPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinPhysicalChannel

        if not self.IsElementExists(short_name, LinPhysicalChannel):
            channel = LinPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name, LinPhysicalChannel)

    def createEthernetPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetPhysicalChannel

        if not self.IsElementExists(short_name, EthernetPhysicalChannel):
            channel = EthernetPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name, EthernetPhysicalChannel)

    def createFlexrayPhysicalChannel(self, short_name: str):
        """
        This relationship defines which channel element belongs to which cluster. A channel shall be assigned to exactly one cluster, whereas a cluster may have one or more channels. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=systemDesignTime
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayPhysicalChannel

        if not self.IsElementExists(short_name, FlexrayPhysicalChannel):
            channel = FlexrayPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name, FlexrayPhysicalChannel)

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


class CommunicationController(Identifiable, VariationPointCapable, ABC):
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


class CommunicationConnector(Identifiable, VariationPointCapable, ABC):
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
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FramePort

        if self.getElement(short_name) is None:
            port = FramePort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createIPduPort(self, short_name) -> IPduPort:
        """
        An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import IPduPort

        if self.getElement(short_name) is None:
            port = IPduPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createISignalPort(self, short_name) -> ISignalPort:
        """
        An ECUs reception or send ports. atpVariation: If signals/PDUs/frames are variable, the corresponding ports shall be variable, too. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuCommPortInstance.shortName, ecu CommPortInstance.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalPort

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


class CommConnectorPort(Identifiable, VariationPointCapable, ABC):
    """
    The Ecu communication relationship defines which signals, Pdus and frames are actually received and transmitted by this ECU. For each signal, Pdu or Frame that is transmitted or received and used by the Ecu an association between an ISignalPort, IPduPort or FramePort with the corresponding Triggering shall be created. An ISignalPort shall be created only if the corresponding signal is handled by COM (RTE or Signal Gateway). If a Pdu Gateway ECU only routes the Pdu without being interested in the content only a FramePort and an IPduPort needs to be created.

    [constr_9103] Existence of communicationDirection: For each CommConnectorPort, the attribute communicationDirection shall exist at the time when the System Description is complete.
    """

    # CommConnectorPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.1, p.303
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCommunicationDirection    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCommunicationDirection    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommConnectorPort:
            raise TypeError("CommConnectorPort is an abstract class.")

        super().__init__(parent, short_name)

        # Communication Direction of the Connector Port (input or output Port).
        self.communicationDirection: Optional[CommunicationDirectionType] = None

    def getCommunicationDirection(self) -> Optional[CommunicationDirectionType]:
        """
        Communication Direction of the Connector Port (input or output Port).
        """
        return self.communicationDirection

    def setCommunicationDirection(self, value: Optional[CommunicationDirectionType]) -> "CommConnectorPort":
        """
        Communication Direction of the Connector Port (input or output Port).
        A None value is a no-op and does not overwrite an existing communicationDirection.
        """
        if value is not None:
            self.communicationDirection = value
        return self


class EcuInstance(FibexElement):
    """
    ECUInstances are used to define the ECUs used in the topology. The type of the ECU is defined by a reference to an ECU specified with the ECU resource description.

    [constr_3008] EcuInstance subelements: The CommunicationConnector and the CommunicationController that is referenced by the CommunicationConnector shall be owned by the same EcuInstance.
    """

    # EcuInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.1, p.52
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAssociatedComIPduGroupRef                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAssociatedComIPduGroupRefs                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAssociatedConsumedProvidedServiceInstanceGroupRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAssociatedConsumedProvidedServiceInstanceGroupRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAssociatedPdurIPduGroupRef                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAssociatedPdurIPduGroupRefs                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getChannelSynchronousWakeup                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setChannelSynchronousWakeup                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClientIdRange                                      [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # [x] setClientIdRange                                      [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] getComConfigurationGwTimeBase                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComConfigurationGwTimeBase                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComConfigurationRxTimeBase                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComConfigurationRxTimeBase                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComConfigurationTxTimeBase                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComConfigurationTxTimeBase                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComEnableMDTForCyclicTransmission                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComEnableMDTForCyclicTransmission                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCanCommunicationController                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createEthernetCommunicationController                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFlexrayCommunicationController                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createLinMaster                                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCommControllers                                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCanCommunicationConnector                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createEthernetCommunicationConnector                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFlexrayCommunicationConnector                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createLinCommunicationConnector                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getConnectors                                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getDltConfig                                          [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # [x] setDltConfig                                          [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] getDoIpConfig                                         [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # [x] setDoIpConfig                                         [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] addEcuTaskProxyRef                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuTaskProxyRefs                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEthSwitchPortGroupDerivation                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEthSwitchPortGroupDerivation                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFirewallRuleRef                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirewallRuleRefs                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createEcuPartition                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPartition                                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPartitions                                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPncNmRequest                                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncNmRequest                                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncPrepareSleepTimer                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncPrepareSleepTimer                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncSynchronousWakeup                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncSynchronousWakeup                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPnResetTime                                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPnResetTime                                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSleepModeSupported                                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSleepModeSupported                                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpPropsRef                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpPropsRef                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpPropsRef                                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpPropsRef                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getV2xSupported                                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setV2xSupported                                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeUpOverBusSupported                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeUpOverBusSupported                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Deferred reader/writer rows ([ ]) pending missing child classes (Rule 0001.10):
    # clientIdRange (ClientIdRange), dltConfig (DltConfig), doIpConfig (DoIpConfig)
    # partition (EcuPartition) wired 2026-09-20: reader via createEcuPartition, writer via getPartitions;
    # addPartition kept as an added convenience mutator (no reader/writer route).

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # With this reference it is possible to identify which ISignalIPduGroups are applicable for which CommunicationConnector/ ECU. Only top level ISignalIPduGroups shall be referenced by an EcuInstance. If an ISignalIPduGroup contains other ISignalIPduGroups than these contained ISignalIPduGroups shall not be referenced by the EcuInstance. Contained ISignalIPduGroups are associated to an EcuInstance via the top level ISignalIPduGroup.
        self.associatedComIPduGroupRefs: List[RefType] = []

        # With this reference it is possible to identify which ConsumedProvidedServiceInstanceGroups are applicable for which ECUInstance.
        self.associatedConsumedProvidedServiceInstanceGroupRefs: List[RefType] = []

        # With this reference it is possible to identify which PduR IPdu Groups are applicable for which CommunicationConnector/ ECU.
        self.associatedPdurIPduGroupRefs: List[RefType] = []

        # If this parameter is available and set to true, then all available channels will be woken up as soon as at least one channel wakeup occurs. If PNCs are configured, then all PNCs will be requested upon a channel wakeup.
        self.channelSynchronousWakeup: Optional[Boolean] = None

        # Restriction of the Client Identifier for this Ecu to an allowed range of numerical values. The Client Identifier of the transaction handle is generated by the client RTE for inter-Ecu Client/Server communication.
        # ClientIdRange class is not yet implemented (Rule 0001.10 placeholder)
        self.clientIdRange: Optional["ClientIdRange"] = None

        # The period between successive calls to Com_MainFunctionRouteSignals of the AUTOSAR COM module in seconds.
        self.comConfigurationGwTimeBase: Optional[TimeValue] = None

        # The period between successive calls to Com_MainFunctionRx of the AUTOSAR COM module in seconds.
        self.comConfigurationRxTimeBase: Optional[TimeValue] = None

        # The period between successive calls to Com_MainFunctionTx of the AUTOSAR COM module in seconds.
        self.comConfigurationTxTimeBase: Optional[TimeValue] = None

        # Enables for the Com module of this EcuInstance the minimum delay time monitoring for cyclic and repeated transmissions (TransmissionModeTiming has cyclicTiming assigned or eventControlledTiming with numberOfRepetitions > 0).
        self.comEnableMDTForCyclicTransmission: Optional[Boolean] = None

        # CommunicationControllers of the ECU.
        self.commControllers: List[CommunicationController] = []

        # All channels controlled by a single controller.
        self.connectors: List[CommunicationConnector] = []

        # Describes the Dlt configuration on this EcuInstance.
        # DltConfig class is not yet implemented (Rule 0001.10 placeholder)
        self.dltConfig: Optional["DltConfig"] = None

        # DoIp configuration on this EcuInstance.
        # DoIpConfig class is not yet implemented (Rule 0001.10 placeholder)
        self.doIpConfig: Optional["DoIpConfig"] = None

        # Reference to OsTaskProxies assigned to the EcuInstance.
        self.ecuTaskProxyRefs: List[RefType] = []

        # Defines whether the derivation of SwitchPortGroups based on VLAN and/or CouplingPort.pncMapping shall be performed for this EcuInstance. If not defined the derivation shall not be done.
        self.ethSwitchPortGroupDerivation: Optional[Boolean] = None

        # Firewall rules defined in the context of an EcuInstance.
        self.firewallRuleRefs: List[RefType] = []

        # Optional definition of Partitions within an Ecu.
        self.partitions: List["EcuPartition"] = []

        # Defines if this EcuInstance shall request Nm on all its PhysicalChannels which have Nm variant set to FULL each time a PNC is requested.
        self.pncNmRequest: Optional[Boolean] = None

        # Time in seconds the PNC state machine shall wait in PNC_PREPARE_SLEEP.
        self.pncPrepareSleepTimer: Optional[TimeValue] = None

        # If this parameter is available and set to true then all available PNCs will be woken up as soon as a channel wakeup occurs. This is ensured by adding all PNCs to all channel wakeup sources during upstream mapping.
        self.pncSynchronousWakeup: Optional[Boolean] = None

        # Specifies the runtime of the reset timer in seconds. This reset time is valid for the reset of PN requests in the EIRA and in the ERA.
        self.pnResetTime: Optional[TimeValue] = None

        # Specifies whether the ECU instance may be put to a "low power mode" • true: sleep mode is supported • false: sleep mode is not supported Note: This flag may only be set to "true" if the feature is supported by both hardware and basic software.
        self.sleepModeSupported: Optional[Boolean] = None

        # EcuInstance specific ICMP (Internet Control Message Protocol) attributes
        self.tcpIpIcmpPropsRef: Optional[RefType] = None

        # EcuInstance specific TcpIp Stack attributes.
        self.tcpIpPropsRef: Optional[RefType] = None

        # This attribute is used to control the existence of the V2X stack on the given EcuInstance.
        # V2xSupportEnum class is not yet implemented (Rule 0001.10 placeholder)
        self.v2xSupported: Optional["V2xSupportEnum"] = None

        # Driver support for wakeup over Bus.
        self.wakeUpOverBusSupported: Optional[Boolean] = None

    def addAssociatedComIPduGroupRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        With this reference it is possible to identify which ISignalIPduGroups are applicable for which CommunicationConnector/ ECU. Only top level ISignalIPduGroups shall be referenced by an EcuInstance. If an ISignalIPduGroup contains other ISignalIPduGroups than these contained ISignalIPduGroups shall not be referenced by the EcuInstance. Contained ISignalIPduGroups are associated to an EcuInstance via the top level ISignalIPduGroup.

        A None value is a no-op and does not add to associatedComIPduGroupRefs.
        """
        if value is not None:
            self.associatedComIPduGroupRefs.append(value)
        return self

    def getAssociatedComIPduGroupRefs(self) -> List[RefType]:
        """
        With this reference it is possible to identify which ISignalIPduGroups are applicable for which CommunicationConnector/ ECU. Only top level ISignalIPduGroups shall be referenced by an EcuInstance. If an ISignalIPduGroup contains other ISignalIPduGroups than these contained ISignalIPduGroups shall not be referenced by the EcuInstance. Contained ISignalIPduGroups are associated to an EcuInstance via the top level ISignalIPduGroup.
        """
        return self.associatedComIPduGroupRefs

    def addAssociatedConsumedProvidedServiceInstanceGroupRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        With this reference it is possible to identify which ConsumedProvidedServiceInstanceGroups are applicable for which ECUInstance.

        A None value is a no-op and does not add to associatedConsumedProvidedServiceInstanceGroupRefs.
        """
        if value is not None:
            self.associatedConsumedProvidedServiceInstanceGroupRefs.append(value)
        return self

    def getAssociatedConsumedProvidedServiceInstanceGroupRefs(self) -> List[RefType]:
        """
        With this reference it is possible to identify which ConsumedProvidedServiceInstanceGroups are applicable for which ECUInstance.
        """
        return self.associatedConsumedProvidedServiceInstanceGroupRefs

    def addAssociatedPdurIPduGroupRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        With this reference it is possible to identify which PduR IPdu Groups are applicable for which CommunicationConnector/ ECU.

        A None value is a no-op and does not add to associatedPdurIPduGroupRefs.
        """
        if value is not None:
            self.associatedPdurIPduGroupRefs.append(value)
        return self

    def getAssociatedPdurIPduGroupRefs(self) -> List[RefType]:
        """
        With this reference it is possible to identify which PduR IPdu Groups are applicable for which CommunicationConnector/ ECU.
        """
        return self.associatedPdurIPduGroupRefs

    def getChannelSynchronousWakeup(self) -> Optional[Boolean]:
        """
        If this parameter is available and set to true, then all available channels will be woken up as soon as at least one channel wakeup occurs. If PNCs are configured, then all PNCs will be requested upon a channel wakeup.
        """
        return self.channelSynchronousWakeup

    def setChannelSynchronousWakeup(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        If this parameter is available and set to true, then all available channels will be woken up as soon as at least one channel wakeup occurs. If PNCs are configured, then all PNCs will be requested upon a channel wakeup.

        A None value is a no-op and does not overwrite an existing channelSynchronousWakeup.
        """
        if value is not None:
            self.channelSynchronousWakeup = value
        return self

    def getClientIdRange(self) -> Optional["ClientIdRange"]:
        """
        Restriction of the Client Identifier for this Ecu to an allowed range of numerical values. The Client Identifier of the transaction handle is generated by the client RTE for inter-Ecu Client/Server communication.
        """
        return self.clientIdRange

    def setClientIdRange(self, value: Optional["ClientIdRange"]) -> "EcuInstance":
        """
        Restriction of the Client Identifier for this Ecu to an allowed range of numerical values. The Client Identifier of the transaction handle is generated by the client RTE for inter-Ecu Client/Server communication.

        A None value is a no-op and does not overwrite an existing clientIdRange.
        """
        if value is not None:
            self.clientIdRange = value
        return self

    def getComConfigurationGwTimeBase(self) -> Optional[TimeValue]:
        """
        The period between successive calls to Com_MainFunctionRouteSignals of the AUTOSAR COM module in seconds.
        """
        return self.comConfigurationGwTimeBase

    def setComConfigurationGwTimeBase(self, value: Optional[TimeValue]) -> "EcuInstance":
        """
        The period between successive calls to Com_MainFunctionRouteSignals of the AUTOSAR COM module in seconds.

        A None value is a no-op and does not overwrite an existing comConfigurationGwTimeBase.
        """
        if value is not None:
            self.comConfigurationGwTimeBase = value
        return self

    def getComConfigurationRxTimeBase(self) -> Optional[TimeValue]:
        """
        The period between successive calls to Com_MainFunctionRx of the AUTOSAR COM module in seconds.
        """
        return self.comConfigurationRxTimeBase

    def setComConfigurationRxTimeBase(self, value: Optional[TimeValue]) -> "EcuInstance":
        """
        The period between successive calls to Com_MainFunctionRx of the AUTOSAR COM module in seconds.

        A None value is a no-op and does not overwrite an existing comConfigurationRxTimeBase.
        """
        if value is not None:
            self.comConfigurationRxTimeBase = value
        return self

    def getComConfigurationTxTimeBase(self) -> Optional[TimeValue]:
        """
        The period between successive calls to Com_MainFunctionTx of the AUTOSAR COM module in seconds.
        """
        return self.comConfigurationTxTimeBase

    def setComConfigurationTxTimeBase(self, value: Optional[TimeValue]) -> "EcuInstance":
        """
        The period between successive calls to Com_MainFunctionTx of the AUTOSAR COM module in seconds.

        A None value is a no-op and does not overwrite an existing comConfigurationTxTimeBase.
        """
        if value is not None:
            self.comConfigurationTxTimeBase = value
        return self

    def getComEnableMDTForCyclicTransmission(self) -> Optional[Boolean]:
        """
        Enables for the Com module of this EcuInstance the minimum delay time monitoring for cyclic and repeated transmissions (TransmissionModeTiming has cyclicTiming assigned or eventControlledTiming with numberOfRepetitions > 0).
        """
        return self.comEnableMDTForCyclicTransmission

    def setComEnableMDTForCyclicTransmission(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        Enables for the Com module of this EcuInstance the minimum delay time monitoring for cyclic and repeated transmissions (TransmissionModeTiming has cyclicTiming assigned or eventControlledTiming with numberOfRepetitions > 0).

        A None value is a no-op and does not overwrite an existing comEnableMDTForCyclicTransmission.
        """
        if value is not None:
            self.comEnableMDTForCyclicTransmission = value
        return self

    def createCanCommunicationController(self, short_name: str) -> CanCommunicationController:
        """
        CommunicationControllers of the ECU.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationController

        if not self.IsElementExists(short_name, CanCommunicationController):
            controller = CanCommunicationController(self, short_name)
            self.addElement(controller)
            self.commControllers.append(controller)
        return self.getElement(short_name, CanCommunicationController)

    def createEthernetCommunicationController(self, short_name: str) -> EthernetCommunicationController:
        """
        CommunicationControllers of the ECU.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationController

        if not self.IsElementExists(short_name, EthernetCommunicationController):
            controller = EthernetCommunicationController(self, short_name)
            self.addElement(controller)
            self.commControllers.append(controller)
        return self.getElement(short_name, EthernetCommunicationController)

    def createFlexrayCommunicationController(self, short_name: str) -> FlexrayCommunicationController:
        """
        CommunicationControllers of the ECU.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationController

        if not self.IsElementExists(short_name, FlexrayCommunicationController):
            controller = FlexrayCommunicationController(self, short_name)
            self.addElement(controller)
            self.commControllers.append(controller)
        return self.getElement(short_name, FlexrayCommunicationController)

    def createLinMaster(self, short_name: str) -> LinMaster:
        """
        CommunicationControllers of the ECU.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinMaster

        if not self.IsElementExists(short_name, LinMaster):
            controller = LinMaster(self, short_name)
            self.addElement(controller)
            self.commControllers.append(controller)
        return self.getElement(short_name, LinMaster)

    def getCommControllers(self) -> List[CommunicationController]:
        """
        CommunicationControllers of the ECU.
        """
        return self.commControllers

    def createCanCommunicationConnector(self, short_name: str) -> CanCommunicationConnector:
        """
        All channels controlled by a single controller.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector

        if not self.IsElementExists(short_name, CanCommunicationConnector):
            connector = CanCommunicationConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, CanCommunicationConnector)

    def createEthernetCommunicationConnector(self, short_name: str) -> EthernetCommunicationConnector:
        """
        All channels controlled by a single controller.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector

        if not self.IsElementExists(short_name, EthernetCommunicationConnector):
            connector = EthernetCommunicationConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, EthernetCommunicationConnector)

    def createFlexrayCommunicationConnector(self, short_name: str) -> FlexrayCommunicationConnector:
        """
        All channels controlled by a single controller.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector

        if not self.IsElementExists(short_name, FlexrayCommunicationConnector):
            connector = FlexrayCommunicationConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, FlexrayCommunicationConnector)

    def createLinCommunicationConnector(self, short_name: str) -> LinCommunicationConnector:
        """
        All channels controlled by a single controller.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector

        if not self.IsElementExists(short_name, LinCommunicationConnector):
            connector = LinCommunicationConnector(self, short_name)
            self.addElement(connector)
            self.connectors.append(connector)
        return self.getElement(short_name, LinCommunicationConnector)

    def getConnectors(self) -> List[CommunicationConnector]:
        """
        All channels controlled by a single controller.
        """
        return self.connectors

    def getDltConfig(self) -> Optional["DltConfig"]:
        """
        Describes the Dlt configuration on this EcuInstance.
        """
        return self.dltConfig

    def setDltConfig(self, value: Optional["DltConfig"]) -> "EcuInstance":
        """
        Describes the Dlt configuration on this EcuInstance.

        A None value is a no-op and does not overwrite an existing dltConfig.
        """
        if value is not None:
            self.dltConfig = value
        return self

    def getDoIpConfig(self) -> Optional["DoIpConfig"]:
        """
        DoIp configuration on this EcuInstance.
        """
        return self.doIpConfig

    def setDoIpConfig(self, value: Optional["DoIpConfig"]) -> "EcuInstance":
        """
        DoIp configuration on this EcuInstance.

        A None value is a no-op and does not overwrite an existing doIpConfig.
        """
        if value is not None:
            self.doIpConfig = value
        return self

    def addEcuTaskProxyRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        Reference to OsTaskProxies assigned to the EcuInstance.

        A None value is a no-op and does not add to ecuTaskProxyRefs.
        """
        if value is not None:
            self.ecuTaskProxyRefs.append(value)
        return self

    def getEcuTaskProxyRefs(self) -> List[RefType]:
        """
        Reference to OsTaskProxies assigned to the EcuInstance.
        """
        return self.ecuTaskProxyRefs

    def getEthSwitchPortGroupDerivation(self) -> Optional[Boolean]:
        """
        Defines whether the derivation of SwitchPortGroups based on VLAN and/or CouplingPort.pncMapping shall be performed for this EcuInstance. If not defined the derivation shall not be done.
        """
        return self.ethSwitchPortGroupDerivation

    def setEthSwitchPortGroupDerivation(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        Defines whether the derivation of SwitchPortGroups based on VLAN and/or CouplingPort.pncMapping shall be performed for this EcuInstance. If not defined the derivation shall not be done.

        A None value is a no-op and does not overwrite an existing ethSwitchPortGroupDerivation.
        """
        if value is not None:
            self.ethSwitchPortGroupDerivation = value
        return self

    def addFirewallRuleRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        Firewall rules defined in the context of an EcuInstance.

        A None value is a no-op and does not add to firewallRuleRefs.
        """
        if value is not None:
            self.firewallRuleRefs.append(value)
        return self

    def getFirewallRuleRefs(self) -> List[RefType]:
        """
        Firewall rules defined in the context of an EcuInstance.
        """
        return self.firewallRuleRefs

    def createEcuPartition(self, short_name: str) -> "EcuPartition":
        """
        Optional definition of Partitions within an Ecu.
        """
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuPartition

        if not self.IsElementExists(short_name, EcuPartition):
            partition = EcuPartition(self, short_name)
            self.addElement(partition)
            self.partitions.append(partition)
        return self.getElement(short_name, EcuPartition)

    def addPartition(self, value: Optional["EcuPartition"]) -> "EcuInstance":
        """
        Optional definition of Partitions within an Ecu.

        A None value is a no-op and does not add to partitions.
        """
        if value is not None:
            self.partitions.append(value)
        return self

    def getPartitions(self) -> List["EcuPartition"]:
        """
        Optional definition of Partitions within an Ecu.
        """
        return self.partitions

    def getPncNmRequest(self) -> Optional[Boolean]:
        """
        Defines if this EcuInstance shall request Nm on all its PhysicalChannels which have Nm variant set to FULL each time a PNC is requested.
        """
        return self.pncNmRequest

    def setPncNmRequest(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        Defines if this EcuInstance shall request Nm on all its PhysicalChannels which have Nm variant set to FULL each time a PNC is requested.

        A None value is a no-op and does not overwrite an existing pncNmRequest.
        """
        if value is not None:
            self.pncNmRequest = value
        return self

    def getPncPrepareSleepTimer(self) -> Optional[TimeValue]:
        """
        Time in seconds the PNC state machine shall wait in PNC_PREPARE_SLEEP.
        """
        return self.pncPrepareSleepTimer

    def setPncPrepareSleepTimer(self, value: Optional[TimeValue]) -> "EcuInstance":
        """
        Time in seconds the PNC state machine shall wait in PNC_PREPARE_SLEEP.

        A None value is a no-op and does not overwrite an existing pncPrepareSleepTimer.
        """
        if value is not None:
            self.pncPrepareSleepTimer = value
        return self

    def getPncSynchronousWakeup(self) -> Optional[Boolean]:
        """
        If this parameter is available and set to true then all available PNCs will be woken up as soon as a channel wakeup occurs. This is ensured by adding all PNCs to all channel wakeup sources during upstream mapping.
        """
        return self.pncSynchronousWakeup

    def setPncSynchronousWakeup(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        If this parameter is available and set to true then all available PNCs will be woken up as soon as a channel wakeup occurs. This is ensured by adding all PNCs to all channel wakeup sources during upstream mapping.

        A None value is a no-op and does not overwrite an existing pncSynchronousWakeup.
        """
        if value is not None:
            self.pncSynchronousWakeup = value
        return self

    def getPnResetTime(self) -> Optional[TimeValue]:
        """
        Specifies the runtime of the reset timer in seconds. This reset time is valid for the reset of PN requests in the EIRA and in the ERA.
        """
        return self.pnResetTime

    def setPnResetTime(self, value: Optional[TimeValue]) -> "EcuInstance":
        """
        Specifies the runtime of the reset timer in seconds. This reset time is valid for the reset of PN requests in the EIRA and in the ERA.

        A None value is a no-op and does not overwrite an existing pnResetTime.
        """
        if value is not None:
            self.pnResetTime = value
        return self

    def getSleepModeSupported(self) -> Optional[Boolean]:
        """
        Specifies whether the ECU instance may be put to a "low power mode" • true: sleep mode is supported • false: sleep mode is not supported Note: This flag may only be set to "true" if the feature is supported by both hardware and basic software.
        """
        return self.sleepModeSupported

    def setSleepModeSupported(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        Specifies whether the ECU instance may be put to a "low power mode" • true: sleep mode is supported • false: sleep mode is not supported Note: This flag may only be set to "true" if the feature is supported by both hardware and basic software.

        A None value is a no-op and does not overwrite an existing sleepModeSupported.
        """
        if value is not None:
            self.sleepModeSupported = value
        return self

    def getTcpIpIcmpPropsRef(self) -> Optional[RefType]:
        """
        EcuInstance specific ICMP (Internet Control Message Protocol) attributes
        """
        return self.tcpIpIcmpPropsRef

    def setTcpIpIcmpPropsRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        EcuInstance specific ICMP (Internet Control Message Protocol) attributes

        A None value is a no-op and does not overwrite an existing tcpIpIcmpPropsRef.
        """
        if value is not None:
            self.tcpIpIcmpPropsRef = value
        return self

    def getTcpIpPropsRef(self) -> Optional[RefType]:
        """
        EcuInstance specific TcpIp Stack attributes.
        """
        return self.tcpIpPropsRef

    def setTcpIpPropsRef(self, value: Optional[RefType]) -> "EcuInstance":
        """
        EcuInstance specific TcpIp Stack attributes.

        A None value is a no-op and does not overwrite an existing tcpIpPropsRef.
        """
        if value is not None:
            self.tcpIpPropsRef = value
        return self

    def getV2xSupported(self) -> Optional["V2xSupportEnum"]:
        """
        This attribute is used to control the existence of the V2X stack on the given EcuInstance.
        """
        return self.v2xSupported

    def setV2xSupported(self, value: Optional["V2xSupportEnum"]) -> "EcuInstance":
        """
        This attribute is used to control the existence of the V2X stack on the given EcuInstance.

        A None value is a no-op and does not overwrite an existing v2xSupported.
        """
        if value is not None:
            self.v2xSupported = value
        return self

    def getWakeUpOverBusSupported(self) -> Optional[Boolean]:
        """
        Driver support for wakeup over Bus.
        """
        return self.wakeUpOverBusSupported

    def setWakeUpOverBusSupported(self, value: Optional[Boolean]) -> "EcuInstance":
        """
        Driver support for wakeup over Bus.

        A None value is a no-op and does not overwrite an existing wakeUpOverBusSupported.
        """
        if value is not None:
            self.wakeUpOverBusSupported = value
        return self
