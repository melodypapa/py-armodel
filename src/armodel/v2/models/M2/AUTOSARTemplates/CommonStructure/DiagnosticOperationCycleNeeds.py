from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCapabilityElement


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide
    information regarding the operation cycle management to the Dem module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticOperationCycleNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 761, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Operation cycles types for the Dem to be supported by APIs.
        self._operationCycle: Optional["OperationCycleType"] = None

    @property
    def operation_cycle(self) -> Optional["OperationCycleType"]:
        """Get operationCycle (Pythonic accessor)."""
        return self._operationCycle

    @operation_cycle.setter
    def operation_cycle(self, value: Optional["OperationCycleType"]) -> None:
        """
        Set operationCycle with validation.

        Args:
            value: The operationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationCycle = None
            return

        if not isinstance(value, OperationCycleType):
            raise TypeError(
                f"operationCycle must be OperationCycleType or None, got {type(value).__name__}"
            )
        self._operationCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationCycle(self) -> "OperationCycleType":
        """
        AUTOSAR-compliant getter for operationCycle.

        Returns:
            The operationCycle value

        Note:
            Delegates to operation_cycle property (CODING_RULE_V2_00017)
        """
        return self.operation_cycle  # Delegates to property

    def setOperationCycle(self, value: "OperationCycleType") -> "DiagnosticOperationCycleNeeds":
        """
        AUTOSAR-compliant setter for operationCycle with method chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation_cycle property setter (gets validation automatically)
        """
        self.operation_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_cycle(self, value: Optional["OperationCycleType"]) -> "DiagnosticOperationCycleNeeds":
        """
        Set operationCycle and return self for chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation_cycle("value")
        """
        self.operation_cycle = value  # Use property setter (gets validation)
        return self
