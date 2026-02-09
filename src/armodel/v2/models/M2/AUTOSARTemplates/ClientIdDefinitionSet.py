from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class ClientIdDefinitionSet(ARElement):
    """
    Set of Client Identifiers that are used for inter-ECU client-server
    communication in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 44, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of a Client Identifier that will be used by the in a inter-ECU
                # client-server communication.
        # atpVariation.
        self._clientId: List["ClientIdDefinition"] = []

    @property
    def client_id(self) -> List["ClientIdDefinition"]:
        """Get clientId (Pythonic accessor)."""
        return self._clientId

    def with_client_id(self, value):
        """
        Set client_id and return self for chaining.

        Args:
            value: The client_id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_id("value")
        """
        self.client_id = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientId(self) -> List["ClientIdDefinition"]:
        """
        AUTOSAR-compliant getter for clientId.

        Returns:
            The clientId value

        Note:
            Delegates to client_id property (CODING_RULE_V2_00017)
        """
        return self.client_id  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
