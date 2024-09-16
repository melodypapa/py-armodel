
from abc import ABCMeta
from ..ar_object import ARObject
from .fibex_core import Frame

class LinFrame(Frame):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == LinFrame:
            raise NotImplementedError("LinFrame is an abstract class.")
        
        super().__init__(parent, short_name)

class LinUnconditionalFrame(LinFrame):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)