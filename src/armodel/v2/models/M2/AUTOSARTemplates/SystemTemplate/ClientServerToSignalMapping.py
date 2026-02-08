from typing import Optional


class ClientServerToSignalMapping(DataMapping):
    """
    This element maps the ClientServerOperation to call- and
    return-SystemSignals.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::ClientServerToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 242, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the callSignal to which the IN and INOUT mapped.
        self._callSignal: Optional["SystemSignal"] = None

    @property
    def call_signal(self) -> Optional["SystemSignal"]:
        """Get callSignal (Pythonic accessor)."""
        return self._callSignal

    @call_signal.setter
    def call_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set callSignal with validation.

        Args:
            value: The callSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._callSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"callSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._callSignal = value
        # a call SystemSignal and a return SystemSignal.
        # by: OperationInSystem.
        self._clientServer: Optional["ClientServerOperation"] = None

    @property
    def client_server(self) -> Optional["ClientServerOperation"]:
        """Get clientServer (Pythonic accessor)."""
        return self._clientServer

    @client_server.setter
    def client_server(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set clientServer with validation.

        Args:
            value: The clientServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientServer = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServer must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._clientServer = value
        # Reference to the returnSignal to which the OUT and are mapped.
        self._returnSignal: Optional["SystemSignal"] = None

    @property
    def return_signal(self) -> Optional["SystemSignal"]:
        """Get returnSignal (Pythonic accessor)."""
        return self._returnSignal

    @return_signal.setter
    def return_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set returnSignal with validation.

        Args:
            value: The returnSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._returnSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"returnSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._returnSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCallSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for callSignal.

        Returns:
            The callSignal value

        Note:
            Delegates to call_signal property (CODING_RULE_V2_00017)
        """
        return self.call_signal  # Delegates to property

    def setCallSignal(self, value: "SystemSignal") -> "ClientServerToSignalMapping":
        """
        AUTOSAR-compliant setter for callSignal with method chaining.

        Args:
            value: The callSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to call_signal property setter (gets validation automatically)
        """
        self.call_signal = value  # Delegates to property setter
        return self

    def getClientServer(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for clientServer.

        Returns:
            The clientServer value

        Note:
            Delegates to client_server property (CODING_RULE_V2_00017)
        """
        return self.client_server  # Delegates to property

    def setClientServer(self, value: "ClientServerOperation") -> "ClientServerToSignalMapping":
        """
        AUTOSAR-compliant setter for clientServer with method chaining.

        Args:
            value: The clientServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_server property setter (gets validation automatically)
        """
        self.client_server = value  # Delegates to property setter
        return self

    def getReturnSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for returnSignal.

        Returns:
            The returnSignal value

        Note:
            Delegates to return_signal property (CODING_RULE_V2_00017)
        """
        return self.return_signal  # Delegates to property

    def setReturnSignal(self, value: "SystemSignal") -> "ClientServerToSignalMapping":
        """
        AUTOSAR-compliant setter for returnSignal with method chaining.

        Args:
            value: The returnSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to return_signal property setter (gets validation automatically)
        """
        self.return_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_call_signal(self, value: Optional["SystemSignal"]) -> "ClientServerToSignalMapping":
        """
        Set callSignal and return self for chaining.

        Args:
            value: The callSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_call_signal("value")
        """
        self.call_signal = value  # Use property setter (gets validation)
        return self

    def with_client_server(self, value: Optional["ClientServerOperation"]) -> "ClientServerToSignalMapping":
        """
        Set clientServer and return self for chaining.

        Args:
            value: The clientServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server("value")
        """
        self.client_server = value  # Use property setter (gets validation)
        return self

    def with_return_signal(self, value: Optional["SystemSignal"]) -> "ClientServerToSignalMapping":
        """
        Set returnSignal and return self for chaining.

        Args:
            value: The returnSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_return_signal("value")
        """
        self.return_signal = value  # Use property setter (gets validation)
        return self
