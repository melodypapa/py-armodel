# This module contains AUTOSAR System Template classes for CAN communication
# It defines CAN frames, frame triggering, and related communication elements for CAN networks

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARPositiveInteger


class CanAddressingModeType(AREnum):
    """Indicates whether standard or extended CAN identifiers are used"""

    # CanAddressingModeType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.111, p.443
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods)

    # Extended 29-bit-identifiers are used (CAN 2.0B) Tags: atp.EnumerationLiteralIndex=0
    ENUM_EXTENDED = "EXTENDED"

    # Standard 11-bit-identifiers are used (CAN 2.0A) Tags: atp.EnumerationLiteralIndex=1
    ENUM_STANDARD = "STANDARD"

    def __init__(self):
        super().__init__(
            [
                CanAddressingModeType.ENUM_EXTENDED,
                CanAddressingModeType.ENUM_STANDARD,
            ]
        )


class CanFrameRxBehaviorEnum(AREnum):
    """Defines different CAN protocols for frame reception behavior."""

    # CanFrameRxBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.113, p.444
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods)

    # This CAN frame may be received as both, CAN 2.0 and CAN FD. Tags: atp.EnumerationLiteralIndex=0
    ENUM_ANY = "ANY"

    # This CAN frame shall be received as CAN 2.0 only. In case the CAN frame is received as CAN FD it is discarded during reception. Tags: atp.EnumerationLiteralIndex=1
    ENUM_CAN_20 = "CAN-20"

    # This CAN frame shall be received as CAN FD only. In case the CAN frame is received as CAN 2.0 it is discarded during reception. Tags: atp.EnumerationLiteralIndex=2
    ENUM_CAN_FD = "CAN-FD"

    def __init__(self):
        super().__init__(
            [
                CanFrameRxBehaviorEnum.ENUM_ANY,
                CanFrameRxBehaviorEnum.ENUM_CAN_20,
                CanFrameRxBehaviorEnum.ENUM_CAN_FD,
            ]
        )


class RxIdentifierRange(ARObject):
    """
    Defines a range of CAN identifiers used for receive filtering in CAN communication.
    This class specifies the lower and upper bounds of CAN message IDs that should
    be accepted by a CAN controller or communication endpoint.
    """

    # RxIdentifierRange method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getLowerCanId                [x] impl  [ ] docstring  [ ] test
    # [ ] setLowerCanId                [x] impl  [ ] docstring  [ ] test
    # [ ] getUpperCanId                [x] impl  [ ] docstring  [ ] test
    # [ ] setUpperCanId                [x] impl  [ ] docstring  [ ] test

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

    # CanFrame method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class CanFrameTriggering(FrameTriggering):
    """
    Defines the triggering mechanism for CAN frames, specifying how and when
    CAN frames are transmitted or received on the network, including timing,
    addressing modes, and frame behavior properties.
    """

    # CanFrameTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAbsolutelyScheduledTimings [x] impl  [ ] docstring  [ ] test
    # [ ] setAbsolutelyScheduledTimings [x] impl  [ ] docstring  [ ] test
    # [ ] getCanAddressingMode         [x] impl  [ ] docstring  [ ] test
    # [ ] setCanAddressingMode         [x] impl  [ ] docstring  [ ] test
    # [ ] getCanFdFrameSupport         [x] impl  [ ] docstring  [ ] test
    # [ ] setCanFdFrameSupport         [x] impl  [ ] docstring  [ ] test
    # [ ] getCanFrameRxBehavior        [x] impl  [ ] docstring  [ ] test
    # [ ] setCanFrameRxBehavior        [x] impl  [ ] docstring  [ ] test
    # [ ] getCanFrameTxBehavior        [x] impl  [ ] docstring  [ ] test
    # [ ] setCanFrameTxBehavior        [x] impl  [ ] docstring  [ ] test
    # [ ] getCanXlFrameTriggeringProps [x] impl  [ ] docstring  [ ] test
    # [ ] setCanXlFrameTriggeringProps [x] impl  [ ] docstring  [ ] test
    # [ ] getIdentifier                [x] impl  [ ] docstring  [ ] test
    # [ ] setIdentifier                [x] impl  [ ] docstring  [ ] test
    # [ ] getJ1939requestable          [x] impl  [ ] docstring  [ ] test
    # [ ] setJ1939requestable          [x] impl  [ ] docstring  [ ] test
    # [ ] getRxIdentifierRange         [x] impl  [ ] docstring  [ ] test
    # [ ] setRxIdentifierRange         [x] impl  [ ] docstring  [ ] test
    # [ ] getRxMask                    [x] impl  [ ] docstring  [ ] test
    # [ ] setRxMask                    [x] impl  [ ] docstring  [ ] test
    # [ ] getTxMask                    [x] impl  [ ] docstring  [ ] test
    # [ ] setTxMask                    [x] impl  [ ] docstring  [ ] test

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
