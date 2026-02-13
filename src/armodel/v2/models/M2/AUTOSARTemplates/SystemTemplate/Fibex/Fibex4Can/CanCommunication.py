"""
AUTOSAR Package - CanCommunication

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.__init__ import (
    Frame,
    FrameTriggering,
)


class CanFrame(Frame):
    """
    CAN specific Frame element. This element shall also be used for TTCan.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication::CanFrame

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 442, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_absolutely(self, value):
        """
        Set absolutely and return self for chaining.

        Args:
            value: The absolutely to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_absolutely("value")
        """
        self.absolutely = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CanFrameTriggering(FrameTriggering):
    """
    CAN specific attributes to the FrameTriggering

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication::CanFrameTriggering

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 443, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Each frame in TTCAN is identified by its slot id and communication cycle.
        # A description is provided by the of AbsolutelyScheduledTiming.
        self._absolutely: List["TtcanAbsolutely"] = []

    @property
    def absolutely(self) -> List["TtcanAbsolutely"]:
        """Get absolutely (Pythonic accessor)."""
        return self._absolutely
        # The CAN protocol supports two types of frame formats.
        # The standard frame format uses 11-bit identifiers and is the CAN
                # specification 2.
        # 0 A.
        # Additionally the format allows 29-bit identifiers and is the CAN
                # specification 2.
        # 0 B.
        self._canAddressing: Optional[CanAddressingMode] = None

    @property
    def can_addressing(self) -> Optional[CanAddressingMode]:
        """Get canAddressing (Pythonic accessor)."""
        return self._canAddressing

    @can_addressing.setter
    def can_addressing(self, value: Optional[CanAddressingMode]) -> None:
        """
        Set canAddressing with validation.

        Args:
            value: The canAddressing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canAddressing = None
            return

        if not isinstance(value, CanAddressingMode):
            raise TypeError(
                f"canAddressing must be CanAddressingMode or None, got {type(value).__name__}"
            )
        self._canAddressing = value
        self._canFrameRx: Optional[CanFrameRxBehavior] = None

    @property
    def can_frame_rx(self) -> Optional[CanFrameRxBehavior]:
        """Get canFrameRx (Pythonic accessor)."""
        return self._canFrameRx

    @can_frame_rx.setter
    def can_frame_rx(self, value: Optional[CanFrameRxBehavior]) -> None:
        """
        Set canFrameRx with validation.

        Args:
            value: The canFrameRx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canFrameRx = None
            return

        if not isinstance(value, CanFrameRxBehavior):
            raise TypeError(
                f"canFrameRx must be CanFrameRxBehavior or None, got {type(value).__name__}"
            )
        self._canFrameRx = value
        self._canFrameTx: Optional[CanFrameTxBehavior] = None

    @property
    def can_frame_tx(self) -> Optional[CanFrameTxBehavior]:
        """Get canFrameTx (Pythonic accessor)."""
        return self._canFrameTx

    @can_frame_tx.setter
    def can_frame_tx(self, value: Optional[CanFrameTxBehavior]) -> None:
        """
        Set canFrameTx with validation.

        Args:
            value: The canFrameTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canFrameTx = None
            return

        if not isinstance(value, CanFrameTxBehavior):
            raise TypeError(
                f"canFrameTx must be CanFrameTxBehavior or None, got {type(value).__name__}"
            )
        self._canFrameTx = value
        self._canXlFrame: Optional[RefType] = None

    @property
    def can_xl_frame(self) -> Optional[RefType]:
        """Get canXlFrame (Pythonic accessor)."""
        return self._canXlFrame

    @can_xl_frame.setter
    def can_xl_frame(self, value: Optional[RefType]) -> None:
        """
        Set canXlFrame with validation.

        Args:
            value: The canXlFrame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canXlFrame = None
            return

        self._canXlFrame = value
        # network.
        self._identifier: Optional[Integer] = None

    @property
    def identifier(self) -> Optional[Integer]:
        """Get identifier (Pythonic accessor)."""
        return self._identifier

    @identifier.setter
    def identifier(self, value: Optional[Integer]) -> None:
        """
        Set identifier with validation.

        Args:
            value: The identifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identifier = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"identifier must be Integer or int or None, got {type(value).__name__}"
            )
        self._identifier = value
        self._j1939requestable: Optional[Boolean] = None

    @property
    def j1939requestable(self) -> Optional[Boolean]:
        """Get j1939requestable (Pythonic accessor)."""
        return self._j1939requestable

    @j1939requestable.setter
    def j1939requestable(self, value: Optional[Boolean]) -> None:
        """
        Set j1939requestable with validation.

        Args:
            value: The j1939requestable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._j1939requestable = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"j1939requestable must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._j1939requestable = value
        # Optional definition of a CanId range.
        self._rxIdentifierRange: Optional[RxIdentifierRange] = None

    @property
    def rx_identifier_range(self) -> Optional[RxIdentifierRange]:
        """Get rxIdentifierRange (Pythonic accessor)."""
        return self._rxIdentifierRange

    @rx_identifier_range.setter
    def rx_identifier_range(self, value: Optional[RxIdentifierRange]) -> None:
        """
        Set rxIdentifierRange with validation.

        Args:
            value: The rxIdentifierRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxIdentifierRange = None
            return

        if not isinstance(value, RxIdentifierRange):
            raise TypeError(
                f"rxIdentifierRange must be RxIdentifierRange or None, got {type(value).__name__}"
            )
        self._rxIdentifierRange = value
        # identifier, this parameter CAN identifier range.
        self._rxMask: Optional[PositiveInteger] = None

    @property
    def rx_mask(self) -> Optional[PositiveInteger]:
        """Get rxMask (Pythonic accessor)."""
        return self._rxMask

    @rx_mask.setter
    def rx_mask(self, value: Optional[PositiveInteger]) -> None:
        """
        Set rxMask with validation.

        Args:
            value: The rxMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxMask = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"rxMask must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._rxMask = value
        # dynamically.
        self._txMask: Optional[PositiveInteger] = None

    @property
    def tx_mask(self) -> Optional[PositiveInteger]:
        """Get txMask (Pythonic accessor)."""
        return self._txMask

    @tx_mask.setter
    def tx_mask(self, value: Optional[PositiveInteger]) -> None:
        """
        Set txMask with validation.

        Args:
            value: The txMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txMask = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"txMask must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._txMask = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbsolutely(self) -> List["TtcanAbsolutely"]:
        """
        AUTOSAR-compliant getter for absolutely.

        Returns:
            The absolutely value

        Note:
            Delegates to absolutely property (CODING_RULE_V2_00017)
        """
        return self.absolutely  # Delegates to property

    def getCanAddressing(self) -> CanAddressingMode:
        """
        AUTOSAR-compliant getter for canAddressing.

        Returns:
            The canAddressing value

        Note:
            Delegates to can_addressing property (CODING_RULE_V2_00017)
        """
        return self.can_addressing  # Delegates to property

    def setCanAddressing(self, value: CanAddressingMode) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for canAddressing with method chaining.

        Args:
            value: The canAddressing to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_addressing property setter (gets validation automatically)
        """
        self.can_addressing = value  # Delegates to property setter
        return self

    def getCanFrameRx(self) -> CanFrameRxBehavior:
        """
        AUTOSAR-compliant getter for canFrameRx.

        Returns:
            The canFrameRx value

        Note:
            Delegates to can_frame_rx property (CODING_RULE_V2_00017)
        """
        return self.can_frame_rx  # Delegates to property

    def setCanFrameRx(self, value: CanFrameRxBehavior) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for canFrameRx with method chaining.

        Args:
            value: The canFrameRx to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_frame_rx property setter (gets validation automatically)
        """
        self.can_frame_rx = value  # Delegates to property setter
        return self

    def getCanFrameTx(self) -> CanFrameTxBehavior:
        """
        AUTOSAR-compliant getter for canFrameTx.

        Returns:
            The canFrameTx value

        Note:
            Delegates to can_frame_tx property (CODING_RULE_V2_00017)
        """
        return self.can_frame_tx  # Delegates to property

    def setCanFrameTx(self, value: CanFrameTxBehavior) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for canFrameTx with method chaining.

        Args:
            value: The canFrameTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_frame_tx property setter (gets validation automatically)
        """
        self.can_frame_tx = value  # Delegates to property setter
        return self

    def getCanXlFrame(self) -> RefType:
        """
        AUTOSAR-compliant getter for canXlFrame.

        Returns:
            The canXlFrame value

        Note:
            Delegates to can_xl_frame property (CODING_RULE_V2_00017)
        """
        return self.can_xl_frame  # Delegates to property

    def setCanXlFrame(self, value: RefType) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for canXlFrame with method chaining.

        Args:
            value: The canXlFrame to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_xl_frame property setter (gets validation automatically)
        """
        self.can_xl_frame = value  # Delegates to property setter
        return self

    def getIdentifier(self) -> Integer:
        """
        AUTOSAR-compliant getter for identifier.

        Returns:
            The identifier value

        Note:
            Delegates to identifier property (CODING_RULE_V2_00017)
        """
        return self.identifier  # Delegates to property

    def setIdentifier(self, value: Integer) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for identifier with method chaining.

        Args:
            value: The identifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to identifier property setter (gets validation automatically)
        """
        self.identifier = value  # Delegates to property setter
        return self

    def getJ1939requestable(self) -> Boolean:
        """
        AUTOSAR-compliant getter for j1939requestable.

        Returns:
            The j1939requestable value

        Note:
            Delegates to j1939requestable property (CODING_RULE_V2_00017)
        """
        return self.j1939requestable  # Delegates to property

    def setJ1939requestable(self, value: Boolean) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for j1939requestable with method chaining.

        Args:
            value: The j1939requestable to set

        Returns:
            self for method chaining

        Note:
            Delegates to j1939requestable property setter (gets validation automatically)
        """
        self.j1939requestable = value  # Delegates to property setter
        return self

    def getRxIdentifierRange(self) -> RxIdentifierRange:
        """
        AUTOSAR-compliant getter for rxIdentifierRange.

        Returns:
            The rxIdentifierRange value

        Note:
            Delegates to rx_identifier_range property (CODING_RULE_V2_00017)
        """
        return self.rx_identifier_range  # Delegates to property

    def setRxIdentifierRange(self, value: RxIdentifierRange) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for rxIdentifierRange with method chaining.

        Args:
            value: The rxIdentifierRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_identifier_range property setter (gets validation automatically)
        """
        self.rx_identifier_range = value  # Delegates to property setter
        return self

    def getRxMask(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for rxMask.

        Returns:
            The rxMask value

        Note:
            Delegates to rx_mask property (CODING_RULE_V2_00017)
        """
        return self.rx_mask  # Delegates to property

    def setRxMask(self, value: PositiveInteger) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for rxMask with method chaining.

        Args:
            value: The rxMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_mask property setter (gets validation automatically)
        """
        self.rx_mask = value  # Delegates to property setter
        return self

    def getTxMask(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for txMask.

        Returns:
            The txMask value

        Note:
            Delegates to tx_mask property (CODING_RULE_V2_00017)
        """
        return self.tx_mask  # Delegates to property

    def setTxMask(self, value: PositiveInteger) -> CanFrameTriggering:
        """
        AUTOSAR-compliant setter for txMask with method chaining.

        Args:
            value: The txMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_mask property setter (gets validation automatically)
        """
        self.tx_mask = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_addressing(self, value: Optional[CanAddressingMode]) -> CanFrameTriggering:
        """
        Set canAddressing and return self for chaining.

        Args:
            value: The canAddressing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_addressing("value")
        """
        self.can_addressing = value  # Use property setter (gets validation)
        return self

    def with_can_frame_rx(self, value: Optional[CanFrameRxBehavior]) -> CanFrameTriggering:
        """
        Set canFrameRx and return self for chaining.

        Args:
            value: The canFrameRx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_frame_rx("value")
        """
        self.can_frame_rx = value  # Use property setter (gets validation)
        return self

    def with_can_frame_tx(self, value: Optional[CanFrameTxBehavior]) -> CanFrameTriggering:
        """
        Set canFrameTx and return self for chaining.

        Args:
            value: The canFrameTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_frame_tx("value")
        """
        self.can_frame_tx = value  # Use property setter (gets validation)
        return self

    def with_can_xl_frame(self, value: Optional[RefType]) -> CanFrameTriggering:
        """
        Set canXlFrame and return self for chaining.

        Args:
            value: The canXlFrame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_xl_frame("value")
        """
        self.can_xl_frame = value  # Use property setter (gets validation)
        return self

    def with_identifier(self, value: Optional[Integer]) -> CanFrameTriggering:
        """
        Set identifier and return self for chaining.

        Args:
            value: The identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identifier("value")
        """
        self.identifier = value  # Use property setter (gets validation)
        return self

    def with_j1939requestable(self, value: Optional[Boolean]) -> CanFrameTriggering:
        """
        Set j1939requestable and return self for chaining.

        Args:
            value: The j1939requestable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_j1939requestable("value")
        """
        self.j1939requestable = value  # Use property setter (gets validation)
        return self

    def with_rx_identifier_range(self, value: Optional[RxIdentifierRange]) -> CanFrameTriggering:
        """
        Set rxIdentifierRange and return self for chaining.

        Args:
            value: The rxIdentifierRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_identifier_range("value")
        """
        self.rx_identifier_range = value  # Use property setter (gets validation)
        return self

    def with_rx_mask(self, value: Optional[PositiveInteger]) -> CanFrameTriggering:
        """
        Set rxMask and return self for chaining.

        Args:
            value: The rxMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_mask("value")
        """
        self.rx_mask = value  # Use property setter (gets validation)
        return self

    def with_tx_mask(self, value: Optional[PositiveInteger]) -> CanFrameTriggering:
        """
        Set txMask and return self for chaining.

        Args:
            value: The txMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_mask("value")
        """
        self.tx_mask = value  # Use property setter (gets validation)
        return self



