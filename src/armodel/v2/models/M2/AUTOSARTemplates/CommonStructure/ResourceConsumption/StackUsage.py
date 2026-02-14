"""
AUTOSAR Package - StackUsage

Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage
"""


from __future__ import annotations

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (
    HardwareConfiguration,
    SoftwareContext,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class StackUsage(Identifiable, ABC):
    """
    Describes the stack memory usage of a software.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage::StackUsage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 149, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2059, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is StackUsage:
            raise TypeError("StackUsage is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The executable entity for which this stack usage is.
        self._executableEntity: Optional[ExecutableEntity] = None

    @property
    def executable_entity(self) -> Optional[ExecutableEntity]:
        """Get executableEntity (Pythonic accessor)."""
        return self._executableEntity

    @executable_entity.setter
    def executable_entity(self, value: Optional[ExecutableEntity]) -> None:
        """
        Set executableEntity with validation.

        Args:
            value: The executableEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executableEntity = None
            return

        if not isinstance(value, ExecutableEntity):
            raise TypeError(
                f"executableEntity must be ExecutableEntity or None, got {type(value).__name__}"
            )
        self._executableEntity = value
        self._hardware: Optional[HardwareConfiguration] = None

    @property
    def hardware(self) -> Optional[HardwareConfiguration]:
        """Get hardware (Pythonic accessor)."""
        return self._hardware

    @hardware.setter
    def hardware(self, value: Optional[HardwareConfiguration]) -> None:
        """
        Set hardware with validation.

        Args:
            value: The hardware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hardware = None
            return

        if not isinstance(value, HardwareConfiguration):
            raise TypeError(
                f"hardware must be HardwareConfiguration or None, got {type(value).__name__}"
            )
        self._hardware = value
        # g.
        # ECU) this is given.
        self._hwElement: Optional[HwElement] = None

    @property
    def hw_element(self) -> Optional[HwElement]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement

    @hw_element.setter
    def hw_element(self, value: Optional[HwElement]) -> None:
        """
        Set hwElement with validation.

        Args:
            value: The hwElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwElement = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"hwElement must be HwElement or None, got {type(value).__name__}"
            )
        self._hwElement = value
        self._softwareContext: Optional[SoftwareContext] = None

    @property
    def software_context(self) -> Optional[SoftwareContext]:
        """Get softwareContext (Pythonic accessor)."""
        return self._softwareContext

    @software_context.setter
    def software_context(self, value: Optional[SoftwareContext]) -> None:
        """
        Set softwareContext with validation.

        Args:
            value: The softwareContext to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._softwareContext = None
            return

        if not isinstance(value, SoftwareContext):
            raise TypeError(
                f"softwareContext must be SoftwareContext or None, got {type(value).__name__}"
            )
        self._softwareContext = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecutableEntity(self) -> ExecutableEntity:
        """
        AUTOSAR-compliant getter for executableEntity.

        Returns:
            The executableEntity value

        Note:
            Delegates to executable_entity property (CODING_RULE_V2_00017)
        """
        return self.executable_entity  # Delegates to property

    def setExecutableEntity(self, value: ExecutableEntity) -> StackUsage:
        """
        AUTOSAR-compliant setter for executableEntity with method chaining.

        Args:
            value: The executableEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to executable_entity property setter (gets validation automatically)
        """
        self.executable_entity = value  # Delegates to property setter
        return self

    def getHardware(self) -> HardwareConfiguration:
        """
        AUTOSAR-compliant getter for hardware.

        Returns:
            The hardware value

        Note:
            Delegates to hardware property (CODING_RULE_V2_00017)
        """
        return self.hardware  # Delegates to property

    def setHardware(self, value: HardwareConfiguration) -> StackUsage:
        """
        AUTOSAR-compliant setter for hardware with method chaining.

        Args:
            value: The hardware to set

        Returns:
            self for method chaining

        Note:
            Delegates to hardware property setter (gets validation automatically)
        """
        self.hardware = value  # Delegates to property setter
        return self

    def getHwElement(self) -> HwElement:
        """
        AUTOSAR-compliant getter for hwElement.

        Returns:
            The hwElement value

        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def setHwElement(self, value: HwElement) -> StackUsage:
        """
        AUTOSAR-compliant setter for hwElement with method chaining.

        Args:
            value: The hwElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to hw_element property setter (gets validation automatically)
        """
        self.hw_element = value  # Delegates to property setter
        return self

    def getSoftwareContext(self) -> SoftwareContext:
        """
        AUTOSAR-compliant getter for softwareContext.

        Returns:
            The softwareContext value

        Note:
            Delegates to software_context property (CODING_RULE_V2_00017)
        """
        return self.software_context  # Delegates to property

    def setSoftwareContext(self, value: SoftwareContext) -> StackUsage:
        """
        AUTOSAR-compliant setter for softwareContext with method chaining.

        Args:
            value: The softwareContext to set

        Returns:
            self for method chaining

        Note:
            Delegates to software_context property setter (gets validation automatically)
        """
        self.software_context = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_executable_entity(self, value: Optional[ExecutableEntity]) -> StackUsage:
        """
        Set executableEntity and return self for chaining.

        Args:
            value: The executableEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_executable_entity("value")
        """
        self.executable_entity = value  # Use property setter (gets validation)
        return self

    def with_hardware(self, value: Optional[HardwareConfiguration]) -> StackUsage:
        """
        Set hardware and return self for chaining.

        Args:
            value: The hardware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hardware("value")
        """
        self.hardware = value  # Use property setter (gets validation)
        return self

    def with_hw_element(self, value: Optional[HwElement]) -> StackUsage:
        """
        Set hwElement and return self for chaining.

        Args:
            value: The hwElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hw_element("value")
        """
        self.hw_element = value  # Use property setter (gets validation)
        return self

    def with_software_context(self, value: Optional[SoftwareContext]) -> StackUsage:
        """
        Set softwareContext and return self for chaining.

        Args:
            value: The softwareContext to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software_context("value")
        """
        self.software_context = value  # Use property setter (gets validation)
        return self



