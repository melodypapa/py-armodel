from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class HwPin(Identifiable):
    """
    This meta-class represents the possibility to describe a hardware pin.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPin

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 20, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute describes the function of the pin (e.
        # g.
        # CLK.
        self._functionName: List["String"] = []

    @property
    def function_name(self) -> List["String"]:
        """Get functionName (Pythonic accessor)."""
        return self._functionName
        # This attribute contains the name of the pin according to packaging of the
                # hardware element (e.
        # g.
        # A03).
        self._packagingPin: Optional["String"] = None

    @property
    def packaging_pin(self) -> Optional["String"]:
        """Get packagingPin (Pythonic accessor)."""
        return self._packagingPin

    @packaging_pin.setter
    def packaging_pin(self, value: Optional["String"]) -> None:
        """
        Set packagingPin with validation.

        Args:
            value: The packagingPin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._packagingPin = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"packagingPin must be String or None, got {type(value).__name__}"
            )
        self._packagingPin = value
        # This attribute contains the physical pin number.
        self._pinNumber: Optional["Integer"] = None

    @property
    def pin_number(self) -> Optional["Integer"]:
        """Get pinNumber (Pythonic accessor)."""
        return self._pinNumber

    @pin_number.setter
    def pin_number(self, value: Optional["Integer"]) -> None:
        """
        Set pinNumber with validation.

        Args:
            value: The pinNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pinNumber = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"pinNumber must be Integer or None, got {type(value).__name__}"
            )
        self._pinNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionName(self) -> List["String"]:
        """
        AUTOSAR-compliant getter for functionName.

        Returns:
            The functionName value

        Note:
            Delegates to function_name property (CODING_RULE_V2_00017)
        """
        return self.function_name  # Delegates to property

    def getPackagingPin(self) -> "String":
        """
        AUTOSAR-compliant getter for packagingPin.

        Returns:
            The packagingPin value

        Note:
            Delegates to packaging_pin property (CODING_RULE_V2_00017)
        """
        return self.packaging_pin  # Delegates to property

    def setPackagingPin(self, value: "String") -> "HwPin":
        """
        AUTOSAR-compliant setter for packagingPin with method chaining.

        Args:
            value: The packagingPin to set

        Returns:
            self for method chaining

        Note:
            Delegates to packaging_pin property setter (gets validation automatically)
        """
        self.packaging_pin = value  # Delegates to property setter
        return self

    def getPinNumber(self) -> "Integer":
        """
        AUTOSAR-compliant getter for pinNumber.

        Returns:
            The pinNumber value

        Note:
            Delegates to pin_number property (CODING_RULE_V2_00017)
        """
        return self.pin_number  # Delegates to property

    def setPinNumber(self, value: "Integer") -> "HwPin":
        """
        AUTOSAR-compliant setter for pinNumber with method chaining.

        Args:
            value: The pinNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to pin_number property setter (gets validation automatically)
        """
        self.pin_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_packaging_pin(self, value: Optional["String"]) -> "HwPin":
        """
        Set packagingPin and return self for chaining.

        Args:
            value: The packagingPin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_packaging_pin("value")
        """
        self.packaging_pin = value  # Use property setter (gets validation)
        return self

    def with_pin_number(self, value: Optional["Integer"]) -> "HwPin":
        """
        Set pinNumber and return self for chaining.

        Args:
            value: The pinNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pin_number("value")
        """
        self.pin_number = value  # Use property setter (gets validation)
        return self
