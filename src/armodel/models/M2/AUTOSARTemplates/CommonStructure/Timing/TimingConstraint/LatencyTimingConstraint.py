"""
This module defines latency timing constraints in AUTOSAR timing specifications.

Latency constraints specify the maximum allowed time between an event
occurrence and a response.

Classes:
    LatencyTimingConstraint: Specifies maximum allowed latency
    LatencyConstraintTypeEnum: Enumeration for latency constraint types
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class LatencyConstraintTypeEnum(AREnum):
    """
    Specifies the latencyConstraintType for a LatencyTimingConstraint .
    """

    # LatencyConstraintTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.58, p.96
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on LatencyTimingConstraint.latencyConstraintType
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The LatencyTimingConstraint is seen from the perspective of the response event of the scope . Given a certain response event, the age interval of the latest stimulus is constrained.
    # Tags: atp.EnumerationLiteralIndex=0
    AGE = "age"

    # The LatencyTimingConstraint is seen from the perspective of the stimulus event of the scope . Given a certain stimulus event, the reaction interval of the first response is constrained.
    # Tags: atp.EnumerationLiteralIndex=1
    REACTION = "reaction"

    def __init__(self):
        """
        Initializes the LatencyConstraintTypeEnum with valid values.
        """
        super().__init__(
            (
                LatencyConstraintTypeEnum.AGE,
                LatencyConstraintTypeEnum.REACTION,
            )
        )


class LatencyTimingConstraint(TimingConstraint):
    """
    Specifies latency requirements in AUTOSAR timing specifications.
    This constraint defines the maximum allowed time between an event
    occurrence and a response.
    """

    # LatencyTimingConstraint method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getLatencyType               [x] impl  [x] docstring  [ ] test
    # [ ] setLatencyType               [x] impl  [x] docstring  [ ] test
    # [ ] getLatency                   [x] impl  [x] docstring  [ ] test
    # [ ] setLatency                   [x] impl  [x] docstring  [ ] test

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
