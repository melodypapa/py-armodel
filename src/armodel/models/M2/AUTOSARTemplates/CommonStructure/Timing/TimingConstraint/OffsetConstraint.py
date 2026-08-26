"""
This module defines offset constraints in AUTOSAR timing specifications.

Offset constraints specify timing offsets relative to a reference event or time base.

Classes:
    OffsetTimingConstraint: Specifies timing offset requirements
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class OffsetTimingConstraint(TimingConstraint):
    """
    Bounds the time offset between the occurrence of two timing events, without requiring a direct functional dependency
    between the source and the target . If the target event occurs, it is expected to occur earliest with the minimum ,
    and latest with the maximum offset relatively after the occurrence of the source event. Note: not every source event
    occurrence shall be followed by a target event occurrence. In contrast to LatencyTimingConstraint , there shall not
    necessarily be a causal dependency between the source and target event.

    (source/target -> TimingDescriptionEvent placeholders, Rule 0001.10)
    """

    # OffsetTimingConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.66, p.114
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMaximum     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximum     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimum     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimum     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSourceRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSourceRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The maximum offset the target event occurs relatively after the occurrence of the source event. Tags: xml.sequenceOffset=20
        self.maximum: Optional[MultidimensionalTime] = None

        # The mimum offset the target event occurs relatively after the occurrence of the source event. Tags: xml.sequenceOffset=10
        self.minimum: Optional[MultidimensionalTime] = None

        # The timing event that the target event is to be synchronized with. (TimingDescriptionEvent placeholder, Rule 0001.10)
        self.sourceRef: Optional[RefType] = None

        # The timing event which is expected to occur timely after the source event. (TimingDescriptionEvent placeholder, Rule 0001.10)
        self.targetRef: Optional[RefType] = None

    def getMaximum(self) -> Optional[MultidimensionalTime]:
        """The maximum offset the target event occurs relatively after the occurrence of the source event."""
        return self.maximum

    def setMaximum(self, value: Optional[MultidimensionalTime]) -> "OffsetTimingConstraint":
        """The maximum offset the target event occurs relatively after the occurrence of the source event. A None value is a no-op and does not overwrite an existing maximum."""
        if value is not None:
            self.maximum = value
        return self

    def getMinimum(self) -> Optional[MultidimensionalTime]:
        """The mimum offset the target event occurs relatively after the occurrence of the source event."""
        return self.minimum

    def setMinimum(self, value: Optional[MultidimensionalTime]) -> "OffsetTimingConstraint":
        """The mimum offset the target event occurs relatively after the occurrence of the source event. A None value is a no-op and does not overwrite an existing minimum."""
        if value is not None:
            self.minimum = value
        return self

    def getSourceRef(self) -> Optional[RefType]:
        """The timing event that the target event is to be synchronized with."""
        return self.sourceRef

    def setSourceRef(self, value: Optional[RefType]) -> "OffsetTimingConstraint":
        """The timing event that the target event is to be synchronized with. A None value is a no-op and does not overwrite an existing source."""
        if value is not None:
            self.sourceRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """The timing event which is expected to occur timely after the source event."""
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "OffsetTimingConstraint":
        """The timing event which is expected to occur timely after the source event. A None value is a no-op and does not overwrite an existing target."""
        if value is not None:
            self.targetRef = value
        return self
