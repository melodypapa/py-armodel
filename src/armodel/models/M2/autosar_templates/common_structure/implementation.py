from abc import ABCMeta

from ....ar_object import ARLiteral, ARObject
from ....general_structure import Referrable


class ImplementationProps(Referrable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ImplementationProps:
            raise NotImplementedError("ImplementationProps is an abstract class.")
        
        super().__init__(parent, short_name)

        self.symbol = None                          # type: ARLiteral

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self
