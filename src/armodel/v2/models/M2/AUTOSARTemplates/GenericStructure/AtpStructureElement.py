from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpStructureElement(Identifiable, ABC):
    """
    A structure element is both a classifier and a feature. As a feature, its
    structure is given by the feature it owns as a classifier.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 175, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpStructureElement:
            raise TypeError("AtpStructureElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
