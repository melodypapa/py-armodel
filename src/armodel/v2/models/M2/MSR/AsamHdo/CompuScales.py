from typing import List


class CompuScales(CompuContent):
    """
    This meta-class represents the ability to stepwise express a computation
    method.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 388, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one scale within the compu method.
        # Note it contains a Variationpoint in order to support enumerations.
        # atpVariation.
        self._compuScale: List["CompuScale"] = []

    @property
    def compu_scale(self) -> List["CompuScale"]:
        """Get compuScale (Pythonic accessor)."""
        return self._compuScale

    def with_compu_scale(self, value):
        """
        Set compu_scale and return self for chaining.

        Args:
            value: The compu_scale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_scale("value")
        """
        self.compu_scale = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuScale(self) -> List["CompuScale"]:
        """
        AUTOSAR-compliant getter for compuScale.

        Returns:
            The compuScale value

        Note:
            Delegates to compu_scale property (CODING_RULE_V2_00017)
        """
        return self.compu_scale  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
