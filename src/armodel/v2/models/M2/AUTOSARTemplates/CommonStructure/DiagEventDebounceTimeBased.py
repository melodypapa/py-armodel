from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that the time-based
    pre-debounce algorithm shall be used by the Dem for this diagnostic monitor.
    This is related to set the EcuC choice container DemDebounceAlgorithmClass
    to DemDebounceTime Base.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagEventDebounceTimeBased
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 260, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 198, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 758, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Threshold to allocate an event memory entry and to the Freeze Frame.
        # atpVariation.
        self._timeBasedFdc: Optional["TimeValue"] = None

    @property
    def time_based_fdc(self) -> Optional["TimeValue"]:
        """Get timeBasedFdc (Pythonic accessor)."""
        return self._timeBasedFdc

    @time_based_fdc.setter
    def time_based_fdc(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeBasedFdc with validation.
        
        Args:
            value: The timeBasedFdc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBasedFdc = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBasedFdc must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBasedFdc = value
        # This value represents the event-specific delay indicating "failed" status.
        self._timeFailed: Optional["TimeValue"] = None

    @property
    def time_failed(self) -> Optional["TimeValue"]:
        """Get timeFailed (Pythonic accessor)."""
        return self._timeFailed

    @time_failed.setter
    def time_failed(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeFailed with validation.
        
        Args:
            value: The timeFailed to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeFailed = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeFailed must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeFailed = value
        # This value represents the event-specific delay indicating "passed" status.
        self._timePassed: Optional["TimeValue"] = None

    @property
    def time_passed(self) -> Optional["TimeValue"]:
        """Get timePassed (Pythonic accessor)."""
        return self._timePassed

    @time_passed.setter
    def time_passed(self, value: Optional["TimeValue"]) -> None:
        """
        Set timePassed with validation.
        
        Args:
            value: The timePassed to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timePassed = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timePassed must be TimeValue or None, got {type(value).__name__}"
            )
        self._timePassed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeBasedFdc(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBasedFdc.
        
        Returns:
            The timeBasedFdc value
        
        Note:
            Delegates to time_based_fdc property (CODING_RULE_V2_00017)
        """
        return self.time_based_fdc  # Delegates to property

    def setTimeBasedFdc(self, value: "TimeValue") -> "DiagEventDebounceTimeBased":
        """
        AUTOSAR-compliant setter for timeBasedFdc with method chaining.
        
        Args:
            value: The timeBasedFdc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_based_fdc property setter (gets validation automatically)
        """
        self.time_based_fdc = value  # Delegates to property setter
        return self

    def getTimeFailed(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeFailed.
        
        Returns:
            The timeFailed value
        
        Note:
            Delegates to time_failed property (CODING_RULE_V2_00017)
        """
        return self.time_failed  # Delegates to property

    def setTimeFailed(self, value: "TimeValue") -> "DiagEventDebounceTimeBased":
        """
        AUTOSAR-compliant setter for timeFailed with method chaining.
        
        Args:
            value: The timeFailed to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_failed property setter (gets validation automatically)
        """
        self.time_failed = value  # Delegates to property setter
        return self

    def getTimePassed(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timePassed.
        
        Returns:
            The timePassed value
        
        Note:
            Delegates to time_passed property (CODING_RULE_V2_00017)
        """
        return self.time_passed  # Delegates to property

    def setTimePassed(self, value: "TimeValue") -> "DiagEventDebounceTimeBased":
        """
        AUTOSAR-compliant setter for timePassed with method chaining.
        
        Args:
            value: The timePassed to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_passed property setter (gets validation automatically)
        """
        self.time_passed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_based_fdc(self, value: Optional["TimeValue"]) -> "DiagEventDebounceTimeBased":
        """
        Set timeBasedFdc and return self for chaining.
        
        Args:
            value: The timeBasedFdc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_based_fdc("value")
        """
        self.time_based_fdc = value  # Use property setter (gets validation)
        return self

    def with_time_failed(self, value: Optional["TimeValue"]) -> "DiagEventDebounceTimeBased":
        """
        Set timeFailed and return self for chaining.
        
        Args:
            value: The timeFailed to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_failed("value")
        """
        self.time_failed = value  # Use property setter (gets validation)
        return self

    def with_time_passed(self, value: Optional["TimeValue"]) -> "DiagEventDebounceTimeBased":
        """
        Set timePassed and return self for chaining.
        
        Args:
            value: The timePassed to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_passed("value")
        """
        self.time_passed = value  # Use property setter (gets validation)
        return self