from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IPduTiming(Describable):
    """
    AUTOSAR COM provides the possibility to define two different TRANSMISSION
    MODES for each IPdu. The Transmission Mode of an IPdu that is valid at a
    specific point in time is selected using the values of the signals that are
    mapped to this IPdu. For each IPdu a Transmission Mode Selector is defined.
    The Transmission Mode Selector is calculated by evaluating the conditions
    for a subset of signals (class TransmissionModeCondition in the System
    Template). The Transmission Mode Selector is defined to be true, if at least
    one Condition evaluates to true and is defined to be false, if all
    Conditions evaluate to false.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::IPduTiming
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 348, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Minimum Delay in seconds between successive this I-PDU, independent of the.
        self._minimumDelay: Optional["TimeValue"] = None

    @property
    def minimum_delay(self) -> Optional["TimeValue"]:
        """Get minimumDelay (Pythonic accessor)."""
        return self._minimumDelay

    @minimum_delay.setter
    def minimum_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimumDelay with validation.
        
        Args:
            value: The minimumDelay to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimumDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimumDelay = value
        # AUTOSAR COM allows configuring statically two different transmission modes
                # for each I-PDU (True and False).
        # The Mode Selector evaluates the conditions for of signals and decides the
                # transmission mode.
        # It to switch between the transmission modes.
        self._transmission: Optional["TransmissionMode"] = None

    @property
    def transmission(self) -> Optional["TransmissionMode"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TransmissionMode"]) -> None:
        """
        Set transmission with validation.
        
        Args:
            value: The transmission to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TransmissionMode):
            raise TypeError(
                f"transmission must be TransmissionMode or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMinimumDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimumDelay.
        
        Returns:
            The minimumDelay value
        
        Note:
            Delegates to minimum_delay property (CODING_RULE_V2_00017)
        """
        return self.minimum_delay  # Delegates to property

    def setMinimumDelay(self, value: "TimeValue") -> "IPduTiming":
        """
        AUTOSAR-compliant setter for minimumDelay with method chaining.
        
        Args:
            value: The minimumDelay to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_delay property setter (gets validation automatically)
        """
        self.minimum_delay = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "TransmissionMode":
        """
        AUTOSAR-compliant getter for transmission.
        
        Returns:
            The transmission value
        
        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionMode") -> "IPduTiming":
        """
        AUTOSAR-compliant setter for transmission with method chaining.
        
        Args:
            value: The transmission to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_minimum_delay(self, value: Optional["TimeValue"]) -> "IPduTiming":
        """
        Set minimumDelay and return self for chaining.
        
        Args:
            value: The minimumDelay to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_delay("value")
        """
        self.minimum_delay = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["TransmissionMode"]) -> "IPduTiming":
        """
        Set transmission and return self for chaining.
        
        Args:
            value: The transmission to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self