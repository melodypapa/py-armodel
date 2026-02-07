from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class FlexrayNmClusterCoupling(NmClusterCoupling):
    """
    FlexRay attributes that are valid for each of the referenced (coupled)
    FlexRay clusters.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::FlexrayNmClusterCoupling
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 679, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to coupled FlexRay Clusters.
        self._coupledCluster: List["FlexrayNmCluster"] = []

    @property
    def coupled_cluster(self) -> List["FlexrayNmCluster"]:
        """Get coupledCluster (Pythonic accessor)."""
        return self._coupledCluster
        # FrNm schedule variant according to FrNm SWS.
        self._nmSchedule: Optional["FlexrayNmSchedule"] = None

    @property
    def nm_schedule(self) -> Optional["FlexrayNmSchedule"]:
        """Get nmSchedule (Pythonic accessor)."""
        return self._nmSchedule

    @nm_schedule.setter
    def nm_schedule(self, value: Optional["FlexrayNmSchedule"]) -> None:
        """
        Set nmSchedule with validation.
        
        Args:
            value: The nmSchedule to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmSchedule = None
            return

        if not isinstance(value, FlexrayNmSchedule):
            raise TypeError(
                f"nmSchedule must be FlexrayNmSchedule or None, got {type(value).__name__}"
            )
        self._nmSchedule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCoupledCluster(self) -> List["FlexrayNmCluster"]:
        """
        AUTOSAR-compliant getter for coupledCluster.
        
        Returns:
            The coupledCluster value
        
        Note:
            Delegates to coupled_cluster property (CODING_RULE_V2_00017)
        """
        return self.coupled_cluster  # Delegates to property

    def getNmSchedule(self) -> "FlexrayNmSchedule":
        """
        AUTOSAR-compliant getter for nmSchedule.
        
        Returns:
            The nmSchedule value
        
        Note:
            Delegates to nm_schedule property (CODING_RULE_V2_00017)
        """
        return self.nm_schedule  # Delegates to property

    def setNmSchedule(self, value: "FlexrayNmSchedule") -> "FlexrayNmClusterCoupling":
        """
        AUTOSAR-compliant setter for nmSchedule with method chaining.
        
        Args:
            value: The nmSchedule to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nm_schedule property setter (gets validation automatically)
        """
        self.nm_schedule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_schedule(self, value: Optional["FlexrayNmSchedule"]) -> "FlexrayNmClusterCoupling":
        """
        Set nmSchedule and return self for chaining.
        
        Args:
            value: The nmSchedule to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nm_schedule("value")
        """
        self.nm_schedule = value  # Use property setter (gets validation)
        return self