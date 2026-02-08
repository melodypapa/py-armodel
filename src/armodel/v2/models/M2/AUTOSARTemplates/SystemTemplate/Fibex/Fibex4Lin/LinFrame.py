from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
)


class LinFrame(Frame, ABC):
    """
    Lin specific Frame element.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 428, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is LinFrame:
            raise TypeError("LinFrame is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
