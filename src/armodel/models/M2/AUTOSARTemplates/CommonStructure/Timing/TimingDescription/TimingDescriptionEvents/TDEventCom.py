"""
This module contains the Communication (COM) level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventCom).
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
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
