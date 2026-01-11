"""
This module contains the HeapUsage abstract class for representing
heap memory usage in AUTOSAR resource consumption models.
"""

from abc import ABCMeta
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class HeapUsage(Identifiable, metaclass = ABCMeta):
    """
    Abstract base class for representing heap usage in AUTOSAR models.
    This class defines the basic structure for heap memory consumption tracking.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the HeapUsage with a parent and short name.
        Raises NotImplementedError if this abstract class is instantiated directly.
        
        Args:
            parent: The parent ARObject that contains this heap usage
            short_name: The unique short name of this heap usage
        """
        if type(self) == HeapUsage:
            raise NotImplementedError("HeapUsage is an abstract class.")
        
        super().__init__(parent, short_name)