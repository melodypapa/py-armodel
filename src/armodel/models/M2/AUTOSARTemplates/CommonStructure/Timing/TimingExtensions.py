"""
This module defines timing extension classes for AUTOSAR software component timing specifications.

Classes:
    TimingExtension: Abstract base class for timing extensions
    SwcTiming: Software component timing specification
"""

from typing import List, Optional
from abc import ABC

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import TimingClock, TimingClockSyncAccuracy
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingCondition, TimingExtensionResource
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TimingExtension(ARElement, ABC):
    """
    The abstract parent class of the different template specific timing extensions. Depending on the specific timing extension the timing descriptions and timing constraints, that can be used to specify the timing behavior, are restricted.
    """

    # TimingExtension method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.65, p.255
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addTimingClock                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingClocks                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createTimingClockSyncAccuracy   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingClockSyncAccuracies    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createTimingCondition           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingConditions             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTimingDescription            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTimingDescriptions           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addTimingGuarantee              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingGuarantees             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTimingRequirement            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingRequirements           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createTimingResource            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingResource               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createExecutionOrderConstraint  [x] impl  [—] docstring  [x] test  [—] reader  [—] writer   (convenience factory appending to timingRequirements)

    __metaclass__ = ABC

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is TimingExtension:
            raise TypeError("TimingExtension is an abstract class.")

        super().__init__(parent, short_name)

        # A list of abstract model Clocks.
        self.timingClocks: List[TimingClock] = []

        # A list of accuracies - which may be used to specify synchronizations from one model clock to another model clock.
        self.timingClockSyncAccuracies: List[TimingClockSyncAccuracy] = []

        # The timing condition specifies a specific condition.
        self.timingConditions: List[TimingCondition] = []

        # The timing descriptions that belong to a specific timing specification.
        # In order to support different timing description variants within a timing specification, the aggregation is marked with the stereotype "atpVariation".
        self.timingDescriptions: List[TimingDescription] = []

        # The timing constraints that belong to a specific timing specification in the role of a timing guarantee. In order to support different timing constraint variants within a timing specification, the aggregation is marked with the stereotype "atpVariation".
        self.timingGuarantees: List[TimingConstraint] = []

        # The timing constraints that belong to a specific timing specification in the role of a timing requirement. In order to support different timing constraint variants within a timing specification, the aggregation is marked with the stereotype "atpVariation".
        self.timingRequirements: List[TimingConstraint] = []

        # The timing resource contains all instance references referred from within a timing condition formula of a timing view.
        self.timingResource: Optional[TimingExtensionResource] = None

    def addTimingClock(self, value: Optional[TimingClock]) -> "TimingExtension":
        """A list of abstract model Clocks. A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingClocks.append(value)
        return self

    def getTimingClocks(self) -> List[TimingClock]:
        """A list of abstract model Clocks."""
        return self.timingClocks

    def createTimingClockSyncAccuracy(self, short_name: str) -> TimingClockSyncAccuracy:
        """A list of accuracies - which may be used to specify synchronizations from one model clock to another model clock."""
        if not self.IsElementExists(short_name, TimingClockSyncAccuracy):
            accuracy = TimingClockSyncAccuracy(self, short_name)
            self.addElement(accuracy)
            self.timingClockSyncAccuracies.append(accuracy)
        return self.getElement(short_name, TimingClockSyncAccuracy)

    def getTimingClockSyncAccuracies(self) -> List[TimingClockSyncAccuracy]:
        """A list of accuracies - which may be used to specify synchronizations from one model clock to another model clock."""
        return self.timingClockSyncAccuracies

    def createTimingCondition(self, short_name: str) -> TimingCondition:
        """The timing condition specifies a specific condition."""
        if not self.IsElementExists(short_name, TimingCondition):
            condition = TimingCondition(self, short_name)
            self.addElement(condition)
            self.timingConditions.append(condition)
        return self.getElement(short_name, TimingCondition)

    def getTimingConditions(self) -> List[TimingCondition]:
        """The timing condition specifies a specific condition."""
        return self.timingConditions

    def addTimingDescription(self, value: Optional[TimingDescription]) -> "TimingExtension":
        """The timing descriptions that belong to a specific timing specification. In order to support different timing description variants within a timing specification, the aggregation is marked with the stereotype "atpVariation". A None value is a no-op and does not append anything."""
        if value is not None:
            self.addElement(value)
            self.timingDescriptions.append(value)
        return self

    def getTimingDescriptions(self) -> List[TimingDescription]:
        """The timing descriptions that belong to a specific timing specification. In order to support different timing description variants within a timing specification, the aggregation is marked with the stereotype "atpVariation"."""
        return self.timingDescriptions

    def addTimingGuarantee(self, value: Optional[TimingConstraint]) -> "TimingExtension":
        """The timing constraints that belong to a specific timing specification in the role of a timing guarantee. In order to support different timing constraint variants within a timing specification, the aggregation is marked with the stereotype "atpVariation". A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingGuarantees.append(value)
        return self

    def getTimingGuarantees(self) -> List[TimingConstraint]:
        """The timing constraints that belong to a specific timing specification in the role of a timing guarantee. In order to support different timing constraint variants within a timing specification, the aggregation is marked with the stereotype "atpVariation"."""
        return self.timingGuarantees

    def addTimingRequirement(self, value: Optional[TimingConstraint]) -> "TimingExtension":
        """The timing constraints that belong to a specific timing specification in the role of a timing requirement. In order to support different timing constraint variants within a timing specification, the aggregation is marked with the stereotype "atpVariation". A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingRequirements.append(value)
        return self

    def getTimingRequirements(self) -> List[TimingConstraint]:
        """The timing constraints that belong to a specific timing specification in the role of a timing requirement. In order to support different timing constraint variants within a timing specification, the aggregation is marked with the stereotype "atpVariation"."""
        return self.timingRequirements

    def createTimingResource(self, short_name: str) -> TimingExtensionResource:
        """The timing resource contains all instance references referred from within a timing condition formula of a timing view."""
        if self.timingResource is None:
            resource = TimingExtensionResource(self, short_name)
            self.addElement(resource)
            self.timingResource = resource
        return self.timingResource

    def getTimingResource(self) -> Optional[TimingExtensionResource]:
        """The timing resource contains all instance references referred from within a timing condition formula of a timing view."""
        return self.timingResource

    def createExecutionOrderConstraint(self, short_name: str) -> ExecutionOrderConstraint:
        if not self.IsElementExists(short_name, ExecutionOrderConstraint):
            constraint = ExecutionOrderConstraint(self, short_name)
            self.addElement(constraint)
            self.timingRequirements.append(constraint)
        return self.getElement(short_name, ExecutionOrderConstraint)


class SwcTiming(TimingExtension):
    """
    The SwcTiming is used to describe the timing of an atomic software component. TimingDescriptions aggregated by SwcTiming are restricted to event chains referring to events which are derived from the classes TDEventVfb and TDEventSwcInternalBehavior.
    """

    # SwcTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.2, p.25
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBehaviorRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBehaviorRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints shall be defined within this scope.
        # Note! The reason for the cardinality of 0..1 is to ensure backward compatibility.
        self.behaviorRef: Optional[RefType] = None

    def getBehaviorRef(self) -> Optional[RefType]:
        """This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints shall be defined within this scope. Note! The reason for the cardinality of 0..1 is to ensure backward compatibility."""
        return self.behaviorRef

    def setBehaviorRef(self, value: Optional[RefType]) -> "SwcTiming":
        """This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints shall be defined within this scope. Note! The reason for the cardinality of 0..1 is to ensure backward compatibility. A None value is a no-op and does not overwrite an existing behaviorRef."""
        if value is not None:
            self.behaviorRef = value
        return self
