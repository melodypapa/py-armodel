from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import AtpFeature
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpClassifier(Identifiable, ABC):
    """
    A classifier classifies M0 instances according to their features. Or: a
    classifier is something that has instances - an M1 classifier has M0
    instances.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpClassifier

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 173, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpClassifier:
            raise TypeError("AtpClassifier is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a feature of the classifier.
        self._atpFeature: List["AtpFeature"] = []

    @property
    def atp_feature(self) -> List["AtpFeature"]:
        """Get atpFeature (Pythonic accessor)."""
        return self._atpFeature

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpFeature(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for atpFeature.

        Returns:
            The atpFeature value

        Note:
            Delegates to atp_feature property (CODING_RULE_V2_00017)
        """
        return self.atp_feature  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
