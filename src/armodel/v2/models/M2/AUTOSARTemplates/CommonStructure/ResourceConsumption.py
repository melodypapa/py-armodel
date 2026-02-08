from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    ExecutionTime,
    HeapUsage,
    MemorySection,
    SectionNamePrefix,
    StackUsage,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
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
        self._executionTime: List["ExecutionTime"] = []

    @property
    def execution_time(self) -> List["ExecutionTime"]:
        """Get executionTime (Pythonic accessor)."""
        return self._executionTime
        # Collection of the heap memory allocated by this atpVariation.
        self._heapUsage: List["HeapUsage"] = []

    @property
    def heap_usage(self) -> List["HeapUsage"]:
        """Get heapUsage (Pythonic accessor)."""
        return self._heapUsage
        # An abstract memory section required by this atpVariation.
        self._memorySection: List["MemorySection"] = []

    @property
    def memory_section(self) -> List["MemorySection"]:
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
        self._stackUsage: List["StackUsage"] = []

    @property
    def stack_usage(self) -> List["StackUsage"]:
        """Get stackUsage (Pythonic accessor)."""
        return self._stackUsage

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

    def getExecutionTime(self) -> List["ExecutionTime"]:
        """
        AUTOSAR-compliant getter for executionTime.

        Returns:
            The executionTime value

        Note:
            Delegates to execution_time property (CODING_RULE_V2_00017)
        """
        return self.execution_time  # Delegates to property

    def getHeapUsage(self) -> List["HeapUsage"]:
        """
        AUTOSAR-compliant getter for heapUsage.

        Returns:
            The heapUsage value

        Note:
            Delegates to heap_usage property (CODING_RULE_V2_00017)
        """
        return self.heap_usage  # Delegates to property

    def getMemorySection(self) -> List["MemorySection"]:
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

    def getStackUsage(self) -> List["StackUsage"]:
        """
        AUTOSAR-compliant getter for stackUsage.

        Returns:
            The stackUsage value

        Note:
            Delegates to stack_usage property (CODING_RULE_V2_00017)
        """
        return self.stack_usage  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
