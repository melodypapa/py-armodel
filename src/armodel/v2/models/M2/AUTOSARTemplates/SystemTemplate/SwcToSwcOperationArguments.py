from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwcToSwcOperationArguments(ARObject):
    """
    The SwcToSwcOperationArguments describes the information (client server
    operation arguments, plus the operation identification, if required) that
    are exchanged between two SW Components from exactly one client to one
    server, or from one server back to one client. The direction attribute
    defines which direction is described. If direction == IN, all arguments sent
    from the client to the server are described by the
    SwcToSwcOperationArguments, in direction == OUT, it’s the arguments sent
    back from server to client.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SwcToSwcOperationArguments

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Direction addressed by this SwcToSwcClientServer element.
        self._direction: Optional["SwcToSwcOperation"] = None

    @property
    def direction(self) -> Optional["SwcToSwcOperation"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["SwcToSwcOperation"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, SwcToSwcOperation):
            raise TypeError(
                f"direction must be SwcToSwcOperation or None, got {type(value).__name__}"
            )
        self._direction = value
        # arguments are described by SwcToSwc two ports referenced shall be a connector
        # in the software component by: OperationInSystem.
        self._operation: List["ClientServerOperation"] = []

    @property
    def operation(self) -> List["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> "SwcToSwcOperation":
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: "SwcToSwcOperation") -> "SwcToSwcOperationArguments":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getOperation(self) -> List["ClientServerOperation"]:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["SwcToSwcOperation"]) -> "SwcToSwcOperationArguments":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self
