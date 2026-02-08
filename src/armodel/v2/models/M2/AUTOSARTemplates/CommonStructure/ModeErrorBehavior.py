from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ModeDeclaration,
    ModeErrorReaction,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ModeErrorBehavior(ARObject):
    """
    This represents the ability to define the error behavior in the context of
    mode handling.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeErrorBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 44, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 637, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the ModeDeclaration that is considered mode in the context of
        # the enclosing Mode.
        self._defaultMode: Optional["ModeDeclaration"] = None

    @property
    def default_mode(self) -> Optional["ModeDeclaration"]:
        """Get defaultMode (Pythonic accessor)."""
        return self._defaultMode

    @default_mode.setter
    def default_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set defaultMode with validation.

        Args:
            value: The defaultMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"defaultMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._defaultMode = value
        # This represents the ability to define the policy in terms of which default
        # model shall apply in case an error occurs.
        self._errorReaction: Optional["ModeErrorReaction"] = None

    @property
    def error_reaction(self) -> Optional["ModeErrorReaction"]:
        """Get errorReaction (Pythonic accessor)."""
        return self._errorReaction

    @error_reaction.setter
    def error_reaction(self, value: Optional["ModeErrorReaction"]) -> None:
        """
        Set errorReaction with validation.

        Args:
            value: The errorReaction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorReaction = None
            return

        if not isinstance(value, ModeErrorReaction):
            raise TypeError(
                f"errorReaction must be ModeErrorReaction or None, got {type(value).__name__}"
            )
        self._errorReaction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for defaultMode.

        Returns:
            The defaultMode value

        Note:
            Delegates to default_mode property (CODING_RULE_V2_00017)
        """
        return self.default_mode  # Delegates to property

    def setDefaultMode(self, value: "ModeDeclaration") -> "ModeErrorBehavior":
        """
        AUTOSAR-compliant setter for defaultMode with method chaining.

        Args:
            value: The defaultMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_mode property setter (gets validation automatically)
        """
        self.default_mode = value  # Delegates to property setter
        return self

    def getErrorReaction(self) -> "ModeErrorReaction":
        """
        AUTOSAR-compliant getter for errorReaction.

        Returns:
            The errorReaction value

        Note:
            Delegates to error_reaction property (CODING_RULE_V2_00017)
        """
        return self.error_reaction  # Delegates to property

    def setErrorReaction(self, value: "ModeErrorReaction") -> "ModeErrorBehavior":
        """
        AUTOSAR-compliant setter for errorReaction with method chaining.

        Args:
            value: The errorReaction to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_reaction property setter (gets validation automatically)
        """
        self.error_reaction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_mode(self, value: Optional["ModeDeclaration"]) -> "ModeErrorBehavior":
        """
        Set defaultMode and return self for chaining.

        Args:
            value: The defaultMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_mode("value")
        """
        self.default_mode = value  # Use property setter (gets validation)
        return self

    def with_error_reaction(self, value: Optional["ModeErrorReaction"]) -> "ModeErrorBehavior":
        """
        Set errorReaction and return self for chaining.

        Args:
            value: The errorReaction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_reaction("value")
        """
        self.error_reaction = value  # Use property setter (gets validation)
        return self
