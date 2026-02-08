from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """
    Defines an Asynchronous Traffic Shapter (ATS) Group for a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchAsynchronousTrafficShaperGroupEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 142, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the maximum duration limit for which frames can in a switch (in
        # seconds).
        self._maximum: Optional["PositiveInteger"] = None

    @property
    def maximum(self) -> Optional["PositiveInteger"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maximum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maximum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "PositiveInteger") -> "SwitchAsynchronousTrafficShaperGroupEntry":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum(self, value: Optional["PositiveInteger"]) -> "SwitchAsynchronousTrafficShaperGroupEntry":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self
