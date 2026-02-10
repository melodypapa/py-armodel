from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    RTEEvent,
)

    RefType,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TransformerHardErrorEvent(RTEEvent):
    """
    This event is raised when data are received which should trigger a
    Client/Server operation or an external Trigger but during transformation of
    the data a hard transformer error occurred.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 546, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # raise this TransformerHardErrorEvent.
        # by: POperationInAtomicSwc.
        self._operation: Optional["ClientServerOperation"] = None

    @property
    def operation(self) -> Optional["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value
        # by: RTriggerInAtomicSwc.
        self._requiredTrigger: RefType = None

    @property
    def required_trigger(self) -> RefType:
        """Get requiredTrigger (Pythonic accessor)."""
        return self._requiredTrigger

    @required_trigger.setter
    def required_trigger(self, value: RefType) -> None:
        """
        Set requiredTrigger with validation.

        Args:
            value: The requiredTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiredTrigger = None
            return

        self._requiredTrigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "TransformerHardErrorEvent":
        """
        AUTOSAR-compliant setter for operation with method chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    def getRequiredTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for requiredTrigger.

        Returns:
            The requiredTrigger value

        Note:
            Delegates to required_trigger property (CODING_RULE_V2_00017)
        """
        return self.required_trigger  # Delegates to property

    def setRequiredTrigger(self, value: RefType) -> "TransformerHardErrorEvent":
        """
        AUTOSAR-compliant setter for requiredTrigger with method chaining.

        Args:
            value: The requiredTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to required_trigger property setter (gets validation automatically)
        """
        self.required_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "TransformerHardErrorEvent":
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_required_trigger(self, value: Optional[RefType]) -> "TransformerHardErrorEvent":
        """
        Set requiredTrigger and return self for chaining.

        Args:
            value: The requiredTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_trigger("value")
        """
        self.required_trigger = value  # Use property setter (gets validation)
        return self
