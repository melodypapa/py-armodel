from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DynamicPart,
    Integer,
    IPdu,
)


class MultiplexedIPdu(IPdu):
    """
    that the absolute position of the selectorField in the MultiplexedIPdu is
    determined by the definition of the selectorFieldByteOrder attribute of the
    Multiplexed Pdu. If Big Endian is specified, the start position indicates
    the bit position of the most significant bit in the IPdu. If Little Endian
    is specified, the start position indicates the bit position of the least
    significant bit in the IPdu. In AUTOSAR the bit counting is always set to
    "sawtooth" and the bit order is set to "Decreasing". The bit counting in
    byte 0 starts with bit 0 (least significant bit). The most significant bit
    in byte 0 is bit 7. In a complete System Description this attribute is
    mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not
    delivered to the IPduM but routed directly to a bus interface then the
    content of the MulitplexedPdu doesn’t need to be described in the System
    Extract/Ecu Extract. To support this use case the multiplicity is set to
    0..1. staticPart StaticPart 0..1 aggr The static part of the multiplexed
    IPdu is the same regardless of the selector field. The static part is
    optional. atpVariation: Content of a multiplexed PDU can vary. Stereotypes:
    atpSplitable; atpVariation , staticPart.variationPoint.short Label
    vh.latestBindingTime=postBuild triggerMode TriggerMode 0..1 attr IPduM can
    be configured to send a transmission request for the new multiplexed IPdu to
    the PDU-Router because of the trigger conditions/ modes that are described
    in the TriggerMode enumeration. In a complete System Description this
    attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and
    is not delivered to the IPduM but routed directly to a bus interface then
    the content of the MulitplexedPdu doesn’t need to be described in the System
    Extract/Ecu Extract. To support this use case the multiplicity is set to
    0..1. (cid:53) 409 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate
    System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::MultiplexedIPdu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 408, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # According to the value of the selector field some parts of have a different
                # layout.
        # In a complete System MultiplexedIPdu shall contain a Dynamic following use
                # cases support the multiplicity to a MultiplexedIPdu is received by a Pdu
                # Gateway and delivered to the IPduM but routed directly to a then the content
                # of the MulitplexedIPdu to be described in the System Extract/ a
                # MultiplexedIPdu is received by an ECU which is in the static part of the
                # MultiplexedIPdu dynamicPart does not need to be described in Extract/Ecu
                # Extract.
        # of a multiplexed PDU can vary.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dynamicPart: Optional["DynamicPart"] = None

    @property
    def dynamic_part(self) -> Optional["DynamicPart"]:
        """Get dynamicPart (Pythonic accessor)."""
        return self._dynamicPart

    @dynamic_part.setter
    def dynamic_part(self, value: Optional["DynamicPart"]) -> None:
        """
        Set dynamicPart with validation.

        Args:
            value: The dynamicPart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicPart = None
            return

        if not isinstance(value, DynamicPart):
            raise TypeError(
                f"dynamicPart must be DynamicPart or None, got {type(value).__name__}"
            )
        self._dynamicPart = value
        # This parameter is necessary to describe the position of selector field within
        # the IPdu.
        self._selectorField: Optional["Integer"] = None

    @property
    def selector_field(self) -> Optional["Integer"]:
        """Get selectorField (Pythonic accessor)."""
        return self._selectorField

    @selector_field.setter
    def selector_field(self, value: Optional["Integer"]) -> None:
        """
        Set selectorField with validation.

        Args:
            value: The selectorField to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._selectorField = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"selectorField must be Integer or None, got {type(value).__name__}"
            )
        self._selectorField = value
        # AUTOSAR COM and AUTOSAR IPDUM are filling not areas of an IPdu with this
                # bit-pattern.
        # This attribute to avoid undefined behavior.
        # This be repeated throughout the IPdu.
        # complete System Description this attribute is a MultiplexedPdu is received by
                # a Pdu is not delivered to the IPduM but routed a bus interface then the
                # content of the need to be described in the Extract.
        # To support this use case the set to 0.
        # 1.
        self._unusedBit: Optional["Integer"] = None

    @property
    def unused_bit(self) -> Optional["Integer"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["Integer"]) -> None:
        """
        Set unusedBit with validation.

        Args:
            value: The unusedBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"unusedBit must be Integer or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicPart(self) -> "DynamicPart":
        """
        AUTOSAR-compliant getter for dynamicPart.

        Returns:
            The dynamicPart value

        Note:
            Delegates to dynamic_part property (CODING_RULE_V2_00017)
        """
        return self.dynamic_part  # Delegates to property

    def setDynamicPart(self, value: "DynamicPart") -> "MultiplexedIPdu":
        """
        AUTOSAR-compliant setter for dynamicPart with method chaining.

        Args:
            value: The dynamicPart to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_part property setter (gets validation automatically)
        """
        self.dynamic_part = value  # Delegates to property setter
        return self

    def getSelectorField(self) -> "Integer":
        """
        AUTOSAR-compliant getter for selectorField.

        Returns:
            The selectorField value

        Note:
            Delegates to selector_field property (CODING_RULE_V2_00017)
        """
        return self.selector_field  # Delegates to property

    def setSelectorField(self, value: "Integer") -> "MultiplexedIPdu":
        """
        AUTOSAR-compliant setter for selectorField with method chaining.

        Args:
            value: The selectorField to set

        Returns:
            self for method chaining

        Note:
            Delegates to selector_field property setter (gets validation automatically)
        """
        self.selector_field = value  # Delegates to property setter
        return self

    def getUnusedBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for unusedBit.

        Returns:
            The unusedBit value

        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "Integer") -> "MultiplexedIPdu":
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.

        Args:
            value: The unusedBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_part(self, value: Optional["DynamicPart"]) -> "MultiplexedIPdu":
        """
        Set dynamicPart and return self for chaining.

        Args:
            value: The dynamicPart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_part("value")
        """
        self.dynamic_part = value  # Use property setter (gets validation)
        return self

    def with_selector_field(self, value: Optional["Integer"]) -> "MultiplexedIPdu":
        """
        Set selectorField and return self for chaining.

        Args:
            value: The selectorField to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_selector_field("value")
        """
        self.selector_field = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["Integer"]) -> "MultiplexedIPdu":
        """
        Set unusedBit and return self for chaining.

        Args:
            value: The unusedBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self
