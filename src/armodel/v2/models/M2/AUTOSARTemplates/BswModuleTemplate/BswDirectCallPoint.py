from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswModuleCallPoint,
    BswModuleEntry,
    ExclusiveAreaNesting,
)


class BswDirectCallPoint(BswModuleCallPoint):
    """
    Represents a concrete point in the code from where a BswModuleEntry is
    called directly, i.e. not via the BSW Scheduler. This information can be
    used to analyze call tree and resource locking scenarios. It is not needed
    to configure the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswDirectCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 78, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The BswModuleEntry called at this point.
        self._calledEntry: Optional["BswModuleEntry"] = None

    @property
    def called_entry(self) -> Optional["BswModuleEntry"]:
        """Get calledEntry (Pythonic accessor)."""
        return self._calledEntry

    @called_entry.setter
    def called_entry(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set calledEntry with validation.

        Args:
            value: The calledEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledEntry = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"calledEntry must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._calledEntry = value
        # This indicates that the call point is located at the deepest level inside one
        # or more ExclusiveAreas that are nested the given order.
        self._calledFrom: Optional["ExclusiveAreaNesting"] = None

    @property
    def called_from(self) -> Optional["ExclusiveAreaNesting"]:
        """Get calledFrom (Pythonic accessor)."""
        return self._calledFrom

    @called_from.setter
    def called_from(self, value: Optional["ExclusiveAreaNesting"]) -> None:
        """
        Set calledFrom with validation.

        Args:
            value: The calledFrom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledFrom = None
            return

        if not isinstance(value, ExclusiveAreaNesting):
            raise TypeError(
                f"calledFrom must be ExclusiveAreaNesting or None, got {type(value).__name__}"
            )
        self._calledFrom = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledEntry(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for calledEntry.

        Returns:
            The calledEntry value

        Note:
            Delegates to called_entry property (CODING_RULE_V2_00017)
        """
        return self.called_entry  # Delegates to property

    def setCalledEntry(self, value: "BswModuleEntry") -> "BswDirectCallPoint":
        """
        AUTOSAR-compliant setter for calledEntry with method chaining.

        Args:
            value: The calledEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_entry property setter (gets validation automatically)
        """
        self.called_entry = value  # Delegates to property setter
        return self

    def getCalledFrom(self) -> "ExclusiveAreaNesting":
        """
        AUTOSAR-compliant getter for calledFrom.

        Returns:
            The calledFrom value

        Note:
            Delegates to called_from property (CODING_RULE_V2_00017)
        """
        return self.called_from  # Delegates to property

    def setCalledFrom(self, value: "ExclusiveAreaNesting") -> "BswDirectCallPoint":
        """
        AUTOSAR-compliant setter for calledFrom with method chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_from property setter (gets validation automatically)
        """
        self.called_from = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_entry(self, value: Optional["BswModuleEntry"]) -> "BswDirectCallPoint":
        """
        Set calledEntry and return self for chaining.

        Args:
            value: The calledEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_entry("value")
        """
        self.called_entry = value  # Use property setter (gets validation)
        return self

    def with_called_from(self, value: Optional["ExclusiveAreaNesting"]) -> "BswDirectCallPoint":
        """
        Set calledFrom and return self for chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_from("value")
        """
        self.called_from = value  # Use property setter (gets validation)
        return self
