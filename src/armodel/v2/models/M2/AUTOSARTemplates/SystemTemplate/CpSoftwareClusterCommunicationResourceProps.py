from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CpSoftwareClusterCommunicationResourceProps(ARObject, ABC):
    """
    Communication properties for cross cluster communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 902, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CpSoftwareClusterCommunicationResourceProps:
            raise TypeError("CpSoftwareClusterCommunicationResourceProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
