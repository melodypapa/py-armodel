from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractDoIpLogicAddressProps(Identifiable, ABC):
    """
    Abstract meta-class that collects common properties for all specialized
    DoIpLogicAddressProps.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::DoIP::AbstractDoIpLogicAddressProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 556, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractDoIpLogicAddressProps:
            raise TypeError("AbstractDoIpLogicAddressProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====