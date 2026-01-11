# This module contains AUTOSAR System Template classes for Ethernet frames
# It defines Ethernet frame structures for network communication

from abc import ABCMeta
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame


class AbstractEthernetFrame(Frame, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractEthernetFrame:
            raise NotImplementedError("AbstractEthernetFrame is an abstract class.")
        
        super().__init__(parent, short_name)


class GenericEthernetFrame(AbstractEthernetFrame):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
