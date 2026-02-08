from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FMFeatureMapAssertion(Identifiable):
    """
    Defines a boolean expression which shall evaluate to true for this mapping
    to become active. The expression is a formula that is based on features and
    system constants, and is defined by fmSyscond.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureMapAssertion

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 55, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The formula that implements the assertion.
        self._fmSyscondAndSwSystemconsts: Optional["FMConditionByFeatures"] = None

    @property
    def fm_syscond_and_sw_systemconsts(self) -> Optional["FMConditionByFeatures"]:
        """Get fmSyscondAndSwSystemconsts (Pythonic accessor)."""
        return self._fmSyscondAndSwSystemconsts

    @fm_syscond_and_sw_systemconsts.setter
    def fm_syscond_and_sw_systemconsts(self, value: Optional["FMConditionByFeatures"]) -> None:
        """
        Set fmSyscondAndSwSystemconsts with validation.

        Args:
            value: The fmSyscondAndSwSystemconsts to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fmSyscondAndSwSystemconsts = None
            return

        if not isinstance(value, FMConditionByFeatures):
            raise TypeError(
                f"fmSyscondAndSwSystemconsts must be FMConditionByFeatures or None, got {type(value).__name__}"
            )
        self._fmSyscondAndSwSystemconsts = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFmSyscondAndSwSystemconsts(self) -> "FMConditionByFeatures":
        """
        AUTOSAR-compliant getter for fmSyscondAndSwSystemconsts.

        Returns:
            The fmSyscondAndSwSystemconsts value

        Note:
            Delegates to fm_syscond_and_sw_systemconsts property (CODING_RULE_V2_00017)
        """
        return self.fm_syscond_and_sw_systemconsts  # Delegates to property

    def setFmSyscondAndSwSystemconsts(self, value: "FMConditionByFeatures") -> "FMFeatureMapAssertion":
        """
        AUTOSAR-compliant setter for fmSyscondAndSwSystemconsts with method chaining.

        Args:
            value: The fmSyscondAndSwSystemconsts to set

        Returns:
            self for method chaining

        Note:
            Delegates to fm_syscond_and_sw_systemconsts property setter (gets validation automatically)
        """
        self.fm_syscond_and_sw_systemconsts = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fm_syscond_and_sw_systemconsts(self, value: Optional["FMConditionByFeatures"]) -> "FMFeatureMapAssertion":
        """
        Set fmSyscondAndSwSystemconsts and return self for chaining.

        Args:
            value: The fmSyscondAndSwSystemconsts to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fm_syscond_and_sw_systemconsts("value")
        """
        self.fm_syscond_and_sw_systemconsts = value  # Use property setter (gets validation)
        return self
