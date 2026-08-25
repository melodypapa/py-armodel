"""
This module defines execution time constraints in AUTOSAR timing specifications.

Execution time constraints specify timing requirements for the execution
of entities such as runnables or operations.

Classes:
    ExecutionTimeConstraint: Specifies execution time requirements
    ExecutionTimeTypeEnum: Enumeration for execution time constraint types
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class ExecutionTimeTypeEnum(AREnum):
    """
    Specifies the type of the executionTimeType for a ExecutionTimeConstraint .
    """

    # ExecutionTimeTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.76, p.131
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ExecutionTimeConstraint.executionTimeType
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # Indicates that the given execution time is the time used to execute the executable WITHOUT any interruption and WITH external calls.
    # Tags: atp.EnumerationLiteralIndex=0
    GROSS = "gross"

    # Indicates that the given execution time is the time used to execute the executable WITHOUT any interruption and WITHOUT any external calls.
    # Tags: atp.EnumerationLiteralIndex=1
    NET = "net"

    def __init__(self):
        """
        Initializes the ExecutionTimeTypeEnum with valid values.
        """
        super().__init__(
            (
                ExecutionTimeTypeEnum.GROSS,
                ExecutionTimeTypeEnum.NET,
            )
        )


class ExecutionTimeConstraint(TimingConstraint):
    """
    Specifies execution time requirements for AUTOSAR entities.
    This constraint defines timing limits for the execution of entities
    such as runnables, operations, or other executable entities.
    """

    # ExecutionTimeConstraint method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getExecutionType             [x] impl  [x] docstring  [ ] test
    # [ ] setExecutionType             [x] impl  [x] docstring  [ ] test
    # [ ] getExecutionTime             [x] impl  [x] docstring  [ ] test
    # [ ] setExecutionTime             [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        """
        Initializes the ExecutionTimeConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this execution time constraint
            short_name: The unique short name of this execution time constraint
        """
        super().__init__(parent, short_name)

        # Type of execution time constraint
        self.execution_type: ExecutionTimeTypeEnum = None
        # Maximum allowed execution time
        self.execution_time: TimeValue = None

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
