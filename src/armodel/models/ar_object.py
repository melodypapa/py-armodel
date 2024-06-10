from abc import ABCMeta

class ARObject(metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
            raise NotImplementedError("ARObject is an abstract class.")
        
        self.parent = None              # type: ARObject
        self.checksum = None            # type: str
        self.timestamp = None           # type: str
