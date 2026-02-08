from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)


class ServerCallPoint(AbstractAccessPoint, ABC):
    """
    If a RunnableEntity owns a ServerCallPoint it is entitled to invoke a
    particular ClientServerOperation of a specific RPortPrototype of the
    corresponding AtomicSwComponentType

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 335, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 580, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2055, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ServerCallPoint:
            raise TypeError("ServerCallPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: ROperationInAtomicSwc.
        self._operationInstanceRef: Optional["ClientServerOperation"] = None

    @property
    def operation_instance_ref(self) -> Optional["ClientServerOperation"]:
        """Get operationInstanceRef (Pythonic accessor)."""
        return self._operationInstanceRef

    @operation_instance_ref.setter
    def operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operationInstanceRef with validation.

        Args:
            value: The operationInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operationInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operationInstanceRef = value
        # Time in seconds before the server call times out and an error message.
        # It depends on the call type asynchronous) how this is reported.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationInstanceRef(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operationInstanceRef.

        Returns:
            The operationInstanceRef value

        Note:
            Delegates to operation_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.operation_instance_ref  # Delegates to property

    def setOperationInstanceRef(self, value: "ClientServerOperation") -> "ServerCallPoint":
        """
        AUTOSAR-compliant setter for operationInstanceRef with method chaining.

        Args:
            value: The operationInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation_instance_ref property setter (gets validation automatically)
        """
        self.operation_instance_ref = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "ServerCallPoint":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> "ServerCallPoint":
        """
        Set operationInstanceRef and return self for chaining.

        Args:
            value: The operationInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation_instance_ref("value")
        """
        self.operation_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> "ServerCallPoint":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self
