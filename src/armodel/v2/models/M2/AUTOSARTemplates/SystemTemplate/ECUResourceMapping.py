from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ECUMapping(Identifiable):
    """
    Represents an ECU mapping that defines the relationship between AUTOSAR software components
    and their physical ECU instances. This class maps communication controllers, hardware ports,
    and other ECU resources to specific ECU instances within the system configuration.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.commControllerMappings = []                                # type: List[CommunicationControllerMapping]
        self.ecuRef: Union[RefType, None] = None
        self.ecuInstanceRef: Union[RefType, None] = None
        self.hwPortMappings = []                                        # type: List[HwPortMapping]

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
