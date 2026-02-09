"""
AUTOSAR Package - EventTriggeringConstraint

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.__init__ import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EventTriggeringConstraint(TimingConstraint, ABC):
    """
    Describes the occurrence behavior of the referenced timing event. The
    occurrence behavior can only be determined when a mapping from the timing
    events to the implementation can be obtained. However, such an occurrence
    behavior can also be described by the modeler as an assumption or as a
    requirement about the occurrence of the event.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::EventTriggeringConstraint
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 100, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EventTriggeringConstraint:
            raise TypeError("EventTriggeringConstraint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced timing event.
        self._event: Optional["TimingDescriptionEvent"] = None

    @property
    def event(self) -> Optional["TimingDescriptionEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set event with validation.
        
        Args:
            value: The event to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"event must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._event = value

    def with_offset(self, value):
        """
        Set offset and return self for chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_confidence(self, value):
        """
        Set confidence and return self for chaining.

        Args:
            value: The confidence to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_confidence("value")
        """
        self.confidence = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value):
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value):
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for event.
        
        Returns:
            The event value
        
        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "TimingDescriptionEvent") -> "EventTriggeringConstraint":
        """
        AUTOSAR-compliant setter for event with method chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["TimingDescriptionEvent"]) -> "EventTriggeringConstraint":
        """
        Set event and return self for chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self



class ConfidenceInterval(ARObject):
    """
    Additionally to the list of measured distances of event occurrences, a
    confidence interval can be specified for the expected distance of two
    consecutive event occurrences with a given probability.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::ConfidenceInterval
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 112, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The lower bound of the expected distance of two occurrences.
        self._lowerBound: Optional["MultidimensionalTime"] = None

    @property
    def lower_bound(self) -> Optional["MultidimensionalTime"]:
        """Get lowerBound (Pythonic accessor)."""
        return self._lowerBound

    @lower_bound.setter
    def lower_bound(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set lowerBound with validation.
        
        Args:
            value: The lowerBound to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerBound = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"lowerBound must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._lowerBound = value
        # The probability for the measured lower and upper bound confidence interval.
        self._propability: Optional["Float"] = None

    @property
    def propability(self) -> Optional["Float"]:
        """Get propability (Pythonic accessor)."""
        return self._propability

    @propability.setter
    def propability(self, value: Optional["Float"]) -> None:
        """
        Set propability with validation.
        
        Args:
            value: The propability to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propability = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"propability must be Float or float or None, got {type(value).__name__}"
            )
        self._propability = value
        # The upper bound of the expected distance of two occurrences.
        self._upperBound: Optional["MultidimensionalTime"] = None

    @property
    def upper_bound(self) -> Optional["MultidimensionalTime"]:
        """Get upperBound (Pythonic accessor)."""
        return self._upperBound

    @upper_bound.setter
    def upper_bound(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set upperBound with validation.
        
        Args:
            value: The upperBound to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperBound = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"upperBound must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._upperBound = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerBound(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for lowerBound.
        
        Returns:
            The lowerBound value
        
        Note:
            Delegates to lower_bound property (CODING_RULE_V2_00017)
        """
        return self.lower_bound  # Delegates to property

    def setLowerBound(self, value: "MultidimensionalTime") -> "ConfidenceInterval":
        """
        AUTOSAR-compliant setter for lowerBound with method chaining.
        
        Args:
            value: The lowerBound to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lower_bound property setter (gets validation automatically)
        """
        self.lower_bound = value  # Delegates to property setter
        return self

    def getPropability(self) -> "Float":
        """
        AUTOSAR-compliant getter for propability.
        
        Returns:
            The propability value
        
        Note:
            Delegates to propability property (CODING_RULE_V2_00017)
        """
        return self.propability  # Delegates to property

    def setPropability(self, value: "Float") -> "ConfidenceInterval":
        """
        AUTOSAR-compliant setter for propability with method chaining.
        
        Args:
            value: The propability to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to propability property setter (gets validation automatically)
        """
        self.propability = value  # Delegates to property setter
        return self

    def getUpperBound(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for upperBound.
        
        Returns:
            The upperBound value
        
        Note:
            Delegates to upper_bound property (CODING_RULE_V2_00017)
        """
        return self.upper_bound  # Delegates to property

    def setUpperBound(self, value: "MultidimensionalTime") -> "ConfidenceInterval":
        """
        AUTOSAR-compliant setter for upperBound with method chaining.
        
        Args:
            value: The upperBound to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to upper_bound property setter (gets validation automatically)
        """
        self.upper_bound = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_bound(self, value: Optional["MultidimensionalTime"]) -> "ConfidenceInterval":
        """
        Set lowerBound and return self for chaining.
        
        Args:
            value: The lowerBound to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lower_bound("value")
        """
        self.lower_bound = value  # Use property setter (gets validation)
        return self

    def with_propability(self, value: Optional["Float"]) -> "ConfidenceInterval":
        """
        Set propability and return self for chaining.
        
        Args:
            value: The propability to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_propability("value")
        """
        self.propability = value  # Use property setter (gets validation)
        return self

    def with_upper_bound(self, value: Optional["MultidimensionalTime"]) -> "ConfidenceInterval":
        """
        Set upperBound and return self for chaining.
        
        Args:
            value: The upperBound to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_upper_bound("value")
        """
        self.upper_bound = value  # Use property setter (gets validation)
        return self



class PeriodicEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event with a strict periodic occurrence
    pattern, given by period. Additionally, it is possible to soften the
    strictness of the periodic occurrence behavior by specifying a jitter, so
    that there can be a deviation from the period up to the size of the jitter.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::PeriodicEventTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 101, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum deviation of the periodic event occurrence.
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
        # The minimum time distance between subsequent occurrences of the associated
                # event.
        # minimumInterArrivalTime is less than the the jitter, then the no effect on
                # the the constraint.
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

    def setJitter(self, value: "MultidimensionalTime") -> "PeriodicEventTriggering":
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

    def getMinimumInter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimumInter.
        
        Returns:
            The minimumInter value
        
        Note:
            Delegates to minimum_inter property (CODING_RULE_V2_00017)
        """
        return self.minimum_inter  # Delegates to property

    def setMinimumInter(self, value: "MultidimensionalTime") -> "PeriodicEventTriggering":
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

    def setPeriod(self, value: "MultidimensionalTime") -> "PeriodicEventTriggering":
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

    def with_jitter(self, value: Optional["MultidimensionalTime"]) -> "PeriodicEventTriggering":
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

    def with_minimum_inter(self, value: Optional["MultidimensionalTime"]) -> "PeriodicEventTriggering":
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

    def with_period(self, value: Optional["MultidimensionalTime"]) -> "PeriodicEventTriggering":
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



class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event that occurs according to a precisely
    known pattern.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::ConcretePatternEventTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 106, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The offset for each occurrence of the event in the interval.
        # A list of point-in-times in the time by the parameter patternLength at which
                # occurs.
        self._offset: List["MultidimensionalTime"] = []

    @property
    def offset(self) -> List["MultidimensionalTime"]:
        """Get offset (Pythonic accessor)."""
        return self._offset
        # The maximum deviation of the time interval’s starting the beginning of the
                # given period.
        # This only applicable in conjunction with the.
        self._patternJitter: Optional["MultidimensionalTime"] = None

    @property
    def pattern_jitter(self) -> Optional["MultidimensionalTime"]:
        """Get patternJitter (Pythonic accessor)."""
        return self._patternJitter

    @pattern_jitter.setter
    def pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternJitter with validation.
        
        Args:
            value: The patternJitter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternJitter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternJitter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternJitter = value
        # The duration of the time interval within which the event The event occurs at
        # concrete points in the given time interval.
        self._patternLength: Optional["MultidimensionalTime"] = None

    @property
    def pattern_length(self) -> Optional["MultidimensionalTime"]:
        """Get patternLength (Pythonic accessor)."""
        return self._patternLength

    @pattern_length.setter
    def pattern_length(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternLength with validation.
        
        Args:
            value: The patternLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternLength = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternLength must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternLength = value
        # The time distance between the beginnings of subsequent the given concrete
        # pattern.
        self._patternPeriod: Optional["MultidimensionalTime"] = None

    @property
    def pattern_period(self) -> Optional["MultidimensionalTime"]:
        """Get patternPeriod (Pythonic accessor)."""
        return self._patternPeriod

    @pattern_period.setter
    def pattern_period(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternPeriod with validation.
        
        Args:
            value: The patternPeriod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternPeriod = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternPeriod must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternPeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOffset(self) -> List["MultidimensionalTime"]:
        """
        AUTOSAR-compliant getter for offset.
        
        Returns:
            The offset value
        
        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def getPatternJitter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternJitter.
        
        Returns:
            The patternJitter value
        
        Note:
            Delegates to pattern_jitter property (CODING_RULE_V2_00017)
        """
        return self.pattern_jitter  # Delegates to property

    def setPatternJitter(self, value: "MultidimensionalTime") -> "ConcretePatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternJitter with method chaining.
        
        Args:
            value: The patternJitter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern_jitter property setter (gets validation automatically)
        """
        self.pattern_jitter = value  # Delegates to property setter
        return self

    def getPatternLength(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternLength.
        
        Returns:
            The patternLength value
        
        Note:
            Delegates to pattern_length property (CODING_RULE_V2_00017)
        """
        return self.pattern_length  # Delegates to property

    def setPatternLength(self, value: "MultidimensionalTime") -> "ConcretePatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternLength with method chaining.
        
        Args:
            value: The patternLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern_length property setter (gets validation automatically)
        """
        self.pattern_length = value  # Delegates to property setter
        return self

    def getPatternPeriod(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternPeriod.
        
        Returns:
            The patternPeriod value
        
        Note:
            Delegates to pattern_period property (CODING_RULE_V2_00017)
        """
        return self.pattern_period  # Delegates to property

    def setPatternPeriod(self, value: "MultidimensionalTime") -> "ConcretePatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternPeriod with method chaining.
        
        Args:
            value: The patternPeriod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern_period property setter (gets validation automatically)
        """
        self.pattern_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> "ConcretePatternEventTriggering":
        """
        Set patternJitter and return self for chaining.
        
        Args:
            value: The patternJitter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern_jitter("value")
        """
        self.pattern_jitter = value  # Use property setter (gets validation)
        return self

    def with_pattern_length(self, value: Optional["MultidimensionalTime"]) -> "ConcretePatternEventTriggering":
        """
        Set patternLength and return self for chaining.
        
        Args:
            value: The patternLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern_length("value")
        """
        self.pattern_length = value  # Use property setter (gets validation)
        return self

    def with_pattern_period(self, value: Optional["MultidimensionalTime"]) -> "ConcretePatternEventTriggering":
        """
        Set patternPeriod and return self for chaining.
        
        Args:
            value: The patternPeriod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern_period("value")
        """
        self.pattern_period = value  # Use property setter (gets validation)
        return self



class BurstPatternEventTriggering(EventTriggeringConstraint):
    """
    Describes the maximum number of occurrences of the same event in a given
    time interval. Typically used to model a worst case activation scenario.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::BurstPatternEventTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 109, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum number of event occurrences within the time interval.
        # The event may never occur, or may times between 1 and the parameter specified
                # then the event least the number of times specified by at maximum by.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.
        
        Args:
            value: The maxNumberOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # Specifies the minimum distance between subsequent of the event within the
        # given time interval.
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
        # The minimum number of event occurrences within the time interval.
        self._minNumberOf: Optional["PositiveInteger"] = None

    @property
    def min_number_of(self) -> Optional["PositiveInteger"]:
        """Get minNumberOf (Pythonic accessor)."""
        return self._minNumberOf

    @min_number_of.setter
    def min_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minNumberOf with validation.
        
        Args:
            value: The minNumberOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minNumberOf = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minNumberOf must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minNumberOf = value
        # The maximum deviation of the time interval’s starting the beginning of the
                # given period.
        # This only applicable in conjunction with the.
        self._patternJitter: Optional["MultidimensionalTime"] = None

    @property
    def pattern_jitter(self) -> Optional["MultidimensionalTime"]:
        """Get patternJitter (Pythonic accessor)."""
        return self._patternJitter

    @pattern_jitter.setter
    def pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternJitter with validation.
        
        Args:
            value: The patternJitter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternJitter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternJitter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternJitter = value
        # The duration of the time interval within which the event The event occurs at
        # arbitrary points in the given time interval.
        self._patternLength: Optional["MultidimensionalTime"] = None

    @property
    def pattern_length(self) -> Optional["MultidimensionalTime"]:
        """Get patternLength (Pythonic accessor)."""
        return self._patternLength

    @pattern_length.setter
    def pattern_length(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternLength with validation.
        
        Args:
            value: The patternLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternLength = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternLength must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternLength = value
        # The time distance between the beginnings of subsequent the given burst
        # pattern.
        self._patternPeriod: Optional["MultidimensionalTime"] = None

    @property
    def pattern_period(self) -> Optional["MultidimensionalTime"]:
        """Get patternPeriod (Pythonic accessor)."""
        return self._patternPeriod

    @pattern_period.setter
    def pattern_period(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternPeriod with validation.
        
        Args:
            value: The patternPeriod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternPeriod = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternPeriod must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternPeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.
        
        Returns:
            The maxNumberOf value
        
        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.
        
        Args:
            value: The maxNumberOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
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

    def setMinimumInter(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
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

    def getMinNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minNumberOf.
        
        Returns:
            The minNumberOf value
        
        Note:
            Delegates to min_number_of property (CODING_RULE_V2_00017)
        """
        return self.min_number_of  # Delegates to property

    def setMinNumberOf(self, value: "PositiveInteger") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for minNumberOf with method chaining.
        
        Args:
            value: The minNumberOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_number_of property setter (gets validation automatically)
        """
        self.min_number_of = value  # Delegates to property setter
        return self

    def getPatternJitter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternJitter.
        
        Returns:
            The patternJitter value
        
        Note:
            Delegates to pattern_jitter property (CODING_RULE_V2_00017)
        """
        return self.pattern_jitter  # Delegates to property

    def setPatternJitter(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternJitter with method chaining.
        
        Args:
            value: The patternJitter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern_jitter property setter (gets validation automatically)
        """
        self.pattern_jitter = value  # Delegates to property setter
        return self

    def getPatternLength(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternLength.
        
        Returns:
            The patternLength value
        
        Note:
            Delegates to pattern_length property (CODING_RULE_V2_00017)
        """
        return self.pattern_length  # Delegates to property

    def setPatternLength(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternLength with method chaining.
        
        Args:
            value: The patternLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern_length property setter (gets validation automatically)
        """
        self.pattern_length = value  # Delegates to property setter
        return self

    def getPatternPeriod(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternPeriod.
        
        Returns:
            The patternPeriod value
        
        Note:
            Delegates to pattern_period property (CODING_RULE_V2_00017)
        """
        return self.pattern_period  # Delegates to property

    def setPatternPeriod(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternPeriod with method chaining.
        
        Args:
            value: The patternPeriod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern_period property setter (gets validation automatically)
        """
        self.pattern_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "BurstPatternEventTriggering":
        """
        Set maxNumberOf and return self for chaining.
        
        Args:
            value: The maxNumberOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_minimum_inter(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
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

    def with_min_number_of(self, value: Optional["PositiveInteger"]) -> "BurstPatternEventTriggering":
        """
        Set minNumberOf and return self for chaining.
        
        Args:
            value: The minNumberOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_number_of("value")
        """
        self.min_number_of = value  # Use property setter (gets validation)
        return self

    def with_pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
        """
        Set patternJitter and return self for chaining.
        
        Args:
            value: The patternJitter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern_jitter("value")
        """
        self.pattern_jitter = value  # Use property setter (gets validation)
        return self

    def with_pattern_length(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
        """
        Set patternLength and return self for chaining.
        
        Args:
            value: The patternLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern_length("value")
        """
        self.pattern_length = value  # Use property setter (gets validation)
        return self

    def with_pattern_period(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
        """
        Set patternPeriod and return self for chaining.
        
        Args:
            value: The patternPeriod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern_period("value")
        """
        self.pattern_period = value  # Use property setter (gets validation)
        return self



class ArbitraryEventTriggering(EventTriggeringConstraint):
    """
    Describes that an event occurs occasionally, singly, irregularly or
    randomly. The primary purpose of this event triggering is to abstract event
    occurrences captured by data acquisition tools (background debugger, trace
    analyzer, etc.) during system runtime.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::ArbitraryEventTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 111, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # List of confidence intervals.
        # xml.
        # sequenceOffset=30 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing
                # Extensions for Classic R23-11.
        self._confidence: List["ConfidenceInterval"] = []

    @property
    def confidence(self) -> List["ConfidenceInterval"]:
        """Get confidence (Pythonic accessor)."""
        return self._confidence
        # The nth array element describes the maximum distance can be observed for a
        # sample of n+1 event an array with an identical number of elements as
        # minimumDistance.
        self._maximum: List["MultidimensionalTime"] = []

    @property
    def maximum(self) -> List["MultidimensionalTime"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum
        # The nth array element describes the minimum distance can be observed for a
        # sample of n+1 event an array with an identical number of elements as
        # maximumDistance.
        self._minimum: List["MultidimensionalTime"] = []

    @property
    def minimum(self) -> List["MultidimensionalTime"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConfidence(self) -> List["ConfidenceInterval"]:
        """
        AUTOSAR-compliant getter for confidence.
        
        Returns:
            The confidence value
        
        Note:
            Delegates to confidence property (CODING_RULE_V2_00017)
        """
        return self.confidence  # Delegates to property

    def getMaximum(self) -> List["MultidimensionalTime"]:
        """
        AUTOSAR-compliant getter for maximum.
        
        Returns:
            The maximum value
        
        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def getMinimum(self) -> List["MultidimensionalTime"]:
        """
        AUTOSAR-compliant getter for minimum.
        
        Returns:
            The minimum value
        
        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
