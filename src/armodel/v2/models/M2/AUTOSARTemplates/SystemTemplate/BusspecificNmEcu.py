from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class BusspecificNmEcu(ARObject, ABC):
    """
    Busspecific NmEcu attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 675, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BusspecificNmEcu:
            raise TypeError("BusspecificNmEcu is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
