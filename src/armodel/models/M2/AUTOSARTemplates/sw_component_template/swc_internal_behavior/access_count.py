from abc import ABCMeta

from .....general_structure import Identifiable
from .....ar_object import ARObject

class AbstractAccessPoint(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractAccessPoint:
            raise NotImplementedError("ARObject is an abstract class.")
        
        super().__init__(parent, short_name)

        self.return_value_provision = None  