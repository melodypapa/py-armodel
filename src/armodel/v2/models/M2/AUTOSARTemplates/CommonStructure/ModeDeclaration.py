"""
AUTOSAR Package - ModeDeclaration

Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class ModeDeclarationGroupPrototype(Identifiable):
    """
    The ModeDeclarationGroupPrototype specifies a set of Modes
    (ModeDeclarationGroup) which is provided or required in the given context.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeDeclarationGroupPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 42, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 323, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 113, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2038, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 233, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This allows for specifying whether or not the enclosing
        # ModeDeclarationGroupPrototype can be measured at.
        self._swCalibration: Optional[SwCalibrationAccess] = None

    @property
    def sw_calibration(self) -> Optional[SwCalibrationAccess]:
        """Get swCalibration (Pythonic accessor)."""
        return self._swCalibration

    @sw_calibration.setter
    def sw_calibration(self, value: Optional[SwCalibrationAccess]) -> None:
        """
        Set swCalibration with validation.

        Args:
            value: The swCalibration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalibration = None
            return

        if not isinstance(value, SwCalibrationAccess):
            raise TypeError(
                f"swCalibration must be SwCalibrationAccess or None, got {type(value).__name__}"
            )
        self._swCalibration = value
        self._type: Optional[RefType] = None

    @property
    def type(self) -> Optional[RefType]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional[RefType]) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        self._type = value

    def with_mode_transition(self, value):
        """
        Set mode_transition and return self for chaining.

        Args:
            value: The mode_transition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_transition("value")
        """
        self.mode_transition = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwCalibration(self) -> SwCalibrationAccess:
        """
        AUTOSAR-compliant getter for swCalibration.

        Returns:
            The swCalibration value

        Note:
            Delegates to sw_calibration property (CODING_RULE_V2_00017)
        """
        return self.sw_calibration  # Delegates to property

    def setSwCalibration(self, value: SwCalibrationAccess) -> ModeDeclarationGroupPrototype:
        """
        AUTOSAR-compliant setter for swCalibration with method chaining.

        Args:
            value: The swCalibration to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_calibration property setter (gets validation automatically)
        """
        self.sw_calibration = value  # Delegates to property setter
        return self

    def getType(self) -> RefType:
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: RefType) -> ModeDeclarationGroupPrototype:
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_calibration(self, value: Optional[SwCalibrationAccess]) -> ModeDeclarationGroupPrototype:
        """
        Set swCalibration and return self for chaining.

        Args:
            value: The swCalibration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_calibration("value")
        """
        self.sw_calibration = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: Optional[RefType]) -> ModeDeclarationGroupPrototype:
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self



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
        self._initialMode: Optional[ModeDeclaration] = None

    @property
    def initial_mode(self) -> Optional[ModeDeclaration]:
        """Get initialMode (Pythonic accessor)."""
        return self._initialMode

    @initial_mode.setter
    def initial_mode(self, value: Optional[ModeDeclaration]) -> None:
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
        self._mode: List[ModeDeclaration] = []

    @property
    def mode(self) -> List[ModeDeclaration]:
        """Get mode (Pythonic accessor)."""
        return self._mode
        # This represents the ability to define the error behavior by the mode manager
                # in case of errors on the side (e.
        # g.
        # terminated mode user).
        self._modeManager: Optional[ModeErrorBehavior] = None

    @property
    def mode_manager(self) -> Optional[ModeErrorBehavior]:
        """Get modeManager (Pythonic accessor)."""
        return self._modeManager

    @mode_manager.setter
    def mode_manager(self, value: Optional[ModeErrorBehavior]) -> None:
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
        self._modeTransition: List[ModeTransition] = []

    @property
    def mode_transition(self) -> List[ModeTransition]:
        """Get modeTransition (Pythonic accessor)."""
        return self._modeTransition
        # This represents the definition of the error behavior by the mode user in case
                # of errors on the mode (e.
        # g.
        # terminated mode manager).
        self._modeUserError: Optional[ModeErrorBehavior] = None

    @property
    def mode_user_error(self) -> Optional[ModeErrorBehavior]:
        """Get modeUserError (Pythonic accessor)."""
        return self._modeUserError

    @mode_user_error.setter
    def mode_user_error(self, value: Optional[ModeErrorBehavior]) -> None:
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
        # programmatically representing a for the transition between two statuses.
        self._onTransition: Optional[PositiveInteger] = None

    @property
    def on_transition(self) -> Optional[PositiveInteger]:
        """Get onTransition (Pythonic accessor)."""
        return self._onTransition

    @on_transition.setter
    def on_transition(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"onTransition must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._onTransition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialMode(self) -> ModeDeclaration:
        """
        AUTOSAR-compliant getter for initialMode.

        Returns:
            The initialMode value

        Note:
            Delegates to initial_mode property (CODING_RULE_V2_00017)
        """
        return self.initial_mode  # Delegates to property

    def setInitialMode(self, value: ModeDeclaration) -> ModeDeclarationGroup:
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

    def getMode(self) -> List[ModeDeclaration]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def getModeManager(self) -> ModeErrorBehavior:
        """
        AUTOSAR-compliant getter for modeManager.

        Returns:
            The modeManager value

        Note:
            Delegates to mode_manager property (CODING_RULE_V2_00017)
        """
        return self.mode_manager  # Delegates to property

    def setModeManager(self, value: ModeErrorBehavior) -> ModeDeclarationGroup:
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

    def getModeTransition(self) -> List[ModeTransition]:
        """
        AUTOSAR-compliant getter for modeTransition.

        Returns:
            The modeTransition value

        Note:
            Delegates to mode_transition property (CODING_RULE_V2_00017)
        """
        return self.mode_transition  # Delegates to property

    def getModeUserError(self) -> ModeErrorBehavior:
        """
        AUTOSAR-compliant getter for modeUserError.

        Returns:
            The modeUserError value

        Note:
            Delegates to mode_user_error property (CODING_RULE_V2_00017)
        """
        return self.mode_user_error  # Delegates to property

    def setModeUserError(self, value: ModeErrorBehavior) -> ModeDeclarationGroup:
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

    def getOnTransition(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for onTransition.

        Returns:
            The onTransition value

        Note:
            Delegates to on_transition property (CODING_RULE_V2_00017)
        """
        return self.on_transition  # Delegates to property

    def setOnTransition(self, value: PositiveInteger) -> ModeDeclarationGroup:
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

    def with_initial_mode(self, value: Optional[ModeDeclaration]) -> ModeDeclarationGroup:
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

    def with_mode_manager(self, value: Optional[ModeErrorBehavior]) -> ModeDeclarationGroup:
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

    def with_mode_user_error(self, value: Optional[ModeErrorBehavior]) -> ModeDeclarationGroup:
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

    def with_on_transition(self, value: Optional[PositiveInteger]) -> ModeDeclarationGroup:
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



