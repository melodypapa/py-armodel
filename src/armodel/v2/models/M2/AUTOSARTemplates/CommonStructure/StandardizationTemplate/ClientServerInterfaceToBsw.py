"""
AUTOSAR Package - ClientServerInterfaceToBsw

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::ClientServerInterfaceToBsw
"""

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class ClientServerOperationBlueprintMapping(ARObject):
    """
    This class describes a specific mapping between a ClientServerOperation in a
    ClientServerInterface blueprint and a BswModuleEntry blueprint.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::ClientServerInterfaceToBsw::ClientServerOperationBlueprintMapping
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 68, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute offers the possibility to provide additional with respect to
        # the mapping.
        self._blueprint: Optional["DocumentationBlock"] = None

    @property
    def blueprint(self) -> Optional["DocumentationBlock"]:
        """Get blueprint (Pythonic accessor)."""
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set blueprint with validation.
        
        Args:
            value: The blueprint to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprint = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"blueprint must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._blueprint = value
        self._bswModule: "BswModuleEntry" = None

    @property
    def bsw_module(self) -> "BswModuleEntry":
        """Get bswModule (Pythonic accessor)."""
        return self._bswModule

    @bsw_module.setter
    def bsw_module(self, value: "BswModuleEntry") -> None:
        """
        Set bswModule with validation.
        
        Args:
            value: The bswModule to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"bswModule must be BswModuleEntry, got {type(value).__name__}"
            )
        self._bswModule = value
        # mapping is dedicated to.
        self._clientServer: "ClientServerOperation" = None

    @property
    def client_server(self) -> "ClientServerOperation":
        """Get clientServer (Pythonic accessor)."""
        return self._clientServer

    @client_server.setter
    def client_server(self, value: "ClientServerOperation") -> None:
        """
        Set clientServer with validation.
        
        Args:
            value: The clientServer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServer must be ClientServerOperation, got {type(value).__name__}"
            )
        self._clientServer = value

    def with_port_defined(self, value):
        """
        Set port_defined and return self for chaining.

        Args:
            value: The port_defined to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_defined("value")
        """
        self.port_defined = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprint(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for blueprint.
        
        Returns:
            The blueprint value
        
        Note:
            Delegates to blueprint property (CODING_RULE_V2_00017)
        """
        return self.blueprint  # Delegates to property

    def setBlueprint(self, value: "DocumentationBlock") -> "ClientServerOperationBlueprintMapping":
        """
        AUTOSAR-compliant setter for blueprint with method chaining.
        
        Args:
            value: The blueprint to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to blueprint property setter (gets validation automatically)
        """
        self.blueprint = value  # Delegates to property setter
        return self

    def getBswModule(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for bswModule.
        
        Returns:
            The bswModule value
        
        Note:
            Delegates to bsw_module property (CODING_RULE_V2_00017)
        """
        return self.bsw_module  # Delegates to property

    def setBswModule(self, value: "BswModuleEntry") -> "ClientServerOperationBlueprintMapping":
        """
        AUTOSAR-compliant setter for bswModule with method chaining.
        
        Args:
            value: The bswModule to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_module property setter (gets validation automatically)
        """
        self.bsw_module = value  # Delegates to property setter
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

    def setClientServer(self, value: "ClientServerOperation") -> "ClientServerOperationBlueprintMapping":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint(self, value: Optional["DocumentationBlock"]) -> "ClientServerOperationBlueprintMapping":
        """
        Set blueprint and return self for chaining.
        
        Args:
            value: The blueprint to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_blueprint("value")
        """
        self.blueprint = value  # Use property setter (gets validation)
        return self

    def with_bsw_module(self, value: "BswModuleEntry") -> "ClientServerOperationBlueprintMapping":
        """
        Set bswModule and return self for chaining.
        
        Args:
            value: The bswModule to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_module("value")
        """
        self.bsw_module = value  # Use property setter (gets validation)
        return self

    def with_client_server(self, value: "ClientServerOperation") -> "ClientServerOperationBlueprintMapping":
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
