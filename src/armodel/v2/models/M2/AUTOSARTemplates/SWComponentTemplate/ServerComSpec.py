from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    PPortComSpec,
)


class ServerComSpec(PPortComSpec):
    """
    Communication attributes for a server port (PPortPrototype and
    ClientServerInterface).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 188, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Operation these communication attributes apply to.
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
        # Length of call queue on the server side.
        # The queue is the RTE.
        # The value shall be greater or 1.
        # Setting the value of queueLength to 1 implies requests are rejected while
                # another request earlier is being processed.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"queueLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._queueLength = value
        # This references the TransformationComSpecProps which define port-specific
        # configuration for data transformation.
        self._transformation: List["TransformationCom"] = []

    @property
    def transformation(self) -> List["TransformationCom"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

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

    def setOperation(self, value: "ClientServerOperation") -> "ServerComSpec":
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

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "ServerComSpec":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationCom"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "ServerComSpec":
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

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "ServerComSpec":
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self
