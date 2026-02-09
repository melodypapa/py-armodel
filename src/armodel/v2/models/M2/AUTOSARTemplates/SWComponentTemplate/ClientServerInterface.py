from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    PortInterface,
)


class ClientServerInterface(PortInterface):
    """
    A client/server interface declares a number of operations that can be
    invoked on a server by a client.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 308, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 235, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 101, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2007, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 432, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ClientServerOperation(s) of this ClientServerInterface.
        # atpVariation.
        self._operation: List["ClientServerOperation"] = []

    @property
    def operation(self) -> List["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation
        # Application errors that are defined as part of this interface.
        self._possibleError: List["ApplicationError"] = []

    @property
    def possible_error(self) -> List["ApplicationError"]:
        """Get possibleError (Pythonic accessor)."""
        return self._possibleError

    def with_operation(self, value):
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

    def with_possible_error(self, value):
        """
        Set possible_error and return self for chaining.

        Args:
            value: The possible_error to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_possible_error("value")
        """
        self.possible_error = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> List["ClientServerOperation"]:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def getPossibleError(self) -> List["ApplicationError"]:
        """
        AUTOSAR-compliant getter for possibleError.

        Returns:
            The possibleError value

        Note:
            Delegates to possible_error property (CODING_RULE_V2_00017)
        """
        return self.possible_error  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
