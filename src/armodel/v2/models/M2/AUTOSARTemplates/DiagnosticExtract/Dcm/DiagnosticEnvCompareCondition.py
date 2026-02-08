from abc import ABC
from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import DiagnosticEnvConditionFormulaPart


class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart, ABC):
    """
    DiagnosticCompareConditions are atomic conditions. They are based on the
    idea of a comparison at runtime of some variable data with something
    constant. The type of the comparison (==, !=, <, <=, ...) is specified in
    DiagnosticCompareCondition.compareType.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvCompareCondition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 82, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticEnvCompareCondition:
            raise TypeError("DiagnosticEnvCompareCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes represents the concrete type of the.
        self._compareType: Optional["DiagnosticCompare"] = None

    @property
    def compare_type(self) -> Optional["DiagnosticCompare"]:
        """Get compareType (Pythonic accessor)."""
        return self._compareType

    @compare_type.setter
    def compare_type(self, value: Optional["DiagnosticCompare"]) -> None:
        """
        Set compareType with validation.

        Args:
            value: The compareType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compareType = None
            return

        if not isinstance(value, DiagnosticCompare):
            raise TypeError(
                f"compareType must be DiagnosticCompare or None, got {type(value).__name__}"
            )
        self._compareType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompareType(self) -> "DiagnosticCompare":
        """
        AUTOSAR-compliant getter for compareType.

        Returns:
            The compareType value

        Note:
            Delegates to compare_type property (CODING_RULE_V2_00017)
        """
        return self.compare_type  # Delegates to property

    def setCompareType(self, value: "DiagnosticCompare") -> "DiagnosticEnvCompareCondition":
        """
        AUTOSAR-compliant setter for compareType with method chaining.

        Args:
            value: The compareType to set

        Returns:
            self for method chaining

        Note:
            Delegates to compare_type property setter (gets validation automatically)
        """
        self.compare_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compare_type(self, value: Optional["DiagnosticCompare"]) -> "DiagnosticEnvCompareCondition":
        """
        Set compareType and return self for chaining.

        Args:
            value: The compareType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compare_type("value")
        """
        self.compare_type = value  # Use property setter (gets validation)
        return self
