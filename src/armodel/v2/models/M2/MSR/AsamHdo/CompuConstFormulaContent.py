
class CompuConstFormulaContent(CompuConstContent):
    """
    This meta-class represents the fact that the constant value of the
    computation method is represented by a variation point. This difference is
    due to compatibility with ASAM HDO.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 900, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value calculated via a system constant.
        # This element is every case where parameters should be numerical values during
                # compile time (not example, the influence of the cylinder number on can be
                # introduced in a repeatable.
        self._vf: "Numerical" = None

    @property
    def vf(self) -> "Numerical":
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: "Numerical") -> None:
        """
        Set vf with validation.

        Args:
            value: The vf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical, got {type(value).__name__}"
            )
        self._vf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVf(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for vf.

        Returns:
            The vf value

        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: "Numerical") -> "CompuConstFormulaContent":
        """
        AUTOSAR-compliant setter for vf with method chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vf(self, value: "Numerical") -> "CompuConstFormulaContent":
        """
        Set vf and return self for chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self
