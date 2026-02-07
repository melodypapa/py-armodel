from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class TDEventModeDeclaration(TDEventVfbPort):
    """
    This is used to describe timing events related to mode switch communication
    at VFB level.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventModeDeclaration
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 57, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional parameter which refines the scope of the If the parameter is set,
        # the only if the mode declaration group prototype enter into the referenced
        # ModeDeclaration.
        self._entryMode: Optional["ModeDeclaration"] = None

    @property
    def entry_mode(self) -> Optional["ModeDeclaration"]:
        """Get entryMode (Pythonic accessor)."""
        return self._entryMode

    @entry_mode.setter
    def entry_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set entryMode with validation.
        
        Args:
            value: The entryMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._entryMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"entryMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._entryMode = value
        # Optional parameter which refines the scope of the If the parameter is set,
        # the only if the mode declaration group prototype exit from the referenced
        # ModeDeclaration.
        self._exitMode: Optional["ModeDeclaration"] = None

    @property
    def exit_mode(self) -> Optional["ModeDeclaration"]:
        """Get exitMode (Pythonic accessor)."""
        return self._exitMode

    @exit_mode.setter
    def exit_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set exitMode with validation.
        
        Args:
            value: The exitMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exitMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"exitMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._exitMode = value
        # The referenced mode declaration group prototype.
        self._mode: RefType = None

    @property
    def mode(self) -> RefType:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: RefType) -> None:
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

        self._mode = value
        # The specific type of this timing event.
        self._tdEventMode: Optional["TDEventMode"] = None

    @property
    def td_event_mode(self) -> Optional["TDEventMode"]:
        """Get tdEventMode (Pythonic accessor)."""
        return self._tdEventMode

    @td_event_mode.setter
    def td_event_mode(self, value: Optional["TDEventMode"]) -> None:
        """
        Set tdEventMode with validation.
        
        Args:
            value: The tdEventMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventMode = None
            return

        if not isinstance(value, TDEventMode):
            raise TypeError(
                f"tdEventMode must be TDEventMode or None, got {type(value).__name__}"
            )
        self._tdEventMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntryMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for entryMode.
        
        Returns:
            The entryMode value
        
        Note:
            Delegates to entry_mode property (CODING_RULE_V2_00017)
        """
        return self.entry_mode  # Delegates to property

    def setEntryMode(self, value: "ModeDeclaration") -> "TDEventModeDeclaration":
        """
        AUTOSAR-compliant setter for entryMode with method chaining.
        
        Args:
            value: The entryMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to entry_mode property setter (gets validation automatically)
        """
        self.entry_mode = value  # Delegates to property setter
        return self

    def getExitMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for exitMode.
        
        Returns:
            The exitMode value
        
        Note:
            Delegates to exit_mode property (CODING_RULE_V2_00017)
        """
        return self.exit_mode  # Delegates to property

    def setExitMode(self, value: "ModeDeclaration") -> "TDEventModeDeclaration":
        """
        AUTOSAR-compliant setter for exitMode with method chaining.
        
        Args:
            value: The exitMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to exit_mode property setter (gets validation automatically)
        """
        self.exit_mode = value  # Delegates to property setter
        return self

    def getMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for mode.
        
        Returns:
            The mode value
        
        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: RefType) -> "TDEventModeDeclaration":
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

    def getTdEventMode(self) -> "TDEventMode":
        """
        AUTOSAR-compliant getter for tdEventMode.
        
        Returns:
            The tdEventMode value
        
        Note:
            Delegates to td_event_mode property (CODING_RULE_V2_00017)
        """
        return self.td_event_mode  # Delegates to property

    def setTdEventMode(self, value: "TDEventMode") -> "TDEventModeDeclaration":
        """
        AUTOSAR-compliant setter for tdEventMode with method chaining.
        
        Args:
            value: The tdEventMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to td_event_mode property setter (gets validation automatically)
        """
        self.td_event_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entry_mode(self, value: Optional["ModeDeclaration"]) -> "TDEventModeDeclaration":
        """
        Set entryMode and return self for chaining.
        
        Args:
            value: The entryMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_entry_mode("value")
        """
        self.entry_mode = value  # Use property setter (gets validation)
        return self

    def with_exit_mode(self, value: Optional["ModeDeclaration"]) -> "TDEventModeDeclaration":
        """
        Set exitMode and return self for chaining.
        
        Args:
            value: The exitMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_exit_mode("value")
        """
        self.exit_mode = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[RefType]) -> "TDEventModeDeclaration":
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

    def with_td_event_mode(self, value: Optional["TDEventMode"]) -> "TDEventModeDeclaration":
        """
        Set tdEventMode and return self for chaining.
        
        Args:
            value: The tdEventMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_td_event_mode("value")
        """
        self.td_event_mode = value  # Use property setter (gets validation)
        return self