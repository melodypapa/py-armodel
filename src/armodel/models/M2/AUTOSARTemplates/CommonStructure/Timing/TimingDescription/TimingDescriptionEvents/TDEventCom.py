"""
This module contains the Communication (COM) level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventCom).
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Integer,
    RefType,
)


class TDEventISignalTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventISignal.
    """

    # TDEventISignalTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.31, p.66
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventISignal.tdEventType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time, where the COM module makes the contained signal / signal group available for the RTE and the corresponding Rx Indication callout is generated (if configured). Tags: atp.EnumerationLiteralIndex=0
    ISIGNAL_AVAILABLE_FOR_RTE = "iSignalAvailableForRte"

    # A point in time, where a transmission request call is issued by the RTE on a named COM signal / signal group and the new value is stored to the carrier COM I-PDU buffer. Tags: atp.EnumerationLiteralIndex=1
    ISIGNAL_SENT_TO_COM = "iSignalSentToCom"

    def __init__(self):
        """
        Initializes the TDEventISignalTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE,
                TDEventISignalTypeEnum.ISIGNAL_SENT_TO_COM,
            )
        )


class TDEventIPduTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventIPdu.
    """

    # TDEventIPduTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.33, p.67
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventIPdu.tdEventType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the received frame is processed by the corresponding (FlexRay / CAN / LIN) Interface BSW module, routed through the PDUR and the contained PDUs are pushed to the COM module. Tags: atp.EnumerationLiteralIndex=0
    IPDU_RECEIVED_BY_COM = "iPduReceivedByCom"

    # A point in time where the carrier COM I-PDU is routed through the PDUR and is pushed to the bus specific (FlexRay / CAN / LIN) Interface BSW module. Tags: atp.EnumerationLiteralIndex=1
    IPDU_SENT_TO_IF = "iPduSentToIf"

    def __init__(self):
        """
        Initializes the TDEventIPduTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM,
                TDEventIPduTypeEnum.IPDU_SENT_TO_IF,
            )
        )


class TDEventFrameTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventFrame.
    """

    # TDEventFrameTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.35, p.68
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventFrame.tdEventType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the frame containing the named signal / I-PDU is queued for transmission within the related Communication Driver. Tags: atp.EnumerationLiteralIndex=0
    FRAME_QUEUED_FOR_TRANSMISSION = "frameQueuedForTransmission"

    # A point in time where the frame is pushed from the subscriber's communication controller to the corresponding (FlexRay / CAN / LIN) Interface BSW module. Tags: atp.EnumerationLiteralIndex=1
    FRAME_RECEIVED_BY_IF = "frameReceivedByIf"

    # A point in time where the transmission of the frame completes successfully, and the subscriber's communication controller receives the frame from the bus. Tags: atp.EnumerationLiteralIndex=2
    FRAME_TRANSMITTED_ON_BUS = "frameTransmittedOnBus"

    def __init__(self):
        """
        Initializes the TDEventFrameTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventFrameTypeEnum.FRAME_QUEUED_FOR_TRANSMISSION,
                TDEventFrameTypeEnum.FRAME_RECEIVED_BY_IF,
                TDEventFrameTypeEnum.FRAME_TRANSMITTED_ON_BUS,
            )
        )


class TDEventFrameEthernetTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventFrameEthernet.
    """

    # TDEventFrameEthernetTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.37, p.70
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventFrameEthernet.tdEventType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the Ethernet frame containing the specified PDUs is queued for transmission within the corresponding Ethernet Communication Driver. Tags: atp.EnumerationLiteralIndex=0
    FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION = "frameEthernetQueuedForTransmission"

    # A point in time where the frame is pushed from the corresponding Ethernet communication controller to the BSW Ethernet communication interface. Tags: atp.EnumerationLiteralIndex=1
    FRAME_ETHERNET_RECEIVED_BY_IF = "frameEthernetReceivedByIf"

    # A point in time where the receipt of the Ethernet frame/packet completes successfully on the recipient's Ethernet communication controller. In other words, the Ethernet frame/packet has entered the recipient's Ethernet communication controller which means the last bit of the Ethernet frame/ packet has been received. Tags: atp.EnumerationLiteralIndex=2
    FRAME_ETHERNET_RECEIVED_ON_BUS = "frameEthernetReceivedOnBus"

    # A point in time where the transmission of the Ethernet frame/packet completes successfully on the physical Ethernet communication network. In other words, the Ethernet frame/packet has left the sender's Ethernet communication controller, which means that the last bit of the Ethernet frame/ packet has been sent. Tags: atp.EnumerationLiteralIndex=3
    FRAME_ETHERNET_SENT_ON_BUS = "frameEthernetSentOnBus"

    def __init__(self):
        """
        Initializes the TDEventFrameEthernetTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION,
                TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_BY_IF,
                TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_RECEIVED_ON_BUS,
                TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_SENT_ON_BUS,
            )
        )


class TDEventCom(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events related to communication including the physical layer.
    """

    # TDEventCom method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.29, p.65
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcuInstanceRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEcuInstanceRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventCom:
            raise TypeError("TDEventCom is an abstract class.")

        super().__init__(parent, short_name)

        # The ECU context for a particular timing event. The link is optional, because the EcuInstance can not be defined for events of type TDEventCycleStart.
        self.ecuInstanceRef: Optional[RefType] = None

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """The ECU context for a particular timing event. The link is optional, because the EcuInstance can not be defined for events of type TDEventCycleStart."""
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> "TDEventCom":
        """The ECU context for a particular timing event. The link is optional, because the EcuInstance can not be defined for events of type TDEventCycleStart. A None value is a no-op and does not overwrite an existing ecuInstanceRef."""
        if value is not None:
            self.ecuInstanceRef = value
        return self


