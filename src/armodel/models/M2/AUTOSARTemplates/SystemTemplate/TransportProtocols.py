from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .Fibex.FibexCore.CoreCommunication import FibexElement

class CanTpConfig(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)