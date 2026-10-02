"""
This module contains the HeapUsage abstract class and its concrete subclasses for
representing heap memory usage in AUTOSAR resource consumption models.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, SoftwareContext


class HeapUsage(Identifiable, VariationPointCapable, ABC):
    """
    Describes the heap memory usage of a SW-Component.
    """

    # HeapUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.13, p.152
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getHardwareConfiguration     [x] impl  [x] docstring  [x] test
    # [x] setHardwareConfiguration     [x] impl  [x] docstring  [x] test
    # [x] getHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] setHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] getSoftwareContext           [x] impl  [x] docstring  [x] test
    # [x] setSoftwareContext           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the HeapUsage with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this heap usage
            short_name: The unique short name of this heap usage
        """
        if type(self) is HeapUsage:
            raise TypeError("HeapUsage is an abstract class.")

        super().__init__(parent, short_name)

        # Contains information about the hardware context this heap usage is describing.
        self.hardwareConfiguration: Optional[HardwareConfiguration] = None

        # Specifies for which hardware element (e.g. ECU) this heap usage is given.
        self.hwElementRef: Optional[RefType] = None

        # Contains details about the software context this heap usage is provided for.
        self.softwareContext: Optional[SoftwareContext] = None

    def getHardwareConfiguration(self) -> Optional[HardwareConfiguration]:
        """
        Gets the hardware configuration this heap usage is describing.

        Returns:
            HardwareConfiguration instance, or None if not set
        """
        return self.hardwareConfiguration

    def setHardwareConfiguration(self, value: Optional[HardwareConfiguration]) -> HeapUsage:
        """
        Sets the hardware configuration this heap usage is describing.
        A None value is a no-op and does not overwrite an existing configuration.

        Args:
            value: The hardware configuration to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hardwareConfiguration = value
        return self

    def getHwElementRef(self) -> Optional[RefType]:
        """
        Gets the reference to the hardware element (e.g. ECU) this heap usage is given for.

        Returns:
            RefType referencing the hardware element, or None if not set
        """
        return self.hwElementRef

    def setHwElementRef(self, value: Optional[RefType]) -> HeapUsage:
        """
        Sets the reference to the hardware element (e.g. ECU) this heap usage is given for.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The hardware element reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementRef = value
        return self

    def getSoftwareContext(self) -> Optional[SoftwareContext]:
        """
        Gets the software context this heap usage is provided for.

        Returns:
            SoftwareContext instance, or None if not set
        """
        return self.softwareContext

    def setSoftwareContext(self, value: Optional[SoftwareContext]) -> HeapUsage:
        """
        Sets the software context this heap usage is provided for.
        A None value is a no-op and does not overwrite an existing context.

        Args:
            value: The software context to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.softwareContext = value
        return self


class MeasuredHeapUsage(HeapUsage):
    """
    The heap usage has been measured.
    """

    # MeasuredHeapUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.15, p.152
# Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAverageMemoryConsumption [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setAverageMemoryConsumption [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMaximumMemoryConsumption [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMaximumMemoryConsumption [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMinimumMemoryConsumption [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMinimumMemoryConsumption [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getTestPattern              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setTestPattern              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The average heap usage measured. Unit: byte.
        self.averageMemoryConsumption: Optional[PositiveInteger] = None

        # The maximum heap usage measured. Unit: byte.
        self.maximumMemoryConsumption: Optional[PositiveInteger] = None

        # The minimum heap usage measured. Unit: byte.
        self.minimumMemoryConsumption: Optional[PositiveInteger] = None

        # Description of the test pattern used to acquire the measured values.
        self.testPattern: Optional[String] = None

    def getAverageMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        The average heap usage measured. Unit: byte.
        """
        return self.averageMemoryConsumption

    def setAverageMemoryConsumption(self, value: Optional[PositiveInteger]) -> MeasuredHeapUsage:
        """
        The average heap usage measured. Unit: byte.
        A None value is a no-op and does not overwrite an existing averageMemoryConsumption.
        """
        if value is not None:
            self.averageMemoryConsumption = value
        return self

    def getMaximumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        The maximum heap usage measured. Unit: byte.
        """
        return self.maximumMemoryConsumption

    def setMaximumMemoryConsumption(self, value: Optional[PositiveInteger]) -> MeasuredHeapUsage:
        """
        The maximum heap usage measured. Unit: byte.
        A None value is a no-op and does not overwrite an existing maximumMemoryConsumption.
        """
        if value is not None:
            self.maximumMemoryConsumption = value
        return self

    def getMinimumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        The minimum heap usage measured. Unit: byte.
        """
        return self.minimumMemoryConsumption

    def setMinimumMemoryConsumption(self, value: Optional[PositiveInteger]) -> MeasuredHeapUsage:
        """
        The minimum heap usage measured. Unit: byte.
        A None value is a no-op and does not overwrite an existing minimumMemoryConsumption.
        """
        if value is not None:
            self.minimumMemoryConsumption = value
        return self

    def getTestPattern(self) -> Optional[String]:
        """
        Description of the test pattern used to acquire the measured values.
        """
        return self.testPattern

    def setTestPattern(self, value: Optional[String]) -> MeasuredHeapUsage:
        """
        Description of the test pattern used to acquire the measured values.
        A None value is a no-op and does not overwrite an existing testPattern.
        """
        if value is not None:
            self.testPattern = value
        return self


class RoughEstimateHeapUsage(HeapUsage):
    """
    Rough estimation of the heap usage.
    """

    # RoughEstimateHeapUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.16, p.153
# Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMemoryConsumption        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMemoryConsumption        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Rough estimate of the heap usage. Unit: byte.
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Rough estimate of the heap usage. Unit: byte.
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> RoughEstimateHeapUsage:
        """
        Rough estimate of the heap usage. Unit: byte.
        A None value is a no-op and does not overwrite an existing memoryConsumption.
        """
        if value is not None:
            self.memoryConsumption = value
        return self


class WorstCaseHeapUsage(HeapUsage):
    """
    Provides a formal worst case heap usage.
    """

    # WorstCaseHeapUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.14, p.152
# Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMemoryConsumption        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMemoryConsumption        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Worst case heap consumption. Unit: byte.
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Worst case heap consumption. Unit: byte.
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> WorstCaseHeapUsage:
        """
        Worst case heap consumption. Unit: byte.
        A None value is a no-op and does not overwrite an existing memoryConsumption.
        """
        if value is not None:
            self.memoryConsumption = value
        return self
