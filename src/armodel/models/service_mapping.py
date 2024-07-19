
from .ar_ref import RefType
from .ar_object import ARObject


class RoleBasedPortAssignment(ARObject):
    def __init__(self):
        super().__init__()
    
        self.port_prototype_ref = None  # type: RefType
        self.role = None                # type: str
