from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage, RoughEstimateStackUsage, StackUsage, WorstCaseStackUsage
from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import HeapUsage
from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from typing import List

class ResourceConsumption(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessCountSets = []                               # type: List[AccessCountSet]
        self.executionTimes = []                                # type: List[ExecutionTime]
        self.heapUsages = []                                    # type: List[HeapUsage]
        self.memorySections = []
        self.sectionNamePrefixs = []                            # type: List[SectionNamePrefix]
        self.stackUsages = []                                   # type: List[StackUsage]

    def createMemorySection(self, short_name: str) -> MemorySection:
        if (short_name not in self.elements):
            section = MemorySection(self, short_name)
            self.addElement(section)
            self.memorySections.append(section)
        return self.getElement(short_name)

    def getMemorySections(self) -> List[MemorySection]:
        return list(sorted(filter(lambda a: isinstance(a, MemorySection), self.elements.values()), key= lambda o:o.short_name))

    def getMemorySection(self, short_name: str) -> MemorySection:
        return next(filter(lambda o: isinstance(o, MemorySection) and (o.short_name == short_name), self.elements.values()), None)
    
    def createMeasuredStackUsage(self, short_name: str) -> MeasuredStackUsage:
        if (short_name not in self.elements):
            section = MeasuredStackUsage(self, short_name)
            self.addElement(section)
            self.stackUsages.append(section)
        return self.getElement(short_name)
    
    def createRoughEstimateStackUsage(self, short_name: str) -> RoughEstimateStackUsage:
        if (short_name not in self.elements):
            section = RoughEstimateStackUsage(self, short_name)
            self.addElement(section)
            self.stackUsages.append(section)
        return self.getElement(short_name)
    
    def createWorstCaseStackUsage(self, short_name: str) -> WorstCaseStackUsage:
        if (short_name not in self.elements):
            section = WorstCaseStackUsage(self, short_name)
            self.addElement(section)
            self.stackUsages.append(section)
        return self.getElement(short_name)
    
    def getStackUsages(self) -> List[StackUsage]:
        return list(sorted(filter(lambda a: isinstance(a, StackUsage), self.elements.values()), key= lambda o:o.short_name))