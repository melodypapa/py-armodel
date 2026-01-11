"""
This module contains the ResourceConsumption class and imports related resource consumption classes
for representing resource consumption in AUTOSAR models. This includes memory sections, stack usage,
heap usage, and other resource consumption metrics.
"""

from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage, RoughEstimateStackUsage, StackUsage, WorstCaseStackUsage
from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import HeapUsage
from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from typing import List

class ResourceConsumption(Identifiable):
    """
    Represents resource consumption information in AUTOSAR models.
    This class aggregates various types of resource consumption including memory sections,
    stack usage, heap usage, execution times, and other resource metrics.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ResourceConsumption with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this resource consumption
            short_name: The unique short name of this resource consumption
        """
        super().__init__(parent, short_name)

        # List of access count sets for resource consumption analysis
        self.accessCountSets: List['AccessCountSet'] = []                               
        # List of execution time measurements for resource consumption analysis
        self.executionTimes: List['ExecutionTime'] = []                                
        # List of heap usage measurements for resource consumption analysis
        self.heapUsages: List[HeapUsage] = []                                    
        # List of memory sections for resource consumption analysis
        self.memorySections = []
        # List of section name prefixes for resource consumption analysis
        self.sectionNamePrefixs: List['SectionNamePrefix'] = []                            
        # List of stack usage measurements for resource consumption analysis
        self.stackUsages: List[StackUsage] = []                                   

    def createMemorySection(self, short_name: str) -> MemorySection:
        """
        Creates and adds a MemorySection to this resource consumption object.
        
        Args:
            short_name: The short name for the new memory section
            
        Returns:
            The created MemorySection instance
        """
        if (short_name not in self.elements):
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
        return list(sorted(filter(lambda a: isinstance(a, MemorySection), self.elements), key= lambda o:o.short_name))

    def getMemorySection(self, short_name: str) -> MemorySection:
        """
        Gets a specific MemorySection by its short name.
        
        Args:
            short_name: The short name of the memory section to find
            
        Returns:
            MemorySection instance with the specified short name, or None if not found
        """
        return next(filter(lambda o: isinstance(o, MemorySection) and (o.short_name == short_name), self.elements), None)
    
    def createMeasuredStackUsage(self, short_name: str) -> MeasuredStackUsage:
        """
        Creates and adds a MeasuredStackUsage to this resource consumption object.
        
        Args:
            short_name: The short name for the new measured stack usage
            
        Returns:
            The created MeasuredStackUsage instance
        """
        if (short_name not in self.elements):
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
        if (short_name not in self.elements):
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
        if (short_name not in self.elements):
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
        return list(sorted(filter(lambda a: isinstance(a, StackUsage), self.elements), key= lambda o:o.short_name))