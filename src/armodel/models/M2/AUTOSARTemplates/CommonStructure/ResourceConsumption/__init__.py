"""
This module contains the ResourceConsumption class, its aggregated context classes
(HardwareConfiguration, SoftwareContext), and imports related resource consumption
classes for representing resource consumption in AUTOSAR models.
"""

from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    AnalyzedExecutionTime,
    ExecutionTime,
    MeasuredExecutionTime,
    RoughEstimateOfExecutionTime,
    SimulatedExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import HeapUsage, MeasuredHeapUsage, RoughEstimateHeapUsage, WorstCaseHeapUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection, SectionNamePrefix
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage, RoughEstimateStackUsage, StackUsage, WorstCaseStackUsage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AccessCountSet


class HardwareConfiguration(ARObject):
    """
    Describes in which mode the hardware is operating while needing this resource
    consumption.
    """

    # HardwareConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.18, p.161
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAdditionalInformation     [x] impl  [x] docstring  [x] test
    # [x] setAdditionalInformation     [x] impl  [x] docstring  [x] test
    # [x] getProcessorMode             [x] impl  [x] docstring  [x] test
    # [x] setProcessorMode             [x] impl  [x] docstring  [x] test
    # [x] getProcessorSpeed            [x] impl  [x] docstring  [x] test
    # [x] setProcessorSpeed            [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the HardwareConfiguration with default values.
        """
        super().__init__()

        # Specifies additional information on the Hardware Configuration.
        # [constr_10315] For each HardwareConfiguration, the attribute
        # additionalInformation shall exist at the time when the configuration of the
        # BSW module is finished.
        self.additionalInformation: Optional[String] = None

        # Specifies in which mode the processor is operating.
        # [constr_10316] For each HardwareConfiguration, the attribute processorMode
        # shall exist at the time when the configuration of the BSW module is finished.
        self.processorMode: Optional[String] = None

        # Specifies the speed the processor is operating.
        # [constr_10317] For each HardwareConfiguration, the attribute processorSpeed
        # shall exist at the time when the configuration of the BSW module is finished.
        self.processorSpeed: Optional[String] = None

    def getAdditionalInformation(self) -> Optional[String]:
        """
        Gets the additional information on the Hardware Configuration.
        [constr_10315]

        Returns:
            String with additional information, or None if not set
        """
        return self.additionalInformation

    def setAdditionalInformation(self, value: Optional[String]) -> "HardwareConfiguration":
        """
        Sets the additional information on the Hardware Configuration.
        [constr_10315] The attribute shall exist at the time when the configuration of
        the BSW module is finished.
        A None value is a no-op and does not overwrite existing information.

        Args:
            value: The additional information to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.additionalInformation = value
        return self

    def getProcessorMode(self) -> Optional[String]:
        """
        Gets the mode in which the processor is operating. [constr_10316]

        Returns:
            String with the processor mode, or None if not set
        """
        return self.processorMode

    def setProcessorMode(self, value: Optional[String]) -> "HardwareConfiguration":
        """
        Sets the mode in which the processor is operating.
        [constr_10316] The attribute shall exist at the time when the configuration of
        the BSW module is finished.
        A None value is a no-op and does not overwrite an existing mode.

        Args:
            value: The processor mode to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.processorMode = value
        return self

    def getProcessorSpeed(self) -> Optional[String]:
        """
        Gets the speed the processor is operating. [constr_10317]

        Returns:
            String with the processor speed, or None if not set
        """
        return self.processorSpeed

    def setProcessorSpeed(self, value: Optional[String]) -> "HardwareConfiguration":
        """
        Sets the speed the processor is operating.
        [constr_10317] The attribute shall exist at the time when the configuration of
        the BSW module is finished.
        A None value is a no-op and does not overwrite an existing speed.

        Args:
            value: The processor speed to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.processorSpeed = value
        return self


