from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class CommunicationCycle(ARObject, ABC):
    """
    The communication cycle where the frame is sent.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology::CommunicationCycle

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 424, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommunicationCycle:
            raise TypeError("CommunicationCycle is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
