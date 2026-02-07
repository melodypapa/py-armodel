from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.CollectableElement import (
    CollectableElement,
)


class PackageableElement(CollectableElement, ABC):
    """
    This meta-class specifies the ability to be a member of an AUTOSAR package.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage::PackageableElement

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 302, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2042, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 54, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PackageableElement:
            raise TypeError("PackageableElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
