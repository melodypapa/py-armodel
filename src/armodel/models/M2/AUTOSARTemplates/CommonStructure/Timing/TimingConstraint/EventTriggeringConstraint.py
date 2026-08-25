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
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
    Float,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class EventTriggeringConstraint(TimingConstraint, ABC):
    """
    Abstract base class for event triggering constraints.
    This class cannot be instantiated directly and serves as the base for
    concrete event triggering constraint implementations.
    """

    # EventTriggeringConstraint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        if type(self) is EventTriggeringConstraint:
            raise TypeError("EventTriggeringConstraint is an abstract class.")

        super().__init__(parent, short_name)


class PeriodicEventTriggering(EventTriggeringConstraint):
    """
    Specifies periodic event triggering requirements.
    This constraint defines the period for periodic event triggering.
    """

    # PeriodicEventTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getPeriod                    [x] impl  [ ] docstring  [ ] test
    # [ ] setPeriod                    [x] impl  [ ] docstring  [ ] test

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

    # SporadicEventTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getMinInterArrivalTime       [x] impl  [ ] docstring  [ ] test
    # [ ] setMinInterArrivalTime       [x] impl  [ ] docstring  [ ] test

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

    # ArbitraryEventTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

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

    # BurstPatternEventTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getBurstSize                 [x] impl  [ ] docstring  [ ] test
    # [ ] setBurstSize                 [x] impl  [ ] docstring  [ ] test
    # [ ] getBurstInterval             [x] impl  [ ] docstring  [ ] test
    # [ ] setBurstInterval             [x] impl  [ ] docstring  [ ] test

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

    # ConcretePatternEventTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

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
    Additionally to the list of measured distances of event occurrences, a confidence interval can be specified for the expected distance of two consecutive event occurrences with a given probability.
    """

    # ConfidenceInterval method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.65, p.112
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLowerBound   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerBound   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPropability  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPropability  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperBound   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperBound   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The lower bound of the expected distance of two consecutive event occurrences.
        self.lowerBound: Optional[MultidimensionalTime] = None

        # The probability for the measured lower and upper bound of the confidence interval.
        self.propability: Optional[Float] = None

        # The upper bound of the expected distance of two consecutive event occurrences.
        self.upperBound: Optional[MultidimensionalTime] = None

    def getLowerBound(self) -> Optional[MultidimensionalTime]:
        """The lower bound of the expected distance of two consecutive event occurrences."""
        return self.lowerBound

    def setLowerBound(self, value: Optional[MultidimensionalTime]) -> "ConfidenceInterval":
        """The lower bound of the expected distance of two consecutive event occurrences. A None value is a no-op and does not overwrite an existing lowerBound."""
        if value is not None:
            self.lowerBound = value
        return self

    def getPropability(self) -> Optional[Float]:
        """The probability for the measured lower and upper bound of the confidence interval."""
        return self.propability

    def setPropability(self, value: Optional[Float]) -> "ConfidenceInterval":
        """The probability for the measured lower and upper bound of the confidence interval. A None value is a no-op and does not overwrite an existing propability."""
        if value is not None:
            self.propability = value
        return self

    def getUpperBound(self) -> Optional[MultidimensionalTime]:
        """The upper bound of the expected distance of two consecutive event occurrences."""
        return self.upperBound

    def setUpperBound(self, value: Optional[MultidimensionalTime]) -> "ConfidenceInterval":
        """The upper bound of the expected distance of two consecutive event occurrences. A None value is a no-op and does not overwrite an existing upperBound."""
        if value is not None:
            self.upperBound = value
        return self
