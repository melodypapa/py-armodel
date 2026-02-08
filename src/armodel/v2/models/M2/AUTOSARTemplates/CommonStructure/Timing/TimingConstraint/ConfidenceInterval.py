from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Float,
    MultidimensionalTime,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ConfidenceInterval(ARObject):
    """
    Additionally to the list of measured distances of event occurrences, a
    confidence interval can be specified for the expected distance of two
    consecutive event occurrences with a given probability.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::ConfidenceInterval

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 112, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The lower bound of the expected distance of two occurrences.
        self._lowerBound: Optional["MultidimensionalTime"] = None

    @property
    def lower_bound(self) -> Optional["MultidimensionalTime"]:
        """Get lowerBound (Pythonic accessor)."""
        return self._lowerBound

    @lower_bound.setter
    def lower_bound(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set lowerBound with validation.

        Args:
            value: The lowerBound to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerBound = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"lowerBound must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._lowerBound = value
        # The probability for the measured lower and upper bound confidence interval.
        self._propability: Optional["Float"] = None

    @property
    def propability(self) -> Optional["Float"]:
        """Get propability (Pythonic accessor)."""
        return self._propability

    @propability.setter
    def propability(self, value: Optional["Float"]) -> None:
        """
        Set propability with validation.

        Args:
            value: The propability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propability = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"propability must be Float or None, got {type(value).__name__}"
            )
        self._propability = value
        # The upper bound of the expected distance of two occurrences.
        self._upperBound: Optional["MultidimensionalTime"] = None

    @property
    def upper_bound(self) -> Optional["MultidimensionalTime"]:
        """Get upperBound (Pythonic accessor)."""
        return self._upperBound

    @upper_bound.setter
    def upper_bound(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set upperBound with validation.

        Args:
            value: The upperBound to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperBound = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"upperBound must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._upperBound = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerBound(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for lowerBound.

        Returns:
            The lowerBound value

        Note:
            Delegates to lower_bound property (CODING_RULE_V2_00017)
        """
        return self.lower_bound  # Delegates to property

    def setLowerBound(self, value: "MultidimensionalTime") -> "ConfidenceInterval":
        """
        AUTOSAR-compliant setter for lowerBound with method chaining.

        Args:
            value: The lowerBound to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_bound property setter (gets validation automatically)
        """
        self.lower_bound = value  # Delegates to property setter
        return self

    def getPropability(self) -> "Float":
        """
        AUTOSAR-compliant getter for propability.

        Returns:
            The propability value

        Note:
            Delegates to propability property (CODING_RULE_V2_00017)
        """
        return self.propability  # Delegates to property

    def setPropability(self, value: "Float") -> "ConfidenceInterval":
        """
        AUTOSAR-compliant setter for propability with method chaining.

        Args:
            value: The propability to set

        Returns:
            self for method chaining

        Note:
            Delegates to propability property setter (gets validation automatically)
        """
        self.propability = value  # Delegates to property setter
        return self

    def getUpperBound(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for upperBound.

        Returns:
            The upperBound value

        Note:
            Delegates to upper_bound property (CODING_RULE_V2_00017)
        """
        return self.upper_bound  # Delegates to property

    def setUpperBound(self, value: "MultidimensionalTime") -> "ConfidenceInterval":
        """
        AUTOSAR-compliant setter for upperBound with method chaining.

        Args:
            value: The upperBound to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_bound property setter (gets validation automatically)
        """
        self.upper_bound = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_bound(self, value: Optional["MultidimensionalTime"]) -> "ConfidenceInterval":
        """
        Set lowerBound and return self for chaining.

        Args:
            value: The lowerBound to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_bound("value")
        """
        self.lower_bound = value  # Use property setter (gets validation)
        return self

    def with_propability(self, value: Optional["Float"]) -> "ConfidenceInterval":
        """
        Set propability and return self for chaining.

        Args:
            value: The propability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_propability("value")
        """
        self.propability = value  # Use property setter (gets validation)
        return self

    def with_upper_bound(self, value: Optional["MultidimensionalTime"]) -> "ConfidenceInterval":
        """
        Set upperBound and return self for chaining.

        Args:
            value: The upperBound to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_bound("value")
        """
        self.upper_bound = value  # Use property setter (gets validation)
        return self
