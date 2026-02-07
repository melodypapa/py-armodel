from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class BswModeSwitchEvent(BswScheduleEvent):
    """
    A BswEvent resulting from a mode switch.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSwitchEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 94, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Kind of activation w.
        # r.
        # t.
        # to the referred mode.
        # ModeDeclaration 0.
        # 2 iref Reference to one or two Modes that initiate the Mode by:
                # ModeInBswModule.
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

    def setActivation(self, value: "ModeActivationKind") -> "BswModeSwitchEvent":
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

    def with_activation(self, value: Optional["ModeActivationKind"]) -> "BswModeSwitchEvent":
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