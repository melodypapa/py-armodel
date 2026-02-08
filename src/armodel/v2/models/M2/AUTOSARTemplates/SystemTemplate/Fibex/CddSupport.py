"""
AUTOSAR Package - CddSupport

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    PhysicalChannel,
)




class UserDefinedCluster(ARObject):
    """
    This element allows the modeling of arbitrary Communication Clusters (e.g.
    bus systems that are not supported by AUTOSAR).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport::UserDefinedCluster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 179, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UserDefinedPhysicalChannel(PhysicalChannel):
    """
    This element allows the modeling of arbitrary Physical Channels.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport::UserDefinedPhysicalChannel
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 179, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UserDefinedCommunicationConnector(CommunicationConnector):
    """
    This element allows the modeling of arbitrary Communication Connectors.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport::UserDefinedCommunicationConnector
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 179, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UserDefinedCommunicationController(ARObject):
    """
    This element allows the modeling of arbitrary Communication Controllers.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport::UserDefinedCommunicationController
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 180, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====