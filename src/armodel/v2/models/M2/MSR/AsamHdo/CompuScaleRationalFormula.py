from typing import Optional


class CompuScaleRationalFormula(CompuScaleContents):
    """
    This meta-class represents the fact that the computation in this scale is
    represented as rational term.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the coefficients of the rational formula.
        # xml.
        # sequenceOffset=110.
        self._compuRational: Optional["CompuRationalCoeffs"] = None

    @property
    def compu_rational(self) -> Optional["CompuRationalCoeffs"]:
        """Get compuRational (Pythonic accessor)."""
        return self._compuRational

    @compu_rational.setter
    def compu_rational(self, value: Optional["CompuRationalCoeffs"]) -> None:
        """
        Set compuRational with validation.

        Args:
            value: The compuRational to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuRational = None
            return

        if not isinstance(value, CompuRationalCoeffs):
            raise TypeError(
                f"compuRational must be CompuRationalCoeffs or None, got {type(value).__name__}"
            )
        self._compuRational = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuRational(self) -> "CompuRationalCoeffs":
        """
        AUTOSAR-compliant getter for compuRational.

        Returns:
            The compuRational value

        Note:
            Delegates to compu_rational property (CODING_RULE_V2_00017)
        """
        return self.compu_rational  # Delegates to property

    def setCompuRational(self, value: "CompuRationalCoeffs") -> "CompuScaleRationalFormula":
        """
        AUTOSAR-compliant setter for compuRational with method chaining.

        Args:
            value: The compuRational to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_rational property setter (gets validation automatically)
        """
        self.compu_rational = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_rational(self, value: Optional["CompuRationalCoeffs"]) -> "CompuScaleRationalFormula":
        """
        Set compuRational and return self for chaining.

        Args:
            value: The compuRational to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_rational("value")
        """
        self.compu_rational = value  # Use property setter (gets validation)
        return self
