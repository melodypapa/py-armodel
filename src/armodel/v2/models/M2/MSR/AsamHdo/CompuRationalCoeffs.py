from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CompuRationalCoeffs(ARObject):
    """
    This meta-class represents the ability to express a rational function by
    specifying the coefficients of nominator and denominator.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 389, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerator of the rational expression.
        # Tags: xml.
        # sequenceOffset=20.
        self._compu: Optional["CompuNominator"] = None

    @property
    def compu(self) -> Optional["CompuNominator"]:
        """Get compu (Pythonic accessor)."""
        return self._compu

    @compu.setter
    def compu(self, value: Optional["CompuNominator"]) -> None:
        """
        Set compu with validation.

        Args:
            value: The compu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compu = None
            return

        if not isinstance(value, CompuNominator):
            raise TypeError(
                f"compu must be CompuNominator or None, got {type(value).__name__}"
            )
        self._compu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompu(self) -> "CompuNominator":
        """
        AUTOSAR-compliant getter for compu.

        Returns:
            The compu value

        Note:
            Delegates to compu property (CODING_RULE_V2_00017)
        """
        return self.compu  # Delegates to property

    def setCompu(self, value: "CompuNominator") -> "CompuRationalCoeffs":
        """
        AUTOSAR-compliant setter for compu with method chaining.

        Args:
            value: The compu to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu property setter (gets validation automatically)
        """
        self.compu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu(self, value: Optional["CompuNominator"]) -> "CompuRationalCoeffs":
        """
        Set compu and return self for chaining.

        Args:
            value: The compu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu("value")
        """
        self.compu = value  # Use property setter (gets validation)
        return self
