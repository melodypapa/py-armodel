from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SynchronizationPointConstraint(TimingConstraint):
    """
    Specifies a synchronization point either between groups of ExecutableEntitys
    or individual ExecutableEntitys referenced via their corresponding RTE or
    BSW events.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationPointConstraint::SynchronizationPointConstraint
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 132, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The source executable entities cluster containing the entities that shall
        # finish execution before the.
        self._sourceEec: List["EOCExecutableEntity"] = []

    @property
    def source_eec(self) -> List["EOCExecutableEntity"]:
        """Get sourceEec (Pythonic accessor)."""
        return self._sourceEec
        # The executable entities — referenced by their events — finish execution
        # before the synchronization.
        self._sourceEvent: List["AbstractEvent"] = []

    @property
    def source_event(self) -> List["AbstractEvent"]:
        """Get sourceEvent (Pythonic accessor)."""
        return self._sourceEvent
        # The target executable entities cluster containing the entities that shall
        # start execution after the.
        self._targetEec: List["EOCExecutableEntity"] = []

    @property
    def target_eec(self) -> List["EOCExecutableEntity"]:
        """Get targetEec (Pythonic accessor)."""
        return self._targetEec
        # The executable entities — referenced by their events — start execution after
        # the synchronization point.
        self._targetEvent: List["AbstractEvent"] = []

    @property
    def target_event(self) -> List["AbstractEvent"]:
        """Get targetEvent (Pythonic accessor)."""
        return self._targetEvent

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSourceEec(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for sourceEec.
        
        Returns:
            The sourceEec value
        
        Note:
            Delegates to source_eec property (CODING_RULE_V2_00017)
        """
        return self.source_eec  # Delegates to property

    def getSourceEvent(self) -> List["AbstractEvent"]:
        """
        AUTOSAR-compliant getter for sourceEvent.
        
        Returns:
            The sourceEvent value
        
        Note:
            Delegates to source_event property (CODING_RULE_V2_00017)
        """
        return self.source_event  # Delegates to property

    def getTargetEec(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for targetEec.
        
        Returns:
            The targetEec value
        
        Note:
            Delegates to target_eec property (CODING_RULE_V2_00017)
        """
        return self.target_eec  # Delegates to property

    def getTargetEvent(self) -> List["AbstractEvent"]:
        """
        AUTOSAR-compliant getter for targetEvent.
        
        Returns:
            The targetEvent value
        
        Note:
            Delegates to target_event property (CODING_RULE_V2_00017)
        """
        return self.target_event  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====