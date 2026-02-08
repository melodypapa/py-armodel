from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwcSupportedFeature(ARObject, ABC):
    """
    This meta-class represents a abstract base class for features that can be
    supported by a RunnableEntity.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 594, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SwcSupportedFeature:
            raise TypeError("SwcSupportedFeature is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
