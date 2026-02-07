from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class LinSporadicFrame(LinFrame):
    """
    A sporadic frame is a group of unconditional frames that share the same
    frame slot. The sporadic frame shall not contain any Pdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::LinSporadicFrame
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 429, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a group of unconditional frames that share the same frame slot.
        # In case that more than one of the needs to be transferred, the one first be
                # chosen.
        # channel a LIN Frame shall be referenced by only This allows a derivation of
                # the a substituted Frame.
        # The identifier is specified element.
        # associated with a LinSporadic not be allocated in the same LinSchedule.
        self._substituted: List["LinUnconditionalFrame"] = []

    @property
    def substituted(self) -> List["LinUnconditionalFrame"]:
        """Get substituted (Pythonic accessor)."""
        return self._substituted

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubstituted(self) -> List["LinUnconditionalFrame"]:
        """
        AUTOSAR-compliant getter for substituted.
        
        Returns:
            The substituted value
        
        Note:
            Delegates to substituted property (CODING_RULE_V2_00017)
        """
        return self.substituted  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====