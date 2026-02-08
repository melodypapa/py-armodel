from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class AgeConstraint(TimingConstraint):
    """
    Constrains the scope by a minimum and maximum time boundary.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::AgeConstraint::AgeConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 115, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The received event referenced by scope should not upper bound.
        self._maximum: Optional["MultidimensionalTime"] = None

    @property
    def maximum(self) -> Optional["MultidimensionalTime"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximum must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximum = value
        # The received event referenced by scope should not lower bound.
        self._minimum: Optional["MultidimensionalTime"] = None

    @property
    def minimum(self) -> Optional["MultidimensionalTime"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimum with validation.

        Args:
            value: The minimum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimum must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimum = value
        # TimingDescriptionEvent to be constrained.
        self._scope: Optional["TimingDescriptionEvent"] = None

    @property
    def scope(self) -> Optional["TimingDescriptionEvent"]:
        """Get scope (Pythonic accessor)."""
        return self._scope

    @scope.setter
    def scope(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set scope with validation.

        Args:
            value: The scope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scope = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"scope must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._scope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "MultidimensionalTime") -> "AgeConstraint":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getMinimum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "MultidimensionalTime") -> "AgeConstraint":
        """
        AUTOSAR-compliant setter for minimum with method chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    def getScope(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for scope.

        Returns:
            The scope value

        Note:
            Delegates to scope property (CODING_RULE_V2_00017)
        """
        return self.scope  # Delegates to property

    def setScope(self, value: "TimingDescriptionEvent") -> "AgeConstraint":
        """
        AUTOSAR-compliant setter for scope with method chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Note:
            Delegates to scope property setter (gets validation automatically)
        """
        self.scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum(self, value: Optional["MultidimensionalTime"]) -> "AgeConstraint":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional["MultidimensionalTime"]) -> "AgeConstraint":
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self

    def with_scope(self, value: Optional["TimingDescriptionEvent"]) -> "AgeConstraint":
        """
        Set scope and return self for chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scope("value")
        """
        self.scope = value  # Use property setter (gets validation)
        return self
