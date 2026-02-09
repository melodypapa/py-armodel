from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Modification(ARObject):
    """
    This meta-class represents the ability to record what has changed in a
    document in comparison to its predecessor.

    Package: M2::MSR::AsamHdo::AdminData

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 86, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property denotes the one particular change which performed on the
        # object.
        self._change: "MultiLanguageOverview" = None

    @property
    def change(self) -> "MultiLanguageOverview":
        """Get change (Pythonic accessor)."""
        return self._change

    @change.setter
    def change(self, value: "MultiLanguageOverview") -> None:
        """
        Set change with validation.

        Args:
            value: The change to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"change must be MultiLanguageOverview, got {type(value).__name__}"
            )
        self._change = value
        self._reason: Optional["MultiLanguageOverview"] = None

    @property
    def reason(self) -> Optional["MultiLanguageOverview"]:
        """Get reason (Pythonic accessor)."""
        return self._reason

    @reason.setter
    def reason(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set reason with validation.

        Args:
            value: The reason to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reason = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"reason must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._reason = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChange(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for change.

        Returns:
            The change value

        Note:
            Delegates to change property (CODING_RULE_V2_00017)
        """
        return self.change  # Delegates to property

    def setChange(self, value: "MultiLanguageOverview") -> "Modification":
        """
        AUTOSAR-compliant setter for change with method chaining.

        Args:
            value: The change to set

        Returns:
            self for method chaining

        Note:
            Delegates to change property setter (gets validation automatically)
        """
        self.change = value  # Delegates to property setter
        return self

    def getReason(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for reason.

        Returns:
            The reason value

        Note:
            Delegates to reason property (CODING_RULE_V2_00017)
        """
        return self.reason  # Delegates to property

    def setReason(self, value: "MultiLanguageOverview") -> "Modification":
        """
        AUTOSAR-compliant setter for reason with method chaining.

        Args:
            value: The reason to set

        Returns:
            self for method chaining

        Note:
            Delegates to reason property setter (gets validation automatically)
        """
        self.reason = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_change(self, value: "MultiLanguageOverview") -> "Modification":
        """
        Set change and return self for chaining.

        Args:
            value: The change to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_change("value")
        """
        self.change = value  # Use property setter (gets validation)
        return self

    def with_reason(self, value: Optional["MultiLanguageOverview"]) -> "Modification":
        """
        Set reason and return self for chaining.

        Args:
            value: The reason to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reason("value")
        """
        self.reason = value  # Use property setter (gets validation)
        return self