class ModeDeclaration(Identifiable):
    """
    Declaration of one Mode. The name and semantics of a specific mode is not
    defined in the meta-model.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 43, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 322, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 628, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2038, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 233, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The RTE shall take the value of this attribute for source code representation
        # of this Mode.
        self._value: Optional[PositiveInteger] = None

    @property
    def value(self) -> Optional[PositiveInteger]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional[PositiveInteger]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"value must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: PositiveInteger) -> ModeDeclaration:
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional[PositiveInteger]) -> ModeDeclaration:
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



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
        self._enteredMode: Optional[ModeDeclaration] = None

    @property
    def entered_mode(self) -> Optional[ModeDeclaration]:
        """Get enteredMode (Pythonic accessor)."""
        return self._enteredMode

    @entered_mode.setter
    def entered_mode(self, value: Optional[ModeDeclaration]) -> None:
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
        self._exitedMode: Optional[ModeDeclaration] = None

    @property
    def exited_mode(self) -> Optional[ModeDeclaration]:
        """Get exitedMode (Pythonic accessor)."""
        return self._exitedMode

    @exited_mode.setter
    def exited_mode(self, value: Optional[ModeDeclaration]) -> None:
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

    def getEnteredMode(self) -> ModeDeclaration:
        """
        AUTOSAR-compliant getter for enteredMode.

        Returns:
            The enteredMode value

        Note:
            Delegates to entered_mode property (CODING_RULE_V2_00017)
        """
        return self.entered_mode  # Delegates to property

    def setEnteredMode(self, value: ModeDeclaration) -> ModeTransition:
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

    def getExitedMode(self) -> ModeDeclaration:
        """
        AUTOSAR-compliant getter for exitedMode.

        Returns:
            The exitedMode value

        Note:
            Delegates to exited_mode property (CODING_RULE_V2_00017)
        """
        return self.exited_mode  # Delegates to property

    def setExitedMode(self, value: ModeDeclaration) -> ModeTransition:
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

    def with_entered_mode(self, value: Optional[ModeDeclaration]) -> ModeTransition:
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

    def with_exited_mode(self, value: Optional[ModeDeclaration]) -> ModeTransition:
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
        self._defaultMode: Optional[ModeDeclaration] = None

    @property
    def default_mode(self) -> Optional[ModeDeclaration]:
        """Get defaultMode (Pythonic accessor)."""
        return self._defaultMode

    @default_mode.setter
    def default_mode(self, value: Optional[ModeDeclaration]) -> None:
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

    def getDefaultMode(self) -> ModeDeclaration:
        """
        AUTOSAR-compliant getter for defaultMode.

        Returns:
            The defaultMode value

        Note:
            Delegates to default_mode property (CODING_RULE_V2_00017)
        """
        return self.default_mode  # Delegates to property

    def setDefaultMode(self, value: ModeDeclaration) -> ModeErrorBehavior:
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

    def setErrorReaction(self, value: "ModeErrorReaction") -> ModeErrorBehavior:
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

    def with_default_mode(self, value: Optional[ModeDeclaration]) -> ModeErrorBehavior:
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

    def with_error_reaction(self, value: Optional["ModeErrorReaction"]) -> ModeErrorBehavior:
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



class ModeRequestTypeMap(ARObject):
    """
    Specifies a mapping between a ModeDeclarationGroup and an
    ImplementationDataType. This ImplementationDataType shall be used to
    implement the ModeDeclarationGroup.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeRequestTypeMap

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 44, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 115, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the corresponding AbstractImplementationData Type.
        # It shall be modeled along the idea of an "unsigned type.
        self._implementation: Optional[AbstractImplementation] = None

    @property
    def implementation(self) -> Optional[AbstractImplementation]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional[AbstractImplementation]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"implementation must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._implementation = value
        self._modeGroup: Optional[RefType] = None

    @property
    def mode_group(self) -> Optional[RefType]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional[RefType]) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementation(self) -> AbstractImplementation:
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: AbstractImplementation) -> ModeRequestTypeMap:
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: RefType) -> ModeRequestTypeMap:
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implementation(self, value: Optional[AbstractImplementation]) -> ModeRequestTypeMap:
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_mode_group(self, value: Optional[RefType]) -> ModeRequestTypeMap:
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self



