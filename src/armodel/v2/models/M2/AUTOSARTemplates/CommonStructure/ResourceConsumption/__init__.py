"""
AUTOSAR Package - ResourceConsumption

Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
)


class ResourceConsumption(Identifiable):
    """
    Description of consumed resources by one implementation of a software.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ResourceConsumption

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 137, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 260, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 238, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Set of access count values atpSplitable; atpVariation 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._accessCount: List[RefType] = []

    @property
    def access_count(self) -> List[RefType]:
        """Get accessCount (Pythonic accessor)."""
        return self._accessCount
        # Collection of the execution time descriptions for this aggregation of
                # executionTime is variability with the purpose to support the of runnable
                # entities.
        # atpVariation.
        self._executionTime: List[ExecutionTime] = []

    @property
    def execution_time(self) -> List[ExecutionTime]:
        """Get executionTime (Pythonic accessor)."""
        return self._executionTime
        # Collection of the heap memory allocated by this atpVariation.
        self._heapUsage: List[HeapUsage] = []

    @property
    def heap_usage(self) -> List[HeapUsage]:
        """Get heapUsage (Pythonic accessor)."""
        return self._heapUsage
        # An abstract memory section required by this atpVariation.
        self._memorySection: List[MemorySection] = []

    @property
    def memory_section(self) -> List[MemorySection]:
        """Get memorySection (Pythonic accessor)."""
        return self._memorySection
        # A prefix to be used for the memory section symbol in the atpVariation.
        self._sectionName: List["SectionNamePrefix"] = []

    @property
    def section_name(self) -> List["SectionNamePrefix"]:
        """Get sectionName (Pythonic accessor)."""
        return self._sectionName
        # Collection of the stack memory usage for each runnable this implementation.
        # The aggregation of Stack subject to variability with the purpose to support
                # existence of runnable entities.
        # atpVariation.
        self._stackUsage: List[StackUsage] = []

    @property
    def stack_usage(self) -> List[StackUsage]:
        """Get stackUsage (Pythonic accessor)."""
        return self._stackUsage

    def with_access_count(self, value):
        """
        Set access_count and return self for chaining.

        Args:
            value: The access_count to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access_count("value")
        """
        self.access_count = value  # Use property setter (gets validation)
        return self

    def with_execution_time(self, value):
        """
        Set execution_time and return self for chaining.

        Args:
            value: The execution_time to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_execution_time("value")
        """
        self.execution_time = value  # Use property setter (gets validation)
        return self

    def with_heap_usage(self, value):
        """
        Set heap_usage and return self for chaining.

        Args:
            value: The heap_usage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_heap_usage("value")
        """
        self.heap_usage = value  # Use property setter (gets validation)
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

    def with_section_name(self, value):
        """
        Set section_name and return self for chaining.

        Args:
            value: The section_name to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_section_name("value")
        """
        self.section_name = value  # Use property setter (gets validation)
        return self

    def with_stack_usage(self, value):
        """
        Set stack_usage and return self for chaining.

        Args:
            value: The stack_usage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stack_usage("value")
        """
        self.stack_usage = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessCount(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for accessCount.

        Returns:
            The accessCount value

        Note:
            Delegates to access_count property (CODING_RULE_V2_00017)
        """
        return self.access_count  # Delegates to property

    def getExecutionTime(self) -> List[ExecutionTime]:
        """
        AUTOSAR-compliant getter for executionTime.

        Returns:
            The executionTime value

        Note:
            Delegates to execution_time property (CODING_RULE_V2_00017)
        """
        return self.execution_time  # Delegates to property

    def getHeapUsage(self) -> List[HeapUsage]:
        """
        AUTOSAR-compliant getter for heapUsage.

        Returns:
            The heapUsage value

        Note:
            Delegates to heap_usage property (CODING_RULE_V2_00017)
        """
        return self.heap_usage  # Delegates to property

    def getMemorySection(self) -> List[MemorySection]:
        """
        AUTOSAR-compliant getter for memorySection.

        Returns:
            The memorySection value

        Note:
            Delegates to memory_section property (CODING_RULE_V2_00017)
        """
        return self.memory_section  # Delegates to property

    def getSectionName(self) -> List["SectionNamePrefix"]:
        """
        AUTOSAR-compliant getter for sectionName.

        Returns:
            The sectionName value

        Note:
            Delegates to section_name property (CODING_RULE_V2_00017)
        """
        return self.section_name  # Delegates to property

    def getStackUsage(self) -> List[StackUsage]:
        """
        AUTOSAR-compliant getter for stackUsage.

        Returns:
            The stackUsage value

        Note:
            Delegates to stack_usage property (CODING_RULE_V2_00017)
        """
        return self.stack_usage  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HardwareConfiguration(ARObject):
    """
    Describes in which mode the hardware is operating while needing this
    resource consumption.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HardwareConfiguration

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 161, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies additional information on the Hardware.
        self._additional: Optional[String] = None

    @property
    def additional(self) -> Optional[String]:
        """Get additional (Pythonic accessor)."""
        return self._additional

    @additional.setter
    def additional(self, value: Optional[String]) -> None:
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
        self._processorMode: Optional[String] = None

    @property
    def processor_mode(self) -> Optional[String]:
        """Get processorMode (Pythonic accessor)."""
        return self._processorMode

    @processor_mode.setter
    def processor_mode(self, value: Optional[String]) -> None:
        """
        Set processorMode with validation.

        Args:
            value: The processorMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processorMode = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"processorMode must be String or str or None, got {type(value).__name__}"
            )
        self._processorMode = value
        self._processorSpeed: Optional[String] = None

    @property
    def processor_speed(self) -> Optional[String]:
        """Get processorSpeed (Pythonic accessor)."""
        return self._processorSpeed

    @processor_speed.setter
    def processor_speed(self, value: Optional[String]) -> None:
        """
        Set processorSpeed with validation.

        Args:
            value: The processorSpeed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processorSpeed = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"processorSpeed must be String or str or None, got {type(value).__name__}"
            )
        self._processorSpeed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdditional(self) -> String:
        """
        AUTOSAR-compliant getter for additional.

        Returns:
            The additional value

        Note:
            Delegates to additional property (CODING_RULE_V2_00017)
        """
        return self.additional  # Delegates to property

    def setAdditional(self, value: String) -> HardwareConfiguration:
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

    def getProcessorMode(self) -> String:
        """
        AUTOSAR-compliant getter for processorMode.

        Returns:
            The processorMode value

        Note:
            Delegates to processor_mode property (CODING_RULE_V2_00017)
        """
        return self.processor_mode  # Delegates to property

    def setProcessorMode(self, value: String) -> HardwareConfiguration:
        """
        AUTOSAR-compliant setter for processorMode with method chaining.

        Args:
            value: The processorMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to processor_mode property setter (gets validation automatically)
        """
        self.processor_mode = value  # Delegates to property setter
        return self

    def getProcessorSpeed(self) -> String:
        """
        AUTOSAR-compliant getter for processorSpeed.

        Returns:
            The processorSpeed value

        Note:
            Delegates to processor_speed property (CODING_RULE_V2_00017)
        """
        return self.processor_speed  # Delegates to property

    def setProcessorSpeed(self, value: String) -> HardwareConfiguration:
        """
        AUTOSAR-compliant setter for processorSpeed with method chaining.

        Args:
            value: The processorSpeed to set

        Returns:
            self for method chaining

        Note:
            Delegates to processor_speed property setter (gets validation automatically)
        """
        self.processor_speed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_additional(self, value: Optional[String]) -> HardwareConfiguration:
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

    def with_processor_mode(self, value: Optional[String]) -> HardwareConfiguration:
        """
        Set processorMode and return self for chaining.

        Args:
            value: The processorMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processor_mode("value")
        """
        self.processor_mode = value  # Use property setter (gets validation)
        return self

    def with_processor_speed(self, value: Optional[String]) -> HardwareConfiguration:
        """
        Set processorSpeed and return self for chaining.

        Args:
            value: The processorSpeed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processor_speed("value")
        """
        self.processor_speed = value  # Use property setter (gets validation)
        return self



