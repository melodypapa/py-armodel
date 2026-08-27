"""
This module contains the Communication (COM) level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventCom).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
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
