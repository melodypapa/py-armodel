# This module contains AUTOSAR System Template classes for Ethernet frames
# It defines Ethernet frame structures for network communication

from abc import ABC
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame


class AbstractEthernetFrame(Frame, ABC):
    """
    Abstract base class for Ethernet frames in the AUTOSAR system,
    extending the generic Frame class with Ethernet-specific properties
    and behavior. This class serves as the foundation for concrete
    Ethernet frame implementations.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractEthernetFrame:
            raise TypeError("AbstractEthernetFrame is an abstract class.")
        
        super().__init__(parent, short_name)


class GenericEthernetFrame(AbstractEthernetFrame):
    """
    Represents a generic Ethernet frame in the AUTOSAR system,
    implementing the basic structure and properties for standard
    Ethernet communication frames.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)