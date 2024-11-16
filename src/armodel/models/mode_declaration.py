
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class ModeDeclarationGroupPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)