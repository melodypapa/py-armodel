from abc import ABCMeta
from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import SoftwareContext
from .....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import HardwareConfiguration
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class StackUsage(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == StackUsage:
            raise NotImplementedError("StackUsage is an abstract class.")
        
        super().__init__(parent, short_name)

        self.executableEntityRef = None                 # type: RefType
        self.hardwareConfiguration = None               # type: HardwareConfiguration
        self.hwElementRef = None                        # type: RefType
        self.softwareContext = None                     # type: SoftwareContext

    def getExecutableEntityRef(self):
        return self.executableEntityRef

    def setExecutableEntityRef(self, value):
        self.executableEntityRef = value
        return self

    def getHardwareConfiguration(self):
        return self.hardwareConfiguration

    def setHardwareConfiguration(self, value):
        self.hardwareConfiguration = value
        return self

    def getHwElementRef(self):
        return self.hwElementRef

    def setHwElementRef(self, value):
        self.hwElementRef = value
        return self

    def getSoftwareContext(self):
        return self.softwareContext

    def setSoftwareContext(self, value):
        self.softwareContext = value
        return self

class MeasuredStackUsage(StackUsage):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.averageMemoryConsumption = None            # type: PositiveInteger
        self.maximumMemoryConsumption = None            # type: PositiveInteger

    def getAverageMemoryConsumption(self):
        return self.averageMemoryConsumption

    def setAverageMemoryConsumption(self, value):
        self.averageMemoryConsumption = value
        return self

    def getMaximumMemoryConsumption(self):
        return self.maximumMemoryConsumption

    def setMaximumMemoryConsumption(self, value):
        self.maximumMemoryConsumption = value
        return self

class RoughEstimateStackUsage(StackUsage):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.memoryConsumption = None                   # type: PositiveInteger

    def getMemoryConsumption(self):
        return self.memoryConsumption

    def setMemoryConsumption(self, value):
        self.memoryConsumption = value
        return self

class WorstCaseStackUsage(StackUsage):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.memoryConsumption = None                   # type: PositiveInteger

    def getMemoryConsumption(self):
        return self.memoryConsumption

    def setMemoryConsumption(self, value):
        self.memoryConsumption = value
        return self