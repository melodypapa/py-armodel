from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticCapabilityElement,
    DiagnosticDenominator,
)


class ObdRatioDenominatorNeeds(DiagnosticCapabilityElement):
    """
    This meta-class shall be used to indicate that a software-component wants to
    access the in-use-monitoring performance ration denominator.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdRatioDenominatorNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 802, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates the applicable denominator condition.
        self._denominator: Optional["DiagnosticDenominator"] = None

    @property
    def denominator(self) -> Optional["DiagnosticDenominator"]:
        """Get denominator (Pythonic accessor)."""
        return self._denominator

    @denominator.setter
    def denominator(self, value: Optional["DiagnosticDenominator"]) -> None:
        """
        Set denominator with validation.

        Args:
            value: The denominator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._denominator = None
            return

        if not isinstance(value, DiagnosticDenominator):
            raise TypeError(
                f"denominator must be DiagnosticDenominator or None, got {type(value).__name__}"
            )
        self._denominator = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDenominator(self) -> "DiagnosticDenominator":
        """
        AUTOSAR-compliant getter for denominator.

        Returns:
            The denominator value

        Note:
            Delegates to denominator property (CODING_RULE_V2_00017)
        """
        return self.denominator  # Delegates to property

    def setDenominator(self, value: "DiagnosticDenominator") -> "ObdRatioDenominatorNeeds":
        """
        AUTOSAR-compliant setter for denominator with method chaining.

        Args:
            value: The denominator to set

        Returns:
            self for method chaining

        Note:
            Delegates to denominator property setter (gets validation automatically)
        """
        self.denominator = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_denominator(self, value: Optional["DiagnosticDenominator"]) -> "ObdRatioDenominatorNeeds":
        """
        Set denominator and return self for chaining.

        Args:
            value: The denominator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_denominator("value")
        """
        self.denominator = value  # Use property setter (gets validation)
        return self
