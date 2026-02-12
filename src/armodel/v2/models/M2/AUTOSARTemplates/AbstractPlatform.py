"""
AUTOSAR Package - AbstractPlatform

Package: M2::AUTOSARTemplates::AbstractPlatform
"""


from __future__ import annotations
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface import (
    Field,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationDataType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerOperation,
    PortInterface,
)


class ApplicationInterface(PortInterface):
    """
    This represents the ability to define a PortInterface that consists of a
    composition of commands (method calls), indications (events) and attributes
    (fields)

    Package: M2::AUTOSARTemplates::AbstractPlatform::ApplicationInterface

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 28, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the set of attributes defined in the context Abstract
        # Platform ApplicationInterface.
        # atpVariation.
        self._attribute: List[Field] = []
        # This represents the collection of commands or function optional data
        # arguments) defined in the context ApplicationInterface.
        # atpVariation.
        self._command: List[ClientServerOperation] = []
        # This represents the collection of indication or events (with argument)
        # defined in the context of an atpVariation.
        self._indication: List[RefType] = []

    @property
    def attribute(self) -> List[Field]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute

    @attribute.setter
    def attribute(self, value: List[Field]) -> None:
        """
        Set attribute with validation.

        Args:
            value: The attribute to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"attribute must be a list, got {type(value).__name__}"
            )
        self._attribute = value

    @property
    def command(self) -> List[ClientServerOperation]:
        """Get command (Pythonic accessor)."""
        return self._command

    @command.setter
    def command(self, value: List[ClientServerOperation]) -> None:
        """
        Set command with validation.

        Args:
            value: The command to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"command must be a list, got {type(value).__name__}"
            )
        self._command = value

    @property
    def indication(self) -> List[RefType]:
        """Get indication (Pythonic accessor)."""
        return self._indication

    @indication.setter
    def indication(self, value: List[RefType]) -> None:
        """
        Set indication with validation.

        Args:
            value: The indication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"indication must be a list, got {type(value).__name__}"
            )
        self._indication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> List[Field]:
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def getCommand(self) -> List[ClientServerOperation]:
        """
        AUTOSAR-compliant getter for command.

        Returns:
            The command value

        Note:
            Delegates to command property (CODING_RULE_V2_00017)
        """
        return self.command  # Delegates to property

    def getIndication(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for indication.

        Returns:
            The indication value

        Note:
            Delegates to indication property (CODING_RULE_V2_00017)
        """
        return self.indication  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_attribute(self, value: List[Field]) -> ApplicationInterface:
        """
        Set attribute and return self for chaining.

        Args:
            value: The attribute to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute("value")
        """
        self.attribute = value  # Use property setter (gets validation)
        return self

    def with_command(self, value: List[ClientServerOperation]) -> ApplicationInterface:
        """
        Set command and return self for chaining.

        Args:
            value: The command to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_command("value")
        """
        self.command = value  # Use property setter (gets validation)
        return self

    def with_indication(self, value: List[RefType]) -> ApplicationInterface:
        """
        Set indication and return self for chaining.

        Args:
            value: The indication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_indication("value")
        """
        self.indication = value  # Use property setter (gets validation)
        return self


class ApplicationDeferredDataType(ApplicationDataType):
    """
    A placeholder data type in which the precise application data type is
    deferred to a later stage.

    Package: M2::AUTOSARTemplates::AbstractPlatform::ApplicationDeferredDataType

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 37, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
