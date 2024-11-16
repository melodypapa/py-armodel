
from abc import ABCMeta
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class IdentCaption(Identifiable):
    
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == IdentCaption:
            raise NotImplementedError("IdentCaption is an abstract class.")
        
        super().__init__(parent, short_name)


class ModeAccessPointIdent(IdentCaption):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)