from abc import ABCMeta

from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from ..GenericStructure.GeneralTemplateClasses.Identifiable import Referrable


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
