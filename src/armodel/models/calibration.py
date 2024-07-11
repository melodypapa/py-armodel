from .ar_object import ARObject
from .ar_ref import RefType

class SwValues(ARObject):
    def __init__(self):
        super().__init__()

        self.v = None                   # type: float

class SwValueCont(ARObject):
    def __init__(self):
        super().__init__()

        self.unit_ref = None            # type: RefType
        self.sw_values_phys = None      # type: SwValues

