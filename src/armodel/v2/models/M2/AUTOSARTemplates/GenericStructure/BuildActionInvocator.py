from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import VerbatimString
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BuildActionInvocator(ARObject):
    """
    that it is optional due to the fact that some actions are hardwired in the
    environment and do not need an explicit command. On the other hand the
    properties of an invocator can be complex and not standardized. sdg Sdg *
    aggr This represents a general data structure intended to denote parameters
    for the BuildAction. Table 10.6: BuildActionInvocator

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionInvocator

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 372, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the command to invocate the processor.
        self._command: Optional["VerbatimString"] = None

    @property
    def command(self) -> Optional["VerbatimString"]:
        """Get command (Pythonic accessor)."""
        return self._command

    @command.setter
    def command(self, value: Optional["VerbatimString"]) -> None:
        """
        Set command with validation.

        Args:
            value: The command to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._command = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"command must be VerbatimString or None, got {type(value).__name__}"
            )
        self._command = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommand(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for command.

        Returns:
            The command value

        Note:
            Delegates to command property (CODING_RULE_V2_00017)
        """
        return self.command  # Delegates to property

    def setCommand(self, value: "VerbatimString") -> "BuildActionInvocator":
        """
        AUTOSAR-compliant setter for command with method chaining.

        Args:
            value: The command to set

        Returns:
            self for method chaining

        Note:
            Delegates to command property setter (gets validation automatically)
        """
        self.command = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_command(self, value: Optional["VerbatimString"]) -> "BuildActionInvocator":
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
