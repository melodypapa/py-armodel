from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TransportProtocolConfiguration(ARObject, ABC):
    """
    Transport Protocol configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TransportProtocolConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransportProtocolConfiguration:
            raise TypeError("TransportProtocolConfiguration is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
