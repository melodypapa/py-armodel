from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame


class AbstractEthernetFrame(Frame, ABC):
    """
    Ethernet specific attributes to the Frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame::AbstractEthernetFrame

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 578, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractEthernetFrame:
            raise TypeError("AbstractEthernetFrame is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
