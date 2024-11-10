from .....ar_object import ARLiteral, ARObject
from ...common_structure.implementation import ImplementationProps

class SymbolProps(ImplementationProps):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
