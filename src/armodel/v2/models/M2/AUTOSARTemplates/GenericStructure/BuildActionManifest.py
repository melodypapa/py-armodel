from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    BuildAction,
    BuildActionEnvironment,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class BuildActionManifest(ARElement):
    """
    This meta-class represents the ability to specify a manifest for processing
    artifacts. An example use case is the processing of ECUC parameter values.

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionManifest

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 134, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 365, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 173, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a build action environment.
        # atpSplitable; atpVariation.
        self._buildAction: List["BuildActionEnvironment"] = []

    @property
    def build_action(self) -> List["BuildActionEnvironment"]:
        """Get buildAction (Pythonic accessor)."""
        return self._buildAction
        # This denotes an Action which is to be executed as part of action set.
        self._dynamicAction: List["BuildAction"] = []

    @property
    def dynamic_action(self) -> List["BuildAction"]:
        """Get dynamicAction (Pythonic accessor)."""
        return self._dynamicAction
        # This specifies the list of actions to be performed at the the process.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._startAction: List["BuildAction"] = []

    @property
    def start_action(self) -> List["BuildAction"]:
        """Get startAction (Pythonic accessor)."""
        return self._startAction
        # This specifies the set of action which shall be performed other actions in
        # the manifest were performed.
        self._tearDownAction: List["BuildAction"] = []

    @property
    def tear_down_action(self) -> List["BuildAction"]:
        """Get tearDownAction (Pythonic accessor)."""
        return self._tearDownAction

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBuildAction(self) -> List["BuildActionEnvironment"]:
        """
        AUTOSAR-compliant getter for buildAction.

        Returns:
            The buildAction value

        Note:
            Delegates to build_action property (CODING_RULE_V2_00017)
        """
        return self.build_action  # Delegates to property

    def getDynamicAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for dynamicAction.

        Returns:
            The dynamicAction value

        Note:
            Delegates to dynamic_action property (CODING_RULE_V2_00017)
        """
        return self.dynamic_action  # Delegates to property

    def getStartAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for startAction.

        Returns:
            The startAction value

        Note:
            Delegates to start_action property (CODING_RULE_V2_00017)
        """
        return self.start_action  # Delegates to property

    def getTearDownAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for tearDownAction.

        Returns:
            The tearDownAction value

        Note:
            Delegates to tear_down_action property (CODING_RULE_V2_00017)
        """
        return self.tear_down_action  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
