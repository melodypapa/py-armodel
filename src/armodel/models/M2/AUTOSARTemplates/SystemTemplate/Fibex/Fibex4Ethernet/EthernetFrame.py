# This module contains AUTOSAR System Template classes for Ethernet frames
# It defines Ethernet frame structures for network communication

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame


class AbstractEthernetFrame(Frame, ABC):
    """
    Ethernet specific attributes to the Frame.
    """

    # AbstractEthernetFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.229, p.578
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractEthernetFrame:
            raise TypeError("AbstractEthernetFrame is an abstract class.")

        super().__init__(parent, short_name)


class GenericEthernetFrame(AbstractEthernetFrame):
    """
    This element is used for EthernetFrames without additional attributes that are routed by the EthIf. Tags: atp.recommendedPackage=Frames
    """

    # GenericEthernetFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.231, p.579
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
