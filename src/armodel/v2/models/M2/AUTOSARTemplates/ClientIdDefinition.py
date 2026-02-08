from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ClientIdDefinition(Identifiable):
    """
    Several clients in one client-ECU can communicate via inter-ECU
    client-server communication with a server on a different ECU, if a client
    identifier is used to distinguish the different clients. The Client
    Identifier of the transaction handle that is used by the RTE can be defined
    by this element.

    Package: M2::AUTOSARTemplates::SystemTemplate

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 45, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Client Identifier of the transaction handle used for an server
        # communication is defined by this defined the RTE generator shall use this
        # client.
        self._clientId: Optional["Numerical"] = None

    @property
    def client_id(self) -> Optional["Numerical"]:
        """Get clientId (Pythonic accessor)."""
        return self._clientId

    @client_id.setter
    def client_id(self, value: Optional["Numerical"]) -> None:
        """
        Set clientId with validation.

        Args:
            value: The clientId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientId = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"clientId must be Numerical or None, got {type(value).__name__}"
            )
        self._clientId = value
        # client.
        # by: OperationInSystem.
        self._clientServerInstanceRef: Optional["ClientServerOperation"] = None

    @property
    def client_server_instance_ref(self) -> Optional["ClientServerOperation"]:
        """Get clientServerInstanceRef (Pythonic accessor)."""
        return self._clientServerInstanceRef

    @client_server_instance_ref.setter
    def client_server_instance_ref(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set clientServerInstanceRef with validation.

        Args:
            value: The clientServerInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientServerInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"clientServerInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._clientServerInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientId(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for clientId.

        Returns:
            The clientId value

        Note:
            Delegates to client_id property (CODING_RULE_V2_00017)
        """
        return self.client_id  # Delegates to property

    def setClientId(self, value: "Numerical") -> "ClientIdDefinition":
        """
        AUTOSAR-compliant setter for clientId with method chaining.

        Args:
            value: The clientId to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_id property setter (gets validation automatically)
        """
        self.client_id = value  # Delegates to property setter
        return self

    def getClientServerInstanceRef(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for clientServerInstanceRef.

        Returns:
            The clientServerInstanceRef value

        Note:
            Delegates to client_server_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.client_server_instance_ref  # Delegates to property

    def setClientServerInstanceRef(self, value: "ClientServerOperation") -> "ClientIdDefinition":
        """
        AUTOSAR-compliant setter for clientServerInstanceRef with method chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_server_instance_ref property setter (gets validation automatically)
        """
        self.client_server_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_client_id(self, value: Optional["Numerical"]) -> "ClientIdDefinition":
        """
        Set clientId and return self for chaining.

        Args:
            value: The clientId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_id("value")
        """
        self.client_id = value  # Use property setter (gets validation)
        return self

    def with_client_server_instance_ref(self, value: Optional["ClientServerOperation"]) -> "ClientIdDefinition":
        """
        Set clientServerInstanceRef and return self for chaining.

        Args:
            value: The clientServerInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server_instance_ref("value")
        """
        self.client_server_instance_ref = value  # Use property setter (gets validation)
        return self
