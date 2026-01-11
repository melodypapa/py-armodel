# This module contains AUTOSAR System Template classes for DoIP (Diagnostics over IP)
# It defines logic address properties and configurations for DoIP communication

from abc import ABCMeta

from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

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

        self.doIpTesterRoutingActivationRef: RefType = None

    def getDoIpTesterRoutingActivationRef(self):
        return self.doIpTesterRoutingActivationRef

    def setDoIpTesterRoutingActivationRef(self, value):
        if value is not None:
            self.doIpTesterRoutingActivationRef = value
        return self