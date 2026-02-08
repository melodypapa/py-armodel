from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswModuleEntry,
    ClientServerOperation,
    DocumentationBlock,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
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
        # The referenced BswModuleEntry represents the Bsw the mapping is dedicated to.
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
        # The referenced ClientServerOperation represents the server operation the
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
