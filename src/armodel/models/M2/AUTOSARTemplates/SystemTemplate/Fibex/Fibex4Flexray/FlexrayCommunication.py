from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCycle


class FlexrayFrame(Frame):
    """
    FlexRay specific Frame element. Tags: atp.recommendedPackage=Frames
    """

    # FlexrayFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.80, p.422
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """
    Each frame in FlexRay is identified by its slot id and communication cycle. A description is provided by the usage of AbsolutelyScheduledTiming. In the static segment a frame can be sent multiple times within one communication cycle. For describing this case multiple AbsolutelyScheduledTimings have to be used. The main use case would be that a frame is sent twice within one communication cycle.

    [constr_9126] Existence of FlexrayAbsolutelyScheduledTiming.slotID: For each FlexrayAbsolutelyScheduledTiming, the attribute slotID shall exist at the time when the System Description is complete.

    [constr_9127] Existence of FlexrayAbsolutelyScheduledTiming.communicationCycle: For each FlexrayAbsolutelyScheduledTiming, the aggregation of CommunicationCycle in the role communicationCycle shall exist at the time when the System Description is complete.
    """

    # FlexrayAbsolutelyScheduledTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.82, p.423
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationCycle  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationCycle  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSlotID              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSlotID              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The communication cycle where the frame is sent.
        self.communicationCycle: Optional[CommunicationCycle] = None

        # In the static part the SlotID defines the slot in which the frame is transmitted. The SlotID also determines, in combination with FlexrayCluster::numberOfStaticSlots, whether the frame is sent in static or dynamic segment. In the dynamic part, the slot id is equivalent to a priority. Lower dynamic slot ids are all sent until the end of the dynamic segment. Higher numbers, which were ignored that time, have to wait one cycle and then shall try again. minValue: 1 maxValue: 2047
        self.slotID: Optional[PositiveInteger] = None

    def getCommunicationCycle(self) -> Optional[CommunicationCycle]:
        """
        The communication cycle where the frame is sent.
        """
        return self.communicationCycle

    def setCommunicationCycle(self, value: Optional[CommunicationCycle]) -> FlexrayAbsolutelyScheduledTiming:
        """
        The communication cycle where the frame is sent.
        A None value is a no-op and does not overwrite an existing communicationCycle.
        """
        if value is not None:
            self.communicationCycle = value
        return self

    def getSlotID(self) -> Optional[PositiveInteger]:
        """
        In the static part the SlotID defines the slot in which the frame is transmitted. The SlotID also determines, in combination with FlexrayCluster::numberOfStaticSlots, whether the frame is sent in static or dynamic segment. In the dynamic part, the slot id is equivalent to a priority. Lower dynamic slot ids are all sent until the end of the dynamic segment. Higher numbers, which were ignored that time, have to wait one cycle and then shall try again. minValue: 1 maxValue: 2047
        """
        return self.slotID

    def setSlotID(self, value: Optional[PositiveInteger]) -> FlexrayAbsolutelyScheduledTiming:
        """
        In the static part the SlotID defines the slot in which the frame is transmitted. The SlotID also determines, in combination with FlexrayCluster::numberOfStaticSlots, whether the frame is sent in static or dynamic segment. In the dynamic part, the slot id is equivalent to a priority. Lower dynamic slot ids are all sent until the end of the dynamic segment. Higher numbers, which were ignored that time, have to wait one cycle and then shall try again. minValue: 1 maxValue: 2047
        A None value is a no-op and does not overwrite an existing slotID.
        """
        if value is not None:
            self.slotID = value
        return self