class WorstCaseStackUsage(StackUsage):
    """
    Provides a formal worst case stack usage.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage::WorstCaseStackUsage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 150, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Worst case stack consumption.
        # Unit: byte.
        self._memoryConsumption: Optional[PositiveInteger] = None

    @property
    def memory_consumption(self) -> Optional[PositiveInteger]:
        """Get memoryConsumption (Pythonic accessor)."""
        return self._memoryConsumption

    @memory_consumption.setter
    def memory_consumption(self, value: Optional[PositiveInteger]) -> None:
        """
        Set memoryConsumption with validation.

        Args:
            value: The memoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryConsumption = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"memoryConsumption must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._memoryConsumption = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMemoryConsumption(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for memoryConsumption.

        Returns:
            The memoryConsumption value

        Note:
            Delegates to memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.memory_consumption  # Delegates to property

    def setMemoryConsumption(self, value: PositiveInteger) -> WorstCaseStackUsage:
        """
        AUTOSAR-compliant setter for memoryConsumption with method chaining.

        Args:
            value: The memoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_consumption property setter (gets validation automatically)
        """
        self.memory_consumption = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_memory_consumption(self, value: Optional[PositiveInteger]) -> WorstCaseStackUsage:
        """
        Set memoryConsumption and return self for chaining.

        Args:
            value: The memoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_consumption("value")
        """
        self.memory_consumption = value  # Use property setter (gets validation)
        return self



