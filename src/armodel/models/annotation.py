
from abc import ABCMeta
from .ar_object import ARObject, MultilanguageLongName


class GeneralAnnotation(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
            raise NotImplementedError("GeneralAnnotation is an abstract class.")
        
        self.label = None       # type: MultilanguageLongName

        super().__init__()

class Annotation(GeneralAnnotation):
    def __init__(self):
        super().__init__()