class TDEventCycleStart(TDEventCom, ABC):
    """
    This is the abstract parent class to describe timing events related to a point in time where a communication cycle starts. Via the attribute "cycleRepetition", a filtered view to the cycle start can be defined.
    """

    # TDEventCycleStart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.39, p.71
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCycleRepetition    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setCycleRepetition    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventCycleStart:
            raise TypeError("TDEventCycleStart is an abstract class.")

        super().__init__(parent, short_name)

        # The start of every <cycleRepetition> cycle is targeted by this event.
        self.cycleRepetition: Optional[Integer] = None

    def getCycleRepetition(self) -> Optional[Integer]:
        """The start of every <cycleRepetition> cycle is targeted by this event."""
        return self.cycleRepetition

    def setCycleRepetition(self, value: Optional[Integer]) -> "TDEventCycleStart":
        """The start of every <cycleRepetition> cycle is targeted by this event. A None value is a no-op and does not overwrite an existing cycleRepetition."""
        if value is not None:
            self.cycleRepetition = value
        return self


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """
    This is used to describe the timing event related to a point in time where a communication cycle starts on a FlexRay cluster.
    """

    # TDEventFrClusterCycleStart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.40, p.71
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFrClusterRef  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setFrClusterRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.frClusterRef: Optional[RefType] = None

    def getFrClusterRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.frClusterRef

    def setFrClusterRef(self, value: Optional[RefType]) -> "TDEventFrClusterCycleStart":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing frClusterRef."""
        if value is not None:
            self.frClusterRef = value
        return self


class TDEventISignal(TDEventCom):
    """
    This is used to describe timing events related to the exchange of I-Signals between COM and RTE.
    """

    # TDEventISignal method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.30, p.65
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getISignalRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setISignalRef           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPhysicalChannelRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPhysicalChannelRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventType          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventType          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.iSignalRef: Optional[RefType] = None

        # The PhysicalChannel on which the ISignal is transmitted.
        self.physicalChannelRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventType: Optional[TDEventISignalTypeEnum] = None

    def getISignalRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.iSignalRef

    def setISignalRef(self, value: Optional[RefType]) -> "TDEventISignal":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing iSignalRef."""
        if value is not None:
            self.iSignalRef = value
        return self

    def getPhysicalChannelRef(self) -> Optional[RefType]:
        """The PhysicalChannel on which the ISignal is transmitted."""
        return self.physicalChannelRef

    def setPhysicalChannelRef(self, value: Optional[RefType]) -> "TDEventISignal":
        """The PhysicalChannel on which the ISignal is transmitted. A None value is a no-op and does not overwrite an existing physicalChannelRef."""
        if value is not None:
            self.physicalChannelRef = value
        return self

    def getTdEventType(self) -> Optional[TDEventISignalTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventType

    def setTdEventType(self, value: Optional[TDEventISignalTypeEnum]) -> "TDEventISignal":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventType."""
        if value is not None:
            self.tdEventType = value
        return self


class TDEventIPdu(TDEventCom):
    """
    This is used to describe timing events related to the exchange of I-PDUs between the bus specific (FlexRay / CAN / LIN) Interface BSW module and COM.
    """

    # TDEventIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.32, p.66
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIPduRef              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setIPduRef              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPhysicalChannelRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPhysicalChannelRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventType          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventType          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.iPduRef: Optional[RefType] = None

        # The PhysicalChannel on which the IPdu is transmitted.
        self.physicalChannelRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventType: Optional[TDEventIPduTypeEnum] = None

    def getIPduRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.iPduRef

    def setIPduRef(self, value: Optional[RefType]) -> "TDEventIPdu":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing iPduRef."""
        if value is not None:
            self.iPduRef = value
        return self

    def getPhysicalChannelRef(self) -> Optional[RefType]:
        """The PhysicalChannel on which the IPdu is transmitted."""
        return self.physicalChannelRef

    def setPhysicalChannelRef(self, value: Optional[RefType]) -> "TDEventIPdu":
        """The PhysicalChannel on which the IPdu is transmitted. A None value is a no-op and does not overwrite an existing physicalChannelRef."""
        if value is not None:
            self.physicalChannelRef = value
        return self

    def getTdEventType(self) -> Optional[TDEventIPduTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventType

    def setTdEventType(self, value: Optional[TDEventIPduTypeEnum]) -> "TDEventIPdu":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventType."""
        if value is not None:
            self.tdEventType = value
        return self


class TDEventFrame(TDEventCom):
    """
    This is used to describe timing events related to the exchange of frames between the communication controller and the bus specific (FlexRay / CAN / LIN) Interface BSW module.
    """

    # TDEventFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.34, p.68
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFrameRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setFrameRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPhysicalChannelRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPhysicalChannelRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventType          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventType          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.frameRef: Optional[RefType] = None

        # The PhysicalChannel on which the Frame is transmitted.
        self.physicalChannelRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventType: Optional[TDEventFrameTypeEnum] = None

    def getFrameRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.frameRef

    def setFrameRef(self, value: Optional[RefType]) -> "TDEventFrame":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing frameRef."""
        if value is not None:
            self.frameRef = value
        return self

    def getPhysicalChannelRef(self) -> Optional[RefType]:
        """The PhysicalChannel on which the Frame is transmitted."""
        return self.physicalChannelRef

    def setPhysicalChannelRef(self, value: Optional[RefType]) -> "TDEventFrame":
        """The PhysicalChannel on which the Frame is transmitted. A None value is a no-op and does not overwrite an existing physicalChannelRef."""
        if value is not None:
            self.physicalChannelRef = value
        return self

    def getTdEventType(self) -> Optional[TDEventFrameTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventType

    def setTdEventType(self, value: Optional[TDEventFrameTypeEnum]) -> "TDEventFrame":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventType."""
        if value is not None:
            self.tdEventType = value
        return self


class TDHeaderIdRange(ARObject):
    """
    Specifies a range of PDU header identifiers. This range is specified by a minimum and maximum header identifier; and the maximum header identifier shall be greater than or equal the minimum header identifier.
    """

    # TDHeaderIdRange method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.38, p.70
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMaxHeaderId       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setMaxHeaderId       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getMinHeaderId       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setMinHeaderId       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self):
        super().__init__()

        # Specifies the maximum PDU header identifier, in other words the upper bound of a range of PDU header identifiers.
        self.maxHeaderId: Optional[Integer] = None

        # Specifies the minimum PDU header identifier, in other words the lower bound of a range of PDU header identifiers.
        self.minHeaderId: Optional[Integer] = None

    def getMaxHeaderId(self) -> Optional[Integer]:
        """Specifies the maximum PDU header identifier, in other words the upper bound of a range of PDU header identifiers."""
        return self.maxHeaderId

    def setMaxHeaderId(self, value: Optional[Integer]) -> "TDHeaderIdRange":
        """Specifies the maximum PDU header identifier, in other words the upper bound of a range of PDU header identifiers. A None value is a no-op and does not overwrite an existing maxHeaderId."""
        if value is not None:
            self.maxHeaderId = value
        return self

    def getMinHeaderId(self) -> Optional[Integer]:
        """Specifies the minimum PDU header identifier, in other words the lower bound of a range of PDU header identifiers."""
        return self.minHeaderId

    def setMinHeaderId(self, value: Optional[Integer]) -> "TDHeaderIdRange":
        """Specifies the minimum PDU header identifier, in other words the lower bound of a range of PDU header identifiers. A None value is a no-op and does not overwrite an existing minHeaderId."""
        if value is not None:
            self.minHeaderId = value
        return self


class TDEventFrameEthernet(TDEventCom):
    """
    This is used to describe timing description events related to the exchange of Ethernet frames between an Ethernet communication controller and the BSW Ethernet interface and driver module.
    """

    # TDEventFrameEthernet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.36, p.69
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getStaticSocketConnectionRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setStaticSocketConnectionRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventType                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventType                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdHeaderIdFilter               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addTDHeaderIdFilter               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdPduTriggeringFilterRefs      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addTdPduTriggeringFilterRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Specifies the SocketConnection by the means of which Physical Data Units (PDU) are transmitted or received within an Ethernet Frame.
        self.staticSocketConnectionRef: Optional[RefType] = None

        # This is used to describe the specific event type of a TDEventFrameEthernet.
        self.tdEventType: Optional[TDEventFrameEthernetTypeEnum] = None

        # Specifies the header identifier or a range of header identifiers that if contained in the Ethernet frame let the TDEventFrameEthernet occur.
        self.tdHeaderIdFilter: List[TDHeaderIdRange] = []

        # Specifies the PDU that if contained in the Ethernet frame let the TDEventFrameEthernet occur.
        self.tdPduTriggeringFilterRefs: List[RefType] = []

    def getStaticSocketConnectionRef(self) -> Optional[RefType]:
        """Specifies the SocketConnection by the means of which Physical Data Units (PDU) are transmitted or received within an Ethernet Frame."""
        return self.staticSocketConnectionRef

    def setStaticSocketConnectionRef(self, value: Optional[RefType]) -> "TDEventFrameEthernet":
        """Specifies the SocketConnection by the means of which Physical Data Units (PDU) are transmitted or received within an Ethernet Frame. A None value is a no-op and does not overwrite an existing staticSocketConnectionRef."""
        if value is not None:
            self.staticSocketConnectionRef = value
        return self

    def getTdEventType(self) -> Optional[TDEventFrameEthernetTypeEnum]:
        """This is used to describe the specific event type of a TDEventFrameEthernet."""
        return self.tdEventType

    def setTdEventType(self, value: Optional[TDEventFrameEthernetTypeEnum]) -> "TDEventFrameEthernet":
        """This is used to describe the specific event type of a TDEventFrameEthernet. A None value is a no-op and does not overwrite an existing tdEventType."""
        if value is not None:
            self.tdEventType = value
        return self

    def getTdHeaderIdFilter(self) -> List[TDHeaderIdRange]:
        """Specifies the header identifier or a range of header identifiers that if contained in the Ethernet frame let the TDEventFrameEthernet occur."""
        return self.tdHeaderIdFilter

    def addTDHeaderIdFilter(self, value: Optional[TDHeaderIdRange]) -> "TDEventFrameEthernet":
        """Specifies the header identifier or a range of header identifiers that if contained in the Ethernet frame let the TDEventFrameEthernet occur. A None value is a no-op and does not append anything."""
        if value is not None:
            self.tdHeaderIdFilter.append(value)
        return self

    def getTdPduTriggeringFilterRefs(self) -> List[RefType]:
        """Specifies the PDU that if contained in the Ethernet frame let the TDEventFrameEthernet occur."""
        return self.tdPduTriggeringFilterRefs

    def addTdPduTriggeringFilterRef(self, value: Optional[RefType]) -> "TDEventFrameEthernet":
        """Specifies the PDU that if contained in the Ethernet frame let the TDEventFrameEthernet occur. A None value is a no-op and does not append anything."""
        if value is not None:
            self.tdPduTriggeringFilterRefs.append(value)
        return self
