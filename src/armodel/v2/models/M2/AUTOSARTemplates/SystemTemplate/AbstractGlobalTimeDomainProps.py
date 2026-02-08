from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class AbstractGlobalTimeDomainProps(ARObject, ABC):
    """
    This abstract class enables a GlobalTimeDomain to specify additional
    properties.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 859, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractGlobalTimeDomainProps:
            raise TypeError("AbstractGlobalTimeDomainProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
