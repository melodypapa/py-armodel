"""
This module defines the abstract base class for timing constraints in AUTOSAR.

Timing constraints represent temporal relationships between AUTOSAR elements,
such as execution order, timing requirements, and synchronization constraints.
This module provides the base abstract class from which specific timing
constraint types inherit their common functionality.

Classes:
    TimingConstraint: Abstract base class for all timing constraints
"""

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from abc import ABC
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import Traceable


class TimingConstraint(Traceable, ABC):
    """
    Abstract base class for all timing constraints in AUTOSAR.
    This class cannot be instantiated directly and serves as the base for concrete
    timing constraint implementations such as execution order constraints.
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is TimingConstraint:
            raise TypeError("TimingConstraint is an abstract class.")

        super().__init__(parent, short_name)

        self.timing_condition_ref: RefType = None

    @property
    def timingConditionRef(self) -> RefType:
        """
        Gets the timing condition reference for this constraint.

        Returns:
            Reference to the timing condition
        """
        return self.timing_condition_ref

    @timingConditionRef.setter
    def timingConditionRef(self, ref: RefType):
        """
        Sets the timing condition reference for this constraint.

        Args:
            ref: Reference to the timing condition
        """
        self.timing_condition_ref = ref
