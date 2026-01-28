"""
This module defines event triggering constraints in AUTOSAR timing specifications.

Event triggering constraints specify timing requirements for event triggering
patterns such as periodic, sporadic, or burst patterns.

Classes:
    EventTriggeringConstraint: Abstract base for event triggering constraints
    PeriodicEventTriggering: Specifies periodic event triggering
    SporadicEventTriggering: Specifies sporadic event triggering
    ArbitraryEventTriggering: Specifies arbitrary event triggering
    BurstPatternEventTriggering: Specifies burst pattern event triggering
    ConcretePatternEventTriggering: Specifies concrete pattern event triggering
    ConfidenceInterval: Specifies confidence interval for timing measurements
"""

from abc import ABC
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
    Float,
)
from .TimingConstraint import TimingConstraint


class EventTriggeringConstraint(TimingConstraint, ABC):
    """
    Abstract base class for event triggering constraints.
    This class cannot be instantiated directly and serves as the base for
    concrete event triggering constraint implementations.
    """

    def __init__(self, parent, short_name: str):
        if type(self) is EventTriggeringConstraint:
            raise TypeError("EventTriggeringConstraint is an abstract class.")

        super().__init__(parent, short_name)


class PeriodicEventTriggering(EventTriggeringConstraint):
    """
    Specifies periodic event triggering requirements.
    This constraint defines the period for periodic event triggering.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the PeriodicEventTriggering with a parent and short name.

        Args:
            parent: The parent ARObject that contains this constraint
            short_name: The unique short name of this constraint
        """
        super().__init__(parent, short_name)

        # Period for event triggering
        self.period: TimeValue = None

    def getPeriod(self):
        return self.period

    def setPeriod(self, value):
        self.period = value
        return self


class SporadicEventTriggering(EventTriggeringConstraint):
    """
    Specifies sporadic event triggering requirements.
    This constraint defines the minimum inter-arrival time for sporadic events.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the SporadicEventTriggering with a parent and short name.

        Args:
            parent: The parent ARObject that contains this constraint
            short_name: The unique short name of this constraint
        """
        super().__init__(parent, short_name)

        # Minimum inter-arrival time
        self.min_inter_arrival_time: TimeValue = None

    def getMinInterArrivalTime(self):
        return self.min_inter_arrival_time

    def setMinInterArrivalTime(self, value):
        self.min_inter_arrival_time = value
        return self


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """
    Specifies arbitrary event triggering requirements.
    This constraint allows for arbitrary event triggering patterns.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the ArbitraryEventTriggering with a parent and short name.

        Args:
            parent: The parent ARObject that contains this constraint
            short_name: The unique short name of this constraint
        """
        super().__init__(parent, short_name)


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """
    Specifies burst pattern event triggering requirements.
    This constraint defines burst pattern parameters for event triggering.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the BurstPatternEventTriggering with a parent and short name.

        Args:
            parent: The parent ARObject that contains this constraint
            short_name: The unique short name of this constraint
        """
        super().__init__(parent, short_name)

        # Number of events in burst
        self.burst_size: int = None
        # Burst interval
        self.burst_interval: TimeValue = None

    def getBurstSize(self):
        return self.burst_size

    def setBurstSize(self, value):
        self.burst_size = value
        return self

    def getBurstInterval(self):
        return self.burst_interval

    def setBurstInterval(self, value):
        self.burst_interval = value
        return self


class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """
    Specifies concrete pattern event triggering requirements.
    This constraint defines a concrete pattern for event triggering.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the ConcretePatternEventTriggering with a parent and short name.

        Args:
            parent: The parent ARObject that contains this constraint
            short_name: The unique short name of this constraint
        """
        super().__init__(parent, short_name)


class ConfidenceInterval(ARObject):
    """
    Specifies a confidence interval for timing measurements.
    This class defines the confidence interval with a confidence level
    and interval bounds.
    """

    def __init__(self):
        """
        Initializes the ConfidenceInterval with default values.
        """
        super().__init__()

        # Confidence level (e.g., 0.95 for 95% confidence)
        self.confidence_level: Float = None
        # Lower bound of the interval
        self.lower_bound: TimeValue = None
        # Upper bound of the interval
        self.upper_bound: TimeValue = None

    def getConfidenceLevel(self):
        return self.confidence_level

    def setConfidenceLevel(self, value):
        self.confidence_level = value
        return self

    def getLowerBound(self):
        return self.lower_bound

    def setLowerBound(self, value):
        self.lower_bound = value
        return self

    def getUpperBound(self):
        return self.upper_bound

    def setUpperBound(self, value):
        self.upper_bound = value
        return self