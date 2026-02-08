from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
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
        # The executable entity for which this execution time is.
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
        # Provides information on the HardwareConfiguration used specify this
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
        # The hardware element (e.
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
        # If this dependency is specified, the execution time of the is included in the
        # execution time data for the.
        self._includedLibrary: List[RefType] = []

    @property
    def included_library(self) -> List[RefType]:
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

    def getIncludedLibrary(self) -> List[RefType]:
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
