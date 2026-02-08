"""
This module defines execution time resource consumption classes in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class AnalyzedExecutionTime(ARObject):
    """
    Represents analyzed execution time in AUTOSAR.
    """

    def __init__(self):
        super().__init__()
        self.executionTime: TimeValue = None

    def getExecutionTime(self):
        return self.executionTime

    def setExecutionTime(self, value):
        self.executionTime = value
        return self


class ExecutionTime(ARObject):
    """
    Represents execution time in AUTOSAR.
    """

    def __init__(self):
        super().__init__()
        self.executionTime: TimeValue = None

    def getExecutionTime(self):
        return self.executionTime

    def setExecutionTime(self, value):
        self.executionTime = value
        return self


class MeasuredExecutionTime(ARObject):
    """
    Represents measured execution time in AUTOSAR.
    """

    def __init__(self):
        super().__init__()
        self.executionTime: TimeValue = None
        self.sampleSize: int = None

    def getExecutionTime(self):
        return self.executionTime

    def setExecutionTime(self, value):
        self.executionTime = value
        return self

    def getSampleSize(self):
        return self.sampleSize

    def setSampleSize(self, value):
        self.sampleSize = value
        return self


class MemorySectionLocation(ARObject):
    """
    Represents memory section location in AUTOSAR.
    """

    def __init__(self):
        super().__init__()
        self.sectionName: str = None

    def getSectionName(self):
        return self.sectionName

    def setSectionName(self, value):
        self.sectionName = value
        return self


class RoughEstimateOfExecutionTime(ARObject):
    """
    Represents rough estimate of execution time in AUTOSAR.
    """

    def __init__(self):
        super().__init__()
        self.executionTime: TimeValue = None
        self.confidenceLevel: str = None

    def getExecutionTime(self):
        return self.executionTime

    def setExecutionTime(self, value):
        self.executionTime = value
        return self

    def getConfidenceLevel(self):
        return self.confidenceLevel

    def setConfidenceLevel(self, value):
        self.confidenceLevel = value
        return self


class SimulatedExecutionTime(ARObject):
    """
    Represents simulated execution time in AUTOSAR.
    """

    def __init__(self):
        super().__init__()
        self.executionTime: TimeValue = None
        self.simulationModel: str = None

    def getExecutionTime(self):
        return self.executionTime

    def setExecutionTime(self, value):
        self.executionTime = value
        return self

    def getSimulationModel(self):
        return self.simulationModel

    def setSimulationModel(self, value):
        self.simulationModel = value
        return self
