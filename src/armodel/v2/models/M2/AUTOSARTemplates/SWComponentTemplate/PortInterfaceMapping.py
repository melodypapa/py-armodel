from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class PortInterfaceMapping(Identifiable, ABC):
    """
    Specifies one PortInterfaceMapping to support the connection of Ports typed
    by two different Port Interfaces with PortInterface elements having unequal
    names and/or unequal semantic (resolution or range).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::PortInterfaceMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 119, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2046, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 200, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PortInterfaceMapping:
            raise TypeError("PortInterfaceMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
