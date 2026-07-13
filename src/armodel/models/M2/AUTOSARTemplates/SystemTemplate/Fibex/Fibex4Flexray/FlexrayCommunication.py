from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering


class FlexrayFrame(Frame):
    """
    Represents a FlexRay frame in the AUTOSAR system, extending the generic
    Frame class with FlexRay-specific properties and behavior. This class
    defines the structure and characteristics of FlexRay messages in the
    communication system.
    """
    # FlexrayFrame method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """
    Defines absolutely scheduled timing properties for FlexRay communication,
    specifying communication cycles and slot IDs for time-triggered
    communication in FlexRay networks.
    """
    # FlexrayAbsolutelyScheduledTiming method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationCycle        [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationCycle        [x] impl  [ ] docstring  [ ] test
    # [ ] getSlotID                    [x] impl  [ ] docstring  [ ] test
    # [ ] setSlotID                    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.communicationCycle = None
        self.slotID: PositiveInteger = None

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
    """
    Defines the triggering mechanism for FlexRay frames, specifying how and when
    FlexRay frames are transmitted or received on the network, including timing,
    message IDs, and payload properties.
    """
    # FlexrayFrameTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAbsolutelyScheduledTimings [x] impl  [ ] docstring  [ ] test
    # [ ] addAbsolutelyScheduledTiming [x] impl  [ ] docstring  [ ] test
    # [ ] getAllowDynamicLSduLength    [x] impl  [ ] docstring  [ ] test
    # [ ] setAllowDynamicLSduLength    [x] impl  [ ] docstring  [ ] test
    # [ ] getMessageId                 [x] impl  [ ] docstring  [ ] test
    # [ ] setMessageId                 [x] impl  [ ] docstring  [ ] test
    # [ ] getPayloadPreambleIndicator  [x] impl  [ ] docstring  [ ] test
    # [ ] setPayloadPreambleIndicator  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.absolutelyScheduledTimings: List[FlexrayAbsolutelyScheduledTiming] = []
        self.allowDynamicLSduLength: Boolean = None
        self.messageId: PositiveInteger = None
        self.payloadPreambleIndicator: Boolean = None

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
