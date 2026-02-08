from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import PortInterface

    RefType,
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
        self._attribute: List["Field"] = []

    @property
    def attribute(self) -> List["Field"]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute
        # This represents the collection of commands or function optional data
                # arguments) defined in the context ApplicationInterface.
        # atpVariation.
        self._command: List["ClientServerOperation"] = []

    @property
    def command(self) -> List["ClientServerOperation"]:
        """Get command (Pythonic accessor)."""
        return self._command
        # This represents the collection of indication or events (with argument)
        # defined in the context of an atpVariation.
        self._indication: List[RefType] = []

    @property
    def indication(self) -> List[RefType]:
        """Get indication (Pythonic accessor)."""
        return self._indication

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> List["Field"]:
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def getCommand(self) -> List["ClientServerOperation"]:
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
