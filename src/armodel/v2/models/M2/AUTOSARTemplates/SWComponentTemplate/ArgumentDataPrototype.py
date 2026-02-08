from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    AutosarDataPrototype,
)


class ArgumentDataPrototype(AutosarDataPrototype):
    """
    An argument of an operation, much like a data element, but also carries
    direction information and is owned by a particular ClientServerOperation.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 303, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 300, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 102, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1998, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 29, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 160, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the direction of the argument.
        self._direction: Optional["ArgumentDirection"] = None

    @property
    def direction(self) -> Optional["ArgumentDirection"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["ArgumentDirection"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, ArgumentDirection):
            raise TypeError(
                f"direction must be ArgumentDirection or None, got {type(value).__name__}"
            )
        self._direction = value
        # This defines how the argument type of the servers RunnableEntity is
                # implemented.
        # attribute is not defined this has the same semantics the attribute is set to
                # the value useArgumentType for and structures.
        self._serverArgument: Optional["ServerArgumentImpl"] = None

    @property
    def server_argument(self) -> Optional["ServerArgumentImpl"]:
        """Get serverArgument (Pythonic accessor)."""
        return self._serverArgument

    @server_argument.setter
    def server_argument(self, value: Optional["ServerArgumentImpl"]) -> None:
        """
        Set serverArgument with validation.

        Args:
            value: The serverArgument to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serverArgument = None
            return

        if not isinstance(value, ServerArgumentImpl):
            raise TypeError(
                f"serverArgument must be ServerArgumentImpl or None, got {type(value).__name__}"
            )
        self._serverArgument = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> "ArgumentDirection":
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: "ArgumentDirection") -> "ArgumentDataPrototype":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getServerArgument(self) -> "ServerArgumentImpl":
        """
        AUTOSAR-compliant getter for serverArgument.

        Returns:
            The serverArgument value

        Note:
            Delegates to server_argument property (CODING_RULE_V2_00017)
        """
        return self.server_argument  # Delegates to property

    def setServerArgument(self, value: "ServerArgumentImpl") -> "ArgumentDataPrototype":
        """
        AUTOSAR-compliant setter for serverArgument with method chaining.

        Args:
            value: The serverArgument to set

        Returns:
            self for method chaining

        Note:
            Delegates to server_argument property setter (gets validation automatically)
        """
        self.server_argument = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["ArgumentDirection"]) -> "ArgumentDataPrototype":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self

    def with_server_argument(self, value: Optional["ServerArgumentImpl"]) -> "ArgumentDataPrototype":
        """
        Set serverArgument and return self for chaining.

        Args:
            value: The serverArgument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_server_argument("value")
        """
        self.server_argument = value  # Use property setter (gets validation)
        return self
