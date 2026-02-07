from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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
        self._canAddressing: Optional["CanAddressingMode"] = None

    @property
    def can_addressing(self) -> Optional["CanAddressingMode"]:
        """Get canAddressing (Pythonic accessor)."""
        return self._canAddressing

    @can_addressing.setter
    def can_addressing(self, value: Optional["CanAddressingMode"]) -> None:
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
        # Defines which CAN protocol shall be expected for frame reception.
        self._canFrameRx: Optional["CanFrameRxBehavior"] = None

    @property
    def can_frame_rx(self) -> Optional["CanFrameRxBehavior"]:
        """Get canFrameRx (Pythonic accessor)."""
        return self._canFrameRx

    @can_frame_rx.setter
    def can_frame_rx(self, value: Optional["CanFrameRxBehavior"]) -> None:
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
        # Defines which CAN protocol shall be used for frame transmission.
        self._canFrameTx: Optional["CanFrameTxBehavior"] = None

    @property
    def can_frame_tx(self) -> Optional["CanFrameTxBehavior"]:
        """Get canFrameTx (Pythonic accessor)."""
        return self._canFrameTx

    @can_frame_tx.setter
    def can_frame_tx(self, value: Optional["CanFrameTxBehavior"]) -> None:
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
        # Definition of CAN XL specific attributes in case the frame is a CAN XL frame.
        self._canXlFrame: RefType = None

    @property
    def can_xl_frame(self) -> RefType:
        """Get canXlFrame (Pythonic accessor)."""
        return self._canXlFrame

    @can_xl_frame.setter
    def can_xl_frame(self, value: RefType) -> None:
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
        # This attribute is used to define the identifier this frame on the CAN
        # network.
        self._identifier: Optional["Integer"] = None

    @property
    def identifier(self) -> Optional["Integer"]:
        """Get identifier (Pythonic accessor)."""
        return self._identifier

    @identifier.setter
    def identifier(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"identifier must be Integer or None, got {type(value).__name__}"
            )
        self._identifier = value
        # Frame can be triggered by the J1939 request message.
        self._j1939requestable: Optional["Boolean"] = None

    @property
    def j1939requestable(self) -> Optional["Boolean"]:
        """Get j1939requestable (Pythonic accessor)."""
        return self._j1939requestable

    @j1939requestable.setter
    def j1939requestable(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"j1939requestable must be Boolean or None, got {type(value).__name__}"
            )
        self._j1939requestable = value
        # Optional definition of a CanId range.
        self._rxIdentifierRange: Optional["RxIdentifierRange"] = None

    @property
    def rx_identifier_range(self) -> Optional["RxIdentifierRange"]:
        """Get rxIdentifierRange (Pythonic accessor)."""
        return self._rxIdentifierRange

    @rx_identifier_range.setter
    def rx_identifier_range(self, value: Optional["RxIdentifierRange"]) -> None:
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
        # Identifier mask which denotes the relevant bits in the CAN with the
        # identifier, this parameter CAN identifier range.
        self._rxMask: Optional["PositiveInteger"] = None

    @property
    def rx_mask(self) -> Optional["PositiveInteger"]:
        """Get rxMask (Pythonic accessor)."""
        return self._rxMask

    @rx_mask.setter
    def rx_mask(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"rxMask must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._rxMask = value
        # Identifier mask which denotes static bits in the CAN other bits can be set
        # dynamically.
        self._txMask: Optional["PositiveInteger"] = None

    @property
    def tx_mask(self) -> Optional["PositiveInteger"]:
        """Get txMask (Pythonic accessor)."""
        return self._txMask

    @tx_mask.setter
    def tx_mask(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"txMask must be PositiveInteger or None, got {type(value).__name__}"
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

    def getCanAddressing(self) -> "CanAddressingMode":
        """
        AUTOSAR-compliant getter for canAddressing.
        
        Returns:
            The canAddressing value
        
        Note:
            Delegates to can_addressing property (CODING_RULE_V2_00017)
        """
        return self.can_addressing  # Delegates to property

    def setCanAddressing(self, value: "CanAddressingMode") -> "CanFrameTriggering":
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

    def getCanFrameRx(self) -> "CanFrameRxBehavior":
        """
        AUTOSAR-compliant getter for canFrameRx.
        
        Returns:
            The canFrameRx value
        
        Note:
            Delegates to can_frame_rx property (CODING_RULE_V2_00017)
        """
        return self.can_frame_rx  # Delegates to property

    def setCanFrameRx(self, value: "CanFrameRxBehavior") -> "CanFrameTriggering":
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

    def getCanFrameTx(self) -> "CanFrameTxBehavior":
        """
        AUTOSAR-compliant getter for canFrameTx.
        
        Returns:
            The canFrameTx value
        
        Note:
            Delegates to can_frame_tx property (CODING_RULE_V2_00017)
        """
        return self.can_frame_tx  # Delegates to property

    def setCanFrameTx(self, value: "CanFrameTxBehavior") -> "CanFrameTriggering":
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

    def setCanXlFrame(self, value: RefType) -> "CanFrameTriggering":
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

    def getIdentifier(self) -> "Integer":
        """
        AUTOSAR-compliant getter for identifier.
        
        Returns:
            The identifier value
        
        Note:
            Delegates to identifier property (CODING_RULE_V2_00017)
        """
        return self.identifier  # Delegates to property

    def setIdentifier(self, value: "Integer") -> "CanFrameTriggering":
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

    def getJ1939requestable(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for j1939requestable.
        
        Returns:
            The j1939requestable value
        
        Note:
            Delegates to j1939requestable property (CODING_RULE_V2_00017)
        """
        return self.j1939requestable  # Delegates to property

    def setJ1939requestable(self, value: "Boolean") -> "CanFrameTriggering":
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

    def getRxIdentifierRange(self) -> "RxIdentifierRange":
        """
        AUTOSAR-compliant getter for rxIdentifierRange.
        
        Returns:
            The rxIdentifierRange value
        
        Note:
            Delegates to rx_identifier_range property (CODING_RULE_V2_00017)
        """
        return self.rx_identifier_range  # Delegates to property

    def setRxIdentifierRange(self, value: "RxIdentifierRange") -> "CanFrameTriggering":
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

    def getRxMask(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rxMask.
        
        Returns:
            The rxMask value
        
        Note:
            Delegates to rx_mask property (CODING_RULE_V2_00017)
        """
        return self.rx_mask  # Delegates to property

    def setRxMask(self, value: "PositiveInteger") -> "CanFrameTriggering":
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

    def getTxMask(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for txMask.
        
        Returns:
            The txMask value
        
        Note:
            Delegates to tx_mask property (CODING_RULE_V2_00017)
        """
        return self.tx_mask  # Delegates to property

    def setTxMask(self, value: "PositiveInteger") -> "CanFrameTriggering":
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

    def with_can_addressing(self, value: Optional["CanAddressingMode"]) -> "CanFrameTriggering":
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

    def with_can_frame_rx(self, value: Optional["CanFrameRxBehavior"]) -> "CanFrameTriggering":
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

    def with_can_frame_tx(self, value: Optional["CanFrameTxBehavior"]) -> "CanFrameTriggering":
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

    def with_can_xl_frame(self, value: Optional[RefType]) -> "CanFrameTriggering":
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

    def with_identifier(self, value: Optional["Integer"]) -> "CanFrameTriggering":
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

    def with_j1939requestable(self, value: Optional["Boolean"]) -> "CanFrameTriggering":
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

    def with_rx_identifier_range(self, value: Optional["RxIdentifierRange"]) -> "CanFrameTriggering":
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

    def with_rx_mask(self, value: Optional["PositiveInteger"]) -> "CanFrameTriggering":
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

    def with_tx_mask(self, value: Optional["PositiveInteger"]) -> "CanFrameTriggering":
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