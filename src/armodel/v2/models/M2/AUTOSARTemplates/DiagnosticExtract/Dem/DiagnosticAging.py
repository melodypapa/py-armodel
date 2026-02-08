from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticAging(DiagnosticCommonElement):
    """
    Defines the aging algorithm.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticAging::DiagnosticAging

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 202, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable aging cycle.
        # atpSplitable; atpVariation.
        self._agingCycle: Optional["DiagnosticOperation"] = None

    @property
    def aging_cycle(self) -> Optional["DiagnosticOperation"]:
        """Get agingCycle (Pythonic accessor)."""
        return self._agingCycle

    @aging_cycle.setter
    def aging_cycle(self, value: Optional["DiagnosticOperation"]) -> None:
        """
        Set agingCycle with validation.

        Args:
            value: The agingCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._agingCycle = None
            return

        if not isinstance(value, DiagnosticOperation):
            raise TypeError(
                f"agingCycle must be DiagnosticOperation or None, got {type(value).__name__}"
            )
        self._agingCycle = value
        # Number of aging cycles needed to unlearn/delete the.
        self._threshold: Optional["PositiveInteger"] = None

    @property
    def threshold(self) -> Optional["PositiveInteger"]:
        """Get threshold (Pythonic accessor)."""
        return self._threshold

    @threshold.setter
    def threshold(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set threshold with validation.

        Args:
            value: The threshold to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._threshold = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"threshold must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._threshold = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAgingCycle(self) -> "DiagnosticOperation":
        """
        AUTOSAR-compliant getter for agingCycle.

        Returns:
            The agingCycle value

        Note:
            Delegates to aging_cycle property (CODING_RULE_V2_00017)
        """
        return self.aging_cycle  # Delegates to property

    def setAgingCycle(self, value: "DiagnosticOperation") -> "DiagnosticAging":
        """
        AUTOSAR-compliant setter for agingCycle with method chaining.

        Args:
            value: The agingCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to aging_cycle property setter (gets validation automatically)
        """
        self.aging_cycle = value  # Delegates to property setter
        return self

    def getThreshold(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for threshold.

        Returns:
            The threshold value

        Note:
            Delegates to threshold property (CODING_RULE_V2_00017)
        """
        return self.threshold  # Delegates to property

    def setThreshold(self, value: "PositiveInteger") -> "DiagnosticAging":
        """
        AUTOSAR-compliant setter for threshold with method chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Note:
            Delegates to threshold property setter (gets validation automatically)
        """
        self.threshold = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aging_cycle(self, value: Optional["DiagnosticOperation"]) -> "DiagnosticAging":
        """
        Set agingCycle and return self for chaining.

        Args:
            value: The agingCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aging_cycle("value")
        """
        self.aging_cycle = value  # Use property setter (gets validation)
        return self

    def with_threshold(self, value: Optional["PositiveInteger"]) -> "DiagnosticAging":
        """
        Set threshold and return self for chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_threshold("value")
        """
        self.threshold = value  # Use property setter (gets validation)
        return self
