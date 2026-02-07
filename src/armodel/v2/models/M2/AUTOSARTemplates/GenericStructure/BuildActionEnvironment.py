from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BuildActionEnvironment(Identifiable):
    """
    This meta-class represents the ability to specify a build action
    environment.

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionEnvironment

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 370, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 173, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a general data structure intended to for the
        # BuildActionEnvironment.
        self._sdg: List["Sdg"] = []

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.

        Returns:
            The sdg value

        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
