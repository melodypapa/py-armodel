"""
This module defines timing extension classes for AUTOSAR software component timing specifications.

Timing extensions provide mechanisms to specify various timing constraints and requirements
for AUTOSAR software components. This includes execution order constraints and other
timing-related specifications that ensure proper temporal behavior of AUTOSAR components.

Classes:
    TimingExtension: Abstract base class for timing extensions
    SwcTiming: Software component timing specification
"""

__all__ = [
    'SwcTiming',
    'TimingExtension',
]


from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    ExecutionOrderConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Identifiable,
)


class TimingExtension(ARElement):
    """
    Abstract base class for timing extensions in AUTOSAR.
    This class cannot be instantiated directly and provides common functionality
    for timing extension implementations such as software component timing specifications.
    """
    __metaclass__ = ABC

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TimingExtension:
            raise TypeError("TimingExtension is an abstract class.")

        super().__init__(parent, short_name)

        self.timing_requirements: List[TimingConstraint] = []

    def createExecutionOrderConstraint(self, short_name: str)-> ExecutionOrderConstraint:
        """
        Creates a new execution order constraint with the specified short name.
        
        Args:
            short_name: Short name for the new execution order constraint
            
        Returns:
            The created ExecutionOrderConstraint instance
        """
        if not self.IsElementExists(short_name):
            constraint = ExecutionOrderConstraint(self, short_name)
            self.addElement(constraint)
            self.timing_requirements.append(constraint)
        return self.getElement(short_name, ExecutionOrderConstraint)

    def getTimingRequirements(self) -> List[TimingConstraint]:
        """
        Returns the list of timing requirements for this extension.
        
        Returns:
            List of timing constraint requirements
        """
        return self.timing_requirements


class SwcTiming(TimingExtension):
    """
    Software component timing specification that defines timing constraints
    for AUTOSAR software components. This class extends TimingExtension to
    provide component-specific timing functionality.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
