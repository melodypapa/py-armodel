"""
This module defines execution time constraints in AUTOSAR timing specifications.

Execution time constraints specify timing requirements for the execution
of entities such as runnables or operations.

Classes:
    ExecutionTimeConstraint: Specifies execution time requirements
    ExecutionTimeTypeEnum: Enumeration for execution time constraint types
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ComponentInCompositionInstanceRef
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
    Constrains the execution time of the referenced executable in component between a minimum and maximum interval. The time to execute the executable including interruptions by other entities and including external calls is commonly called "response time". The TimingExtensions provide the concept of event chains and latency constraints for that purpose. An event chain from the start of the entity to the termination of the entity with according latency constraint represents a response time constraint for that executable entity.
    """

    # ExecutionTimeConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.75, p.130
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getComponentIRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setComponentIRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecutableRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExecutableRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecutionTimeType        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExecutionTimeType        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximum                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximum                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimum                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimum                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The component that containts the referenced Executable Entity for the ExecutionTimeConstraint. If the entity is in a basic software module no component shall be provided. InstanceRef implemented by: ComponentInCompositionInstanceRef
        self.componentIRef: Optional[ComponentInCompositionInstanceRef] = None

        # The referenced ExecutableEntity for the ExecutionTime Constraint.
        self.executableRef: Optional[RefType] = None

        # Specifies the type of the execution time constrained by ExecutionTimeConstraint,
        self.executionTimeType: Optional[ExecutionTimeTypeEnum] = None

        # The maximum execution time.
        self.maximum: Optional[MultidimensionalTime] = None

        # The minimum execution time.
        self.minimum: Optional[MultidimensionalTime] = None

    def getComponentIRef(self) -> Optional[ComponentInCompositionInstanceRef]:
        """The component that containts the referenced Executable Entity for the ExecutionTimeConstraint. If the entity is in a basic software module no component shall be provided. InstanceRef implemented by: ComponentInCompositionInstanceRef"""
        return self.componentIRef

    def setComponentIRef(self, value: Optional[ComponentInCompositionInstanceRef]) -> "ExecutionTimeConstraint":
        """The component that containts the referenced Executable Entity for the ExecutionTimeConstraint. If the entity is in a basic software module no component shall be provided. InstanceRef implemented by: ComponentInCompositionInstanceRef. A None value is a no-op and does not overwrite an existing componentIRef."""
        if value is not None:
            self.componentIRef = value
        return self

    def getExecutableRef(self) -> Optional[RefType]:
        """The referenced ExecutableEntity for the ExecutionTime Constraint."""
        return self.executableRef

    def setExecutableRef(self, value: Optional[RefType]) -> "ExecutionTimeConstraint":
        """The referenced ExecutableEntity for the ExecutionTime Constraint. A None value is a no-op and does not overwrite an existing executable."""
        if value is not None:
            self.executableRef = value
        return self

    def getExecutionTimeType(self) -> Optional[ExecutionTimeTypeEnum]:
        """Specifies the type of the execution time constrained by ExecutionTimeConstraint,"""
        return self.executionTimeType

    def setExecutionTimeType(self, value: Optional[ExecutionTimeTypeEnum]) -> "ExecutionTimeConstraint":
        """Specifies the type of the execution time constrained by ExecutionTimeConstraint, A None value is a no-op and does not overwrite an existing executionTimeType."""
        if value is not None:
            self.executionTimeType = value
        return self

    def getMaximum(self) -> Optional[MultidimensionalTime]:
        """The maximum execution time."""
        return self.maximum

    def setMaximum(self, value: Optional[MultidimensionalTime]) -> "ExecutionTimeConstraint":
        """The maximum execution time. A None value is a no-op and does not overwrite an existing maximum."""
        if value is not None:
            self.maximum = value
        return self

    def getMinimum(self) -> Optional[MultidimensionalTime]:
        """The minimum execution time."""
        return self.minimum

    def setMinimum(self, value: Optional[MultidimensionalTime]) -> "ExecutionTimeConstraint":
        """The minimum execution time. A None value is a no-op and does not overwrite an existing minimum."""
        if value is not None:
            self.minimum = value
        return self
