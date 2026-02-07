from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SwitchStreamGateEntry(Identifiable):
    """
    Defines a Asynchronous Traffic Shapter (ATS) Group for a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamGateEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 142, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Internal Priority Value (IPV), a priority value that the assigned traffic
        # class.
        self._internalPriority: Optional["PositiveInteger"] = None

    @property
    def internal_priority(self) -> Optional["PositiveInteger"]:
        """Get internalPriority (Pythonic accessor)."""
        return self._internalPriority

    @internal_priority.setter
    def internal_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set internalPriority with validation.

        Args:
            value: The internalPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._internalPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"internalPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._internalPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInternalPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for internalPriority.

        Returns:
            The internalPriority value

        Note:
            Delegates to internal_priority property (CODING_RULE_V2_00017)
        """
        return self.internal_priority  # Delegates to property

    def setInternalPriority(self, value: "PositiveInteger") -> "SwitchStreamGateEntry":
        """
        AUTOSAR-compliant setter for internalPriority with method chaining.

        Args:
            value: The internalPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to internal_priority property setter (gets validation automatically)
        """
        self.internal_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_internal_priority(self, value: Optional["PositiveInteger"]) -> "SwitchStreamGateEntry":
        """
        Set internalPriority and return self for chaining.

        Args:
            value: The internalPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal_priority("value")
        """
        self.internal_priority = value  # Use property setter (gets validation)
        return self