class FlexrayFrameTriggering(FrameTriggering):
    """
    FlexRay specific attributes to the FrameTriggering

    [constr_9124] Existence of FlexrayFrameTriggering.allowDynamicLSduLength: For each FlexrayFrameTriggering, the attribute allowDynamicLSduLength shall exist at the time when the System Description is complete.

    [constr_9125] Existence of FlexrayFrameTriggering.payloadPreambleIndicator: For each FlexrayFrameTriggering, the attribute payloadPreambleIndicator shall exist at the time when the System Description is complete.
    """

    # FlexrayFrameTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.81, p.423
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAbsolutelyScheduledTiming  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAbsolutelyScheduledTimings [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getAllowDynamicLSduLength     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAllowDynamicLSduLength     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMessageId                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageId                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPayloadPreambleIndicator   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPayloadPreambleIndicator   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specification of a sending behaviour where the exact time for the frames transmission is guaranteed.
        self.absolutelyScheduledTimings: List[FlexrayAbsolutelyScheduledTiming] = []

        # Allows L-PDU length reduction and indicates that the related CC buffer has to be reconfigured for the actual length and Header-CRC before transmission of the L-PDU. If this attribute is set to true than the referenced Frame length attribute defines the max. length.
        self.allowDynamicLSduLength: Optional[Boolean] = None

        # The first two bytes of the payload segment of the FlexRay frame format for frames transmitted in the dynamic segment can be used as receiver filterable data called the message ID.
        self.messageId: Optional[PositiveInteger] = None

        # Switching the Payload Preamble bit.
        self.payloadPreambleIndicator: Optional[Boolean] = None

    def addAbsolutelyScheduledTiming(self, value: Optional[FlexrayAbsolutelyScheduledTiming]) -> FlexrayFrameTriggering:
        """
        Specification of a sending behaviour where the exact time for the frames transmission is guaranteed.
        A None value is a no-op and does not extend the absolutelyScheduledTimings.
        """
        if value is not None:
            self.absolutelyScheduledTimings.append(value)
        return self

    def getAbsolutelyScheduledTimings(self) -> List[FlexrayAbsolutelyScheduledTiming]:
        """
        Specification of a sending behaviour where the exact time for the frames transmission is guaranteed.
        """
        return self.absolutelyScheduledTimings

    def getAllowDynamicLSduLength(self) -> Optional[Boolean]:
        """
        Allows L-PDU length reduction and indicates that the related CC buffer has to be reconfigured for the actual length and Header-CRC before transmission of the L-PDU. If this attribute is set to true than the referenced Frame length attribute defines the max. length.
        """
        return self.allowDynamicLSduLength

    def setAllowDynamicLSduLength(self, value: Optional[Boolean]) -> FlexrayFrameTriggering:
        """
        Allows L-PDU length reduction and indicates that the related CC buffer has to be reconfigured for the actual length and Header-CRC before transmission of the L-PDU. If this attribute is set to true than the referenced Frame length attribute defines the max. length.
        A None value is a no-op and does not overwrite an existing allowDynamicLSduLength.
        """
        if value is not None:
            self.allowDynamicLSduLength = value
        return self

    def getMessageId(self) -> Optional[PositiveInteger]:
        """
        The first two bytes of the payload segment of the FlexRay frame format for frames transmitted in the dynamic segment can be used as receiver filterable data called the message ID.
        """
        return self.messageId

    def setMessageId(self, value: Optional[PositiveInteger]) -> FlexrayFrameTriggering:
        """
        The first two bytes of the payload segment of the FlexRay frame format for frames transmitted in the dynamic segment can be used as receiver filterable data called the message ID.
        A None value is a no-op and does not overwrite an existing messageId.
        """
        if value is not None:
            self.messageId = value
        return self

    def getPayloadPreambleIndicator(self) -> Optional[Boolean]:
        """
        Switching the Payload Preamble bit.
        """
        return self.payloadPreambleIndicator

    def setPayloadPreambleIndicator(self, value: Optional[Boolean]) -> FlexrayFrameTriggering:
        """
        Switching the Payload Preamble bit.
        A None value is a no-op and does not overwrite an existing payloadPreambleIndicator.
        """
        if value is not None:
            self.payloadPreambleIndicator = value
        return self
