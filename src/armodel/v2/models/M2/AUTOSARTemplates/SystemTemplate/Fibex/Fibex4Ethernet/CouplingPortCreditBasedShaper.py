from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CouplingPortCreditBasedShaper(Identifiable):
    """
    Defines a Credit Based Shaper (CBS) for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortCreditBasedShaper

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2013, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the increase of credit in bits per second for the.
        self._idleSlope: Optional["PositiveInteger"] = None

    @property
    def idle_slope(self) -> Optional["PositiveInteger"]:
        """Get idleSlope (Pythonic accessor)."""
        return self._idleSlope

    @idle_slope.setter
    def idle_slope(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set idleSlope with validation.

        Args:
            value: The idleSlope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idleSlope = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"idleSlope must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._idleSlope = value
        # Defines the lower boundary of credit for the CBS shaper.
        self._lowerBoundary: Optional["PositiveInteger"] = None

    @property
    def lower_boundary(self) -> Optional["PositiveInteger"]:
        """Get lowerBoundary (Pythonic accessor)."""
        return self._lowerBoundary

    @lower_boundary.setter
    def lower_boundary(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set lowerBoundary with validation.

        Args:
            value: The lowerBoundary to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerBoundary = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"lowerBoundary must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._lowerBoundary = value
        # Defines the upper boundary of credit for the CBS shaper.
        self._upperBoundary: Optional["PositiveInteger"] = None

    @property
    def upper_boundary(self) -> Optional["PositiveInteger"]:
        """Get upperBoundary (Pythonic accessor)."""
        return self._upperBoundary

    @upper_boundary.setter
    def upper_boundary(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set upperBoundary with validation.

        Args:
            value: The upperBoundary to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperBoundary = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"upperBoundary must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._upperBoundary = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdleSlope(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for idleSlope.

        Returns:
            The idleSlope value

        Note:
            Delegates to idle_slope property (CODING_RULE_V2_00017)
        """
        return self.idle_slope  # Delegates to property

    def setIdleSlope(self, value: "PositiveInteger") -> "CouplingPortCreditBasedShaper":
        """
        AUTOSAR-compliant setter for idleSlope with method chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Note:
            Delegates to idle_slope property setter (gets validation automatically)
        """
        self.idle_slope = value  # Delegates to property setter
        return self

    def getLowerBoundary(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for lowerBoundary.

        Returns:
            The lowerBoundary value

        Note:
            Delegates to lower_boundary property (CODING_RULE_V2_00017)
        """
        return self.lower_boundary  # Delegates to property

    def setLowerBoundary(self, value: "PositiveInteger") -> "CouplingPortCreditBasedShaper":
        """
        AUTOSAR-compliant setter for lowerBoundary with method chaining.

        Args:
            value: The lowerBoundary to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_boundary property setter (gets validation automatically)
        """
        self.lower_boundary = value  # Delegates to property setter
        return self

    def getUpperBoundary(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for upperBoundary.

        Returns:
            The upperBoundary value

        Note:
            Delegates to upper_boundary property (CODING_RULE_V2_00017)
        """
        return self.upper_boundary  # Delegates to property

    def setUpperBoundary(self, value: "PositiveInteger") -> "CouplingPortCreditBasedShaper":
        """
        AUTOSAR-compliant setter for upperBoundary with method chaining.

        Args:
            value: The upperBoundary to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_boundary property setter (gets validation automatically)
        """
        self.upper_boundary = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_idle_slope(self, value: Optional["PositiveInteger"]) -> "CouplingPortCreditBasedShaper":
        """
        Set idleSlope and return self for chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idle_slope("value")
        """
        self.idle_slope = value  # Use property setter (gets validation)
        return self

    def with_lower_boundary(self, value: Optional["PositiveInteger"]) -> "CouplingPortCreditBasedShaper":
        """
        Set lowerBoundary and return self for chaining.

        Args:
            value: The lowerBoundary to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_boundary("value")
        """
        self.lower_boundary = value  # Use property setter (gets validation)
        return self

    def with_upper_boundary(self, value: Optional["PositiveInteger"]) -> "CouplingPortCreditBasedShaper":
        """
        Set upperBoundary and return self for chaining.

        Args:
            value: The upperBoundary to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_boundary("value")
        """
        self.upper_boundary = value  # Use property setter (gets validation)
        return self