class SoftwareContext(ARObject):
    """
    Specifies the context of the software for this resource consumption.
    """

    # SoftwareContext method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.20, p.163
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getInput                     [x] impl  [x] docstring  [x] test
    # [x] setInput                     [x] impl  [x] docstring  [x] test
    # [x] getState                     [x] impl  [x] docstring  [x] test
    # [x] setState                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the SoftwareContext with default values.
        """
        super().__init__()

        # Specifies the input vector which is used to provide the ExecutionTime.
        self.input: Optional[String] = None

        # Specifies the state the software is in when the ExecutionTime is provided.
        self.state: Optional[String] = None

    def getInput(self) -> Optional[String]:
        """
        Gets the input vector which is used to provide the ExecutionTime.

        Returns:
            String with the input vector, or None if not set
        """
        return self.input

    def setInput(self, value: Optional[String]) -> "SoftwareContext":
        """
        Sets the input vector which is used to provide the ExecutionTime.
        A None value is a no-op and does not overwrite an existing input.

        Args:
            value: The input vector to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.input = value
        return self

    def getState(self) -> Optional[String]:
        """
        Gets the state the software is in when the ExecutionTime is provided.

        Returns:
            String with the software state, or None if not set
        """
        return self.state

    def setState(self, value: Optional[String]) -> "SoftwareContext":
        """
        Sets the state the software is in when the ExecutionTime is provided.
        A None value is a no-op and does not overwrite an existing state.

        Args:
            value: The software state to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.state = value
        return self


class ResourceConsumption(Identifiable):
    """
    Represents resource consumption information in AUTOSAR models.
    This class aggregates various types of resource consumption including memory sections,
    stack usage, heap usage, execution times, and other resource metrics.
    """

    # ResourceConsumption method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 8.1, p.137
    # [x] __init__                          [x] impl  [x] docstring  [x] test
    # [x] addAccessCountSet                 [x] impl  [x] docstring  [x] test
    # [x] getAccessCountSets                [x] impl  [x] docstring  [x] test
    # [x] createAnalyzedExecutionTime       [x] impl  [x] docstring  [x] test
    # [x] createMeasuredExecutionTime       [x] impl  [x] docstring  [x] test
    # [x] createRoughEstimateOfExecutionTime [x] impl [x] docstring  [x] test
    # [x] createSimulatedExecutionTime      [x] impl  [x] docstring  [x] test
    # [x] getExecutionTimes                 [x] impl  [x] docstring  [x] test
    # [x] createMeasuredHeapUsage           [x] impl  [x] docstring  [x] test
    # [x] createRoughEstimateHeapUsage      [x] impl  [x] docstring  [x] test
    # [x] createWorstCaseHeapUsage          [x] impl  [x] docstring  [x] test
    # [x] getHeapUsages                     [x] impl  [x] docstring  [x] test
    # [x] createMemorySection               [x] impl  [x] docstring  [x] test
    # [x] getMemorySections                 [x] impl  [x] docstring  [x] test
    # [x] getMemorySection                  [x] impl  [x] docstring  [x] test
    # [x] createSectionNamePrefix           [x] impl  [x] docstring  [x] test
    # [x] getSectionNamePrefixes            [x] impl  [x] docstring  [x] test
    # [x] createMeasuredStackUsage          [x] impl  [x] docstring  [x] test
    # [x] createRoughEstimateStackUsage     [x] impl  [x] docstring  [x] test
    # [x] createWorstCaseStackUsage         [x] impl  [x] docstring  [x] test
    # [x] getStackUsages                    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ResourceConsumption with a parent and short name.

        Args:
            parent: The parent ARObject that contains this resource consumption
            short_name: The unique short name of this resource consumption
        """
        super().__init__(parent, short_name)

        # Set of access count values
        self.accessCountSets: List["AccessCountSet"] = []

        # Collection of the execution time descriptions for this implementation
        self.executionTimes: List[ExecutionTime] = []

        # Collection of the heap memory allocated by this implementation
        self.heapUsages: List[HeapUsage] = []

        # An abstract memory section required by this Implementation
        self.memorySections: List[MemorySection] = []

        # A prefix to be used for the memory section symbol in the code
        self.sectionNamePrefixes: List[SectionNamePrefix] = []

        # Collection of the stack memory usage for each runnable entity of this implementation
        self.stackUsages: List[StackUsage] = []

    def addAccessCountSet(self, value: Optional["AccessCountSet"]) -> "ResourceConsumption":
        """
        Adds an AccessCountSet to this resource consumption object.

        Args:
            value: The access count set to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessCountSets.append(value)
        return self

    def getAccessCountSets(self) -> List["AccessCountSet"]:
        """
        Gets all AccessCountSet instances of this resource consumption object.

        Returns:
            List of AccessCountSet instances
        """
        return self.accessCountSets

    def createAnalyzedExecutionTime(self, short_name: str) -> AnalyzedExecutionTime:
        """
        Creates and adds an AnalyzedExecutionTime to this resource consumption object.

        Args:
            short_name: The short name for the new analyzed execution time

        Returns:
            The created AnalyzedExecutionTime instance
        """
        if short_name not in self.elements:
            execution_time = AnalyzedExecutionTime(self, short_name)
            self.addElement(execution_time)
            self.executionTimes.append(execution_time)
        return self.getElement(short_name)

    def createMeasuredExecutionTime(self, short_name: str) -> MeasuredExecutionTime:
        """
        Creates and adds a MeasuredExecutionTime to this resource consumption object.

        Args:
            short_name: The short name for the new measured execution time

        Returns:
            The created MeasuredExecutionTime instance
        """
        if short_name not in self.elements:
            execution_time = MeasuredExecutionTime(self, short_name)
            self.addElement(execution_time)
            self.executionTimes.append(execution_time)
        return self.getElement(short_name)

    def createRoughEstimateOfExecutionTime(self, short_name: str) -> RoughEstimateOfExecutionTime:
        """
        Creates and adds a RoughEstimateOfExecutionTime to this resource consumption object.

        Args:
            short_name: The short name for the new rough estimate of execution time

        Returns:
            The created RoughEstimateOfExecutionTime instance
        """
        if short_name not in self.elements:
            execution_time = RoughEstimateOfExecutionTime(self, short_name)
            self.addElement(execution_time)
            self.executionTimes.append(execution_time)
        return self.getElement(short_name)

    def createSimulatedExecutionTime(self, short_name: str) -> SimulatedExecutionTime:
        """
        Creates and adds a SimulatedExecutionTime to this resource consumption object.

        Args:
            short_name: The short name for the new simulated execution time

        Returns:
            The created SimulatedExecutionTime instance
        """
        if short_name not in self.elements:
            execution_time = SimulatedExecutionTime(self, short_name)
            self.addElement(execution_time)
            self.executionTimes.append(execution_time)
        return self.getElement(short_name)

    def getExecutionTimes(self) -> List[ExecutionTime]:
        """
        Gets all ExecutionTime instances from the elements list, sorted by short name.

        Returns:
            List of ExecutionTime instances sorted by short name
        """
        return list(
            sorted(filter(lambda a: isinstance(a, (AnalyzedExecutionTime, MeasuredExecutionTime, RoughEstimateOfExecutionTime, SimulatedExecutionTime)), self.elements), key=lambda o: o.short_name)
        )

    def createMeasuredHeapUsage(self, short_name: str) -> MeasuredHeapUsage:
        """
        Creates and adds a MeasuredHeapUsage to this resource consumption object.

        Args:
            short_name: The short name for the new measured heap usage

        Returns:
            The created MeasuredHeapUsage instance
        """
        if short_name not in self.elements:
            heap_usage = MeasuredHeapUsage(self, short_name)
            self.addElement(heap_usage)
            self.heapUsages.append(heap_usage)
        return self.getElement(short_name)

    def createRoughEstimateHeapUsage(self, short_name: str) -> RoughEstimateHeapUsage:
        """
        Creates and adds a RoughEstimateHeapUsage to this resource consumption object.

        Args:
            short_name: The short name for the new rough estimate heap usage

        Returns:
            The created RoughEstimateHeapUsage instance
        """
        if short_name not in self.elements:
            heap_usage = RoughEstimateHeapUsage(self, short_name)
            self.addElement(heap_usage)
            self.heapUsages.append(heap_usage)
        return self.getElement(short_name)

    def createWorstCaseHeapUsage(self, short_name: str) -> WorstCaseHeapUsage:
        """
        Creates and adds a WorstCaseHeapUsage to this resource consumption object.

        Args:
            short_name: The short name for the new worst case heap usage

        Returns:
            The created WorstCaseHeapUsage instance
        """
        if short_name not in self.elements:
            heap_usage = WorstCaseHeapUsage(self, short_name)
            self.addElement(heap_usage)
            self.heapUsages.append(heap_usage)
        return self.getElement(short_name)

    def getHeapUsages(self) -> List[HeapUsage]:
        """
        Gets all HeapUsage instances from the elements list, sorted by short name.

        Returns:
            List of HeapUsage instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, HeapUsage), self.elements), key=lambda o: o.short_name))

    def createMemorySection(self, short_name: str) -> MemorySection:
        """
        Creates and adds a MemorySection to this resource consumption object.

        Args:
            short_name: The short name for the new memory section

        Returns:
            The created MemorySection instance
        """
        if short_name not in self.elements:
            section = MemorySection(self, short_name)
            self.addElement(section)
            self.memorySections.append(section)
        return self.getElement(short_name)

    def getMemorySections(self) -> List[MemorySection]:
        """
        Gets all MemorySection instances from the elements list, sorted by short name.

        Returns:
            List of MemorySection instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, MemorySection), self.elements), key=lambda o: o.short_name))

    def getMemorySection(self, short_name: str) -> MemorySection:
        """
        Gets a specific MemorySection by its short name.

        Args:
            short_name: The short name of the memory section to find

        Returns:
            MemorySection instance with the specified short name, or None if not found
        """
        return next(filter(lambda o: isinstance(o, MemorySection) and (o.short_name == short_name), self.elements), None)

    def createSectionNamePrefix(self, short_name: str) -> SectionNamePrefix:
        """
        Creates and adds a SectionNamePrefix to this resource consumption object.

        Args:
            short_name: The short name for the new section name prefix

        Returns:
            The created SectionNamePrefix instance
        """
        if short_name not in self.elements:
            prefix = SectionNamePrefix(self, short_name)
            self.addElement(prefix)
            self.sectionNamePrefixes.append(prefix)
        return self.getElement(short_name)

    def getSectionNamePrefixes(self) -> List[SectionNamePrefix]:
        """
        Gets all SectionNamePrefix instances from the elements list, sorted by short name.

        Returns:
            List of SectionNamePrefix instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, SectionNamePrefix), self.elements), key=lambda o: o.short_name))

    def createMeasuredStackUsage(self, short_name: str) -> MeasuredStackUsage:
        """
        Creates and adds a MeasuredStackUsage to this resource consumption object.

        Args:
            short_name: The short name for the new measured stack usage

        Returns:
            The created MeasuredStackUsage instance
        """
        if short_name not in self.elements:
            section = MeasuredStackUsage(self, short_name)
            self.addElement(section)
            self.stackUsages.append(section)
        return self.getElement(short_name)

    def createRoughEstimateStackUsage(self, short_name: str) -> RoughEstimateStackUsage:
        """
        Creates and adds a RoughEstimateStackUsage to this resource consumption object.

        Args:
            short_name: The short name for the new rough estimate stack usage

        Returns:
            The created RoughEstimateStackUsage instance
        """
        if short_name not in self.elements:
            section = RoughEstimateStackUsage(self, short_name)
            self.addElement(section)
            self.stackUsages.append(section)
        return self.getElement(short_name)

    def createWorstCaseStackUsage(self, short_name: str) -> WorstCaseStackUsage:
        """
        Creates and adds a WorstCaseStackUsage to this resource consumption object.

        Args:
            short_name: The short name for the new worst case stack usage

        Returns:
            The created WorstCaseStackUsage instance
        """
        if short_name not in self.elements:
            section = WorstCaseStackUsage(self, short_name)
            self.addElement(section)
            self.stackUsages.append(section)
        return self.getElement(short_name)

    def getStackUsages(self) -> List[StackUsage]:
        """
        Gets all StackUsage instances from the elements list, sorted by short name.

        Returns:
            List of StackUsage instances sorted by short name
        """
        return list(sorted(filter(lambda a: isinstance(a, StackUsage), self.elements), key=lambda o: o.short_name))
