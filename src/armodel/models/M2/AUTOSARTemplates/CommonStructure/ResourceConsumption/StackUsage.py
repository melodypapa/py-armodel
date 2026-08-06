"""
This module contains classes for representing stack usage in AUTOSAR resource consumption models.
It includes abstract base classes and concrete implementations for different types of stack usage analysis.
"""

from __future__ import annotations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, SoftwareContext


class StackUsage(Identifiable, ABC):
    """
    Abstract base class for representing stack usage in AUTOSAR models.
    This class defines the basic structure for stack memory consumption tracking with hardware and software context.
    """

    # StackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.9, p.149
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getExecutableEntityRef       [x] impl  [x] docstring  [x] test
    # [x] setExecutableEntityRef       [x] impl  [x] docstring  [x] test
    # [x] getHardwareConfiguration     [x] impl  [x] docstring  [x] test
    # [x] setHardwareConfiguration     [x] impl  [x] docstring  [x] test
    # [x] getHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] setHwElementRef              [x] impl  [x] docstring  [x] test
    # [x] getSoftwareContext           [x] impl  [x] docstring  [x] test
    # [x] setSoftwareContext           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the StackUsage with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this stack usage
            short_name: The unique short name of this stack usage
        """
        if type(self) is StackUsage:
            raise TypeError("StackUsage is an abstract class.")

        super().__init__(parent, short_name)

        # Reference to the executable entity for which stack usage is measured
        self.executableEntityRef: Optional[RefType] = None

        # Hardware configuration associated with this stack usage
        self.hardwareConfiguration: Optional[HardwareConfiguration] = None

        # Reference to hardware element for this stack usage
        self.hwElementRef: Optional[RefType] = None

        # Software context for this stack usage
        self.softwareContext: Optional[SoftwareContext] = None

    def getExecutableEntityRef(self) -> Optional[RefType]:
        """
        Gets the reference to the executable entity for which stack usage is measured.

        Returns:
            RefType: Reference to the executable entity
        """
        return self.executableEntityRef

    def setExecutableEntityRef(self, value: Optional[RefType]) -> "StackUsage":
        """
        Sets the reference to the executable entity for which stack usage is measured.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The executable entity reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.executableEntityRef = value
        return self

    def getHardwareConfiguration(self) -> Optional[HardwareConfiguration]:
        """
        Gets the hardware configuration associated with this stack usage.

        Returns:
            HardwareConfiguration: Hardware configuration object
        """
        return self.hardwareConfiguration

    def setHardwareConfiguration(self, value: Optional[HardwareConfiguration]) -> "StackUsage":
        """
        Sets the hardware configuration associated with this stack usage.
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
        Gets the reference to hardware element for this stack usage.

        Returns:
            RefType: Reference to hardware element
        """
        return self.hwElementRef

    def setHwElementRef(self, value: Optional[RefType]) -> "StackUsage":
        """
        Sets the reference to hardware element for this stack usage.
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
        Gets the software context for this stack usage.

        Returns:
            SoftwareContext: Software context object
        """
        return self.softwareContext

    def setSoftwareContext(self, value: Optional[SoftwareContext]) -> "StackUsage":
        """
        Sets the software context for this stack usage.
        A None value is a no-op and does not overwrite an existing context.

        Args:
            value: The software context to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.softwareContext = value
        return self


class MeasuredStackUsage(StackUsage):
    """
    Represents measured stack usage in AUTOSAR models.
    This class provides concrete measurements of stack consumption under specific conditions.
    """

    # MeasuredStackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.11, p.150
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
        Initializes the MeasuredStackUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this measured stack usage
            short_name: The unique short name of this measured stack usage
        """
        super().__init__(parent, short_name)

        # Average memory consumption measured for this stack usage
        self.averageMemoryConsumption: Optional[PositiveInteger] = None

        # Maximum memory consumption measured for this stack usage
        self.maximumMemoryConsumption: Optional[PositiveInteger] = None

        # Minimum memory consumption measured for this stack usage
        self.minimumMemoryConsumption: Optional[PositiveInteger] = None

        # Description of the test pattern used to acquire the measured values
        self.testPattern: Optional[String] = None

    def getAverageMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the average memory consumption measured for this stack usage.

        Returns:
            PositiveInteger: Average memory consumption value
        """
        return self.averageMemoryConsumption

    def setAverageMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsage":
        """
        Sets the average memory consumption measured for this stack usage.

        Args:
            value: The average memory consumption value to set

        Returns:
            self for method chaining
        """
        self.averageMemoryConsumption = value
        return self

    def getMaximumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the maximum memory consumption measured for this stack usage.

        Returns:
            PositiveInteger: Maximum memory consumption value
        """
        return self.maximumMemoryConsumption

    def setMaximumMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsage":
        """
        Sets the maximum memory consumption measured for this stack usage.

        Args:
            value: The maximum memory consumption value to set

        Returns:
            self for method chaining
        """
        self.maximumMemoryConsumption = value
        return self

    def getMinimumMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the minimum memory consumption measured for this stack usage.

        Returns:
            PositiveInteger: Minimum memory consumption value
        """
        return self.minimumMemoryConsumption

    def setMinimumMemoryConsumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsage":
        """
        Sets the minimum memory consumption measured for this stack usage.

        Args:
            value: The minimum memory consumption value to set

        Returns:
            self for method chaining
        """
        self.minimumMemoryConsumption = value
        return self

    def getTestPattern(self) -> Optional[String]:
        """
        Gets the description of the test pattern used to acquire the measured values.

        Returns:
            String: Test pattern description
        """
        return self.testPattern

    def setTestPattern(self, value: Optional[String]) -> "MeasuredStackUsage":
        """
        Sets the description of the test pattern used to acquire the measured values.

        Args:
            value: The test pattern description to set

        Returns:
            self for method chaining
        """
        self.testPattern = value
        return self


class RoughEstimateStackUsage(StackUsage):
    """
    Represents rough estimate stack usage in AUTOSAR models.
    This class provides estimated values for stack consumption when exact measurements are not available.
    """

    # RoughEstimateStackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.12, p.151
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMemoryConsumption         [x] impl  [x] docstring  [x] test
    # [x] setMemoryConsumption         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RoughEstimateStackUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this rough estimate stack usage
            short_name: The unique short name of this rough estimate stack usage
        """
        super().__init__(parent, short_name)

        # Estimated memory consumption for this stack usage
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the estimated memory consumption for this stack usage.

        Returns:
            PositiveInteger: Estimated memory consumption value
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> "RoughEstimateStackUsage":
        """
        Sets the estimated memory consumption for this stack usage.

        Args:
            value: The estimated memory consumption value to set

        Returns:
            self for method chaining
        """
        self.memoryConsumption = value
        return self


class WorstCaseStackUsage(StackUsage):
    """
    Represents worst case stack usage in AUTOSAR models.
    This class provides the worst-case scenario analysis for stack consumption under maximum load conditions.
    """

    # WorstCaseStackUsage method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.10, p.150
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMemoryConsumption         [x] impl  [x] docstring  [x] test
    # [x] setMemoryConsumption         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the WorstCaseStackUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this worst case stack usage
            short_name: The unique short name of this worst case stack usage
        """
        super().__init__(parent, short_name)

        # Memory consumption in worst case scenario for this stack usage
        self.memoryConsumption: Optional[PositiveInteger] = None

    def getMemoryConsumption(self) -> Optional[PositiveInteger]:
        """
        Gets the memory consumption in worst case scenario for this stack usage.

        Returns:
            PositiveInteger: Worst case memory consumption value
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value: Optional[PositiveInteger]) -> "WorstCaseStackUsage":
        """
        Sets the memory consumption in worst case scenario for this stack usage.

        Args:
            value: The worst case memory consumption value to set

        Returns:
            self for method chaining
        """
        self.memoryConsumption = value
        return self
