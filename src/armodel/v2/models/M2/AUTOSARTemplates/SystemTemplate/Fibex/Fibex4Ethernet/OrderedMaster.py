from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class OrderedMaster(ARObject):
    """
    Element in the network endpoint list.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::OrderedMaster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 470, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the order of the network endpoint list (e.
        # g.
        # 0, 1, 2,.
        self._index: Optional["PositiveInteger"] = None

    @property
    def index(self) -> Optional["PositiveInteger"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set index with validation.
        
        Args:
            value: The index to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"index must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._index = value
        # Reference to a master (Time Sync Server).
        self._timeSyncServerConfiguration: Optional["TimeSyncServer"] = None

    @property
    def time_sync_server_configuration(self) -> Optional["TimeSyncServer"]:
        """Get timeSyncServerConfiguration (Pythonic accessor)."""
        return self._timeSyncServerConfiguration

    @time_sync_server_configuration.setter
    def time_sync_server_configuration(self, value: Optional["TimeSyncServer"]) -> None:
        """
        Set timeSyncServerConfiguration with validation.
        
        Args:
            value: The timeSyncServerConfiguration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncServerConfiguration = None
            return

        if not isinstance(value, TimeSyncServer):
            raise TypeError(
                f"timeSyncServerConfiguration must be TimeSyncServer or None, got {type(value).__name__}"
            )
        self._timeSyncServerConfiguration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for index.
        
        Returns:
            The index value
        
        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "PositiveInteger") -> "OrderedMaster":
        """
        AUTOSAR-compliant setter for index with method chaining.
        
        Args:
            value: The index to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    def getTimeSyncServerConfiguration(self) -> "TimeSyncServer":
        """
        AUTOSAR-compliant getter for timeSyncServerConfiguration.
        
        Returns:
            The timeSyncServerConfiguration value
        
        Note:
            Delegates to time_sync_server_configuration property (CODING_RULE_V2_00017)
        """
        return self.time_sync_server_configuration  # Delegates to property

    def setTimeSyncServerConfiguration(self, value: "TimeSyncServer") -> "OrderedMaster":
        """
        AUTOSAR-compliant setter for timeSyncServerConfiguration with method chaining.
        
        Args:
            value: The timeSyncServerConfiguration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_sync_server_configuration property setter (gets validation automatically)
        """
        self.time_sync_server_configuration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional["PositiveInteger"]) -> "OrderedMaster":
        """
        Set index and return self for chaining.
        
        Args:
            value: The index to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

    def with_time_sync_server_configuration(self, value: Optional["TimeSyncServer"]) -> "OrderedMaster":
        """
        Set timeSyncServerConfiguration and return self for chaining.
        
        Args:
            value: The timeSyncServerConfiguration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_sync_server_configuration("value")
        """
        self.time_sync_server_configuration = value  # Use property setter (gets validation)
        return self