from typing import List

from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering


class FlexrayFrame(Frame):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class FlexrayAbsolutelyScheduledTiming(ARObject):
    def __init__(self):
        super().__init__()

        self.communicationCycle = None                              # type: CommunicationCycle
        self.slotID = None                                          # type: PositiveInteger

    def getCommunicationCycle(self):
        return self.communicationCycle

    def setCommunicationCycle(self, value):
        if value is not None:
            self.communicationCycle = value
        return self

    def getSlotID(self):
        return self.slotID

    def setSlotID(self, value):
        if value is not None:
            self.slotID = value
        return self


class FlexrayFrameTriggering(FrameTriggering):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.absolutelyScheduledTimings = []                        # type: List[FlexrayAbsolutelyScheduledTiming]
        self.allowDynamicLSduLength = None                          # type: Boolean
        self.messageId = None                                       # type: PositiveInteger
        self.payloadPreambleIndicator = None                        # type: Boolean

    def getAbsolutelyScheduledTimings(self):
        return self.absolutelyScheduledTimings

    def addAbsolutelyScheduledTiming(self, value):
        if value is not None:
            self.absolutelyScheduledTimings.append(value)
        return self

    def getAllowDynamicLSduLength(self):
        return self.allowDynamicLSduLength

    def setAllowDynamicLSduLength(self, value):
        if value is not None:
            self.allowDynamicLSduLength = value
        return self

    def getMessageId(self):
        return self.messageId

    def setMessageId(self, value):
        if value is not None:
            self.messageId = value
        return self

    def getPayloadPreambleIndicator(self):
        return self.payloadPreambleIndicator

    def setPayloadPreambleIndicator(self, value):
        if value is not None:
            self.payloadPreambleIndicator = value
        return self
