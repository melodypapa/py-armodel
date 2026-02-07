from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CycleRepetition(CommunicationCycle):
    """
    The communication cycle where the frame is send is described by the
    attributes baseCycle and cycle Repetition. (cid:53) 424 of 2090 Document ID
    63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology::CycleRepetition
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 424, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The first communication cycle where the frame is sent.
        # is incremented at the beginning of each new from 0 to 63, and is reset to 0
                # after a 64 cycles.
        self._BaseCycle: Optional["Integer"] = None

    @property
    def base_cycle(self) -> Optional["Integer"]:
        """Get BaseCycle (Pythonic accessor)."""
        return self._BaseCycle

    @base_cycle.setter
    def base_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set BaseCycle with validation.
        
        Args:
            value: The BaseCycle to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._BaseCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"BaseCycle must be Integer or None, got {type(value).__name__}"
            )
        self._BaseCycle = value
        # The number of communication cycles (after the first cycle) frame described by
        # this timing is sent again.
        self._CycleRepetition: Optional["CycleRepetitionType"] = None

    @property
    def cycle_repetition(self) -> Optional["CycleRepetitionType"]:
        """Get CycleRepetition (Pythonic accessor)."""
        return self._CycleRepetition

    @cycle_repetition.setter
    def cycle_repetition(self, value: Optional["CycleRepetitionType"]) -> None:
        """
        Set CycleRepetition with validation.
        
        Args:
            value: The CycleRepetition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._CycleRepetition = None
            return

        if not isinstance(value, CycleRepetitionType):
            raise TypeError(
                f"CycleRepetition must be CycleRepetitionType or None, got {type(value).__name__}"
            )
        self._CycleRepetition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for BaseCycle.
        
        Returns:
            The BaseCycle value
        
        Note:
            Delegates to base_cycle property (CODING_RULE_V2_00017)
        """
        return self.base_cycle  # Delegates to property

    def setBaseCycle(self, value: "Integer") -> "CycleRepetition":
        """
        AUTOSAR-compliant setter for BaseCycle with method chaining.
        
        Args:
            value: The BaseCycle to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base_cycle property setter (gets validation automatically)
        """
        self.base_cycle = value  # Delegates to property setter
        return self

    def getCycleRepetition(self) -> "CycleRepetitionType":
        """
        AUTOSAR-compliant getter for CycleRepetition.
        
        Returns:
            The CycleRepetition value
        
        Note:
            Delegates to cycle_repetition property (CODING_RULE_V2_00017)
        """
        return self.cycle_repetition  # Delegates to property

    def setCycleRepetition(self, value: "CycleRepetitionType") -> "CycleRepetition":
        """
        AUTOSAR-compliant setter for CycleRepetition with method chaining.
        
        Args:
            value: The CycleRepetition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cycle_repetition property setter (gets validation automatically)
        """
        self.cycle_repetition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_cycle(self, value: Optional["Integer"]) -> "CycleRepetition":
        """
        Set BaseCycle and return self for chaining.
        
        Args:
            value: The BaseCycle to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base_cycle("value")
        """
        self.base_cycle = value  # Use property setter (gets validation)
        return self

    def with_cycle_repetition(self, value: Optional["CycleRepetitionType"]) -> "CycleRepetition":
        """
        Set CycleRepetition and return self for chaining.
        
        Args:
            value: The CycleRepetition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cycle_repetition("value")
        """
        self.cycle_repetition = value  # Use property setter (gets validation)
        return self