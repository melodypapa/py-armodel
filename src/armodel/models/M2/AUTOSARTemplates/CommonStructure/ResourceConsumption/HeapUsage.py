from abc import ABCMeta
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class HeapUsage(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == HeapUsage:
            raise NotImplementedError("HeapUsage is an abstract class.")
        
        super().__init__(parent, short_name)