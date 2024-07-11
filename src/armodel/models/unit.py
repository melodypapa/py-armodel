
from .ar_object import ARLiteral, ARObject
from .general_structure import ARElement


class SingleLanguageUnitNames(ARLiteral):
    def __init__(self) -> None:
        super().__init__()

class Unit(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.display_name = None    # type: SingleLanguageUnitNames