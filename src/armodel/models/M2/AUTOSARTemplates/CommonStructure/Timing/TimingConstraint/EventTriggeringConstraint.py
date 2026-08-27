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
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class EventTriggeringConstraint(TimingConstraint, ABC):
    """
    Describes the occurrence behavior of the referenced timing event. The occurrence behavior can only be determined when a mapping from the timing events to the implementation can be obtained. However, such an occurrence behavior can also be described by the modeler as an assumption or as a requirement about the occurrence of the event.

    (event -> TimingDescriptionEvent placeholder, Rule 0001.10)
    """

    # EventTriggeringConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.59, p.100
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEventRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        if type(self) is EventTriggeringConstraint:
            raise TypeError("EventTriggeringConstraint is an abstract class.")

        super().__init__(parent, short_name)

        # The referenced timing event. (TimingDescriptionEvent placeholder, Rule 0001.10)
        self.eventRef: Optional[RefType] = None

    def getEventRef(self) -> Optional[RefType]:
        """The referenced timing event."""
        return self.eventRef

    def setEventRef(self, value: Optional[RefType]) -> "EventTriggeringConstraint":
        """The referenced timing event. A None value is a no-op and does not overwrite an existing event."""
        if value is not None:
            self.eventRef = value
        return self


class PeriodicEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event with a strict periodic occurrence pattern, given by period . Additionally, it is possible to soften the strictness of the periodic occurrence behavior by specifying a jitter , so that there can be a deviation from the period up to the size of the jitter .
    """

    # PeriodicEventTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.60, p.101
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getJitter                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setJitter                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimumInterArrivalTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumInterArrivalTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPeriod                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPeriod                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The maximum deviation of the periodic event occurrence.
        self.jitter: Optional[MultidimensionalTime] = None

        # The minimum time distance between subsequent consecutive occurrences of the associated event. If the minimumInterArrivalTime is less than the period minus the jitter , then the minimumInterArrivalTime has no effect on the properties of the constraint.
        self.minimumInterArrivalTime: Optional[MultidimensionalTime] = None

        # The periodic distance between subsequent occurrences of the event.
        self.period: Optional[MultidimensionalTime] = None

    def getJitter(self) -> Optional[MultidimensionalTime]:
        """The maximum deviation of the periodic event occurrence."""
        return self.jitter

    def setJitter(self, value: Optional[MultidimensionalTime]) -> "PeriodicEventTriggering":
        """The maximum deviation of the periodic event occurrence. A None value is a no-op and does not overwrite an existing jitter."""
        if value is not None:
            self.jitter = value
        return self

    def getMinimumInterArrivalTime(self) -> Optional[MultidimensionalTime]:
        """The minimum time distance between subsequent consecutive occurrences of the associated event. If the minimumInterArrivalTime is less than the period minus the jitter , then the minimumInterArrivalTime has no effect on the properties of the constraint."""
        return self.minimumInterArrivalTime

    def setMinimumInterArrivalTime(self, value: Optional[MultidimensionalTime]) -> "PeriodicEventTriggering":
        """The minimum time distance between subsequent consecutive occurrences of the associated event. If the minimumInterArrivalTime is less than the period minus the jitter , then the minimumInterArrivalTime has no effect on the properties of the constraint. A None value is a no-op and does not overwrite an existing minimumInterArrivalTime."""
        if value is not None:
            self.minimumInterArrivalTime = value
        return self

    def getPeriod(self) -> Optional[MultidimensionalTime]:
        """The periodic distance between subsequent occurrences of the event."""
        return self.period

    def setPeriod(self, value: Optional[MultidimensionalTime]) -> "PeriodicEventTriggering":
        """The periodic distance between subsequent occurrences of the event. A None value is a no-op and does not overwrite an existing period."""
        if value is not None:
            self.period = value
        return self


class SporadicEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event which occurs occasionally or singularly.
    """

    # SporadicEventTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.61, p.105
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getJitter                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setJitter                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximumInterArrivalTime    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximumInterArrivalTime    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimumInterArrivalTime    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumInterArrivalTime    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPeriod                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPeriod                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The maximum devation of the sporadic event occurrence. Jitter=max |nthPeriod - standardPeriod|
        self.jitter: Optional[MultidimensionalTime] = None

        # The maximum time distance between two consecutive (subsequent) occurrences of the associated event.
        self.maximumInterArrivalTime: Optional[MultidimensionalTime] = None

        # The minimum time distance between two consecutive (subsequent) occurrences of the associated event.
        self.minimumInterArrivalTime: Optional[MultidimensionalTime] = None

        # The periodic distance between subsequent occurrences of the event.
        self.period: Optional[MultidimensionalTime] = None

    def getJitter(self) -> Optional[MultidimensionalTime]:
        """The maximum devation of the sporadic event occurrence. Jitter=max |nthPeriod - standardPeriod|"""
        return self.jitter

    def setJitter(self, value: Optional[MultidimensionalTime]) -> "SporadicEventTriggering":
        """The maximum devation of the sporadic event occurrence. Jitter=max |nthPeriod - standardPeriod| A None value is a no-op and does not overwrite an existing jitter."""
        if value is not None:
            self.jitter = value
        return self

    def getMaximumInterArrivalTime(self) -> Optional[MultidimensionalTime]:
        """The maximum time distance between two consecutive (subsequent) occurrences of the associated event."""
        return self.maximumInterArrivalTime

    def setMaximumInterArrivalTime(self, value: Optional[MultidimensionalTime]) -> "SporadicEventTriggering":
        """The maximum time distance between two consecutive (subsequent) occurrences of the associated event. A None value is a no-op and does not overwrite an existing maximumInterArrivalTime."""
        if value is not None:
            self.maximumInterArrivalTime = value
        return self

    def getMinimumInterArrivalTime(self) -> Optional[MultidimensionalTime]:
        """The minimum time distance between two consecutive (subsequent) occurrences of the associated event."""
        return self.minimumInterArrivalTime

    def setMinimumInterArrivalTime(self, value: Optional[MultidimensionalTime]) -> "SporadicEventTriggering":
        """The minimum time distance between two consecutive (subsequent) occurrences of the associated event. A None value is a no-op and does not overwrite an existing minimumInterArrivalTime."""
        if value is not None:
            self.minimumInterArrivalTime = value
        return self

    def getPeriod(self) -> Optional[MultidimensionalTime]:
        """The periodic distance between subsequent occurrences of the event."""
        return self.period

    def setPeriod(self, value: Optional[MultidimensionalTime]) -> "SporadicEventTriggering":
        """The periodic distance between subsequent occurrences of the event. A None value is a no-op and does not overwrite an existing period."""
        if value is not None:
            self.period = value
        return self


