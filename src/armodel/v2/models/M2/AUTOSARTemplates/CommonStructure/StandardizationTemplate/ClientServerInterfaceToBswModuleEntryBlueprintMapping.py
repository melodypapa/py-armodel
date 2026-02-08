from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class ClientServerInterfaceToBswModuleEntryBlueprintMapping(ARElement):
    """
    This represents a mapping between one ClientServerInterface blueprint and
    BswModuleEntry blueprint in order to express the intended implementation of
    ClientServerOperations by specific BswModuleEntries under consideration of
    PortDefinedArguments. Such a mapping enables the formal check whether the
    number of arguments and the data types of arguments of the operation +
    additional PortDefined Arguments matches the signature of the
    BswModuleEntry.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::ClientServerInterfaceToBsw::ClientServerInterfaceToBswModuleEntryBlueprintMapping

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 174, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced ClientServerInterface represents the server interface the
        # mapping is dedicated to.
        self._clientServer: "ClientServerInterface" = None

    @property
    def client_server(self) -> "ClientServerInterface":
        """Get clientServer (Pythonic accessor)."""
        return self._clientServer

    @client_server.setter
    def client_server(self, value: "ClientServerInterface") -> None:
        """
        Set clientServer with validation.

        Args:
            value: The clientServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ClientServerInterface):
            raise TypeError(
                f"clientServer must be ClientServerInterface, got {type(value).__name__}"
            )
        self._clientServer = value
        # between the ClientServerInterface and the BswModule atpVariation.
        self._operation: "ClientServerOperation" = None

    @property
    def operation(self) -> "ClientServerOperation":
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: "ClientServerOperation") -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation, got {type(value).__name__}"
            )
        self._operation = value
        # This specifies the PortDefinedArguments used in the mapping between the
        # ClientServerInterface and the Bsw atpSplitable; atpVariation.
        self._portDefined: List["PortDefinedArgument"] = []

    @property
    def port_defined(self) -> List["PortDefinedArgument"]:
        """Get portDefined (Pythonic accessor)."""
        return self._portDefined

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientServer(self) -> "ClientServerInterface":
        """
        AUTOSAR-compliant getter for clientServer.

        Returns:
            The clientServer value

        Note:
            Delegates to client_server property (CODING_RULE_V2_00017)
        """
        return self.client_server  # Delegates to property

    def setClientServer(self, value: "ClientServerInterface") -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
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

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
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

    def getPortDefined(self) -> List["PortDefinedArgument"]:
        """
        AUTOSAR-compliant getter for portDefined.

        Returns:
            The portDefined value

        Note:
            Delegates to port_defined property (CODING_RULE_V2_00017)
        """
        return self.port_defined  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_client_server(self, value: "ClientServerInterface") -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
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

    def with_operation(self, value: "ClientServerOperation") -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
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
