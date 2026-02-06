"""
This module contains classes for representing stack usage in AUTOSAR resource consumption models.
It includes abstract base classes and concrete implementations for different types of stack usage analysis.
"""

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (
    SoftwareContext,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import (
    HardwareConfiguration,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)


class StackUsage(Identifiable, ABC):
    """
    Abstract base class for representing stack usage in AUTOSAR models.
    This class defines the basic structure for stack memory consumption tracking with hardware and software context.
    """

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
        self.executableEntityRef: RefType = None
        # Hardware configuration associated with this stack usage
        self.hardwareConfiguration: HardwareConfiguration = None
        # Reference to hardware element for this stack usage
        self.hwElementRef: RefType = None
        # Software context for this stack usage
        self.softwareContext: SoftwareContext = None

    def getExecutableEntityRef(self):
        """
        Gets the reference to the executable entity for which stack usage is measured.

        Returns:
            RefType: Reference to the executable entity
        """
        return self.executableEntityRef

    def setExecutableEntityRef(self, value):
        """
        Sets the reference to the executable entity for which stack usage is measured.

        Args:
            value: The executable entity reference to set

        Returns:
            self for method chaining
        """
        self.executableEntityRef = value
        return self

    def getHardwareConfiguration(self):
        """
        Gets the hardware configuration associated with this stack usage.

        Returns:
            HardwareConfiguration: Hardware configuration object
        """
        return self.hardwareConfiguration

    def setHardwareConfiguration(self, value):
        """
        Sets the hardware configuration associated with this stack usage.

        Args:
            value: The hardware configuration to set

        Returns:
            self for method chaining
        """
        self.hardwareConfiguration = value
        return self

    def getHwElementRef(self):
        """
        Gets the reference to hardware element for this stack usage.

        Returns:
            RefType: Reference to hardware element
        """
        return self.hwElementRef

    def setHwElementRef(self, value):
        """
        Sets the reference to hardware element for this stack usage.

        Args:
            value: The hardware element reference to set

        Returns:
            self for method chaining
        """
        self.hwElementRef = value
        return self

    def getSoftwareContext(self):
        """
        Gets the software context for this stack usage.

        Returns:
            SoftwareContext: Software context object
        """
        return self.softwareContext

    def setSoftwareContext(self, value):
        """
        Sets the software context for this stack usage.

        Args:
            value: The software context to set

        Returns:
            self for method chaining
        """
        self.softwareContext = value
        return self

class MeasuredStackUsage(StackUsage):
    """
    Represents measured stack usage in AUTOSAR models.
    This class provides concrete measurements of stack consumption under specific conditions.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the MeasuredStackUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this measured stack usage
            short_name: The unique short name of this measured stack usage
        """
        super().__init__(parent, short_name)

        # Average memory consumption measured for this stack usage
        self.averageMemoryConsumption: PositiveInteger = None
        # Maximum memory consumption measured for this stack usage
        self.maximumMemoryConsumption: PositiveInteger = None

    def getAverageMemoryConsumption(self):
        """
        Gets the average memory consumption measured for this stack usage.

        Returns:
            PositiveInteger: Average memory consumption value
        """
        return self.averageMemoryConsumption

    def setAverageMemoryConsumption(self, value):
        """
        Sets the average memory consumption measured for this stack usage.

        Args:
            value: The average memory consumption value to set

        Returns:
            self for method chaining
        """
        self.averageMemoryConsumption = value
        return self

    def getMaximumMemoryConsumption(self):
        """
        Gets the maximum memory consumption measured for this stack usage.

        Returns:
            PositiveInteger: Maximum memory consumption value
        """
        return self.maximumMemoryConsumption

    def setMaximumMemoryConsumption(self, value):
        """
        Sets the maximum memory consumption measured for this stack usage.

        Args:
            value: The maximum memory consumption value to set

        Returns:
            self for method chaining
        """
        self.maximumMemoryConsumption = value
        return self

class RoughEstimateStackUsage(StackUsage):
    """
    Represents rough estimate stack usage in AUTOSAR models.
    This class provides estimated values for stack consumption when exact measurements are not available.
    """

    def __init__(self, parent, short_name):
        """
        Initializes the RoughEstimateStackUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this rough estimate stack usage
            short_name: The unique short name of this rough estimate stack usage
        """
        super().__init__(parent, short_name)

        # Estimated memory consumption for this stack usage
        self.memoryConsumption: PositiveInteger = None

    def getMemoryConsumption(self):
        """
        Gets the estimated memory consumption for this stack usage.

        Returns:
            PositiveInteger: Estimated memory consumption value
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value):
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

    def __init__(self, parent, short_name):
        """
        Initializes the WorstCaseStackUsage with a parent and short name.

        Args:
            parent: The parent ARObject that contains this worst case stack usage
            short_name: The unique short name of this worst case stack usage
        """
        super().__init__(parent, short_name)

        # Memory consumption in worst case scenario for this stack usage
        self.memoryConsumption: PositiveInteger = None

    def getMemoryConsumption(self):
        """
        Gets the memory consumption in worst case scenario for this stack usage.

        Returns:
            PositiveInteger: Worst case memory consumption value
        """
        return self.memoryConsumption

    def setMemoryConsumption(self, value):
        """
        Sets the memory consumption in worst case scenario for this stack usage.

        Args:
            value: The worst case memory consumption value to set

        Returns:
            self for method chaining
        """
        self.memoryConsumption = value
        return self