class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event that occurs according to a precisely known pattern.
    """

    # ConcretePatternEventTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.62, p.107
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addOffset             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOffsets            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPatternJitter      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPatternJitter      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPatternLength      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPatternLength      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPatternPeriod      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPatternPeriod      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The offset for each occurrence of the event in the specified time interval. A list of point-in-times in the time interval given by the parameter patternLength at which the event occurs.
        self.offsets: List[MultidimensionalTime] = []

        # The maximum deviation of the time interval's starting point from the beginning of the given period. This parameter is only applicable in conjunction with the parameter patternPeriod .
        self.patternJitter: Optional[MultidimensionalTime] = None

        # The duration of the time interval within which the event repeatedly occurs. The event occurs at concrete points in time within the given time interval.
        self.patternLength: Optional[MultidimensionalTime] = None

        # The time distance between the beginnings of subsequent repetitions of the given concrete pattern.
        self.patternPeriod: Optional[MultidimensionalTime] = None

    def addOffset(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggering":
        """The offset for each occurrence of the event in the specified time interval. A list of point-in-times in the time interval given by the parameter patternLength at which the event occurs. A None value is a no-op and does not change the offsets list."""
        if value is not None:
            self.offsets.append(value)
        return self

    def getOffsets(self) -> List[MultidimensionalTime]:
        """The offset for each occurrence of the event in the specified time interval. A list of point-in-times in the time interval given by the parameter patternLength at which the event occurs."""
        return self.offsets

    def getPatternJitter(self) -> Optional[MultidimensionalTime]:
        """The maximum deviation of the time interval's starting point from the beginning of the given period. This parameter is only applicable in conjunction with the parameter patternPeriod ."""
        return self.patternJitter

    def setPatternJitter(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggering":
        """The maximum deviation of the time interval's starting point from the beginning of the given period. This parameter is only applicable in conjunction with the parameter patternPeriod . A None value is a no-op and does not overwrite an existing patternJitter."""
        if value is not None:
            self.patternJitter = value
        return self

    def getPatternLength(self) -> Optional[MultidimensionalTime]:
        """The duration of the time interval within which the event repeatedly occurs. The event occurs at concrete points in time within the given time interval."""
        return self.patternLength

    def setPatternLength(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggering":
        """The duration of the time interval within which the event repeatedly occurs. The event occurs at concrete points in time within the given time interval. A None value is a no-op and does not overwrite an existing patternLength."""
        if value is not None:
            self.patternLength = value
        return self

    def getPatternPeriod(self) -> Optional[MultidimensionalTime]:
        """The time distance between the beginnings of subsequent repetitions of the given concrete pattern."""
        return self.patternPeriod

    def setPatternPeriod(self, value: Optional[MultidimensionalTime]) -> "ConcretePatternEventTriggering":
        """The time distance between the beginnings of subsequent repetitions of the given concrete pattern. A None value is a no-op and does not overwrite an existing patternPeriod."""
        if value is not None:
            self.patternPeriod = value
        return self


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """
    Describes the maximum number of occurrences of the same event in a given time interval. Typically used to model a worst case activation scenario.
    """

    # BurstPatternEventTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.63, p.109
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMaxNumberOfOccurrences   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxNumberOfOccurrences   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimumInterArrivalTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumInterArrivalTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinNumberOfOccurrences   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinNumberOfOccurrences   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPatternJitter            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPatternJitter            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPatternLength            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPatternLength            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPatternPeriod            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPatternPeriod            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The maximum number of event occurrences within the given time interval. The event may never occur, or may occur N times between 1 and maxNumberOfOccurrences . If the parameter minNumberOfOccurrences is specified then the event occurs at least the number of times specified by minNumberOfOccurrences and at maximum by maxNumberOfOccurrences .
        self.maxNumberOfOccurrences: Optional[PositiveInteger] = None

        # Specifies the minimum distance between subsequent occurrences of the event within the given time interval.
        self.minimumInterArrivalTime: Optional[MultidimensionalTime] = None

        # The minimum number of event occurrences within the given time interval.
        self.minNumberOfOccurrences: Optional[PositiveInteger] = None

        # The maximum deviation of the time interval's starting point from the beginning of the given period. This parameter is only applicable in conjunction with the parameter patternPeriod
        self.patternJitter: Optional[MultidimensionalTime] = None

        # The duration of the time interval within which the event repeatedly occurs. The event occurs at arbitrary points in time within the given time interval.
        self.patternLength: Optional[MultidimensionalTime] = None

        # The time distance between the beginnings of subsequent repetitions of the given burst pattern.
        self.patternPeriod: Optional[MultidimensionalTime] = None

    def getMaxNumberOfOccurrences(self) -> Optional[PositiveInteger]:
        """The maximum number of event occurrences within the given time interval. The event may never occur, or may occur N times between 1 and maxNumberOfOccurrences . If the parameter minNumberOfOccurrences is specified then the event occurs at least the number of times specified by minNumberOfOccurrences and at maximum by maxNumberOfOccurrences ."""
        return self.maxNumberOfOccurrences

    def setMaxNumberOfOccurrences(self, value: Optional[PositiveInteger]) -> "BurstPatternEventTriggering":
        """The maximum number of event occurrences within the given time interval. The event may never occur, or may occur N times between 1 and maxNumberOfOccurrences . If the parameter minNumberOfOccurrences is specified then the event occurs at least the number of times specified by minNumberOfOccurrences and at maximum by maxNumberOfOccurrences . A None value is a no-op and does not overwrite an existing maxNumberOfOccurrences."""
        if value is not None:
            self.maxNumberOfOccurrences = value
        return self

    def getMinimumInterArrivalTime(self) -> Optional[MultidimensionalTime]:
        """Specifies the minimum distance between subsequent occurrences of the event within the given time interval."""
        return self.minimumInterArrivalTime

    def setMinimumInterArrivalTime(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggering":
        """Specifies the minimum distance between subsequent occurrences of the event within the given time interval. A None value is a no-op and does not overwrite an existing minimumInterArrivalTime."""
        if value is not None:
            self.minimumInterArrivalTime = value
        return self

    def getMinNumberOfOccurrences(self) -> Optional[PositiveInteger]:
        """The minimum number of event occurrences within the given time interval."""
        return self.minNumberOfOccurrences

    def setMinNumberOfOccurrences(self, value: Optional[PositiveInteger]) -> "BurstPatternEventTriggering":
        """The minimum number of event occurrences within the given time interval. A None value is a no-op and does not overwrite an existing minNumberOfOccurrences."""
        if value is not None:
            self.minNumberOfOccurrences = value
        return self

    def getPatternJitter(self) -> Optional[MultidimensionalTime]:
        """The maximum deviation of the time interval's starting point from the beginning of the given period. This parameter is only applicable in conjunction with the parameter patternPeriod"""
        return self.patternJitter

    def setPatternJitter(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggering":
        """The maximum deviation of the time interval's starting point from the beginning of the given period. This parameter is only applicable in conjunction with the parameter patternPeriod A None value is a no-op and does not overwrite an existing patternJitter."""
        if value is not None:
            self.patternJitter = value
        return self

    def getPatternLength(self) -> Optional[MultidimensionalTime]:
        """The duration of the time interval within which the event repeatedly occurs. The event occurs at arbitrary points in time within the given time interval."""
        return self.patternLength

    def setPatternLength(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggering":
        """The duration of the time interval within which the event repeatedly occurs. The event occurs at arbitrary points in time within the given time interval. A None value is a no-op and does not overwrite an existing patternLength."""
        if value is not None:
            self.patternLength = value
        return self

    def getPatternPeriod(self) -> Optional[MultidimensionalTime]:
        """The time distance between the beginnings of subsequent repetitions of the given burst pattern."""
        return self.patternPeriod

    def setPatternPeriod(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggering":
        """The time distance between the beginnings of subsequent repetitions of the given burst pattern. A None value is a no-op and does not overwrite an existing patternPeriod."""
        if value is not None:
            self.patternPeriod = value
        return self


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """
    Describes that an event occurs occasionally, singly, irregularly or randomly. The primary purpose of this event triggering is to abstract event occurrences captured by data acquisition tools (background debugger, trace analyzer, etc.) during system runtime.
    """

    # ArbitraryEventTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.64, p.112
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addConfidenceInterval    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConfidenceIntervals   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addMaximumDistance       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximumDistances      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addMinimumDistance       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimumDistances      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # List of confidence intervals.
        self.confidenceIntervals: List["ConfidenceInterval"] = []

        # The nth array element describes the maximum distance that can be observed for a sample of n+1 event occurrences. This is an array with an identical number of elements as for the minimumDistance.
        self.maximumDistances: List[MultidimensionalTime] = []

        # The nth array element describes the minimum distance that can be observed for a sample of n+1 event occurrences. This is an array with an identical number of elements as for the maximumDistance.
        self.minimumDistances: List[MultidimensionalTime] = []

    def addConfidenceInterval(self, value: Optional["ConfidenceInterval"]) -> "ArbitraryEventTriggering":
        """List of confidence intervals. A None value is a no-op and does not change the confidenceIntervals list."""
        if value is not None:
            self.confidenceIntervals.append(value)
        return self

    def getConfidenceIntervals(self) -> List["ConfidenceInterval"]:
        """List of confidence intervals."""
        return self.confidenceIntervals

    def addMaximumDistance(self, value: Optional[MultidimensionalTime]) -> "ArbitraryEventTriggering":
        """The nth array element describes the maximum distance that can be observed for a sample of n+1 event occurrences. This is an array with an identical number of elements as for the minimumDistance. A None value is a no-op and does not change the maximumDistances list."""
        if value is not None:
            self.maximumDistances.append(value)
        return self

    def getMaximumDistances(self) -> List[MultidimensionalTime]:
        """The nth array element describes the maximum distance that can be observed for a sample of n+1 event occurrences. This is an array with an identical number of elements as for the minimumDistance."""
        return self.maximumDistances

    def addMinimumDistance(self, value: Optional[MultidimensionalTime]) -> "ArbitraryEventTriggering":
        """The nth array element describes the minimum distance that can be observed for a sample of n+1 event occurrences. This is an array with an identical number of elements as for the maximumDistance. A None value is a no-op and does not change the minimumDistances list."""
        if value is not None:
            self.minimumDistances.append(value)
        return self

    def getMinimumDistances(self) -> List[MultidimensionalTime]:
        """The nth array element describes the minimum distance that can be observed for a sample of n+1 event occurrences. This is an array with an identical number of elements as for the maximumDistance."""
        return self.minimumDistances


class ConfidenceInterval(ARObject):
    """
    Additionally to the list of measured distances of event occurrences, a confidence interval can be specified for the expected distance of two consecutive event occurrences with a given probability.
    """

    # ConfidenceInterval method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.65, p.112
    # Spec verified: R23-11
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
