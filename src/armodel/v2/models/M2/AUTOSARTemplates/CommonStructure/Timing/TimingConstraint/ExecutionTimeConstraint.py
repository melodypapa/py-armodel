"""
This module defines execution time constraints in AUTOSAR timing specifications.

Execution time constraints specify timing requirements for the execution
of entities such as runnables or operations.

Classes:
    ExecutionTimeConstraint: Specifies execution time requirements
    ExecutionTimeTypeEnum: Enumeration for execution time constraint types
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    TimeValue,
)


class ExecutionTimeTypeEnum(AREnum):
    """
    Enumeration for execution time constraint types.
    """

    BEST_CASE = "best-case"
    WORST_CASE = "worst-case"
    AVERAGE_CASE = "average-case"

    def __init__(self) -> None:
        super().__init__((
            ExecutionTimeTypeEnum.BEST_CASE,
            ExecutionTimeTypeEnum.WORST_CASE,
            ExecutionTimeTypeEnum.AVERAGE_CASE,
        ))


class ExecutionTimeConstraint(TimingConstraint):
    """
    Specifies execution time requirements for AUTOSAR entities.
    This constraint defines timing limits for the execution of entities
    such as runnables, operations, or other executable entities.
    """

    def __init__(self, parent, short_name: str) -> None:
        """
        Initializes the ExecutionTimeConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this execution time constraint
            short_name: The unique short name of this execution time constraint
        """
        super().__init__(parent, short_name)

        # Type of execution time constraint
        self.execution_type: Union[Union[ExecutionTimeTypeEnum, None] , None] = None
        # Maximum allowed execution time
        self.execution_time: Union[Union[TimeValue, None] , None] = None

    def getExecutionType(self):
        """
        Gets the type of execution time constraint.

        Returns:
            ExecutionTimeTypeEnum: The execution time type
        """
        return self.execution_type

    def setExecutionType(self, value):
        """
        Sets the type of execution time constraint.

        Args:
            value: The execution time type to set

        Returns:
            self for method chaining
        """
        self.execution_type = value
        return self

    def getExecutionTime(self):
        """
        Gets the maximum allowed execution time.

        Returns:
            TimeValue: The maximum execution time
        """
        return self.execution_time

    def setExecutionTime(self, value):
        """
        Sets the maximum allowed execution time.

        Args:
            value: The maximum execution time to set

        Returns:
            self for method chaining
        """
        self.execution_time = value
        return self
