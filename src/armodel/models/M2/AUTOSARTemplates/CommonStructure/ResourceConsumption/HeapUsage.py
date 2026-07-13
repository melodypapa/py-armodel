"""
This module contains the HeapUsage abstract class for representing
heap memory usage in AUTOSAR resource consumption models.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class HeapUsage(Identifiable, ABC):
    """
    Abstract base class for representing heap usage in AUTOSAR models.
    This class defines the basic structure for heap memory consumption tracking.
    """
    # HeapUsage method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the HeapUsage with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.
        
        Args:
            parent: The parent ARObject that contains this heap usage
            short_name: The unique short name of this heap usage
        """
        if type(self) is HeapUsage:
            raise TypeError("HeapUsage is an abstract class.")
        
        super().__init__(parent, short_name)

class MeasuredHeapUsage(HeapUsage):
    """
    Represents measured heap usage in AUTOSAR.
    """
    # MeasuredHeapUsage method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSampleSize                [x] impl  [ ] docstring  [ ] test
    # [ ] setSampleSize                [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()
        self.sampleSize: int = None

    def getSampleSize(self):
        return self.sampleSize

    def setSampleSize(self, value):
        self.sampleSize = value
        return self


class RoughEstimateHeapUsage(HeapUsage):
    """
    Represents rough estimate of heap usage in AUTOSAR.
    """
    # RoughEstimateHeapUsage method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getConfidenceLevel           [x] impl  [ ] docstring  [ ] test
    # [ ] setConfidenceLevel           [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()
        self.confidenceLevel: str = None

    def getConfidenceLevel(self):
        return self.confidenceLevel

    def setConfidenceLevel(self, value):
        self.confidenceLevel = value
        return self


class WorstCaseHeapUsage(HeapUsage):
    """
    Represents worst case heap usage in AUTOSAR.
    """
    # WorstCaseHeapUsage method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getConfidenceLevel           [x] impl  [ ] docstring  [ ] test
    # [ ] setConfidenceLevel           [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()
        self.confidenceLevel: str = None

    def getConfidenceLevel(self):
        return self.confidenceLevel

    def setConfidenceLevel(self, value):
        self.confidenceLevel = value
        return self
