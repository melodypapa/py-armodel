"""
This module defines timing extension classes for AUTOSAR software component timing specifications.

Classes:
    TimingExtension: Abstract base class for timing extensions
    SwcTiming: Software component timing specification
"""

from typing import List, Optional
from abc import ABC

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import (
    TimingCondition,
    TimingExtensionResource,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TimingExtension(ARElement, ABC):
    """
    The abstract parent class of the different template specific timing extensions.

    Depending on the specific timing extension (VfbTiming, SwcTiming, SystemTiming, BswModuleTiming, EcuTiming) the timing descriptions and timing constraints, that can be used to specify the timing behavior, are restricted.
    """

    # TimingExtension method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.65 (XSD group TIMING-EXTENSION), p.157
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addTimingGuarantee              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingConditions             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createTimingCondition           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingGuarantees             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTimingRequirements           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTimingRequirement            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createTimingResource            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingResource               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createExecutionOrderConstraint  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer   (convenience factory appending to timingRequirements)
    # timingDescription (* aggr, TimingDescription family) is NOT modeled: item classes out of scope (Rule 0001.10)

    __metaclass__ = ABC

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is TimingExtension:
            raise TypeError("TimingExtension is an abstract class.")

        super().__init__(parent, short_name)

        self.timingConditions: List[TimingCondition] = []

        self.timingGuarantees: List[TimingConstraint] = []

        self.timingRequirements: List[TimingConstraint] = []

        self.timingResource: Optional[TimingExtensionResource] = None

    def createTimingCondition(self, short_name: str) -> TimingCondition:
        if not self.IsElementExists(short_name):
            condition = TimingCondition(self, short_name)
            self.addElement(condition)
            self.timingConditions.append(condition)
        return self.getElement(short_name, TimingCondition)

    def getTimingConditions(self) -> List[TimingCondition]:
        return self.timingConditions

    def addTimingGuarantee(self, value: Optional[TimingConstraint]) -> "TimingExtension":
        """A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingGuarantees.append(value)
        return self

    def getTimingGuarantees(self) -> List[TimingConstraint]:
        return self.timingGuarantees

    def addTimingRequirement(self, value: Optional[TimingConstraint]) -> "TimingExtension":
        """A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingRequirements.append(value)
        return self

    def getTimingRequirements(self) -> List[TimingConstraint]:
        return self.timingRequirements

    def createTimingResource(self, short_name: str) -> TimingExtensionResource:
        if self.timingResource is None:
            resource = TimingExtensionResource(self, short_name)
            self.addElement(resource)
            self.timingResource = resource
        return self.timingResource

    def getTimingResource(self) -> Optional[TimingExtensionResource]:
        return self.timingResource

    def createExecutionOrderConstraint(self, short_name: str) -> ExecutionOrderConstraint:
        """Convenience factory creating an ExecutionOrderConstraint and appending it to timingRequirements."""
        if not self.IsElementExists(short_name):
            constraint = ExecutionOrderConstraint(self, short_name)
            self.addElement(constraint)
            self.timingRequirements.append(constraint)
        return self.getElement(short_name, ExecutionOrderConstraint)


class SwcTiming(TimingExtension):
    """
    The SwcTiming is used to describe the timing of an atomic software component. TimingDescriptions aggregated by SwcTiming are restricted to event chains referring to events which are derived from the classes TDEventVfb and TDEventSwcInternalBehavior.
    """

    # SwcTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.2, p.31
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBehaviorRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBehaviorRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints must be defined within this scope.
        # Note! The reason for the cardinality of 0..1 is to ensure backward compatibility.
        self.behaviorRef: Optional[RefType] = None

    def getBehaviorRef(self) -> Optional[RefType]:
        """This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints must be defined within this scope. Note! The reason for the cardinality of 0..1 is to ensure backward compatibility."""
        return self.behaviorRef

    def setBehaviorRef(self, value: Optional[RefType]) -> "SwcTiming":
        """This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints must be defined within this scope. Note! The reason for the cardinality of 0..1 is to ensure backward compatibility. A None value is a no-op and does not overwrite an existing behaviorRef."""
        if value is not None:
            self.behaviorRef = value
        return self
