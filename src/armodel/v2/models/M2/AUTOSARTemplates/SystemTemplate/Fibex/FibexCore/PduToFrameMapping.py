from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class PduToFrameMapping(ARObject):
    """
    that the exact bit position of the updateIndicationBit Position is linked to
    the value of the attribute packingByte Order because the method of finding
    the bit position is different for the values mostSignificantByteFirst and
    most SignificantByteLast. This means that if the value of packingByteOrder
    is changed while the value of update IndicationBitPosition remains unchanged
    the exact bit position of updateIndicationBitPosition within the enclosing
    Frame still undergoes a change. This attribute denotes the least significant
    bit for "Little Endian" and the most significant bit for "Big Endian"
    (cid:53) (cid:53) 346 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate
    System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::PduToFrameMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 346, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the order of the bytes of the Pdu the packing into the
                # Frame.
        # Please consider that [constr_3222] are restricting the usage attribute.
        self._packingByte: Optional["ByteOrderEnum"] = None

    @property
    def packing_byte(self) -> Optional["ByteOrderEnum"]:
        """Get packingByte (Pythonic accessor)."""
        return self._packingByte

    @packing_byte.setter
    def packing_byte(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set packingByte with validation.

        Args:
            value: The packingByte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._packingByte = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"packingByte must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._packingByte = value
        # Reference to a I-Pdu, N-Pdu or NmPdu that is transmitted Frame.
        self._pdu: Optional["Pdu"] = None

    @property
    def pdu(self) -> Optional["Pdu"]:
        """Get pdu (Pythonic accessor)."""
        return self._pdu

    @pdu.setter
    def pdu(self, value: Optional["Pdu"]) -> None:
        """
        Set pdu with validation.

        Args:
            value: The pdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdu = None
            return

        if not isinstance(value, Pdu):
            raise TypeError(
                f"pdu must be Pdu or None, got {type(value).__name__}"
            )
        self._pdu = value
        # This attribute describes the bitposition of a Pdu within a that the absolute
                # position of the Pdu in the determined by the definition of the packingByte If
                # Big Endian is specified, the start the bit position of the most significant
                # bit Frame.
        # If Little Endian is specified, the start position bit position of the least
                # significant bit in the bit counting in byte 0 starts with bit 0 (least The
                # most significant bit in byte 0 is bit 7.
        # are byte aligned in a Frame and only the values 16, 24,.
        # (for little endian) and 7, 15, 23,.
        # (for big allowed.
        self._startPosition: Optional["Integer"] = None

    @property
    def start_position(self) -> Optional["Integer"]:
        """Get startPosition (Pythonic accessor)."""
        return self._startPosition

    @start_position.setter
    def start_position(self, value: Optional["Integer"]) -> None:
        """
        Set startPosition with validation.

        Args:
            value: The startPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startPosition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"startPosition must be Integer or None, got {type(value).__name__}"
            )
        self._startPosition = value
        # Indication to the receivers that the corresponding Pdu updated by the sender.
        # This attribute describes the of the update bit in the frame that aggregates
                # this is always one bit.
        # within the IPdu (see the description of the In AUTOSAR the bit always set to
                # "sawtooth" and the bit order is "Decreasing".
        # The bit counting in byte 0 starts with (least significant bit).
        # The most significant bit in byte bit 7.
        self._update: Optional["Integer"] = None

    @property
    def update(self) -> Optional["Integer"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["Integer"]) -> None:
        """
        Set update with validation.

        Args:
            value: The update to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"update must be Integer or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPackingByte(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for packingByte.

        Returns:
            The packingByte value

        Note:
            Delegates to packing_byte property (CODING_RULE_V2_00017)
        """
        return self.packing_byte  # Delegates to property

    def setPackingByte(self, value: "ByteOrderEnum") -> "PduToFrameMapping":
        """
        AUTOSAR-compliant setter for packingByte with method chaining.

        Args:
            value: The packingByte to set

        Returns:
            self for method chaining

        Note:
            Delegates to packing_byte property setter (gets validation automatically)
        """
        self.packing_byte = value  # Delegates to property setter
        return self

    def getPdu(self) -> "Pdu":
        """
        AUTOSAR-compliant getter for pdu.

        Returns:
            The pdu value

        Note:
            Delegates to pdu property (CODING_RULE_V2_00017)
        """
        return self.pdu  # Delegates to property

    def setPdu(self, value: "Pdu") -> "PduToFrameMapping":
        """
        AUTOSAR-compliant setter for pdu with method chaining.

        Args:
            value: The pdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdu property setter (gets validation automatically)
        """
        self.pdu = value  # Delegates to property setter
        return self

    def getStartPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for startPosition.

        Returns:
            The startPosition value

        Note:
            Delegates to start_position property (CODING_RULE_V2_00017)
        """
        return self.start_position  # Delegates to property

    def setStartPosition(self, value: "Integer") -> "PduToFrameMapping":
        """
        AUTOSAR-compliant setter for startPosition with method chaining.

        Args:
            value: The startPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to start_position property setter (gets validation automatically)
        """
        self.start_position = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "Integer":
        """
        AUTOSAR-compliant getter for update.

        Returns:
            The update value

        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "Integer") -> "PduToFrameMapping":
        """
        AUTOSAR-compliant setter for update with method chaining.

        Args:
            value: The update to set

        Returns:
            self for method chaining

        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_packing_byte(self, value: Optional["ByteOrderEnum"]) -> "PduToFrameMapping":
        """
        Set packingByte and return self for chaining.

        Args:
            value: The packingByte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_packing_byte("value")
        """
        self.packing_byte = value  # Use property setter (gets validation)
        return self

    def with_pdu(self, value: Optional["Pdu"]) -> "PduToFrameMapping":
        """
        Set pdu and return self for chaining.

        Args:
            value: The pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu("value")
        """
        self.pdu = value  # Use property setter (gets validation)
        return self

    def with_start_position(self, value: Optional["Integer"]) -> "PduToFrameMapping":
        """
        Set startPosition and return self for chaining.

        Args:
            value: The startPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start_position("value")
        """
        self.start_position = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["Integer"]) -> "PduToFrameMapping":
        """
        Set update and return self for chaining.

        Args:
            value: The update to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self
