"""
This module defines latency timing constraints in AUTOSAR timing specifications.

Latency constraints specify the maximum allowed time between an event
occurrence and a response.

Classes:
    LatencyTimingConstraint: Specifies maximum allowed latency
    LatencyConstraintTypeEnum: Enumeration for latency constraint types
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class LatencyConstraintTypeEnum(AREnum):
    """
    Specifies the latencyConstraintType for a LatencyTimingConstraint .
    """

    # LatencyConstraintTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.58, p.96
    # Spec verified: R23-11
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
    Constrains the time duration between the occurrence of the stimulus and the occurrence of the corresponding response
    of that scope . In contrast to scope , a causal dependency between the stimulus and the corresponding response of the
    scope is required.

    (scope -> TimingDescriptionEventChain placeholder, Rule 0001.10)
    """

    # LatencyTimingConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.57, p.95
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLatencyConstraintType    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLatencyConstraintType    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximum                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximum                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimum                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimum                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNominal                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNominal                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScopeRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setScopeRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The specific type of this latency constraint.
        self.latencyConstraintType: Optional[LatencyConstraintTypeEnum] = None

        # The maximum latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain. Tags: xml.sequenceOffset=20
        self.maximum: Optional[MultidimensionalTime] = None

        # The minimum latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain. Tags: xml.sequenceOffset=10
        self.minimum: Optional[MultidimensionalTime] = None

        # The nominal latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain. Tags: xml.sequenceOffset=30
        self.nominal: Optional[MultidimensionalTime] = None

        # The event chain that defines the scope of the constraint. (TimingDescriptionEventChain placeholder, Rule 0001.10)
        self.scopeRef: Optional[RefType] = None

    def getLatencyConstraintType(self) -> Optional[LatencyConstraintTypeEnum]:
        """The specific type of this latency constraint."""
        return self.latencyConstraintType

    def setLatencyConstraintType(self, value: Optional[LatencyConstraintTypeEnum]) -> "LatencyTimingConstraint":
        """The specific type of this latency constraint. A None value is a no-op and does not overwrite an existing latencyConstraintType."""
        if value is not None:
            self.latencyConstraintType = value
        return self

    def getMaximum(self) -> Optional[MultidimensionalTime]:
        """The maximum latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain."""
        return self.maximum

    def setMaximum(self, value: Optional[MultidimensionalTime]) -> "LatencyTimingConstraint":
        """The maximum latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain. A None value is a no-op and does not overwrite an existing maximum."""
        if value is not None:
            self.maximum = value
        return self

    def getMinimum(self) -> Optional[MultidimensionalTime]:
        """The minimum latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain."""
        return self.minimum

    def setMinimum(self, value: Optional[MultidimensionalTime]) -> "LatencyTimingConstraint":
        """The minimum latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain. A None value is a no-op and does not overwrite an existing minimum."""
        if value is not None:
            self.minimum = value
        return self

    def getNominal(self) -> Optional[MultidimensionalTime]:
        """The nominal latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain."""
        return self.nominal

    def setNominal(self, value: Optional[MultidimensionalTime]) -> "LatencyTimingConstraint":
        """The nominal latency between the occurrence of the stimulus and the occurrence of the corresponding response of the associated event chain. A None value is a no-op and does not overwrite an existing nominal."""
        if value is not None:
            self.nominal = value
        return self

    def getScopeRef(self) -> Optional[RefType]:
        """The event chain that defines the scope of the constraint."""
        return self.scopeRef

    def setScopeRef(self, value: Optional[RefType]) -> "LatencyTimingConstraint":
        """The event chain that defines the scope of the constraint. A None value is a no-op and does not overwrite an existing scope."""
        if value is not None:
            self.scopeRef = value
        return self
