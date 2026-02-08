from typing import Optional


class CompuScaleConstantContents(CompuScaleContents):
    """
    This meta-class represents the fact that a particular scale of the
    computation method is constant.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the fact that the scale is a constant.
        # The is mainly a non interpolated scale.
        # It is a the fact that a constant scale can also be rational function of order
                # 0.
        self._compuConst: Optional["CompuConst"] = None

    @property
    def compu_const(self) -> Optional["CompuConst"]:
        """Get compuConst (Pythonic accessor)."""
        return self._compuConst

    @compu_const.setter
    def compu_const(self, value: Optional["CompuConst"]) -> None:
        """
        Set compuConst with validation.

        Args:
            value: The compuConst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuConst = None
            return

        if not isinstance(value, CompuConst):
            raise TypeError(
                f"compuConst must be CompuConst or None, got {type(value).__name__}"
            )
        self._compuConst = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuConst(self) -> "CompuConst":
        """
        AUTOSAR-compliant getter for compuConst.

        Returns:
            The compuConst value

        Note:
            Delegates to compu_const property (CODING_RULE_V2_00017)
        """
        return self.compu_const  # Delegates to property

    def setCompuConst(self, value: "CompuConst") -> "CompuScaleConstantContents":
        """
        AUTOSAR-compliant setter for compuConst with method chaining.

        Args:
            value: The compuConst to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_const property setter (gets validation automatically)
        """
        self.compu_const = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_const(self, value: Optional["CompuConst"]) -> "CompuScaleConstantContents":
        """
        Set compuConst and return self for chaining.

        Args:
            value: The compuConst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_const("value")
        """
        self.compu_const = value  # Use property setter (gets validation)
        return self
