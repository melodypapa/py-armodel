from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class NetworkEndpointAddress(ARObject, ABC):
    """
    To build a valid network endpoint address there has to be either one MAC
    multicast group reference or an ipv4 configuration or an ipv6 configuration.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::NetworkEndpointAddress
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 464, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is NetworkEndpointAddress:
            raise TypeError("NetworkEndpointAddress is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====