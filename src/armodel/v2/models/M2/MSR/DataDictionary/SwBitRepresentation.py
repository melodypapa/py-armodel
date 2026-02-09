from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwBitRepresentation(ARObject):
    """
    Description of the structure of a bit variable: Comprises of the bitPosition
    in a memory object (e.g. sw HostVariable, which stands parallel to
    swBitRepresentation) and the numberOfBits . In this way, interrelated memory
    areas can be described. Non-related memory areas are not supported.

    Package: M2::MSR::DataDictionary::DataDefProperties

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 333, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the "bit data object" is hosted within another data object the memory can
        # be accessed via byte as well as this attribute specifies the position of the
        # The count starts at zero (0).
        self._bitPosition: Optional["Integer"] = None

    @property
    def bit_position(self) -> Optional["Integer"]:
        """Get bitPosition (Pythonic accessor)."""
        return self._bitPosition

    @bit_position.setter
    def bit_position(self, value: Optional["Integer"]) -> None:
        """
        Set bitPosition with validation.

        Args:
            value: The bitPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitPosition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"bitPosition must be Integer or None, got {type(value).__name__}"
            )
        self._bitPosition = value
        self._numberOfBits: Optional["Integer"] = None

    @property
    def number_of_bits(self) -> Optional["Integer"]:
        """Get numberOfBits (Pythonic accessor)."""
        return self._numberOfBits

    @number_of_bits.setter
    def number_of_bits(self, value: Optional["Integer"]) -> None:
        """
        Set numberOfBits with validation.

        Args:
            value: The numberOfBits to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOfBits = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"numberOfBits must be Integer or None, got {type(value).__name__}"
            )
        self._numberOfBits = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for bitPosition.

        Returns:
            The bitPosition value

        Note:
            Delegates to bit_position property (CODING_RULE_V2_00017)
        """
        return self.bit_position  # Delegates to property

    def setBitPosition(self, value: "Integer") -> "SwBitRepresentation":
        """
        AUTOSAR-compliant setter for bitPosition with method chaining.

        Args:
            value: The bitPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to bit_position property setter (gets validation automatically)
        """
        self.bit_position = value  # Delegates to property setter
        return self

    def getNumberOfBits(self) -> "Integer":
        """
        AUTOSAR-compliant getter for numberOfBits.

        Returns:
            The numberOfBits value

        Note:
            Delegates to number_of_bits property (CODING_RULE_V2_00017)
        """
        return self.number_of_bits  # Delegates to property

    def setNumberOfBits(self, value: "Integer") -> "SwBitRepresentation":
        """
        AUTOSAR-compliant setter for numberOfBits with method chaining.

        Args:
            value: The numberOfBits to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of_bits property setter (gets validation automatically)
        """
        self.number_of_bits = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_position(self, value: Optional["Integer"]) -> "SwBitRepresentation":
        """
        Set bitPosition and return self for chaining.

        Args:
            value: The bitPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bit_position("value")
        """
        self.bit_position = value  # Use property setter (gets validation)
        return self

    def with_number_of_bits(self, value: Optional["Integer"]) -> "SwBitRepresentation":
        """
        Set numberOfBits and return self for chaining.

        Args:
            value: The numberOfBits to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of_bits("value")
        """
        self.number_of_bits = value  # Use property setter (gets validation)
        return self
