from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class NmClusterCoupling(ARObject, ABC):
    """
    Attributes that are valid for each of the referenced (coupled) clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 676, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is NmClusterCoupling:
            raise TypeError("NmClusterCoupling is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
