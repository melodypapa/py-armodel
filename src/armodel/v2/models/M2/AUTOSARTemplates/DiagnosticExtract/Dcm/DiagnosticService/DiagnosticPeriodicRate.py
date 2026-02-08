from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DiagnosticPeriodicRate(ARObject):
    """
    This represents the ability to define a periodic rate for the specification
    of the "read data by periodic ID" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID::DiagnosticPeriodicRate

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 131, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the period of the DiagnosticPeriodicRate.
        self._period: Optional["TimeValue"] = None

    @property
    def period(self) -> Optional["TimeValue"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["TimeValue"]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value
        # This attribute represents the category of the periodic rate.
        self._periodicRate: Optional["DiagnosticPeriodicRate"] = None

    @property
    def periodic_rate(self) -> Optional["DiagnosticPeriodicRate"]:
        """Get periodicRate (Pythonic accessor)."""
        return self._periodicRate

    @periodic_rate.setter
    def periodic_rate(self, value: Optional["DiagnosticPeriodicRate"]) -> None:
        """
        Set periodicRate with validation.

        Args:
            value: The periodicRate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._periodicRate = None
            return

        if not isinstance(value, DiagnosticPeriodicRate):
            raise TypeError(
                f"periodicRate must be DiagnosticPeriodicRate or None, got {type(value).__name__}"
            )
        self._periodicRate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> "DiagnosticPeriodicRate":
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    def getPeriodicRate(self) -> "DiagnosticPeriodicRate":
        """
        AUTOSAR-compliant getter for periodicRate.

        Returns:
            The periodicRate value

        Note:
            Delegates to periodic_rate property (CODING_RULE_V2_00017)
        """
        return self.periodic_rate  # Delegates to property

    def setPeriodicRate(self, value: "DiagnosticPeriodicRate") -> "DiagnosticPeriodicRate":
        """
        AUTOSAR-compliant setter for periodicRate with method chaining.

        Args:
            value: The periodicRate to set

        Returns:
            self for method chaining

        Note:
            Delegates to periodic_rate property setter (gets validation automatically)
        """
        self.periodic_rate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional["TimeValue"]) -> "DiagnosticPeriodicRate":
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self

    def with_periodic_rate(self, value: Optional["DiagnosticPeriodicRate"]) -> "DiagnosticPeriodicRate":
        """
        Set periodicRate and return self for chaining.

        Args:
            value: The periodicRate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_periodic_rate("value")
        """
        self.periodic_rate = value  # Use property setter (gets validation)
        return self
