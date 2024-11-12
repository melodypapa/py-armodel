from .ar_object import ARObject

class RefType(ARObject):
    def __init__(self):
        self.dest = ""
        self.value = ""

    def getDest(self):
        return self.dest

    def setDest(self, value):
        self.dest = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self

class TRefType(RefType):
    def __init__(self):
        super().__init__()

