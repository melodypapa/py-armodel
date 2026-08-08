"""
This module contains the HeapUsage abstract class and its concrete subclasses for
representing heap memory usage in AUTOSAR resource consumption models.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, SoftwareContext


class HeapUsage(Identifiable, ABC):
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

    def setHardwareConfiguration(self, value: Optional[HardwareConfiguration]) -> "HeapUsage":
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

    def setHwElementRef(self, value: Optional[RefType]) -> "HeapUsage":
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

    def setSoftwareContext(self, value: Optional[SoftwareContext]) -> "HeapUsage":
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
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAverageMemoryConsumption  [x] impl  [x] docstring  [x] test
    # [x] setAverageMemoryConsumption  [x] impl  [x] docstring  [x] test
    # [x] getMaximumMemoryConsumption  [x] impl  [x] docstring  [x] test
    # [x] setMaximumMemoryConsumption  [x] impl  [x] docstring  [x] test
    # [x] getMinimumMemoryConsumption  [x] impl  [x] docstring  [x] test
    # [x] setMinimumMemoryConsumption  [x] impl  [x] docstring  [x] test
    # [x] getTestPattern               [x] impl  [x] docstring  [x] test
    # [x] setTestPattern               [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the MeasuredHeapUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this measured heap usage
            short_name: The unique short name of this measured heap usage
        """
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
        Gets the average heap usage measured.

        Returns:
            PositiveInteger of the average heap usage, or None if not set
        """
        return self.averageMemoryConsumption

    def setAverageMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredHeapUsage":
        """
        Sets the average heap usage measured.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The average heap usage to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.averageMemoryConsumption = value
        return self

    def getMaximumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the maximum heap usage measured.

        Returns:
            PositiveInteger of the maximum heap usage, or None if not set
        """
        return self.maximumMemoryConsumption

    def setMaximumMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredHeapUsage":
        """
        Sets the maximum heap usage measured.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The maximum heap usage to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maximumMemoryConsumption = value
        return self

    def getMinimumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the minimum heap usage measured.

        Returns:
            PositiveInteger of the minimum heap usage, or None if not set
        """
        return self.minimumMemoryConsumption

    def setMinimumMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredHeapUsage":
        """
        Sets the minimum heap usage measured.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The minimum heap usage to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minimumMemoryConsumption = value
        return self

    def getTestPattern(self) -> Optional[String]:
        """
        Gets the description of the test pattern used to acquire the measured values.

        Returns:
            String describing the test pattern, or None if not set
        """
        return self.testPattern

    def setTestPattern(self, value: Optional[String]) -> "MeasuredHeapUsage":
        """
        Sets the description of the test pattern used to acquire the measured values.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The test pattern description to set

        Returns:
            self for method chaining
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
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMemoryConsumption         [x] impl  [x] docstring  [x] test
    # [x] setMemoryConsumption         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RoughEstimateHeapUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this rough estimate heap usage
            short_name: The unique short name of this rough estimate heap usage
        """
        super().__init__(parent, short_name)

        # Rough estimate of the heap usage. Unit: byte.
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the rough estimate of the heap usage.

        Returns:
            PositiveInteger of the rough estimate heap usage, or None if not set
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> "RoughEstimateHeapUsage":
        """
        Sets the rough estimate of the heap usage.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The rough estimate heap usage to set

        Returns:
            self for method chaining
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
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMemoryConsumption         [x] impl  [x] docstring  [x] test
    # [x] setMemoryConsumption         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the WorstCaseHeapUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this worst case heap usage
            short_name: The unique short name of this worst case heap usage
        """
        super().__init__(parent, short_name)

        # Worst case heap consumption. Unit: byte.
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the worst case heap consumption.

        Returns:
            PositiveInteger of the worst case heap usage, or None if not set
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> "WorstCaseHeapUsage":
        """
        Sets the worst case heap consumption.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The worst case heap usage to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.memoryConsumption = value
        return self
