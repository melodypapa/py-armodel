from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimeSynchronization(ARObject):
    """
    Defines the servers / clients in a time synchronised network.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TimeSynchronization
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 469, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration of the time synchronisation client.
        self._timeSyncClientConfiguration: Optional["TimeSyncClient"] = None

    @property
    def time_sync_client_configuration(self) -> Optional["TimeSyncClient"]:
        """Get timeSyncClientConfiguration (Pythonic accessor)."""
        return self._timeSyncClientConfiguration

    @time_sync_client_configuration.setter
    def time_sync_client_configuration(self, value: Optional["TimeSyncClient"]) -> None:
        """
        Set timeSyncClientConfiguration with validation.
        
        Args:
            value: The timeSyncClientConfiguration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncClientConfiguration = None
            return

        if not isinstance(value, TimeSyncClient):
            raise TypeError(
                f"timeSyncClientConfiguration must be TimeSyncClient or None, got {type(value).__name__}"
            )
        self._timeSyncClientConfiguration = value
        # Configuration of the time synchronisation server.
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

    def getTimeSyncClientConfiguration(self) -> "TimeSyncClient":
        """
        AUTOSAR-compliant getter for timeSyncClientConfiguration.
        
        Returns:
            The timeSyncClientConfiguration value
        
        Note:
            Delegates to time_sync_client_configuration property (CODING_RULE_V2_00017)
        """
        return self.time_sync_client_configuration  # Delegates to property

    def setTimeSyncClientConfiguration(self, value: "TimeSyncClient") -> "TimeSynchronization":
        """
        AUTOSAR-compliant setter for timeSyncClientConfiguration with method chaining.
        
        Args:
            value: The timeSyncClientConfiguration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_sync_client_configuration property setter (gets validation automatically)
        """
        self.time_sync_client_configuration = value  # Delegates to property setter
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

    def setTimeSyncServerConfiguration(self, value: "TimeSyncServer") -> "TimeSynchronization":
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

    def with_time_sync_client_configuration(self, value: Optional["TimeSyncClient"]) -> "TimeSynchronization":
        """
        Set timeSyncClientConfiguration and return self for chaining.
        
        Args:
            value: The timeSyncClientConfiguration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_sync_client_configuration("value")
        """
        self.time_sync_client_configuration = value  # Use property setter (gets validation)
        return self

    def with_time_sync_server_configuration(self, value: Optional["TimeSyncServer"]) -> "TimeSynchronization":
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