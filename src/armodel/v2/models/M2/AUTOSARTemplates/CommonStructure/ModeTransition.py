from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ModeTransition(Identifiable):
    """
    This meta-class represents the ability to describe possible ModeTransitions
    in the context of a Mode DeclarationGroup.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeTransition

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 43, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 630, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the entered model of the ModeTransition.
        self._enteredMode: Optional["ModeDeclaration"] = None

    @property
    def entered_mode(self) -> Optional["ModeDeclaration"]:
        """Get enteredMode (Pythonic accessor)."""
        return self._enteredMode

    @entered_mode.setter
    def entered_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set enteredMode with validation.

        Args:
            value: The enteredMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enteredMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"enteredMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._enteredMode = value
        # This represents the exited mode of the ModeTransition.
        self._exitedMode: Optional["ModeDeclaration"] = None

    @property
    def exited_mode(self) -> Optional["ModeDeclaration"]:
        """Get exitedMode (Pythonic accessor)."""
        return self._exitedMode

    @exited_mode.setter
    def exited_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set exitedMode with validation.

        Args:
            value: The exitedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exitedMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"exitedMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._exitedMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnteredMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for enteredMode.

        Returns:
            The enteredMode value

        Note:
            Delegates to entered_mode property (CODING_RULE_V2_00017)
        """
        return self.entered_mode  # Delegates to property

    def setEnteredMode(self, value: "ModeDeclaration") -> "ModeTransition":
        """
        AUTOSAR-compliant setter for enteredMode with method chaining.

        Args:
            value: The enteredMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to entered_mode property setter (gets validation automatically)
        """
        self.entered_mode = value  # Delegates to property setter
        return self

    def getExitedMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for exitedMode.

        Returns:
            The exitedMode value

        Note:
            Delegates to exited_mode property (CODING_RULE_V2_00017)
        """
        return self.exited_mode  # Delegates to property

    def setExitedMode(self, value: "ModeDeclaration") -> "ModeTransition":
        """
        AUTOSAR-compliant setter for exitedMode with method chaining.

        Args:
            value: The exitedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to exited_mode property setter (gets validation automatically)
        """
        self.exited_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entered_mode(self, value: Optional["ModeDeclaration"]) -> "ModeTransition":
        """
        Set enteredMode and return self for chaining.

        Args:
            value: The enteredMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entered_mode("value")
        """
        self.entered_mode = value  # Use property setter (gets validation)
        return self

    def with_exited_mode(self, value: Optional["ModeDeclaration"]) -> "ModeTransition":
        """
        Set exitedMode and return self for chaining.

        Args:
            value: The exitedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exited_mode("value")
        """
        self.exited_mode = value  # Use property setter (gets validation)
        return self
