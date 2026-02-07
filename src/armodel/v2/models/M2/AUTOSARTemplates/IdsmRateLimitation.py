from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class IdsmRateLimitation(Identifiable):
    """
    This meta-class represents the configuration of a rate limitation filter for
    security events. This means that security events are dropped if the number
    of events (of any type) processed within a configurable time window is
    greater than a configurable threshold.
    
    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmRateLimitation
    
    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 28, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute configures the threshold for dropping events if the number of
        # all processed security the threshold in the respective time.
        self._maxEventsIn: "PositiveInteger" = None

    @property
    def max_events_in(self) -> "PositiveInteger":
        """Get maxEventsIn (Pythonic accessor)."""
        return self._maxEventsIn

    @max_events_in.setter
    def max_events_in(self, value: "PositiveInteger") -> None:
        """
        Set maxEventsIn with validation.
        
        Args:
            value: The maxEventsIn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxEventsIn must be PositiveInteger, got {type(value).__name__}"
            )
        self._maxEventsIn = value
        # This attribute configures the length of the time interval in dropping
        # security events if the number of all events exceeds the configurable the
        # respective time interval.
        self._timeInterval: "Float" = None

    @property
    def time_interval(self) -> "Float":
        """Get timeInterval (Pythonic accessor)."""
        return self._timeInterval

    @time_interval.setter
    def time_interval(self, value: "Float") -> None:
        """
        Set timeInterval with validation.
        
        Args:
            value: The timeInterval to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Float):
            raise TypeError(
                f"timeInterval must be Float, got {type(value).__name__}"
            )
        self._timeInterval = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxEventsIn(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxEventsIn.
        
        Returns:
            The maxEventsIn value
        
        Note:
            Delegates to max_events_in property (CODING_RULE_V2_00017)
        """
        return self.max_events_in  # Delegates to property

    def setMaxEventsIn(self, value: "PositiveInteger") -> "IdsmRateLimitation":
        """
        AUTOSAR-compliant setter for maxEventsIn with method chaining.
        
        Args:
            value: The maxEventsIn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_events_in property setter (gets validation automatically)
        """
        self.max_events_in = value  # Delegates to property setter
        return self

    def getTimeInterval(self) -> "Float":
        """
        AUTOSAR-compliant getter for timeInterval.
        
        Returns:
            The timeInterval value
        
        Note:
            Delegates to time_interval property (CODING_RULE_V2_00017)
        """
        return self.time_interval  # Delegates to property

    def setTimeInterval(self, value: "Float") -> "IdsmRateLimitation":
        """
        AUTOSAR-compliant setter for timeInterval with method chaining.
        
        Args:
            value: The timeInterval to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_interval property setter (gets validation automatically)
        """
        self.time_interval = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_events_in(self, value: "PositiveInteger") -> "IdsmRateLimitation":
        """
        Set maxEventsIn and return self for chaining.
        
        Args:
            value: The maxEventsIn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_events_in("value")
        """
        self.max_events_in = value  # Use property setter (gets validation)
        return self

    def with_time_interval(self, value: "Float") -> "IdsmRateLimitation":
        """
        Set timeInterval and return self for chaining.
        
        Args:
            value: The timeInterval to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_interval("value")
        """
        self.time_interval = value  # Use property setter (gets validation)
        return self