class SoftwareContext(ARObject):
    """
    Specifies the context of the software for this resource consumption.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::SoftwareContext

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 163, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the input vector which is used to provide the.
        self._input: Optional[String] = None

    @property
    def input(self) -> Optional[String]:
        """Get input (Pythonic accessor)."""
        return self._input

    @input.setter
    def input(self, value: Optional[String]) -> None:
        """
        Set input with validation.

        Args:
            value: The input to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._input = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"input must be String or str or None, got {type(value).__name__}"
            )
        self._input = value
        self._state: Optional[String] = None

    @property
    def state(self) -> Optional[String]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional[String]) -> None:
        """
        Set state with validation.

        Args:
            value: The state to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"state must be String or str or None, got {type(value).__name__}"
            )
        self._state = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInput(self) -> String:
        """
        AUTOSAR-compliant getter for input.

        Returns:
            The input value

        Note:
            Delegates to input property (CODING_RULE_V2_00017)
        """
        return self.input  # Delegates to property

    def setInput(self, value: String) -> SoftwareContext:
        """
        AUTOSAR-compliant setter for input with method chaining.

        Args:
            value: The input to set

        Returns:
            self for method chaining

        Note:
            Delegates to input property setter (gets validation automatically)
        """
        self.input = value  # Delegates to property setter
        return self

    def getState(self) -> String:
        """
        AUTOSAR-compliant getter for state.

        Returns:
            The state value

        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: String) -> SoftwareContext:
        """
        AUTOSAR-compliant setter for state with method chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_input(self, value: Optional[String]) -> SoftwareContext:
        """
        Set input and return self for chaining.

        Args:
            value: The input to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_input("value")
        """
        self.input = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional[String]) -> SoftwareContext:
        """
        Set state and return self for chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self
