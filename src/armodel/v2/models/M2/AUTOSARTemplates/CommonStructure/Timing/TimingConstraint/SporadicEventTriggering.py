from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SporadicEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event which occurs occasionally or singularly.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::SporadicEventTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 105, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum devation of the sporadic event occurrence.
        # - standardPeriod|.
        self._jitter: Optional["MultidimensionalTime"] = None

    @property
    def jitter(self) -> Optional["MultidimensionalTime"]:
        """Get jitter (Pythonic accessor)."""
        return self._jitter

    @jitter.setter
    def jitter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set jitter with validation.
        
        Args:
            value: The jitter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._jitter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"jitter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._jitter = value
        # The maximum time distance between two consecutive occurrences of the
        # associated event.
        self._maximumInter: Optional["MultidimensionalTime"] = None

    @property
    def maximum_inter(self) -> Optional["MultidimensionalTime"]:
        """Get maximumInter (Pythonic accessor)."""
        return self._maximumInter

    @maximum_inter.setter
    def maximum_inter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximumInter with validation.
        
        Args:
            value: The maximumInter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumInter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximumInter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximumInter = value
        # The minimum time distance between two consecutive occurrences of the
        # associated event.
        self._minimumInter: Optional["MultidimensionalTime"] = None

    @property
    def minimum_inter(self) -> Optional["MultidimensionalTime"]:
        """Get minimumInter (Pythonic accessor)."""
        return self._minimumInter

    @minimum_inter.setter
    def minimum_inter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimumInter with validation.
        
        Args:
            value: The minimumInter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumInter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimumInter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimumInter = value
        # The periodic distance between subsequent occurrences event.
        self._period: Optional["MultidimensionalTime"] = None

    @property
    def period(self) -> Optional["MultidimensionalTime"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set period with validation.
        
        Args:
            value: The period to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"period must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._period = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getJitter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for jitter.
        
        Returns:
            The jitter value
        
        Note:
            Delegates to jitter property (CODING_RULE_V2_00017)
        """
        return self.jitter  # Delegates to property

    def setJitter(self, value: "MultidimensionalTime") -> "SporadicEventTriggering":
        """
        AUTOSAR-compliant setter for jitter with method chaining.
        
        Args:
            value: The jitter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to jitter property setter (gets validation automatically)
        """
        self.jitter = value  # Delegates to property setter
        return self

    def getMaximumInter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximumInter.
        
        Returns:
            The maximumInter value
        
        Note:
            Delegates to maximum_inter property (CODING_RULE_V2_00017)
        """
        return self.maximum_inter  # Delegates to property

    def setMaximumInter(self, value: "MultidimensionalTime") -> "SporadicEventTriggering":
        """
        AUTOSAR-compliant setter for maximumInter with method chaining.
        
        Args:
            value: The maximumInter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to maximum_inter property setter (gets validation automatically)
        """
        self.maximum_inter = value  # Delegates to property setter
        return self

    def getMinimumInter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimumInter.
        
        Returns:
            The minimumInter value
        
        Note:
            Delegates to minimum_inter property (CODING_RULE_V2_00017)
        """
        return self.minimum_inter  # Delegates to property

    def setMinimumInter(self, value: "MultidimensionalTime") -> "SporadicEventTriggering":
        """
        AUTOSAR-compliant setter for minimumInter with method chaining.
        
        Args:
            value: The minimumInter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_inter property setter (gets validation automatically)
        """
        self.minimum_inter = value  # Delegates to property setter
        return self

    def getPeriod(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for period.
        
        Returns:
            The period value
        
        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "MultidimensionalTime") -> "SporadicEventTriggering":
        """
        AUTOSAR-compliant setter for period with method chaining.
        
        Args:
            value: The period to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_jitter(self, value: Optional["MultidimensionalTime"]) -> "SporadicEventTriggering":
        """
        Set jitter and return self for chaining.
        
        Args:
            value: The jitter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_jitter("value")
        """
        self.jitter = value  # Use property setter (gets validation)
        return self

    def with_maximum_inter(self, value: Optional["MultidimensionalTime"]) -> "SporadicEventTriggering":
        """
        Set maximumInter and return self for chaining.
        
        Args:
            value: The maximumInter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_maximum_inter("value")
        """
        self.maximum_inter = value  # Use property setter (gets validation)
        return self

    def with_minimum_inter(self, value: Optional["MultidimensionalTime"]) -> "SporadicEventTriggering":
        """
        Set minimumInter and return self for chaining.
        
        Args:
            value: The minimumInter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_inter("value")
        """
        self.minimum_inter = value  # Use property setter (gets validation)
        return self

    def with_period(self, value: Optional["MultidimensionalTime"]) -> "SporadicEventTriggering":
        """
        Set period and return self for chaining.
        
        Args:
            value: The period to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self