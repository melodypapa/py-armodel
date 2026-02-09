from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    RPortComSpec,
)


class ClientComSpec(RPortComSpec):
    """
    Client-specific communication attributes (RPortPrototype typed by
    ClientServerInterface).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 187, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the maximum time interval in which application shall
        # expect the servers’s response (time the sending of the call invocation until
        # the arrival server’s response).
        self._endToEndCall: Optional["TimeValue"] = None

    @property
    def end_to_end_call(self) -> Optional["TimeValue"]:
        """Get endToEndCall (Pythonic accessor)."""
        return self._endToEndCall

    @end_to_end_call.setter
    def end_to_end_call(self, value: Optional["TimeValue"]) -> None:
        """
        Set endToEndCall with validation.

        Args:
            value: The endToEndCall to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._endToEndCall = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"endToEndCall must be TimeValue or None, got {type(value).__name__}"
            )
        self._endToEndCall = value
        # This represents the corresponding ClientServerOperation.
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
        # This references the TransformationComSpecProps which define port-specific
        # configuration for data transformation.
        self._transformation: List["TransformationCom"] = []

    @property
    def transformation(self) -> List["TransformationCom"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEndToEndCall(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for endToEndCall.

        Returns:
            The endToEndCall value

        Note:
            Delegates to end_to_end_call property (CODING_RULE_V2_00017)
        """
        return self.end_to_end_call  # Delegates to property

    def setEndToEndCall(self, value: "TimeValue") -> "ClientComSpec":
        """
        AUTOSAR-compliant setter for endToEndCall with method chaining.

        Args:
            value: The endToEndCall to set

        Returns:
            self for method chaining

        Note:
            Delegates to end_to_end_call property setter (gets validation automatically)
        """
        self.end_to_end_call = value  # Delegates to property setter
        return self

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "ClientComSpec":
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

    def with_end_to_end_call(self, value: Optional["TimeValue"]) -> "ClientComSpec":
        """
        Set endToEndCall and return self for chaining.

        Args:
            value: The endToEndCall to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_end_to_end_call("value")
        """
        self.end_to_end_call = value  # Use property setter (gets validation)
        return self

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "ClientComSpec":
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
