
from ....ar_object import ARObject
from ....fibex.fibex_core.core_communication import FibexElement

class CanTpConfig(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)