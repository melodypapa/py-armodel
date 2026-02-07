from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class BswEvent(AbstractEvent, ABC):
    """
    Base class of various kinds of events which are used to trigger a
    BswModuleEntity of this BSW module or cluster. The event is local to the BSW
    module or cluster. The short name of the meta-class instance is intended as
    an input to configure the required API of the BSW Scheduler.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 87, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 206, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswEvent:
            raise TypeError("BswEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this reference indicates that the usage of the event is
        # limited to the context of the referred Bsw.
        self._context: List["BswDistinguished"] = []

    @property
    def context(self) -> List["BswDistinguished"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # by: ModeInBswModule.
        self._disabledInModeDescriptionInstanceRef: List["ModeDeclaration"] = []

    @property
    def disabled_in_mode_description_instance_ref(self) -> List["ModeDeclaration"]:
        """Get disabledInModeDescriptionInstanceRef (Pythonic accessor)."""
        return self._disabledInModeDescriptionInstanceRef
        # The entity which is started by the event.
        self._startsOnEvent: Optional["BswModuleEntity"] = None

    @property
    def starts_on_event(self) -> Optional["BswModuleEntity"]:
        """Get startsOnEvent (Pythonic accessor)."""
        return self._startsOnEvent

    @starts_on_event.setter
    def starts_on_event(self, value: Optional["BswModuleEntity"]) -> None:
        """
        Set startsOnEvent with validation.
        
        Args:
            value: The startsOnEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startsOnEvent = None
            return

        if not isinstance(value, BswModuleEntity):
            raise TypeError(
                f"startsOnEvent must be BswModuleEntity or None, got {type(value).__name__}"
            )
        self._startsOnEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getDisabledInModeDescriptionInstanceRef(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for disabledInModeDescriptionInstanceRef.
        
        Returns:
            The disabledInModeDescriptionInstanceRef value
        
        Note:
            Delegates to disabled_in_mode_description_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.disabled_in_mode_description_instance_ref  # Delegates to property

    def getStartsOnEvent(self) -> "BswModuleEntity":
        """
        AUTOSAR-compliant getter for startsOnEvent.
        
        Returns:
            The startsOnEvent value
        
        Note:
            Delegates to starts_on_event property (CODING_RULE_V2_00017)
        """
        return self.starts_on_event  # Delegates to property

    def setStartsOnEvent(self, value: "BswModuleEntity") -> "BswEvent":
        """
        AUTOSAR-compliant setter for startsOnEvent with method chaining.
        
        Args:
            value: The startsOnEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to starts_on_event property setter (gets validation automatically)
        """
        self.starts_on_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_starts_on_event(self, value: Optional["BswModuleEntity"]) -> "BswEvent":
        """
        Set startsOnEvent and return self for chaining.
        
        Args:
            value: The startsOnEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_starts_on_event("value")
        """
        self.starts_on_event = value  # Use property setter (gets validation)
        return self