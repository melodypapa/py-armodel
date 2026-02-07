from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class PortGroup(Identifiable):
    """
    Group of ports which share a common functionality , e.g. need specific
    network resources. This information shall be available on the VFB level in
    order to delegate it properly via compositions. When propagated into the ECU
    extract, this information is used as input for the configuration of Services
    like the Communication Manager. A PortGroup is defined locally in a
    component (which can be a composition) and refers to the "outer" ports
    belonging to the group as well as to the "inner" groups which propagate this
    group into the components which are part of a composition. A PortGroup
    within an atomic SWC cannot be linked to inner groups.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::PortGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 203, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2045, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # defined in a component which is part of this by: InnerPortGroupIn.
        self._innerGroup: List[RefType] = []

    @property
    def inner_group(self) -> List[RefType]:
        """Get innerGroup (Pythonic accessor)."""
        return self._innerGroup
        # Outer PortPrototype of this AtomicSwComponentType to the group.
        # A port can belong to several to no group at all.
        # atpVariation.
        self._outerPort: List[RefType] = []

    @property
    def outer_port(self) -> List[RefType]:
        """Get outerPort (Pythonic accessor)."""
        return self._outerPort

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInnerGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for innerGroup.
        
        Returns:
            The innerGroup value
        
        Note:
            Delegates to inner_group property (CODING_RULE_V2_00017)
        """
        return self.inner_group  # Delegates to property

    def getOuterPort(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for outerPort.
        
        Returns:
            The outerPort value
        
        Note:
            Delegates to outer_port property (CODING_RULE_V2_00017)
        """
        return self.outer_port  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====