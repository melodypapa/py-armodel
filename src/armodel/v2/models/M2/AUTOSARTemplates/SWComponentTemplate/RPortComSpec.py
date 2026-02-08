from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class RPortComSpec(ARObject, ABC):
    """
    Communication attributes of a required PortPrototype. This class will
    contain attributes that are valid for all kinds of require-ports,
    independent of client-server or sender-receiver communication patterns.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 167, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 202, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is RPortComSpec:
            raise TypeError("RPortComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
