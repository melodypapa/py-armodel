from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DoIpActivationLineNeeds(DoIpServiceNeeds):
    """
    A DoIP entity needs to be informed when an external tester is attached or
    activated. The DoIpActivation ServiceNeeds specifies the trigger for such an
    event. Examples would be a Pdu via a regular communication bus, a PWM
    signal, or an I/O. For details please refer to the ISO 13400.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpActivationLineNeeds
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 807, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====