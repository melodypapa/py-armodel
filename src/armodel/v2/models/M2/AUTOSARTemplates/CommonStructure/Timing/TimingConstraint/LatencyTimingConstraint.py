"""
AUTOSAR Package - LatencyTimingConstraint

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.__init__ import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class LatencyTimingConstraint(TimingConstraint):
    """
    Constrains the time duration between the occurrence of the stimulus and the
    occurrence of the corresponding response of that scope. In contrast to
    scope, a causal dependency between the stimulus and the corresponding
    response of the scope is required.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint::LatencyTimingConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 95, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The specific type of this latency constraint.
        self._latency: Optional["LatencyConstraintType"] = None

    @property
    def latency(self) -> Optional["LatencyConstraintType"]:
        """Get latency (Pythonic accessor)."""
        return self._latency

    @latency.setter
    def latency(self, value: Optional["LatencyConstraintType"]) -> None:
        """
        Set latency with validation.

        Args:
            value: The latency to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._latency = None
            return

        if not isinstance(value, LatencyConstraintType):
            raise TypeError(
                f"latency must be LatencyConstraintType or None, got {type(value).__name__}"
            )
        self._latency = value
        # corresponding the associated event chain.
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
        # corresponding the associated event chain.
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
        # corresponding the associated event chain.
        self._nominal: Optional["MultidimensionalTime"] = None

    @property
    def nominal(self) -> Optional["MultidimensionalTime"]:
        """Get nominal (Pythonic accessor)."""
        return self._nominal

    @nominal.setter
    def nominal(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set nominal with validation.

        Args:
            value: The nominal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nominal = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"nominal must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._nominal = value
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

    def getLatency(self) -> "LatencyConstraintType":
        """
        AUTOSAR-compliant getter for latency.

        Returns:
            The latency value

        Note:
            Delegates to latency property (CODING_RULE_V2_00017)
        """
        return self.latency  # Delegates to property

    def setLatency(self, value: "LatencyConstraintType") -> LatencyTimingConstraint:
        """
        AUTOSAR-compliant setter for latency with method chaining.

        Args:
            value: The latency to set

        Returns:
            self for method chaining

        Note:
            Delegates to latency property setter (gets validation automatically)
        """
        self.latency = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "MultidimensionalTime") -> LatencyTimingConstraint:
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

    def setMinimum(self, value: "MultidimensionalTime") -> LatencyTimingConstraint:
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

    def getNominal(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for nominal.

        Returns:
            The nominal value

        Note:
            Delegates to nominal property (CODING_RULE_V2_00017)
        """
        return self.nominal  # Delegates to property

    def setNominal(self, value: "MultidimensionalTime") -> LatencyTimingConstraint:
        """
        AUTOSAR-compliant setter for nominal with method chaining.

        Args:
            value: The nominal to set

        Returns:
            self for method chaining

        Note:
            Delegates to nominal property setter (gets validation automatically)
        """
        self.nominal = value  # Delegates to property setter
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

    def setScope(self, value: "TimingDescriptionEvent") -> LatencyTimingConstraint:
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

    def with_latency(self, value: Optional["LatencyConstraintType"]) -> LatencyTimingConstraint:
        """
        Set latency and return self for chaining.

        Args:
            value: The latency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_latency("value")
        """
        self.latency = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["MultidimensionalTime"]) -> LatencyTimingConstraint:
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

    def with_minimum(self, value: Optional["MultidimensionalTime"]) -> LatencyTimingConstraint:
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

    def with_nominal(self, value: Optional["MultidimensionalTime"]) -> LatencyTimingConstraint:
        """
        Set nominal and return self for chaining.

        Args:
            value: The nominal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nominal("value")
        """
        self.nominal = value  # Use property setter (gets validation)
        return self

    def with_scope(self, value: Optional["TimingDescriptionEvent"]) -> LatencyTimingConstraint:
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


class LatencyConstraintTypeEnum(AREnum):
    """
    LatencyConstraintTypeEnum enumeration

Specifies the latencyConstraintType for a LatencyTimingConstraint. Aggregated by LatencyTimingConstraint.latencyConstraintType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::LatencyTimingConstraint
    """
    # The LatencyTimingConstraint is seen from the perspective of the response event of the
    age = "0"

    # The LatencyTimingConstraint is seen from the perspective of the stimulus event of the
    reaction = "1"
