from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import Integer
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TpAddress(Identifiable):
    """
    An ECUs TP address on the referenced channel. This represents the diagnostic
    Address.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::TpAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 588, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An ECUs TP address on the referenced channel.
        # This diagnostic Address.
        self._tpAddress: Optional["Integer"] = None

    @property
    def tp_address(self) -> Optional["Integer"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional["Integer"]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"tpAddress must be Integer or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> "Integer":
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: "Integer") -> "TpAddress":
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional["Integer"]) -> "TpAddress":
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self
