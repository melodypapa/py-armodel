"""
This module defines synchronization point constraints in AUTOSAR timing specifications.

Synchronization point constraints specify synchronization requirements
between distributed AUTOSAR elements.

Classes:
    SynchronizationPointConstraint: Specifies synchronization point requirements
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class SynchronizationPointConstraint(TimingConstraint):
    """
    Specifies a synchronization point either between groups of ExecutableEntity s or individual ExecutableEntity s referenced via their corresponding RTE or BSW events.
    """

    # SynchronizationPointConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.77, p.132
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addSourceEecRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSourceEecRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSourceEventRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSourceEventRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTargetEecRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetEecRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTargetEventRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetEventRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The source executable entities cluster containing the executable entities that shall finish execution before the synchronization point.
        self.sourceEecRefs: List[RefType] = []

        # The executable entities -referenced by their events- that shall finish execution before the synchronization point.
        self.sourceEventRefs: List[RefType] = []

        # The target executable entities cluster containing the executable entities that shall start execution after the synchronization point.
        self.targetEecRefs: List[RefType] = []

        # The executable entities -referenced by their events- that shall start execution after the synchronization point.
        self.targetEventRefs: List[RefType] = []

    def addSourceEecRef(self, ref: Optional[RefType]) -> "SynchronizationPointConstraint":
        """The source executable entities cluster containing the executable entities that shall finish execution before the synchronization point. A None value is a no-op."""
        if ref is not None:
            self.sourceEecRefs.append(ref)
        return self

    def getSourceEecRefs(self) -> List[RefType]:
        """The source executable entities cluster containing the executable entities that shall finish execution before the synchronization point."""
        return self.sourceEecRefs

    def addSourceEventRef(self, ref: Optional[RefType]) -> "SynchronizationPointConstraint":
        """The executable entities -referenced by their events- that shall finish execution before the synchronization point. A None value is a no-op."""
        if ref is not None:
            self.sourceEventRefs.append(ref)
        return self

    def getSourceEventRefs(self) -> List[RefType]:
        """The executable entities -referenced by their events- that shall finish execution before the synchronization point."""
        return self.sourceEventRefs

    def addTargetEecRef(self, ref: Optional[RefType]) -> "SynchronizationPointConstraint":
        """The target executable entities cluster containing the executable entities that shall start execution after the synchronization point. A None value is a no-op."""
        if ref is not None:
            self.targetEecRefs.append(ref)
        return self

    def getTargetEecRefs(self) -> List[RefType]:
        """The target executable entities cluster containing the executable entities that shall start execution after the synchronization point."""
        return self.targetEecRefs

    def addTargetEventRef(self, ref: Optional[RefType]) -> "SynchronizationPointConstraint":
        """The executable entities -referenced by their events- that shall start execution after the synchronization point. A None value is a no-op."""
        if ref is not None:
            self.targetEventRefs.append(ref)
        return self

    def getTargetEventRefs(self) -> List[RefType]:
        """The executable entities -referenced by their events- that shall start execution after the synchronization point."""
        return self.targetEventRefs
