from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class ECUMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.commControllerMappings = []                                # type: List[CommunicationControllerMapping]
        self.ecuRef = None                                              # type: RefType
        self.ecuInstanceRef = None                                      # type: RefType
        self.hwPortMappings =[]                                         # type: List[HwPortMapping]

    def getCommControllerMappings(self):
        return self.commControllerMappings

    def setCommControllerMappings(self, value):
        if value is not None:
            self.commControllerMappings = value
        return self

    def getEcuRef(self):
        return self.ecuRef

    def setEcuRef(self, value):
        if value is not None:
            self.ecuRef = value
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getHwPortMappings(self):
        return self.hwPortMappings

    def setHwPortMappings(self, value):
        if value is not None:
            self.hwPortMappings = value
        return self
