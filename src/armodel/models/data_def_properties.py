from typing import List
from .ar_object import ARFloat, ARLiteral, ARObject


class ValueList(ARObject):
    def __init__(self):
        super().__init__()

        self.v = None                                       # type: ARFloat
        self._vf = []                                       # type: List[ARLiteral]

    def addVf(self, vf: ARLiteral):
        self._vf.append(vf)

    def getVfs(self) -> List[ARLiteral]:
        return sorted(self._vf)