class MeasuredStackUsage(StackUsage):
    """
    The stack usage has been measured.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage::MeasuredStackUsage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 150, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The average stack usage measured.
        # Unit: byte.
        self._averageMemoryConsumption: Optional[PositiveInteger] = None

    @property
    def average_memory_consumption(self) -> Optional[PositiveInteger]:
        """Get averageMemoryConsumption (Pythonic accessor)."""
        return self._averageMemoryConsumption

    @average_memory_consumption.setter
    def average_memory_consumption(self, value: Optional[PositiveInteger]) -> None:
        """
        Set averageMemoryConsumption with validation.

        Args:
            value: The averageMemoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._averageMemoryConsumption = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"averageMemoryConsumption must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._averageMemoryConsumption = value
        # Unit: byte.
        self._maximumMemoryConsumption: Optional[PositiveInteger] = None

    @property
    def maximum_memory_consumption(self) -> Optional[PositiveInteger]:
        """Get maximumMemoryConsumption (Pythonic accessor)."""
        return self._maximumMemoryConsumption

    @maximum_memory_consumption.setter
    def maximum_memory_consumption(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maximumMemoryConsumption with validation.

        Args:
            value: The maximumMemoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumMemoryConsumption = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maximumMemoryConsumption must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maximumMemoryConsumption = value
        # Unit: byte.
        self._minimumMemoryConsumption: Optional[PositiveInteger] = None

    @property
    def minimum_memory_consumption(self) -> Optional[PositiveInteger]:
        """Get minimumMemoryConsumption (Pythonic accessor)."""
        return self._minimumMemoryConsumption

    @minimum_memory_consumption.setter
    def minimum_memory_consumption(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minimumMemoryConsumption with validation.

        Args:
            value: The minimumMemoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumMemoryConsumption = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minimumMemoryConsumption must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minimumMemoryConsumption = value
        self._testPattern: Optional[String] = None

    @property
    def test_pattern(self) -> Optional[String]:
        """Get testPattern (Pythonic accessor)."""
        return self._testPattern

    @test_pattern.setter
    def test_pattern(self, value: Optional[String]) -> None:
        """
        Set testPattern with validation.

        Args:
            value: The testPattern to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._testPattern = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"testPattern must be String or str or None, got {type(value).__name__}"
            )
        self._testPattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAverageMemoryConsumption(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for averageMemoryConsumption.

        Returns:
            The averageMemoryConsumption value

        Note:
            Delegates to average_memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.average_memory_consumption  # Delegates to property

    def setAverageMemoryConsumption(self, value: PositiveInteger) -> MeasuredStackUsage:
        """
        AUTOSAR-compliant setter for averageMemoryConsumption with method chaining.

        Args:
            value: The averageMemoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to average_memory_consumption property setter (gets validation automatically)
        """
        self.average_memory_consumption = value  # Delegates to property setter
        return self

    def getMaximumMemoryConsumption(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maximumMemoryConsumption.

        Returns:
            The maximumMemoryConsumption value

        Note:
            Delegates to maximum_memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.maximum_memory_consumption  # Delegates to property

    def setMaximumMemoryConsumption(self, value: PositiveInteger) -> MeasuredStackUsage:
        """
        AUTOSAR-compliant setter for maximumMemoryConsumption with method chaining.

        Args:
            value: The maximumMemoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum_memory_consumption property setter (gets validation automatically)
        """
        self.maximum_memory_consumption = value  # Delegates to property setter
        return self

    def getMinimumMemoryConsumption(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minimumMemoryConsumption.

        Returns:
            The minimumMemoryConsumption value

        Note:
            Delegates to minimum_memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.minimum_memory_consumption  # Delegates to property

    def setMinimumMemoryConsumption(self, value: PositiveInteger) -> MeasuredStackUsage:
        """
        AUTOSAR-compliant setter for minimumMemoryConsumption with method chaining.

        Args:
            value: The minimumMemoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_memory_consumption property setter (gets validation automatically)
        """
        self.minimum_memory_consumption = value  # Delegates to property setter
        return self

    def getTestPattern(self) -> String:
        """
        AUTOSAR-compliant getter for testPattern.

        Returns:
            The testPattern value

        Note:
            Delegates to test_pattern property (CODING_RULE_V2_00017)
        """
        return self.test_pattern  # Delegates to property

    def setTestPattern(self, value: String) -> MeasuredStackUsage:
        """
        AUTOSAR-compliant setter for testPattern with method chaining.

        Args:
            value: The testPattern to set

        Returns:
            self for method chaining

        Note:
            Delegates to test_pattern property setter (gets validation automatically)
        """
        self.test_pattern = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_average_memory_consumption(self, value: Optional[PositiveInteger]) -> MeasuredStackUsage:
        """
        Set averageMemoryConsumption and return self for chaining.

        Args:
            value: The averageMemoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_average_memory_consumption("value")
        """
        self.average_memory_consumption = value  # Use property setter (gets validation)
        return self

    def with_maximum_memory_consumption(self, value: Optional[PositiveInteger]) -> MeasuredStackUsage:
        """
        Set maximumMemoryConsumption and return self for chaining.

        Args:
            value: The maximumMemoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum_memory_consumption("value")
        """
        self.maximum_memory_consumption = value  # Use property setter (gets validation)
        return self

    def with_minimum_memory_consumption(self, value: Optional[PositiveInteger]) -> MeasuredStackUsage:
        """
        Set minimumMemoryConsumption and return self for chaining.

        Args:
            value: The minimumMemoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_memory_consumption("value")
        """
        self.minimum_memory_consumption = value  # Use property setter (gets validation)
        return self

    def with_test_pattern(self, value: Optional[String]) -> MeasuredStackUsage:
        """
        Set testPattern and return self for chaining.

        Args:
            value: The testPattern to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_test_pattern("value")
        """
        self.test_pattern = value  # Use property setter (gets validation)
        return self



class RoughEstimateStackUsage(StackUsage):
    """
    Rough estimation of the stack usage.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage::RoughEstimateStackUsage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 151, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Rough estimate of the stack usage.
        # Unit: byte.
        self._memoryConsumption: Optional[PositiveInteger] = None

    @property
    def memory_consumption(self) -> Optional[PositiveInteger]:
        """Get memoryConsumption (Pythonic accessor)."""
        return self._memoryConsumption

    @memory_consumption.setter
    def memory_consumption(self, value: Optional[PositiveInteger]) -> None:
        """
        Set memoryConsumption with validation.

        Args:
            value: The memoryConsumption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryConsumption = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"memoryConsumption must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._memoryConsumption = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMemoryConsumption(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for memoryConsumption.

        Returns:
            The memoryConsumption value

        Note:
            Delegates to memory_consumption property (CODING_RULE_V2_00017)
        """
        return self.memory_consumption  # Delegates to property

    def setMemoryConsumption(self, value: PositiveInteger) -> RoughEstimateStackUsage:
        """
        AUTOSAR-compliant setter for memoryConsumption with method chaining.

        Args:
            value: The memoryConsumption to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_consumption property setter (gets validation automatically)
        """
        self.memory_consumption = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_memory_consumption(self, value: Optional[PositiveInteger]) -> RoughEstimateStackUsage:
        """
        Set memoryConsumption and return self for chaining.

        Args:
            value: The memoryConsumption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_consumption("value")
        """
        self.memory_consumption = value  # Use property setter (gets validation)
        return self
