from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimeSyncClientConfiguration(ARObject):
    """
    Defines the configuration of the time synchronisation client.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TimeSyncClientConfiguration
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 469, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines a list of ordered NetworkEndpoints.
        # xml.
        # namePlural=ORDERED-MASTER-LIST.
        self._orderedMaster: List["OrderedMaster"] = []

    @property
    def ordered_master(self) -> List["OrderedMaster"]:
        """Get orderedMaster (Pythonic accessor)."""
        return self._orderedMaster
        # Defines the time synchronisation technology used.
        self._timeSync: Optional["TimeSyncTechnology"] = None

    @property
    def time_sync(self) -> Optional["TimeSyncTechnology"]:
        """Get timeSync (Pythonic accessor)."""
        return self._timeSync

    @time_sync.setter
    def time_sync(self, value: Optional["TimeSyncTechnology"]) -> None:
        """
        Set timeSync with validation.
        
        Args:
            value: The timeSync to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSync = None
            return

        if not isinstance(value, TimeSyncTechnology):
            raise TypeError(
                f"timeSync must be TimeSyncTechnology or None, got {type(value).__name__}"
            )
        self._timeSync = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOrderedMaster(self) -> List["OrderedMaster"]:
        """
        AUTOSAR-compliant getter for orderedMaster.
        
        Returns:
            The orderedMaster value
        
        Note:
            Delegates to ordered_master property (CODING_RULE_V2_00017)
        """
        return self.ordered_master  # Delegates to property

    def getTimeSync(self) -> "TimeSyncTechnology":
        """
        AUTOSAR-compliant getter for timeSync.
        
        Returns:
            The timeSync value
        
        Note:
            Delegates to time_sync property (CODING_RULE_V2_00017)
        """
        return self.time_sync  # Delegates to property

    def setTimeSync(self, value: "TimeSyncTechnology") -> "TimeSyncClientConfiguration":
        """
        AUTOSAR-compliant setter for timeSync with method chaining.
        
        Args:
            value: The timeSync to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_sync property setter (gets validation automatically)
        """
        self.time_sync = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_sync(self, value: Optional["TimeSyncTechnology"]) -> "TimeSyncClientConfiguration":
        """
        Set timeSync and return self for chaining.
        
        Args:
            value: The timeSync to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_sync("value")
        """
        self.time_sync = value  # Use property setter (gets validation)
        return self