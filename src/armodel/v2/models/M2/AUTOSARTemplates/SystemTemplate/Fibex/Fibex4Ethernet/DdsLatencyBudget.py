from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import Float
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DdsLatencyBudget(ARObject):
    """
    Describes the DDS LATENCY_BUDGET QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsLatencyBudget

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 532, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "LATENCY_BUDGET" chapter of DDS.
        # given in seconds.
        self._latencyBudget: Optional["Float"] = None

    @property
    def latency_budget(self) -> Optional["Float"]:
        """Get latencyBudget (Pythonic accessor)."""
        return self._latencyBudget

    @latency_budget.setter
    def latency_budget(self, value: Optional["Float"]) -> None:
        """
        Set latencyBudget with validation.

        Args:
            value: The latencyBudget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._latencyBudget = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"latencyBudget must be Float or None, got {type(value).__name__}"
            )
        self._latencyBudget = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLatencyBudget(self) -> "Float":
        """
        AUTOSAR-compliant getter for latencyBudget.

        Returns:
            The latencyBudget value

        Note:
            Delegates to latency_budget property (CODING_RULE_V2_00017)
        """
        return self.latency_budget  # Delegates to property

    def setLatencyBudget(self, value: "Float") -> "DdsLatencyBudget":
        """
        AUTOSAR-compliant setter for latencyBudget with method chaining.

        Args:
            value: The latencyBudget to set

        Returns:
            self for method chaining

        Note:
            Delegates to latency_budget property setter (gets validation automatically)
        """
        self.latency_budget = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_latency_budget(self, value: Optional["Float"]) -> "DdsLatencyBudget":
        """
        Set latencyBudget and return self for chaining.

        Args:
            value: The latencyBudget to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_latency_budget("value")
        """
        self.latency_budget = value  # Use property setter (gets validation)
        return self