class ModeDeclarationGroupPrototypeMapping(ARObject):
    """
    Defines the mapping of two particular ModeDeclarationGroupPrototypes (in the
    given context) that are unequally named and/or require a reference to a
    ModeDeclarationMappingSet in order to become compatible by definition of
    ModeDeclarationMappings.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeDeclarationGroupPrototypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 130, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ModeDeclarationGroupPrototype to be mapped.
        self._firstModeGroupPrototype: Optional[RefType] = None

    @property
    def first_mode_group_prototype(self) -> Optional[RefType]:
        """Get firstModeGroupPrototype (Pythonic accessor)."""
        return self._firstModeGroupPrototype

    @first_mode_group_prototype.setter
    def first_mode_group_prototype(self, value: Optional[RefType]) -> None:
        """
        Set firstModeGroupPrototype with validation.

        Args:
            value: The firstModeGroupPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstModeGroupPrototype = None
            return

        self._firstModeGroupPrototype = value
        # this ModeDeclarationGroup.
        self._mode: Optional[ModeDeclaration] = None

    @property
    def mode(self) -> Optional[ModeDeclaration]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional[ModeDeclaration]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"mode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._mode = value
        self._secondMode: Optional[RefType] = None

    @property
    def second_mode(self) -> Optional[RefType]:
        """Get secondMode (Pythonic accessor)."""
        return self._secondMode

    @second_mode.setter
    def second_mode(self, value: Optional[RefType]) -> None:
        """
        Set secondMode with validation.

        Args:
            value: The secondMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondMode = None
            return

        self._secondMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstModeGroupPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for firstModeGroupPrototype.

        Returns:
            The firstModeGroupPrototype value

        Note:
            Delegates to first_mode_group_prototype property (CODING_RULE_V2_00017)
        """
        return self.first_mode_group_prototype  # Delegates to property

    def setFirstModeGroupPrototype(self, value: RefType) -> ModeDeclarationGroupPrototypeMapping:
        """
        AUTOSAR-compliant setter for firstModeGroupPrototype with method chaining.

        Args:
            value: The firstModeGroupPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_mode_group_prototype property setter (gets validation automatically)
        """
        self.first_mode_group_prototype = value  # Delegates to property setter
        return self

    def getMode(self) -> ModeDeclaration:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: ModeDeclaration) -> ModeDeclarationGroupPrototypeMapping:
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getSecondMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for secondMode.

        Returns:
            The secondMode value

        Note:
            Delegates to second_mode property (CODING_RULE_V2_00017)
        """
        return self.second_mode  # Delegates to property

    def setSecondMode(self, value: RefType) -> ModeDeclarationGroupPrototypeMapping:
        """
        AUTOSAR-compliant setter for secondMode with method chaining.

        Args:
            value: The secondMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_mode property setter (gets validation automatically)
        """
        self.second_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_mode_group_prototype(self, value: Optional[RefType]) -> ModeDeclarationGroupPrototypeMapping:
        """
        Set firstModeGroupPrototype and return self for chaining.

        Args:
            value: The firstModeGroupPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_mode_group_prototype("value")
        """
        self.first_mode_group_prototype = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[ModeDeclaration]) -> ModeDeclarationGroupPrototypeMapping:
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_second_mode(self, value: Optional[RefType]) -> ModeDeclarationGroupPrototypeMapping:
        """
        Set secondMode and return self for chaining.

        Args:
            value: The secondMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_mode("value")
        """
        self.second_mode = value  # Use property setter (gets validation)
        return self


class ModeErrorReactionPolicyEnum(AREnum):
    """
    ModeErrorReactionPolicyEnum enumeration

This represents the ability to specify the reaction on a mode error. Aggregated by ModeErrorBehavior.errorReactionPolicy

Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration
    """
    # This represents the ability to switch to the defaultMode in case of a mode error.
    defaultMode = "0"

    # This represents the ability to keep the last mode in case of a mode error.
    lastMode = "1"



class ModeActivationKind(AREnum):
    """
    ModeActivationKind enumeration

Kind of mode switch condition used for activation of an event, as further described for each enumeration field. Aggregated by BswModeSwitchEvent.activation, SwcModeSwitchEvent.activation

Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration
    """
    # On entering the referred mode.
    onEntry = "0"

    # On exiting the referred mode.
    onExit = "1"

    # On transition of the 1st referred mode to the 2nd referred mode.
    onTransition = "2"
