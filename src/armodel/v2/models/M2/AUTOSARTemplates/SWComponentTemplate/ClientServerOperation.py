from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
    RefType,
)


class ClientServerOperation(Identifiable):
    """
    An operation declared within the scope of a client/server interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 309, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 306, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 102, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2008, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 218, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 28, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 433, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 174, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An argument of this ClientServerOperation atpSplitable; atpVariation.
        self._argument: List[RefType] = []

    @property
    def argument(self) -> List[RefType]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This attribute shall only be used in the implementation of to support the
                # case where input and are allocated in a shared buffer and overwrite input
                # arguments by operations to output arguments.
        # can happen during sliced execution or while are arrays (call by reference).
        # The means that the ClientServerOperation is aware usage of a shared buffer
                # and takes precautions to overwrite of input arguments.
        # attribute does not exist or is set to false the Client not have to consider
                # the usage of a.
        self._diagArgIntegrity: Optional["Boolean"] = None

    @property
    def diag_arg_integrity(self) -> Optional["Boolean"]:
        """Get diagArgIntegrity (Pythonic accessor)."""
        return self._diagArgIntegrity

    @diag_arg_integrity.setter
    def diag_arg_integrity(self, value: Optional["Boolean"]) -> None:
        """
        Set diagArgIntegrity with validation.

        Args:
            value: The diagArgIntegrity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagArgIntegrity = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"diagArgIntegrity must be Boolean or None, got {type(value).__name__}"
            )
        self._diagArgIntegrity = value
        # Possible errors that may by raised by the referring.
        self._possibleError: List["ApplicationError"] = []

    @property
    def possible_error(self) -> List["ApplicationError"]:
        """Get possibleError (Pythonic accessor)."""
        return self._possibleError

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getDiagArgIntegrity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for diagArgIntegrity.

        Returns:
            The diagArgIntegrity value

        Note:
            Delegates to diag_arg_integrity property (CODING_RULE_V2_00017)
        """
        return self.diag_arg_integrity  # Delegates to property

    def setDiagArgIntegrity(self, value: "Boolean") -> "ClientServerOperation":
        """
        AUTOSAR-compliant setter for diagArgIntegrity with method chaining.

        Args:
            value: The diagArgIntegrity to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag_arg_integrity property setter (gets validation automatically)
        """
        self.diag_arg_integrity = value  # Delegates to property setter
        return self

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

    def with_diag_arg_integrity(self, value: Optional["Boolean"]) -> "ClientServerOperation":
        """
        Set diagArgIntegrity and return self for chaining.

        Args:
            value: The diagArgIntegrity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag_arg_integrity("value")
        """
        self.diag_arg_integrity = value  # Use property setter (gets validation)
        return self
