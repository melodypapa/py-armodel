from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class CompuConst(ARObject):
    """
    This meta-class represents the fact that the value of a computation method
    scale is constant.

    Package: M2::MSR::AsamHdo::ComputationMethod::CompuConst

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the actual content of the constant compu method.
        self._compuConst: Optional["CompuConstContent"] = None

    @property
    def compu_const(self) -> Optional["CompuConstContent"]:
        """Get compuConst (Pythonic accessor)."""
        return self._compuConst

    @compu_const.setter
    def compu_const(self, value: Optional["CompuConstContent"]) -> None:
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

        if not isinstance(value, CompuConstContent):
            raise TypeError(
                f"compuConst must be CompuConstContent or None, got {type(value).__name__}"
            )
        self._compuConst = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuConst(self) -> "CompuConstContent":
        """
        AUTOSAR-compliant getter for compuConst.

        Returns:
            The compuConst value

        Note:
            Delegates to compu_const property (CODING_RULE_V2_00017)
        """
        return self.compu_const  # Delegates to property

    def setCompuConst(self, value: "CompuConstContent") -> "CompuConst":
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

    def with_compu_const(self, value: Optional["CompuConstContent"]) -> "CompuConst":
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
