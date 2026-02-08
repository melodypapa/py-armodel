from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class ModeDeclarationGroup(ARElement):
    """
    A collection of Mode Declarations. Also, the initial mode is explicitly
    identified.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeDeclarationGroup

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 42, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 322, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 628, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2038, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 197, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The initial mode of the ModeDeclarationGroup.
        # This active before any mode switches occurred.
        self._initialMode: Optional["ModeDeclaration"] = None

    @property
    def initial_mode(self) -> Optional["ModeDeclaration"]:
        """Get initialMode (Pythonic accessor)."""
        return self._initialMode

    @initial_mode.setter
    def initial_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set initialMode with validation.

        Args:
            value: The initialMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"initialMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._initialMode = value
        # The ModeDeclarations collected in this ModeDeclaration atpVariation.
        self._mode: List["ModeDeclaration"] = []

    @property
    def mode(self) -> List["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode
        # This represents the ability to define the error behavior by the mode manager
                # in case of errors on the side (e.
        # g.
        # terminated mode user).
        self._modeManager: Optional["ModeErrorBehavior"] = None

    @property
    def mode_manager(self) -> Optional["ModeErrorBehavior"]:
        """Get modeManager (Pythonic accessor)."""
        return self._modeManager

    @mode_manager.setter
    def mode_manager(self, value: Optional["ModeErrorBehavior"]) -> None:
        """
        Set modeManager with validation.

        Args:
            value: The modeManager to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeManager = None
            return

        if not isinstance(value, ModeErrorBehavior):
            raise TypeError(
                f"modeManager must be ModeErrorBehavior or None, got {type(value).__name__}"
            )
        self._modeManager = value
        # This represents the avaliable ModeTransitions of the.
        self._modeTransition: List["ModeTransition"] = []

    @property
    def mode_transition(self) -> List["ModeTransition"]:
        """Get modeTransition (Pythonic accessor)."""
        return self._modeTransition
        # This represents the definition of the error behavior by the mode user in case
                # of errors on the mode (e.
        # g.
        # terminated mode manager).
        self._modeUserError: Optional["ModeErrorBehavior"] = None

    @property
    def mode_user_error(self) -> Optional["ModeErrorBehavior"]:
        """Get modeUserError (Pythonic accessor)."""
        return self._modeUserError

    @mode_user_error.setter
    def mode_user_error(self, value: Optional["ModeErrorBehavior"]) -> None:
        """
        Set modeUserError with validation.

        Args:
            value: The modeUserError to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeUserError = None
            return

        if not isinstance(value, ModeErrorBehavior):
            raise TypeError(
                f"modeUserError must be ModeErrorBehavior or None, got {type(value).__name__}"
            )
        self._modeUserError = value
        # The value of this attribute shall be taken into account by RTE generator for
        # programmatically representing a for the transition between two statuses.
        self._onTransition: Optional["PositiveInteger"] = None

    @property
    def on_transition(self) -> Optional["PositiveInteger"]:
        """Get onTransition (Pythonic accessor)."""
        return self._onTransition

    @on_transition.setter
    def on_transition(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set onTransition with validation.

        Args:
            value: The onTransition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onTransition = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"onTransition must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._onTransition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for initialMode.

        Returns:
            The initialMode value

        Note:
            Delegates to initial_mode property (CODING_RULE_V2_00017)
        """
        return self.initial_mode  # Delegates to property

    def setInitialMode(self, value: "ModeDeclaration") -> "ModeDeclarationGroup":
        """
        AUTOSAR-compliant setter for initialMode with method chaining.

        Args:
            value: The initialMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_mode property setter (gets validation automatically)
        """
        self.initial_mode = value  # Delegates to property setter
        return self

    def getMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def getModeManager(self) -> "ModeErrorBehavior":
        """
        AUTOSAR-compliant getter for modeManager.

        Returns:
            The modeManager value

        Note:
            Delegates to mode_manager property (CODING_RULE_V2_00017)
        """
        return self.mode_manager  # Delegates to property

    def setModeManager(self, value: "ModeErrorBehavior") -> "ModeDeclarationGroup":
        """
        AUTOSAR-compliant setter for modeManager with method chaining.

        Args:
            value: The modeManager to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_manager property setter (gets validation automatically)
        """
        self.mode_manager = value  # Delegates to property setter
        return self

    def getModeTransition(self) -> List["ModeTransition"]:
        """
        AUTOSAR-compliant getter for modeTransition.

        Returns:
            The modeTransition value

        Note:
            Delegates to mode_transition property (CODING_RULE_V2_00017)
        """
        return self.mode_transition  # Delegates to property

    def getModeUserError(self) -> "ModeErrorBehavior":
        """
        AUTOSAR-compliant getter for modeUserError.

        Returns:
            The modeUserError value

        Note:
            Delegates to mode_user_error property (CODING_RULE_V2_00017)
        """
        return self.mode_user_error  # Delegates to property

    def setModeUserError(self, value: "ModeErrorBehavior") -> "ModeDeclarationGroup":
        """
        AUTOSAR-compliant setter for modeUserError with method chaining.

        Args:
            value: The modeUserError to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_user_error property setter (gets validation automatically)
        """
        self.mode_user_error = value  # Delegates to property setter
        return self

    def getOnTransition(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for onTransition.

        Returns:
            The onTransition value

        Note:
            Delegates to on_transition property (CODING_RULE_V2_00017)
        """
        return self.on_transition  # Delegates to property

    def setOnTransition(self, value: "PositiveInteger") -> "ModeDeclarationGroup":
        """
        AUTOSAR-compliant setter for onTransition with method chaining.

        Args:
            value: The onTransition to set

        Returns:
            self for method chaining

        Note:
            Delegates to on_transition property setter (gets validation automatically)
        """
        self.on_transition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_mode(self, value: Optional["ModeDeclaration"]) -> "ModeDeclarationGroup":
        """
        Set initialMode and return self for chaining.

        Args:
            value: The initialMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_mode("value")
        """
        self.initial_mode = value  # Use property setter (gets validation)
        return self

    def with_mode_manager(self, value: Optional["ModeErrorBehavior"]) -> "ModeDeclarationGroup":
        """
        Set modeManager and return self for chaining.

        Args:
            value: The modeManager to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_manager("value")
        """
        self.mode_manager = value  # Use property setter (gets validation)
        return self

    def with_mode_user_error(self, value: Optional["ModeErrorBehavior"]) -> "ModeDeclarationGroup":
        """
        Set modeUserError and return self for chaining.

        Args:
            value: The modeUserError to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_user_error("value")
        """
        self.mode_user_error = value  # Use property setter (gets validation)
        return self

    def with_on_transition(self, value: Optional["PositiveInteger"]) -> "ModeDeclarationGroup":
        """
        Set onTransition and return self for chaining.

        Args:
            value: The onTransition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_on_transition("value")
        """
        self.on_transition = value  # Use property setter (gets validation)
        return self
