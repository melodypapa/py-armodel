from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class PPortComSpec(ARObject, ABC):
    """
    Communication attributes of a provided PortPrototype. This class will
    contain attributes that are valid for all kinds of provide ports,
    independent of client-server or sender-receiver communication patterns.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::PPortComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 166, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PPortComSpec:
            raise TypeError("PPortComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
