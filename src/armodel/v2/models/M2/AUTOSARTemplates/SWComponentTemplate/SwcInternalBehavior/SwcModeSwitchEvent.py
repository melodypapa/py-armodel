from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ModeActivationKind,
    RTEEvent,
)


class SwcModeSwitchEvent(RTEEvent):
    """
    This event is raised when the specified mode change occurs.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::SwcModeSwitchEvent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 544, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if the event is raised on entering or exiting a or is raised on the
                # transition between two ModeDeclaration 0.
        # 2 iref The referenced mode or the transition between two this
                # SwcModeSwitchEvent.
        # by: RModeInAtomicSwc.
        self._activation: Optional["ModeActivationKind"] = None

    @property
    def activation(self) -> Optional["ModeActivationKind"]:
        """Get activation (Pythonic accessor)."""
        return self._activation

    @activation.setter
    def activation(self, value: Optional["ModeActivationKind"]) -> None:
        """
        Set activation with validation.

        Args:
            value: The activation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._activation = None
            return

        if not isinstance(value, ModeActivationKind):
            raise TypeError(
                f"activation must be ModeActivationKind or None, got {type(value).__name__}"
            )
        self._activation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivation(self) -> "ModeActivationKind":
        """
        AUTOSAR-compliant getter for activation.

        Returns:
            The activation value

        Note:
            Delegates to activation property (CODING_RULE_V2_00017)
        """
        return self.activation  # Delegates to property

    def setActivation(self, value: "ModeActivationKind") -> "SwcModeSwitchEvent":
        """
        AUTOSAR-compliant setter for activation with method chaining.

        Args:
            value: The activation to set

        Returns:
            self for method chaining

        Note:
            Delegates to activation property setter (gets validation automatically)
        """
        self.activation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_activation(self, value: Optional["ModeActivationKind"]) -> "SwcModeSwitchEvent":
        """
        Set activation and return self for chaining.

        Args:
            value: The activation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_activation("value")
        """
        self.activation = value  # Use property setter (gets validation)
        return self
