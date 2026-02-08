from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractReferenceDef


class EcucAbstractExternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """
    Common abstract class to gather attributes for external references (where
    the destination is not located in the ECU Configuration Description but in
    an another AUTOSAR Template).

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractExternalReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 72, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractExternalReferenceDef:
            raise TypeError("EcucAbstractExternalReferenceDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
