from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterfaceMapping,
)


class ClientServerInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of ClientServerOperations in context of two different
    ClientServerInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 128, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Map two different ApplicationErrors defined in the context two different
        # ClientServerInterfaces.
        self._errorMapping: List["ClientServerApplication"] = []

    @property
    def error_mapping(self) -> List["ClientServerApplication"]:
        """Get errorMapping (Pythonic accessor)."""
        return self._errorMapping
        # Mapping of two ClientServerOperations in two different
        # ClientServerInterfaces.
        self._operation: List["ClientServerOperation"] = []

    @property
    def operation(self) -> List["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorMapping(self) -> List["ClientServerApplication"]:
        """
        AUTOSAR-compliant getter for errorMapping.

        Returns:
            The errorMapping value

        Note:
            Delegates to error_mapping property (CODING_RULE_V2_00017)
        """
        return self.error_mapping  # Delegates to property

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
