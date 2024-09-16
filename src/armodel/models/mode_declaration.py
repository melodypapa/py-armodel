
from .ar_object import ARObject
from .general_structure import Identifiable


class ModeDeclarationGroupPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)