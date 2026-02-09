"""
AUTOSAR Package - ExecutionTime

Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ExecutionTime(Identifiable, ABC):
    """
    Base class for several means how to describe the ExecutionTime of software.
    The required context information is provided through this class.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::ExecutionTime
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 159, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2025, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ExecutionTime:
            raise TypeError("ExecutionTime is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the ExclusiveArea this execution time is.
        self._exclusiveArea: Optional["ExclusiveArea"] = None

    @property
    def exclusive_area(self) -> Optional["ExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea

    @exclusive_area.setter
    def exclusive_area(self, value: Optional["ExclusiveArea"]) -> None:
        """
        Set exclusiveArea with validation.
        
        Args:
            value: The exclusiveArea to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exclusiveArea = None
            return

        if not isinstance(value, ExclusiveArea):
            raise TypeError(
                f"exclusiveArea must be ExclusiveArea or None, got {type(value).__name__}"
            )
        self._exclusiveArea = value
        self._executableEntity: Optional["ExecutableEntity"] = None

    @property
    def executable_entity(self) -> Optional["ExecutableEntity"]:
        """Get executableEntity (Pythonic accessor)."""
        return self._executableEntity

    @executable_entity.setter
    def executable_entity(self, value: Optional["ExecutableEntity"]) -> None:
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
        # ExecutionTime.
        self._hardware: Optional["HardwareConfiguration"] = None

    @property
    def hardware(self) -> Optional["HardwareConfiguration"]:
        """Get hardware (Pythonic accessor)."""
        return self._hardware

    @hardware.setter
    def hardware(self, value: Optional["HardwareConfiguration"]) -> None:
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
        # type of ECU) for which the is specified.
        self._hwElement: Optional["HwElement"] = None

    @property
    def hw_element(self) -> Optional["HwElement"]:
        """Get hwElement (Pythonic accessor)."""
        return self._hwElement

    @hw_element.setter
    def hw_element(self, value: Optional["HwElement"]) -> None:
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
        # execution time data for the.
        self._includedLibrary: List["RefType"] = []

    @property
    def included_library(self) -> List["RefType"]:
        """Get includedLibrary (Pythonic accessor)."""
        return self._includedLibrary
        # Provides information on the MemorySectionLocation is involved in the
        # ExecutionTime description.
        self._memorySection: List["MemorySectionLocation"] = []

    @property
    def memory_section(self) -> List["MemorySectionLocation"]:
        """Get memorySection (Pythonic accessor)."""
        return self._memorySection
        # Provides information on the detailed SoftwareContext provide the
        # ExecutionTime description.
        self._softwareContext: Optional["SoftwareContext"] = None

    @property
    def software_context(self) -> Optional["SoftwareContext"]:
        """Get softwareContext (Pythonic accessor)."""
        return self._softwareContext

    @software_context.setter
    def software_context(self, value: Optional["SoftwareContext"]) -> None:
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

    def with_included_library(self, value):
        """
        Set included_library and return self for chaining.

        Args:
            value: The included_library to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_included_library("value")
        """
        self.included_library = value  # Use property setter (gets validation)
        return self

    def with_memory_section(self, value):
        """
        Set memory_section and return self for chaining.

        Args:
            value: The memory_section to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_section("value")
        """
        self.memory_section = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExclusiveArea(self) -> "ExclusiveArea":
        """
        AUTOSAR-compliant getter for exclusiveArea.
        
        Returns:
            The exclusiveArea value
        
        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def setExclusiveArea(self, value: "ExclusiveArea") -> "ExecutionTime":
        """
        AUTOSAR-compliant setter for exclusiveArea with method chaining.
        
        Args:
            value: The exclusiveArea to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to exclusive_area property setter (gets validation automatically)
        """
        self.exclusive_area = value  # Delegates to property setter
        return self

    def getExecutableEntity(self) -> "ExecutableEntity":
        """
        AUTOSAR-compliant getter for executableEntity.
        
        Returns:
            The executableEntity value
        
        Note:
            Delegates to executable_entity property (CODING_RULE_V2_00017)
        """
        return self.executable_entity  # Delegates to property

    def setExecutableEntity(self, value: "ExecutableEntity") -> "ExecutionTime":
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

    def getHardware(self) -> "HardwareConfiguration":
        """
        AUTOSAR-compliant getter for hardware.
        
        Returns:
            The hardware value
        
        Note:
            Delegates to hardware property (CODING_RULE_V2_00017)
        """
        return self.hardware  # Delegates to property

    def setHardware(self, value: "HardwareConfiguration") -> "ExecutionTime":
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

    def getHwElement(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for hwElement.
        
        Returns:
            The hwElement value
        
        Note:
            Delegates to hw_element property (CODING_RULE_V2_00017)
        """
        return self.hw_element  # Delegates to property

    def setHwElement(self, value: "HwElement") -> "ExecutionTime":
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

    def getIncludedLibrary(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for includedLibrary.
        
        Returns:
            The includedLibrary value
        
        Note:
            Delegates to included_library property (CODING_RULE_V2_00017)
        """
        return self.included_library  # Delegates to property

    def getMemorySection(self) -> List["MemorySectionLocation"]:
        """
        AUTOSAR-compliant getter for memorySection.
        
        Returns:
            The memorySection value
        
        Note:
            Delegates to memory_section property (CODING_RULE_V2_00017)
        """
        return self.memory_section  # Delegates to property

    def getSoftwareContext(self) -> "SoftwareContext":
        """
        AUTOSAR-compliant getter for softwareContext.
        
        Returns:
            The softwareContext value
        
        Note:
            Delegates to software_context property (CODING_RULE_V2_00017)
        """
        return self.software_context  # Delegates to property

    def setSoftwareContext(self, value: "SoftwareContext") -> "ExecutionTime":
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

    def with_exclusive_area(self, value: Optional["ExclusiveArea"]) -> "ExecutionTime":
        """
        Set exclusiveArea and return self for chaining.
        
        Args:
            value: The exclusiveArea to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_exclusive_area("value")
        """
        self.exclusive_area = value  # Use property setter (gets validation)
        return self

    def with_executable_entity(self, value: Optional["ExecutableEntity"]) -> "ExecutionTime":
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

    def with_hardware(self, value: Optional["HardwareConfiguration"]) -> "ExecutionTime":
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

    def with_hw_element(self, value: Optional["HwElement"]) -> "ExecutionTime":
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

    def with_software_context(self, value: Optional["SoftwareContext"]) -> "ExecutionTime":
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



class MemorySectionLocation(ARObject):
    """
    Specifies in which hardware ProvidedMemorySegment the softwareMemorySection
    is located.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::MemorySectionLocation
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 162, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the hardware ProvidedMemorySegment.
        self._providedMemory: Optional["HwElement"] = None

    @property
    def provided_memory(self) -> Optional["HwElement"]:
        """Get providedMemory (Pythonic accessor)."""
        return self._providedMemory

    @provided_memory.setter
    def provided_memory(self, value: Optional["HwElement"]) -> None:
        """
        Set providedMemory with validation.
        
        Args:
            value: The providedMemory to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedMemory = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"providedMemory must be HwElement or None, got {type(value).__name__}"
            )
        self._providedMemory = value
        self._software: Optional["MemorySection"] = None

    @property
    def software(self) -> Optional["MemorySection"]:
        """Get software (Pythonic accessor)."""
        return self._software

    @software.setter
    def software(self, value: Optional["MemorySection"]) -> None:
        """
        Set software with validation.
        
        Args:
            value: The software to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._software = None
            return

        if not isinstance(value, MemorySection):
            raise TypeError(
                f"software must be MemorySection or None, got {type(value).__name__}"
            )
        self._software = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedMemory(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for providedMemory.
        
        Returns:
            The providedMemory value
        
        Note:
            Delegates to provided_memory property (CODING_RULE_V2_00017)
        """
        return self.provided_memory  # Delegates to property

    def setProvidedMemory(self, value: "HwElement") -> "MemorySectionLocation":
        """
        AUTOSAR-compliant setter for providedMemory with method chaining.
        
        Args:
            value: The providedMemory to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to provided_memory property setter (gets validation automatically)
        """
        self.provided_memory = value  # Delegates to property setter
        return self

    def getSoftware(self) -> "MemorySection":
        """
        AUTOSAR-compliant getter for software.
        
        Returns:
            The software value
        
        Note:
            Delegates to software property (CODING_RULE_V2_00017)
        """
        return self.software  # Delegates to property

    def setSoftware(self, value: "MemorySection") -> "MemorySectionLocation":
        """
        AUTOSAR-compliant setter for software with method chaining.
        
        Args:
            value: The software to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to software property setter (gets validation automatically)
        """
        self.software = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided_memory(self, value: Optional["HwElement"]) -> "MemorySectionLocation":
        """
        Set providedMemory and return self for chaining.
        
        Args:
            value: The providedMemory to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_provided_memory("value")
        """
        self.provided_memory = value  # Use property setter (gets validation)
        return self

    def with_software(self, value: Optional["MemorySection"]) -> "MemorySectionLocation":
        """
        Set software and return self for chaining.
        
        Args:
            value: The software to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_software("value")
        """
        self.software = value  # Use property setter (gets validation)
        return self



class AnalyzedExecutionTime(ExecutionTime):
    """
    AnalyzedExecutionTime provides an analytic method for specifying the best
    and worst case execution time.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::AnalyzedExecutionTime
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 164, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The best case execution time (BCET) defines the amount of time the related
        # executable entity its execution.
        self._bestCase: Optional["MultidimensionalTime"] = None

    @property
    def best_case(self) -> Optional["MultidimensionalTime"]:
        """Get bestCase (Pythonic accessor)."""
        return self._bestCase

    @best_case.setter
    def best_case(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set bestCase with validation.
        
        Args:
            value: The bestCase to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bestCase = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"bestCase must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._bestCase = value
        # executable entity its execution.
        self._worstCase: Optional["MultidimensionalTime"] = None

    @property
    def worst_case(self) -> Optional["MultidimensionalTime"]:
        """Get worstCase (Pythonic accessor)."""
        return self._worstCase

    @worst_case.setter
    def worst_case(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set worstCase with validation.
        
        Args:
            value: The worstCase to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._worstCase = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"worstCase must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._worstCase = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBestCase(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for bestCase.
        
        Returns:
            The bestCase value
        
        Note:
            Delegates to best_case property (CODING_RULE_V2_00017)
        """
        return self.best_case  # Delegates to property

    def setBestCase(self, value: "MultidimensionalTime") -> "AnalyzedExecutionTime":
        """
        AUTOSAR-compliant setter for bestCase with method chaining.
        
        Args:
            value: The bestCase to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to best_case property setter (gets validation automatically)
        """
        self.best_case = value  # Delegates to property setter
        return self

    def getWorstCase(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for worstCase.
        
        Returns:
            The worstCase value
        
        Note:
            Delegates to worst_case property (CODING_RULE_V2_00017)
        """
        return self.worst_case  # Delegates to property

    def setWorstCase(self, value: "MultidimensionalTime") -> "AnalyzedExecutionTime":
        """
        AUTOSAR-compliant setter for worstCase with method chaining.
        
        Args:
            value: The worstCase to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to worst_case property setter (gets validation automatically)
        """
        self.worst_case = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_best_case(self, value: Optional["MultidimensionalTime"]) -> "AnalyzedExecutionTime":
        """
        Set bestCase and return self for chaining.
        
        Args:
            value: The bestCase to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_best_case("value")
        """
        self.best_case = value  # Use property setter (gets validation)
        return self

    def with_worst_case(self, value: Optional["MultidimensionalTime"]) -> "AnalyzedExecutionTime":
        """
        Set worstCase and return self for chaining.
        
        Args:
            value: The worstCase to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_worst_case("value")
        """
        self.worst_case = value  # Use property setter (gets validation)
        return self



class MeasuredExecutionTime(ExecutionTime):
    """
    Specifies the ExecutionTime which has been gathered using measurement means.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::MeasuredExecutionTime
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 166, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum measured execution time.
        self._maximumExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def maximum_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get maximumExecutionTime (Pythonic accessor)."""
        return self._maximumExecutionTime

    @maximum_execution_time.setter
    def maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximumExecutionTime with validation.
        
        Args:
            value: The maximumExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximumExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximumExecutionTime = value
        self._minimumExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def minimum_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get minimumExecutionTime (Pythonic accessor)."""
        return self._minimumExecutionTime

    @minimum_execution_time.setter
    def minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimumExecutionTime with validation.
        
        Args:
            value: The minimumExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimumExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimumExecutionTime = value
        self._nominalExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def nominal_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get nominalExecutionTime (Pythonic accessor)."""
        return self._nominalExecutionTime

    @nominal_execution_time.setter
    def nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set nominalExecutionTime with validation.
        
        Args:
            value: The nominalExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nominalExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"nominalExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._nominalExecutionTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximumExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximumExecutionTime.
        
        Returns:
            The maximumExecutionTime value
        
        Note:
            Delegates to maximum_execution_time property (CODING_RULE_V2_00017)
        """
        return self.maximum_execution_time  # Delegates to property

    def setMaximumExecutionTime(self, value: "MultidimensionalTime") -> "MeasuredExecutionTime":
        """
        AUTOSAR-compliant setter for maximumExecutionTime with method chaining.
        
        Args:
            value: The maximumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to maximum_execution_time property setter (gets validation automatically)
        """
        self.maximum_execution_time = value  # Delegates to property setter
        return self

    def getMinimumExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimumExecutionTime.
        
        Returns:
            The minimumExecutionTime value
        
        Note:
            Delegates to minimum_execution_time property (CODING_RULE_V2_00017)
        """
        return self.minimum_execution_time  # Delegates to property

    def setMinimumExecutionTime(self, value: "MultidimensionalTime") -> "MeasuredExecutionTime":
        """
        AUTOSAR-compliant setter for minimumExecutionTime with method chaining.
        
        Args:
            value: The minimumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_execution_time property setter (gets validation automatically)
        """
        self.minimum_execution_time = value  # Delegates to property setter
        return self

    def getNominalExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for nominalExecutionTime.
        
        Returns:
            The nominalExecutionTime value
        
        Note:
            Delegates to nominal_execution_time property (CODING_RULE_V2_00017)
        """
        return self.nominal_execution_time  # Delegates to property

    def setNominalExecutionTime(self, value: "MultidimensionalTime") -> "MeasuredExecutionTime":
        """
        AUTOSAR-compliant setter for nominalExecutionTime with method chaining.
        
        Args:
            value: The nominalExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nominal_execution_time property setter (gets validation automatically)
        """
        self.nominal_execution_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "MeasuredExecutionTime":
        """
        Set maximumExecutionTime and return self for chaining.
        
        Args:
            value: The maximumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_maximum_execution_time("value")
        """
        self.maximum_execution_time = value  # Use property setter (gets validation)
        return self

    def with_minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "MeasuredExecutionTime":
        """
        Set minimumExecutionTime and return self for chaining.
        
        Args:
            value: The minimumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_execution_time("value")
        """
        self.minimum_execution_time = value  # Use property setter (gets validation)
        return self

    def with_nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> "MeasuredExecutionTime":
        """
        Set nominalExecutionTime and return self for chaining.
        
        Args:
            value: The nominalExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nominal_execution_time("value")
        """
        self.nominal_execution_time = value  # Use property setter (gets validation)
        return self



class SimulatedExecutionTime(ExecutionTime):
    """
    Specifies the ExecutionTime which has been gathered using simulation means.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::SimulatedExecutionTime
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 167, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum simulated execution time.
        self._maximumExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def maximum_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get maximumExecutionTime (Pythonic accessor)."""
        return self._maximumExecutionTime

    @maximum_execution_time.setter
    def maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximumExecutionTime with validation.
        
        Args:
            value: The maximumExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximumExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximumExecutionTime = value
        self._minimumExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def minimum_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get minimumExecutionTime (Pythonic accessor)."""
        return self._minimumExecutionTime

    @minimum_execution_time.setter
    def minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimumExecutionTime with validation.
        
        Args:
            value: The minimumExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimumExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimumExecutionTime = value
        self._nominalExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def nominal_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get nominalExecutionTime (Pythonic accessor)."""
        return self._nominalExecutionTime

    @nominal_execution_time.setter
    def nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set nominalExecutionTime with validation.
        
        Args:
            value: The nominalExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nominalExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"nominalExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._nominalExecutionTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximumExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximumExecutionTime.
        
        Returns:
            The maximumExecutionTime value
        
        Note:
            Delegates to maximum_execution_time property (CODING_RULE_V2_00017)
        """
        return self.maximum_execution_time  # Delegates to property

    def setMaximumExecutionTime(self, value: "MultidimensionalTime") -> "SimulatedExecutionTime":
        """
        AUTOSAR-compliant setter for maximumExecutionTime with method chaining.
        
        Args:
            value: The maximumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to maximum_execution_time property setter (gets validation automatically)
        """
        self.maximum_execution_time = value  # Delegates to property setter
        return self

    def getMinimumExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimumExecutionTime.
        
        Returns:
            The minimumExecutionTime value
        
        Note:
            Delegates to minimum_execution_time property (CODING_RULE_V2_00017)
        """
        return self.minimum_execution_time  # Delegates to property

    def setMinimumExecutionTime(self, value: "MultidimensionalTime") -> "SimulatedExecutionTime":
        """
        AUTOSAR-compliant setter for minimumExecutionTime with method chaining.
        
        Args:
            value: The minimumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_execution_time property setter (gets validation automatically)
        """
        self.minimum_execution_time = value  # Delegates to property setter
        return self

    def getNominalExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for nominalExecutionTime.
        
        Returns:
            The nominalExecutionTime value
        
        Note:
            Delegates to nominal_execution_time property (CODING_RULE_V2_00017)
        """
        return self.nominal_execution_time  # Delegates to property

    def setNominalExecutionTime(self, value: "MultidimensionalTime") -> "SimulatedExecutionTime":
        """
        AUTOSAR-compliant setter for nominalExecutionTime with method chaining.
        
        Args:
            value: The nominalExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nominal_execution_time property setter (gets validation automatically)
        """
        self.nominal_execution_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "SimulatedExecutionTime":
        """
        Set maximumExecutionTime and return self for chaining.
        
        Args:
            value: The maximumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_maximum_execution_time("value")
        """
        self.maximum_execution_time = value  # Use property setter (gets validation)
        return self

    def with_minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "SimulatedExecutionTime":
        """
        Set minimumExecutionTime and return self for chaining.
        
        Args:
            value: The minimumExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_execution_time("value")
        """
        self.minimum_execution_time = value  # Use property setter (gets validation)
        return self

    def with_nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> "SimulatedExecutionTime":
        """
        Set nominalExecutionTime and return self for chaining.
        
        Args:
            value: The nominalExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nominal_execution_time("value")
        """
        self.nominal_execution_time = value  # Use property setter (gets validation)
        return self



class RoughEstimateOfExecutionTime(ExecutionTime):
    """
    Provides a description of a rough estimate on the ExecutionTime.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::RoughEstimateOfExecutionTime
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 167, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Provides description on the rough estimate of the.
        self._additional: Optional["String"] = None

    @property
    def additional(self) -> Optional["String"]:
        """Get additional (Pythonic accessor)."""
        return self._additional

    @additional.setter
    def additional(self, value: Optional["String"]) -> None:
        """
        Set additional with validation.
        
        Args:
            value: The additional to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._additional = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"additional must be String or str or None, got {type(value).__name__}"
            )
        self._additional = value
        self._estimatedExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def estimated_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get estimatedExecutionTime (Pythonic accessor)."""
        return self._estimatedExecutionTime

    @estimated_execution_time.setter
    def estimated_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set estimatedExecutionTime with validation.
        
        Args:
            value: The estimatedExecutionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._estimatedExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"estimatedExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._estimatedExecutionTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdditional(self) -> "String":
        """
        AUTOSAR-compliant getter for additional.
        
        Returns:
            The additional value
        
        Note:
            Delegates to additional property (CODING_RULE_V2_00017)
        """
        return self.additional  # Delegates to property

    def setAdditional(self, value: "String") -> "RoughEstimateOfExecutionTime":
        """
        AUTOSAR-compliant setter for additional with method chaining.
        
        Args:
            value: The additional to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to additional property setter (gets validation automatically)
        """
        self.additional = value  # Delegates to property setter
        return self

    def getEstimatedExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for estimatedExecutionTime.
        
        Returns:
            The estimatedExecutionTime value
        
        Note:
            Delegates to estimated_execution_time property (CODING_RULE_V2_00017)
        """
        return self.estimated_execution_time  # Delegates to property

    def setEstimatedExecutionTime(self, value: "MultidimensionalTime") -> "RoughEstimateOfExecutionTime":
        """
        AUTOSAR-compliant setter for estimatedExecutionTime with method chaining.
        
        Args:
            value: The estimatedExecutionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to estimated_execution_time property setter (gets validation automatically)
        """
        self.estimated_execution_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_additional(self, value: Optional["String"]) -> "RoughEstimateOfExecutionTime":
        """
        Set additional and return self for chaining.
        
        Args:
            value: The additional to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_additional("value")
        """
        self.additional = value  # Use property setter (gets validation)
        return self

    def with_estimated_execution_time(self, value: Optional["MultidimensionalTime"]) -> "RoughEstimateOfExecutionTime":
        """
        Set estimatedExecutionTime and return self for chaining.
        
        Args:
            value: The estimatedExecutionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_estimated_execution_time("value")
        """
        self.estimated_execution_time = value  # Use property setter (gets validation)
        return self
