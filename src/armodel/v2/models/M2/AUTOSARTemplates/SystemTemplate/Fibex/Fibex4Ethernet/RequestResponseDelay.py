from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class RequestResponseDelay(ARObject):
    """
    Time to wait before answering the query.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 515, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum allowable response delay to entries received by seconds.
        self._maxValue: Optional["TimeValue"] = None

    @property
    def max_value(self) -> Optional["TimeValue"]:
        """Get maxValue (Pythonic accessor)."""
        return self._maxValue

    @max_value.setter
    def max_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxValue with validation.

        Args:
            value: The maxValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxValue = value
        # Minimum allowable response delay to entries received by seconds.
        self._minValue: Optional["TimeValue"] = None

    @property
    def min_value(self) -> Optional["TimeValue"]:
        """Get minValue (Pythonic accessor)."""
        return self._minValue

    @min_value.setter
    def min_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set minValue with validation.

        Args:
            value: The minValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._minValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxValue.

        Returns:
            The maxValue value

        Note:
            Delegates to max_value property (CODING_RULE_V2_00017)
        """
        return self.max_value  # Delegates to property

    def setMaxValue(self, value: "TimeValue") -> "RequestResponseDelay":
        """
        AUTOSAR-compliant setter for maxValue with method chaining.

        Args:
            value: The maxValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_value property setter (gets validation automatically)
        """
        self.max_value = value  # Delegates to property setter
        return self

    def getMinValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minValue.

        Returns:
            The minValue value

        Note:
            Delegates to min_value property (CODING_RULE_V2_00017)
        """
        return self.min_value  # Delegates to property

    def setMinValue(self, value: "TimeValue") -> "RequestResponseDelay":
        """
        AUTOSAR-compliant setter for minValue with method chaining.

        Args:
            value: The minValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_value property setter (gets validation automatically)
        """
        self.min_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_value(self, value: Optional["TimeValue"]) -> "RequestResponseDelay":
        """
        Set maxValue and return self for chaining.

        Args:
            value: The maxValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_value("value")
        """
        self.max_value = value  # Use property setter (gets validation)
        return self

    def with_min_value(self, value: Optional["TimeValue"]) -> "RequestResponseDelay":
        """
        Set minValue and return self for chaining.

        Args:
            value: The minValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_value("value")
        """
        self.min_value = value  # Use property setter (gets validation)
        return self
