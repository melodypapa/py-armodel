from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class AtpDefinition(Referrable, ABC):
    """
    This abstract meta class represents "definition"-elements which identify the
    respective values. For example the value of a particular system constant is
    identified by the definition of this system constant.

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 383, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpDefinition:
            raise TypeError("AtpDefinition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
