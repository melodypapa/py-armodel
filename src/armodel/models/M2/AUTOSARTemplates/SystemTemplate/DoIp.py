from abc import ABCMeta

from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class AbstractDoIpLogicAddressProps(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractDoIpLogicAddressProps:
            raise NotImplementedError("AbstractDoIpLogicAddressProps is an abstract class.")
        
        super().__init__(parent, short_name)

class DoIpLogicTargetAddressProps(AbstractDoIpLogicAddressProps):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.doIpTesterRoutingActivationRef = None                              # type: RefType

    def getDoIpTesterRoutingActivationRef(self):
        return self.doIpTesterRoutingActivationRef

    def setDoIpTesterRoutingActivationRef(self, value):
        if value is not None:
            self.doIpTesterRoutingActivationRef = value
        return self
