from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EventControlledTiming(Describable):
    """
    Specification of a event driven sending behavior. The PDU is sent n
    (numberOfRepeat + 1) times separated by the repetitionPeriod. If
    numberOfRepeats = 0, then the Pdu is sent just once.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::EventControlledTiming
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 397, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the number of repetitions for the Direct/N-Times mode and the event
        # driven part of Mixed.
        self._numberOf: Optional["Integer"] = None

    @property
    def number_of(self) -> Optional["Integer"]:
        """Get numberOf (Pythonic accessor)."""
        return self._numberOf

    @number_of.setter
    def number_of(self, value: Optional["Integer"]) -> None:
        """
        Set numberOf with validation.
        
        Args:
            value: The numberOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOf = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"numberOf must be Integer or None, got {type(value).__name__}"
            )
        self._numberOf = value
        # The repetitionPeriod specifies the time in seconds that the pdu can be sent
                # the next time gap between two pdus).
        # The repetition optional in case that no repetitions are.
        self._repetitionPeriod: Optional["TimeRangeType"] = None

    @property
    def repetition_period(self) -> Optional["TimeRangeType"]:
        """Get repetitionPeriod (Pythonic accessor)."""
        return self._repetitionPeriod

    @repetition_period.setter
    def repetition_period(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set repetitionPeriod with validation.
        
        Args:
            value: The repetitionPeriod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._repetitionPeriod = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"repetitionPeriod must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._repetitionPeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNumberOf(self) -> "Integer":
        """
        AUTOSAR-compliant getter for numberOf.
        
        Returns:
            The numberOf value
        
        Note:
            Delegates to number_of property (CODING_RULE_V2_00017)
        """
        return self.number_of  # Delegates to property

    def setNumberOf(self, value: "Integer") -> "EventControlledTiming":
        """
        AUTOSAR-compliant setter for numberOf with method chaining.
        
        Args:
            value: The numberOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to number_of property setter (gets validation automatically)
        """
        self.number_of = value  # Delegates to property setter
        return self

    def getRepetitionPeriod(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for repetitionPeriod.
        
        Returns:
            The repetitionPeriod value
        
        Note:
            Delegates to repetition_period property (CODING_RULE_V2_00017)
        """
        return self.repetition_period  # Delegates to property

    def setRepetitionPeriod(self, value: "TimeRangeType") -> "EventControlledTiming":
        """
        AUTOSAR-compliant setter for repetitionPeriod with method chaining.
        
        Args:
            value: The repetitionPeriod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to repetition_period property setter (gets validation automatically)
        """
        self.repetition_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_number_of(self, value: Optional["Integer"]) -> "EventControlledTiming":
        """
        Set numberOf and return self for chaining.
        
        Args:
            value: The numberOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_number_of("value")
        """
        self.number_of = value  # Use property setter (gets validation)
        return self

    def with_repetition_period(self, value: Optional["TimeRangeType"]) -> "EventControlledTiming":
        """
        Set repetitionPeriod and return self for chaining.
        
        Args:
            value: The repetitionPeriod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_repetition_period("value")
        """
        self.repetition_period = value  # Use property setter (gets validation)
        return self