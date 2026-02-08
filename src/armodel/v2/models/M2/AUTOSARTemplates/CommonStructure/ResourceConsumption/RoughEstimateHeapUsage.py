from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import (
    HeapUsage,
)


class RoughEstimateHeapUsage(HeapUsage):
    """
    Rough estimation of the heap usage.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 153, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Rough estimate of the heap usage.
        # Unit: byte.
        self._memoryConsumption: Optional["PositiveInteger"] = None

    @property
    def memory_consumption(self) -> Optional["PositiveInteger"]:
        """Get memoryConsumption (Pythonic accessor)."""
        return self._memoryConsumption

    @memory_consumption.setter
    def memory_consumption(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set memoryConsumption with validation.

        Args:
            value: The memoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryConsumption = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"memoryConsumption must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._memoryConsumption = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMemoryConsumption(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for memoryConsumption.

        Returns:
            The memoryConsumption value

        Note:
            Delegates to memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.memory_consumption  # Delegates to property

    def setMemoryConsumption(self, value: "PositiveInteger") -> "RoughEstimateHeapUsage":
        """
        AUTOSAR-compliant setter for memoryConsumption with method chaining.

        Args:
            value: The memoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_consumption property setter (gets validation automatically)
        """
        self.memory_consumption = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_memory_consumption(self, value: Optional["PositiveInteger"]) -> "RoughEstimateHeapUsage":
        """
        Set memoryConsumption and return self for chaining.

        Args:
            value: The memoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_consumption("value")
        """
        self.memory_consumption = value  # Use property setter (gets validation)
        return self
