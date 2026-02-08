from typing import Optional


class CompuConstNumericContent(CompuConstContent):
    """
    This meta-class represents the fact that the constant value of the
    computation method is a numerical value. It is separated from
    CompuConstFormulaContent to support compatibility with ASAM HDO.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 389, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical value.
        self._v: Optional["Numerical"] = None

    @property
    def v(self) -> Optional["Numerical"]:
        """Get v (Pythonic accessor)."""
        return self._v

    @v.setter
    def v(self, value: Optional["Numerical"]) -> None:
        """
        Set v with validation.

        Args:
            value: The v to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"v must be Numerical or None, got {type(value).__name__}"
            )
        self._v = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getV(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for v.

        Returns:
            The v value

        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: "Numerical") -> "CompuConstNumericContent":
        """
        AUTOSAR-compliant setter for v with method chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Note:
            Delegates to v property setter (gets validation automatically)
        """
        self.v = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_v(self, value: Optional["Numerical"]) -> "CompuConstNumericContent":
        """
        Set v and return self for chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v("value")
        """
        self.v = value  # Use property setter (gets validation)
        return self
