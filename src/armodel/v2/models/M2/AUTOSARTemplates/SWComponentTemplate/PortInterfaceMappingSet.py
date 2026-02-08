from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortInterfaceMappingSet(ARElement):
    """
    Specifies a set of (one or more) PortInterfaceMappings.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::PortInterfaceMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 119, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 201, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies one PortInterfaceMapping to support the of Ports typed by two
                # different PortInterfaces elements having unequal names and/or (resolution or
                # range).
        # atpVariation.
        self._portInterface: List[RefType] = []

    @property
    def port_interface(self) -> List[RefType]:
        """Get portInterface (Pythonic accessor)."""
        return self._portInterface

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPortInterface(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for portInterface.

        Returns:
            The portInterface value

        Note:
            Delegates to port_interface property (CODING_RULE_V2_00017)
        """
        return self.port_interface  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
