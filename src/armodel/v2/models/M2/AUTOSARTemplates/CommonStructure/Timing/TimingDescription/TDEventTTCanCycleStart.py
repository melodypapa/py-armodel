from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TDEventTTCanCycleStart(TDEventCycleStart):
    """
    This is used to describe the timing event related to a point in time where a
    communication cycle starts on a TTCAN cluster.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventTTCanCycleStart
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 72, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._ttCanCluster: Optional["TtcanCluster"] = None

    @property
    def tt_can_cluster(self) -> Optional["TtcanCluster"]:
        """Get ttCanCluster (Pythonic accessor)."""
        return self._ttCanCluster

    @tt_can_cluster.setter
    def tt_can_cluster(self, value: Optional["TtcanCluster"]) -> None:
        """
        Set ttCanCluster with validation.
        
        Args:
            value: The ttCanCluster to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ttCanCluster = None
            return

        if not isinstance(value, TtcanCluster):
            raise TypeError(
                f"ttCanCluster must be TtcanCluster or None, got {type(value).__name__}"
            )
        self._ttCanCluster = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTtCanCluster(self) -> "TtcanCluster":
        """
        AUTOSAR-compliant getter for ttCanCluster.
        
        Returns:
            The ttCanCluster value
        
        Note:
            Delegates to tt_can_cluster property (CODING_RULE_V2_00017)
        """
        return self.tt_can_cluster  # Delegates to property

    def setTtCanCluster(self, value: "TtcanCluster") -> "TDEventTTCanCycleStart":
        """
        AUTOSAR-compliant setter for ttCanCluster with method chaining.
        
        Args:
            value: The ttCanCluster to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tt_can_cluster property setter (gets validation automatically)
        """
        self.tt_can_cluster = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tt_can_cluster(self, value: Optional["TtcanCluster"]) -> "TDEventTTCanCycleStart":
        """
        Set ttCanCluster and return self for chaining.
        
        Args:
            value: The ttCanCluster to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tt_can_cluster("value")
        """
        self.tt_can_cluster = value  # Use property setter (gets validation)
        return self