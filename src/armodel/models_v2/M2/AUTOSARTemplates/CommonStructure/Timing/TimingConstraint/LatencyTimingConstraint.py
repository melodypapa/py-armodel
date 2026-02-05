"""
This module defines latency timing constraints in AUTOSAR timing specifications.

Latency constraints specify the maximum allowed time between an event
occurrence and a response.

Classes:
    LatencyTimingConstraint: Specifies maximum allowed latency
    LatencyConstraintTypeEnum: Enumeration for latency constraint types
"""

from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    TimeValue,
)


class LatencyConstraintTypeEnum(AREnum):
    """
    Enumeration for latency constraint types.
    """

    RESPONSE_TIME = "response-time"
    REACTION_TIME = "reaction-time"
    END_TO_END_LATENCY = "end-to-end-latency"

    def __init__(self):
        super().__init__((
            LatencyConstraintTypeEnum.RESPONSE_TIME,
            LatencyConstraintTypeEnum.REACTION_TIME,
            LatencyConstraintTypeEnum.END_TO_END_LATENCY,
        ))


class LatencyTimingConstraint(TimingConstraint):
    """
    Specifies latency requirements in AUTOSAR timing specifications.
    This constraint defines the maximum allowed time between an event
    occurrence and a response.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the LatencyTimingConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this latency constraint
            short_name: The unique short name of this latency constraint
        """
        super().__init__(parent, short_name)

        # Type of latency constraint
        self.latency_type: LatencyConstraintTypeEnum = None
        # Maximum allowed latency
        self.latency: TimeValue = None

    def getLatencyType(self):
        """
        Gets the type of latency constraint.

        Returns:
            LatencyConstraintTypeEnum: The latency type
        """
        return self.latency_type

    def setLatencyType(self, value):
        """
        Sets the type of latency constraint.

        Args:
            value: The latency type to set

        Returns:
            self for method chaining
        """
        self.latency_type = value
        return self

    def getLatency(self):
        """
        Gets the maximum allowed latency.

        Returns:
            TimeValue: The maximum latency
        """
        return self.latency

    def setLatency(self, value):
        """
        Sets the maximum allowed latency.

        Args:
            value: The maximum latency to set

        Returns:
            self for method chaining
        """
        self.latency = value
        return self
