# This module contains AUTOSAR System Template classes for CAN communication
# It defines CAN frames, frame triggering, and related communication elements for CAN networks

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARPositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
    FrameTriggering,
)


class RxIdentifierRange(ARObject):
    """
    Defines a range of CAN identifiers used for receive filtering in CAN communication.
    This class specifies the lower and upper bounds of CAN message IDs that should
    be accepted by a CAN controller or communication endpoint.
    """
    def __init__(self):
        super().__init__()

        self.lowerCanId: ARPositiveInteger = None
        self.upperCanId: ARPositiveInteger = None

    def getLowerCanId(self) -> ARPositiveInteger:
        return self.lowerCanId

    def setLowerCanId(self, value: ARPositiveInteger):
        self.lowerCanId = value
        return self

    def getUpperCanId(self) -> ARPositiveInteger:
        return self.upperCanId

    def setUpperCanId(self, value: ARPositiveInteger):
        self.upperCanId = value
        return self

class CanFrame(Frame):
    """
    Represents a CAN frame in the AUTOSAR system, extending the generic Frame class
    with CAN-specific properties and behavior. This class defines the structure
    and characteristics of CAN messages in the communication system.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class CanFrameTriggering(FrameTriggering):
    """
    Defines the triggering mechanism for CAN frames, specifying how and when
    CAN frames are transmitted or received on the network, including timing,
    addressing modes, and frame behavior properties.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.absolutelyScheduledTimings = []
        self.canAddressingMode = None
        self.canFdFrameSupport = None
        self.canFrameRxBehavior = None
        self.canFrameTxBehavior = None
        self.canXlFrameTriggeringProps = None
        self.identifier = None
        self.j1939requestable = None
        self.rxIdentifierRange: RxIdentifierRange = None
        self.rxMask = None
        self.txMask = None

    def getAbsolutelyScheduledTimings(self):
        return self.absolutelyScheduledTimings

    def setAbsolutelyScheduledTimings(self, value):
        self.absolutelyScheduledTimings = value
        return self

    def getCanAddressingMode(self):
        return self.canAddressingMode

    def setCanAddressingMode(self, value):
        self.canAddressingMode = value
        return self

    def getCanFdFrameSupport(self):
        return self.canFdFrameSupport

    def setCanFdFrameSupport(self, value):
        self.canFdFrameSupport = value
        return self

    def getCanFrameRxBehavior(self):
        return self.canFrameRxBehavior

    def setCanFrameRxBehavior(self, value):
        self.canFrameRxBehavior = value
        return self

    def getCanFrameTxBehavior(self):
        return self.canFrameTxBehavior

    def setCanFrameTxBehavior(self, value):
        self.canFrameTxBehavior = value
        return self

    def getCanXlFrameTriggeringProps(self):
        return self.canXlFrameTriggeringProps

    def setCanXlFrameTriggeringProps(self, value):
        self.canXlFrameTriggeringProps = value
        return self

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, value):
        self.identifier = value
        return self

    def getJ1939requestable(self):
        return self.j1939requestable

    def setJ1939requestable(self, value):
        self.j1939requestable = value
        return self

    def getRxIdentifierRange(self) -> RxIdentifierRange:
        return self.rxIdentifierRange

    def setRxIdentifierRange(self, value: RxIdentifierRange):
        self.rxIdentifierRange = value
        return self

    def getRxMask(self):
        return self.rxMask

    def setRxMask(self, value):
        self.rxMask = value
        return self

    def getTxMask(self):
        return self.txMask

    def setTxMask(self, value):
        self.txMask = value
        return self
