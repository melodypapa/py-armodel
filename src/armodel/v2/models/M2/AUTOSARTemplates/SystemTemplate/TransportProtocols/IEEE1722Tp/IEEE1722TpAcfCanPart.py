from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    """
    Definition of one CAN part (frame or frame range) transported over the
    IEEE1722Tp channel.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfCanPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 661, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether standard or extended address format shall be used.
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
        # Defines whether the bit rate switch bit shall be set.
        self._canBitRate: Optional["Boolean"] = None

    @property
    def can_bit_rate(self) -> Optional["Boolean"]:
        """Get canBitRate (Pythonic accessor)."""
        return self._canBitRate

    @can_bit_rate.setter
    def can_bit_rate(self, value: Optional["Boolean"]) -> None:
        """
        Set canBitRate with validation.
        
        Args:
            value: The canBitRate to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canBitRate = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"canBitRate must be Boolean or None, got {type(value).__name__}"
            )
        self._canBitRate = value
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
        # Definition of the identifier range for IEEE1722Tp ACF Can.
        self._canIdentifier: Optional["RxIdentifierRange"] = None

    @property
    def can_identifier(self) -> Optional["RxIdentifierRange"]:
        """Get canIdentifier (Pythonic accessor)."""
        return self._canIdentifier

    @can_identifier.setter
    def can_identifier(self, value: Optional["RxIdentifierRange"]) -> None:
        """
        Set canIdentifier with validation.
        
        Args:
            value: The canIdentifier to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canIdentifier = None
            return

        if not isinstance(value, RxIdentifierRange):
            raise TypeError(
                f"canIdentifier must be RxIdentifierRange or None, got {type(value).__name__}"
            )
        self._canIdentifier = value
        # Reference to the Pdu transported in the IEEE1722Tp.
        self._sdu: RefType = None

    @property
    def sdu(self) -> RefType:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    @sdu.setter
    def sdu(self, value: RefType) -> None:
        """
        Set sdu with validation.
        
        Args:
            value: The sdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdu = None
            return

        self._sdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanAddressing(self) -> "CanAddressingMode":
        """
        AUTOSAR-compliant getter for canAddressing.
        
        Returns:
            The canAddressing value
        
        Note:
            Delegates to can_addressing property (CODING_RULE_V2_00017)
        """
        return self.can_addressing  # Delegates to property

    def setCanAddressing(self, value: "CanAddressingMode") -> "IEEE1722TpAcfCanPart":
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

    def getCanBitRate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for canBitRate.
        
        Returns:
            The canBitRate value
        
        Note:
            Delegates to can_bit_rate property (CODING_RULE_V2_00017)
        """
        return self.can_bit_rate  # Delegates to property

    def setCanBitRate(self, value: "Boolean") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for canBitRate with method chaining.
        
        Args:
            value: The canBitRate to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to can_bit_rate property setter (gets validation automatically)
        """
        self.can_bit_rate = value  # Delegates to property setter
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

    def setCanFrameTx(self, value: "CanFrameTxBehavior") -> "IEEE1722TpAcfCanPart":
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

    def getCanIdentifier(self) -> "RxIdentifierRange":
        """
        AUTOSAR-compliant getter for canIdentifier.
        
        Returns:
            The canIdentifier value
        
        Note:
            Delegates to can_identifier property (CODING_RULE_V2_00017)
        """
        return self.can_identifier  # Delegates to property

    def setCanIdentifier(self, value: "RxIdentifierRange") -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for canIdentifier with method chaining.
        
        Args:
            value: The canIdentifier to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to can_identifier property setter (gets validation automatically)
        """
        self.can_identifier = value  # Delegates to property setter
        return self

    def getSdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for sdu.
        
        Returns:
            The sdu value
        
        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    def setSdu(self, value: RefType) -> "IEEE1722TpAcfCanPart":
        """
        AUTOSAR-compliant setter for sdu with method chaining.
        
        Args:
            value: The sdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdu property setter (gets validation automatically)
        """
        self.sdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_addressing(self, value: Optional["CanAddressingMode"]) -> "IEEE1722TpAcfCanPart":
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

    def with_can_bit_rate(self, value: Optional["Boolean"]) -> "IEEE1722TpAcfCanPart":
        """
        Set canBitRate and return self for chaining.
        
        Args:
            value: The canBitRate to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_can_bit_rate("value")
        """
        self.can_bit_rate = value  # Use property setter (gets validation)
        return self

    def with_can_frame_tx(self, value: Optional["CanFrameTxBehavior"]) -> "IEEE1722TpAcfCanPart":
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

    def with_can_identifier(self, value: Optional["RxIdentifierRange"]) -> "IEEE1722TpAcfCanPart":
        """
        Set canIdentifier and return self for chaining.
        
        Args:
            value: The canIdentifier to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_can_identifier("value")
        """
        self.can_identifier = value  # Use property setter (gets validation)
        return self

    def with_sdu(self, value: Optional[RefType]) -> "IEEE1722TpAcfCanPart":
        """
        Set sdu and return self for chaining.
        
        Args:
            value: The sdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdu("value")
        """
        self.sdu = value  # Use property setter (gets validation)
        return self