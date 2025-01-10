from abc import ABCMeta

from ...GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractAccessPoint(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractAccessPoint:
            raise NotImplementedError("ARObject is an abstract class.")
        
        super().__init__(parent, short_name)

        self.returnValueProvision = None                                    # type: RteApiReturnValueProvisionEnum

    def getReturnValueProvision(self):
        return self.returnValueProvision

    def setReturnValueProvision(self, value):
        if value is not None:
            self.returnValueProvision = value
        return self
