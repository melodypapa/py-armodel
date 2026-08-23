# This module contains AUTOSAR System Template classes for CAN communication
# It defines CAN frames, frame triggering, and related communication elements for CAN networks

from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, Boolean, Integer, PositiveInteger

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import TtcanAbsolutelyScheduledTiming


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


class CanFrameTxBehaviorEnum(AREnum):
    """Defines different CAN protocols for frame transmission behavior."""

    # CanFrameTxBehaviorEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.114, p.445
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods)

    # This CAN frame shall be sent as CAN 2.0 only. Tags: atp.EnumerationLiteralIndex=0
    ENUM_CAN_20 = "CAN-20"

    # This CAN frame shall be sent as CAN FD. Tags: atp.EnumerationLiteralIndex=1
    ENUM_CAN_FD = "CAN-FD"

    def __init__(self):
        super().__init__(
            [
                CanFrameTxBehaviorEnum.ENUM_CAN_20,
                CanFrameTxBehaviorEnum.ENUM_CAN_FD,
            ]
        )


class CanXlFrameTriggeringProps(ARObject):
    """This element indicates the frame being CAN XL and contains further CAN XL specific attributes."""

    # CanXlFrameTriggeringProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.27, p.2007
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAcceptanceField           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setAcceptanceField           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPriorityId                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPriorityId                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSduType                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setSduType                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getVcid                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setVcid                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self):
        super().__init__()

        # Acceptance field of a CAN XL message.
        self.acceptanceField: Optional[PositiveInteger] = None

        # Priority ID of a CAN XL message.
        self.priorityId: Optional[PositiveInteger] = None

        # SDU type of a CAN XL message.
        self.sduType: Optional[PositiveInteger] = None

        # Virtual CAN network ID of a CAN XL message.
        self.vcid: Optional[PositiveInteger] = None

    def getAcceptanceField(self) -> Optional[PositiveInteger]:
        """Acceptance field of a CAN XL message."""
        return self.acceptanceField

    def setAcceptanceField(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringProps":
        """
        Acceptance field of a CAN XL message.
        A None value is a no-op and does not overwrite an existing acceptanceField.
        """
        if value is not None:
            self.acceptanceField = value
        return self

    def getPriorityId(self) -> Optional[PositiveInteger]:
        """Priority ID of a CAN XL message."""
        return self.priorityId

    def setPriorityId(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringProps":
        """
        Priority ID of a CAN XL message.
        A None value is a no-op and does not overwrite an existing priorityId.
        """
        if value is not None:
            self.priorityId = value
        return self

    def getSduType(self) -> Optional[PositiveInteger]:
        """SDU type of a CAN XL message."""
        return self.sduType

    def setSduType(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringProps":
        """
        SDU type of a CAN XL message.
        A None value is a no-op and does not overwrite an existing sduType.
        """
        if value is not None:
            self.sduType = value
        return self

    def getVcid(self) -> Optional[PositiveInteger]:
        """Virtual CAN network ID of a CAN XL message."""
        return self.vcid

    def setVcid(self, value: Optional[PositiveInteger]) -> "CanXlFrameTriggeringProps":
        """
        Virtual CAN network ID of a CAN XL message.
        A None value is a no-op and does not overwrite an existing vcid.
        """
        if value is not None:
            self.vcid = value
        return self


class RxIdentifierRange(ARObject):
    """Optional definition of a CanId range to reduce the effort of specifying every possible FrameTriggering within the defined Id range during reception. All frames received within a range are mapped to the same Pdu that is passed to a upper layer module (e.g. Nm, CDD, PduR)."""

    # RxIdentifierRange method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.112, p.444
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLowerCanId                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerCanId                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperCanId                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperCanId                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute can be used together with the upperCanId attribute to define a range of CanIds.
        self.lowerCanId: Optional[PositiveInteger] = None

        # This attribute can be used together with the lowerCanId attribute to define a range of CanIds.
        self.upperCanId: Optional[PositiveInteger] = None

    def getLowerCanId(self) -> Optional[PositiveInteger]:
        """This attribute can be used together with the upperCanId attribute to define a range of CanIds."""
        return self.lowerCanId

    def setLowerCanId(self, value: Optional[PositiveInteger]) -> "RxIdentifierRange":
        """
        This attribute can be used together with the upperCanId attribute to define a range of CanIds.
        A None value is a no-op and does not overwrite an existing lowerCanId.
        """
        if value is not None:
            self.lowerCanId = value
        return self

    def getUpperCanId(self) -> Optional[PositiveInteger]:
        """This attribute can be used together with the lowerCanId attribute to define a range of CanIds."""
        return self.upperCanId

    def setUpperCanId(self, value: Optional[PositiveInteger]) -> "RxIdentifierRange":
        """
        This attribute can be used together with the lowerCanId attribute to define a range of CanIds.
        A None value is a no-op and does not overwrite an existing upperCanId.
        """
        if value is not None:
            self.upperCanId = value
        return self


class CanFrame(Frame):
    """
    CAN specific Frame element. This element shall also be used for TTCan.
    """

    # CanFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.109, p.442
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # (no own attributes; Base = ARObject, CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class CanFrameTriggering(FrameTriggering):
    """
    CAN specific attributes to the FrameTriggering
    """

    # CanFrameTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.110, p.443
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAbsolutelyScheduledTimings      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addAbsolutelyScheduledTiming       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanAddressingMode               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanAddressingMode               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanFrameRxBehavior              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanFrameRxBehavior              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanFrameTxBehavior              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanFrameTxBehavior              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanXlFrameTriggeringProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanXlFrameTriggeringProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdentifier                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIdentifier                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getJ1939requestable                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setJ1939requestable                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRxIdentifierRange               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRxIdentifierRange               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRxMask                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRxMask                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTxMask                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTxMask                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Each frame in TTCAN is identified by its slot id and communication cycle. A description is provided by the usage of AbsolutelyScheduledTiming.
        self.absolutelyScheduledTimings: "List[TtcanAbsolutelyScheduledTiming]" = []

        # The CAN protocol supports two types of frame formats. The standard frame format uses 11-bit identifiers and is defined in the CAN specification 2.0 A. Additionally the extended frame format allows 29-bit identifiers and is defined in the CAN specification 2.0 B.
        self.canAddressingMode: Optional[ARLiteral] = None

        # Defines which CAN protocol shall be expected for frame reception.
        self.canFrameRxBehavior: Optional[ARLiteral] = None

        # Defines which CAN protocol shall be used for frame transmission.
        self.canFrameTxBehavior: Optional[ARLiteral] = None

        # Definition of CAN XL specific attributes in case the frame is a CAN XL frame.
        self.canXlFrameTriggeringProps: Optional[CanXlFrameTriggeringProps] = None

        # This attribute is used to define the identifier this frame shall use on the CAN network.
        self.identifier: Optional[Integer] = None

        # Frame can be triggered by the J1939 request message.
        self.j1939requestable: Optional[Boolean] = None

        # Optional definition of a CanId range.
        self.rxIdentifierRange: Optional[RxIdentifierRange] = None

        # Identifier mask which denotes the relevant bits in the CAN Identifier. Together with the identifier, this parameter defines a CAN identifier range.
        self.rxMask: Optional[PositiveInteger] = None

        # Identifier mask which denotes static bits in the CAN identifier. The other bits can be set dynamically.
        self.txMask: Optional[PositiveInteger] = None

    def getAbsolutelyScheduledTimings(self) -> "List[TtcanAbsolutelyScheduledTiming]":
        """Each frame in TTCAN is identified by its slot id and communication cycle. A description is provided by the usage of AbsolutelyScheduledTiming."""
        return self.absolutelyScheduledTimings

    def addAbsolutelyScheduledTiming(self, value: "Optional[TtcanAbsolutelyScheduledTiming]") -> "CanFrameTriggering":
        """
        Each frame in TTCAN is identified by its slot id and communication cycle. A description is provided by the usage of AbsolutelyScheduledTiming.
        A None value is a no-op and is not appended to absolutelyScheduledTimings.
        """
        if value is not None:
            self.absolutelyScheduledTimings.append(value)
        return self

    def getCanAddressingMode(self) -> Optional[ARLiteral]:
        """The CAN protocol supports two types of frame formats. The standard frame format uses 11-bit identifiers and is defined in the CAN specification 2.0 A. Additionally the extended frame format allows 29-bit identifiers and is defined in the CAN specification 2.0 B."""
        return self.canAddressingMode

    def setCanAddressingMode(self, value: Optional[ARLiteral]) -> "CanFrameTriggering":
        """
        The CAN protocol supports two types of frame formats. The standard frame format uses 11-bit identifiers and is defined in the CAN specification 2.0 A. Additionally the extended frame format allows 29-bit identifiers and is defined in the CAN specification 2.0 B.
        A None value is a no-op and does not overwrite an existing canAddressingMode.
        """
        if value is not None:
            self.canAddressingMode = value
        return self

    def getCanFrameRxBehavior(self) -> Optional[ARLiteral]:
        """Defines which CAN protocol shall be expected for frame reception."""
        return self.canFrameRxBehavior

    def setCanFrameRxBehavior(self, value: Optional[ARLiteral]) -> "CanFrameTriggering":
        """
        Defines which CAN protocol shall be expected for frame reception.
        A None value is a no-op and does not overwrite an existing canFrameRxBehavior.
        """
        if value is not None:
            self.canFrameRxBehavior = value
        return self

    def getCanFrameTxBehavior(self) -> Optional[ARLiteral]:
        """Defines which CAN protocol shall be used for frame transmission."""
        return self.canFrameTxBehavior

    def setCanFrameTxBehavior(self, value: Optional[ARLiteral]) -> "CanFrameTriggering":
        """
        Defines which CAN protocol shall be used for frame transmission.
        A None value is a no-op and does not overwrite an existing canFrameTxBehavior.
        """
        if value is not None:
            self.canFrameTxBehavior = value
        return self

    def getCanXlFrameTriggeringProps(self) -> Optional[CanXlFrameTriggeringProps]:
        """Definition of CAN XL specific attributes in case the frame is a CAN XL frame."""
        return self.canXlFrameTriggeringProps

    def setCanXlFrameTriggeringProps(self, value: Optional[CanXlFrameTriggeringProps]) -> "CanFrameTriggering":
        """
        Definition of CAN XL specific attributes in case the frame is a CAN XL frame.
        A None value is a no-op and does not overwrite an existing canXlFrameTriggeringProps.
        """
        if value is not None:
            self.canXlFrameTriggeringProps = value
        return self

    def getIdentifier(self) -> Optional[Integer]:
        """This attribute is used to define the identifier this frame shall use on the CAN network."""
        return self.identifier

    def setIdentifier(self, value: Optional[Integer]) -> "CanFrameTriggering":
        """
        This attribute is used to define the identifier this frame shall use on the CAN network.
        A None value is a no-op and does not overwrite an existing identifier.
        """
        if value is not None:
            self.identifier = value
        return self

    def getJ1939requestable(self) -> Optional[Boolean]:
        """Frame can be triggered by the J1939 request message."""
        return self.j1939requestable

    def setJ1939requestable(self, value: Optional[Boolean]) -> "CanFrameTriggering":
        """
        Frame can be triggered by the J1939 request message.
        A None value is a no-op and does not overwrite an existing j1939requestable.
        """
        if value is not None:
            self.j1939requestable = value
        return self

    def getRxIdentifierRange(self) -> Optional[RxIdentifierRange]:
        """Optional definition of a CanId range."""
        return self.rxIdentifierRange

    def setRxIdentifierRange(self, value: Optional[RxIdentifierRange]) -> "CanFrameTriggering":
        """
        Optional definition of a CanId range.
        A None value is a no-op and does not overwrite an existing rxIdentifierRange.
        """
        if value is not None:
            self.rxIdentifierRange = value
        return self

    def getRxMask(self) -> Optional[PositiveInteger]:
        """Identifier mask which denotes the relevant bits in the CAN Identifier. Together with the identifier, this parameter defines a CAN identifier range."""
        return self.rxMask

    def setRxMask(self, value: Optional[PositiveInteger]) -> "CanFrameTriggering":
        """
        Identifier mask which denotes the relevant bits in the CAN Identifier. Together with the identifier, this parameter defines a CAN identifier range.
        A None value is a no-op and does not overwrite an existing rxMask.
        """
        if value is not None:
            self.rxMask = value
        return self

    def getTxMask(self) -> Optional[PositiveInteger]:
        """Identifier mask which denotes static bits in the CAN identifier. The other bits can be set dynamically."""
        return self.txMask

    def setTxMask(self, value: Optional[PositiveInteger]) -> "CanFrameTriggering":
        """
        Identifier mask which denotes static bits in the CAN identifier. The other bits can be set dynamically.
        A None value is a no-op and does not overwrite an existing txMask.
        """
        if value is not None:
            self.txMask = value
        return self
