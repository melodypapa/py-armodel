from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class Code(Identifiable):
    """
    A generic code descriptor. The type of the code (source or object) is
    defined via the category attribute of the associated engineering object.

    Package: M2::AUTOSARTemplates::CommonStructure::Implementation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 130, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 622, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the artifact belonging to this code descriptor.
        self._artifact: List["AutosarEngineering"] = []

    @property
    def artifact(self) -> List["AutosarEngineering"]:
        """Get artifact (Pythonic accessor)."""
        return self._artifact
        # The association callbackHeader describes in which the function declarations
                # of callback functions to a service module.
        # With this information module can include the appropriate header its
                # configuration files.
        self._callbackHeader: List["ServiceNeeds"] = []

    @property
    def callback_header(self) -> List["ServiceNeeds"]:
        """Get callbackHeader (Pythonic accessor)."""
        return self._callbackHeader

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArtifact(self) -> List["AutosarEngineering"]:
        """
        AUTOSAR-compliant getter for artifact.

        Returns:
            The artifact value

        Note:
            Delegates to artifact property (CODING_RULE_V2_00017)
        """
        return self.artifact  # Delegates to property

    def getCallbackHeader(self) -> List["ServiceNeeds"]:
        """
        AUTOSAR-compliant getter for callbackHeader.

        Returns:
            The callbackHeader value

        Note:
            Delegates to callback_header property (CODING_RULE_V2_00017)
        """
        return self.callback_header  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