class RxIdentifierRange(ARObject):
    """
    Optional definition of a CanId range to reduce the effort of specifying
    every possible FrameTriggering within the defined Id range during reception.
    All frames received within a range are mapped to the same Pdu that is passed
    to a upper layer module (e.g. Nm, CDD, PduR).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication::RxIdentifierRange

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 444, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used together with the upperCanId define a range of
        # CanIds.
        self._lowerCanId: Optional[PositiveInteger] = None

    @property
    def lower_can_id(self) -> Optional[PositiveInteger]:
        """Get lowerCanId (Pythonic accessor)."""
        return self._lowerCanId

    @lower_can_id.setter
    def lower_can_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set lowerCanId with validation.

        Args:
            value: The lowerCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerCanId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"lowerCanId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._lowerCanId = value
        # CanIds.
        self._upperCanId: Optional[PositiveInteger] = None

    @property
    def upper_can_id(self) -> Optional[PositiveInteger]:
        """Get upperCanId (Pythonic accessor)."""
        return self._upperCanId

    @upper_can_id.setter
    def upper_can_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set upperCanId with validation.

        Args:
            value: The upperCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperCanId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"upperCanId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._upperCanId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerCanId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for lowerCanId.

        Returns:
            The lowerCanId value

        Note:
            Delegates to lower_can_id property (CODING_RULE_V2_00017)
        """
        return self.lower_can_id  # Delegates to property

    def setLowerCanId(self, value: PositiveInteger) -> RxIdentifierRange:
        """
        AUTOSAR-compliant setter for lowerCanId with method chaining.

        Args:
            value: The lowerCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_can_id property setter (gets validation automatically)
        """
        self.lower_can_id = value  # Delegates to property setter
        return self

    def getUpperCanId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for upperCanId.

        Returns:
            The upperCanId value

        Note:
            Delegates to upper_can_id property (CODING_RULE_V2_00017)
        """
        return self.upper_can_id  # Delegates to property

    def setUpperCanId(self, value: PositiveInteger) -> RxIdentifierRange:
        """
        AUTOSAR-compliant setter for upperCanId with method chaining.

        Args:
            value: The upperCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_can_id property setter (gets validation automatically)
        """
        self.upper_can_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_can_id(self, value: Optional[PositiveInteger]) -> RxIdentifierRange:
        """
        Set lowerCanId and return self for chaining.

        Args:
            value: The lowerCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_can_id("value")
        """
        self.lower_can_id = value  # Use property setter (gets validation)
        return self

    def with_upper_can_id(self, value: Optional[PositiveInteger]) -> RxIdentifierRange:
        """
        Set upperCanId and return self for chaining.

        Args:
            value: The upperCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_can_id("value")
        """
        self.upper_can_id = value  # Use property setter (gets validation)
        return self



class CanXlFrameTriggeringProps(ARObject):
    """
    This element indicates the frame being CAN XL and contains further CAN XL
    specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication::CanXlFrameTriggeringProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2007, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Acceptance field of a CAN XL message.
        self._acceptanceField: Optional[PositiveInteger] = None

    @property
    def acceptance_field(self) -> Optional[PositiveInteger]:
        """Get acceptanceField (Pythonic accessor)."""
        return self._acceptanceField

    @acceptance_field.setter
    def acceptance_field(self, value: Optional[PositiveInteger]) -> None:
        """
        Set acceptanceField with validation.

        Args:
            value: The acceptanceField to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._acceptanceField = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"acceptanceField must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._acceptanceField = value
        self._priorityId: Optional[PositiveInteger] = None

    @property
    def priority_id(self) -> Optional[PositiveInteger]:
        """Get priorityId (Pythonic accessor)."""
        return self._priorityId

    @priority_id.setter
    def priority_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set priorityId with validation.

        Args:
            value: The priorityId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priorityId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priorityId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priorityId = value
        self._sduType: Optional[PositiveInteger] = None

    @property
    def sdu_type(self) -> Optional[PositiveInteger]:
        """Get sduType (Pythonic accessor)."""
        return self._sduType

    @sdu_type.setter
    def sdu_type(self, value: Optional[PositiveInteger]) -> None:
        """
        Set sduType with validation.

        Args:
            value: The sduType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sduType = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sduType must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sduType = value
        self._vcid: Optional[PositiveInteger] = None

    @property
    def vcid(self) -> Optional[PositiveInteger]:
        """Get vcid (Pythonic accessor)."""
        return self._vcid

    @vcid.setter
    def vcid(self, value: Optional[PositiveInteger]) -> None:
        """
        Set vcid with validation.

        Args:
            value: The vcid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vcid = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"vcid must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._vcid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAcceptanceField(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for acceptanceField.

        Returns:
            The acceptanceField value

        Note:
            Delegates to acceptance_field property (CODING_RULE_V2_00017)
        """
        return self.acceptance_field  # Delegates to property

    def setAcceptanceField(self, value: PositiveInteger) -> CanXlFrameTriggeringProps:
        """
        AUTOSAR-compliant setter for acceptanceField with method chaining.

        Args:
            value: The acceptanceField to set

        Returns:
            self for method chaining

        Note:
            Delegates to acceptance_field property setter (gets validation automatically)
        """
        self.acceptance_field = value  # Delegates to property setter
        return self

    def getPriorityId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priorityId.

        Returns:
            The priorityId value

        Note:
            Delegates to priority_id property (CODING_RULE_V2_00017)
        """
        return self.priority_id  # Delegates to property

    def setPriorityId(self, value: PositiveInteger) -> CanXlFrameTriggeringProps:
        """
        AUTOSAR-compliant setter for priorityId with method chaining.

        Args:
            value: The priorityId to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority_id property setter (gets validation automatically)
        """
        self.priority_id = value  # Delegates to property setter
        return self

    def getSduType(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for sduType.

        Returns:
            The sduType value

        Note:
            Delegates to sdu_type property (CODING_RULE_V2_00017)
        """
        return self.sdu_type  # Delegates to property

    def setSduType(self, value: PositiveInteger) -> CanXlFrameTriggeringProps:
        """
        AUTOSAR-compliant setter for sduType with method chaining.

        Args:
            value: The sduType to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdu_type property setter (gets validation automatically)
        """
        self.sdu_type = value  # Delegates to property setter
        return self

    def getVcid(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for vcid.

        Returns:
            The vcid value

        Note:
            Delegates to vcid property (CODING_RULE_V2_00017)
        """
        return self.vcid  # Delegates to property

    def setVcid(self, value: PositiveInteger) -> CanXlFrameTriggeringProps:
        """
        AUTOSAR-compliant setter for vcid with method chaining.

        Args:
            value: The vcid to set

        Returns:
            self for method chaining

        Note:
            Delegates to vcid property setter (gets validation automatically)
        """
        self.vcid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_acceptance_field(self, value: Optional[PositiveInteger]) -> CanXlFrameTriggeringProps:
        """
        Set acceptanceField and return self for chaining.

        Args:
            value: The acceptanceField to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acceptance_field("value")
        """
        self.acceptance_field = value  # Use property setter (gets validation)
        return self

    def with_priority_id(self, value: Optional[PositiveInteger]) -> CanXlFrameTriggeringProps:
        """
        Set priorityId and return self for chaining.

        Args:
            value: The priorityId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority_id("value")
        """
        self.priority_id = value  # Use property setter (gets validation)
        return self

    def with_sdu_type(self, value: Optional[PositiveInteger]) -> CanXlFrameTriggeringProps:
        """
        Set sduType and return self for chaining.

        Args:
            value: The sduType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdu_type("value")
        """
        self.sdu_type = value  # Use property setter (gets validation)
        return self

    def with_vcid(self, value: Optional[PositiveInteger]) -> CanXlFrameTriggeringProps:
        """
        Set vcid and return self for chaining.

        Args:
            value: The vcid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vcid("value")
        """
        self.vcid = value  # Use property setter (gets validation)
        return self


class CanAddressingModeType(AREnum):
    """
    CanAddressingModeType enumeration

Indicates whether standard or extended CAN identifiers are used Aggregated by CanFrameTriggering.canAddressingMode, IEEE1722TpAcfCanPart.canAddressingMode

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication
    """
    # Extended 29-bit-identifiers are used (CAN 2.0B)
    extended = "0"

    # Standard 11-bit-identifiers are used (CAN 2.0A)
    standard = "1"



class CanFrameRxBehaviorEnum(AREnum):
    """
    CanFrameRxBehaviorEnum enumeration

Defines different CAN protocols for frame reception behavior. Aggregated by CanFrameTriggering.canFrameRxBehavior

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication
    """
    # This CAN frame may be received as both, CAN 2.0 and CAN FD.
    any = "0"

    # This CAN frame shall be received as CAN 2.0 only. In case the CAN frame is received as CAN FD it is discarded during reception.
    can20 = "1"

    # This CAN frame shall be received as CAN FD only. In case the CAN frame is received as CAN 2.0 it is discarded during reception.
    canFd = "2"



class CanFrameTxBehaviorEnum(AREnum):
    """
    CanFrameTxBehaviorEnum enumeration

Defines different CAN protocols for frame transmission behavior. Aggregated by CanFrameTriggering.canFrameTxBehavior, IEEE1722TpAcfCanPart.canFrameTxBehavior

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication
    """
    # This CAN frame shall be sent as CAN 2.0 only.
    can20 = "0"

    # This CAN frame shall be sent as CAN FD.
    canFd = "1"
