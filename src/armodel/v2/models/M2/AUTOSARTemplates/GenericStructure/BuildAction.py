from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import (
    BuildActionEntity,
)


class BuildAction(BuildActionEntity):
    """
    This meta-class represents the ability to specify a build action.

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 366, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 172, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the artifacts which are created by the.
        self._createdData: List["BuildActionIoElement"] = []

    @property
    def created_data(self) -> List["BuildActionIoElement"]:
        """Get createdData (Pythonic accessor)."""
        return self._createdData
        # This association specifies a set of follow up actions.
        self._followUpAction: List["BuildAction"] = []

    @property
    def follow_up_action(self) -> List["BuildAction"]:
        """Get followUpAction (Pythonic accessor)."""
        return self._followUpAction
        # This represents the artifacts which are read by the.
        self._inputData: List["BuildActionIoElement"] = []

    @property
    def input_data(self) -> List["BuildActionIoElement"]:
        """Get inputData (Pythonic accessor)."""
        return self._inputData
        # This denotes the data which are modified by the action.
        self._modifiedData: List["BuildActionIoElement"] = []

    @property
    def modified_data(self) -> List["BuildActionIoElement"]:
        """Get modifiedData (Pythonic accessor)."""
        return self._modifiedData
        # This association specifies a set of predecessors.
        # These shall be finished before but necessarily the given action.
        # need to be performed in the specified.
        self._predecessor: List["BuildAction"] = []

    @property
    def predecessor(self) -> List["BuildAction"]:
        """Get predecessor (Pythonic accessor)."""
        return self._predecessor
        # This represents the environment which is required to use specified Processor.
        self._required: "BuildActionEnvironment" = None

    @property
    def required(self) -> "BuildActionEnvironment":
        """Get required (Pythonic accessor)."""
        return self._required

    @required.setter
    def required(self, value: "BuildActionEnvironment") -> None:
        """
        Set required with validation.

        Args:
            value: The required to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BuildActionEnvironment):
            raise TypeError(
                f"required must be BuildActionEnvironment, got {type(value).__name__}"
            )
        self._required = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCreatedData(self) -> List["BuildActionIoElement"]:
        """
        AUTOSAR-compliant getter for createdData.

        Returns:
            The createdData value

        Note:
            Delegates to created_data property (CODING_RULE_V2_00017)
        """
        return self.created_data  # Delegates to property

    def getFollowUpAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for followUpAction.

        Returns:
            The followUpAction value

        Note:
            Delegates to follow_up_action property (CODING_RULE_V2_00017)
        """
        return self.follow_up_action  # Delegates to property

    def getInputData(self) -> List["BuildActionIoElement"]:
        """
        AUTOSAR-compliant getter for inputData.

        Returns:
            The inputData value

        Note:
            Delegates to input_data property (CODING_RULE_V2_00017)
        """
        return self.input_data  # Delegates to property

    def getModifiedData(self) -> List["BuildActionIoElement"]:
        """
        AUTOSAR-compliant getter for modifiedData.

        Returns:
            The modifiedData value

        Note:
            Delegates to modified_data property (CODING_RULE_V2_00017)
        """
        return self.modified_data  # Delegates to property

    def getPredecessor(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for predecessor.

        Returns:
            The predecessor value

        Note:
            Delegates to predecessor property (CODING_RULE_V2_00017)
        """
        return self.predecessor  # Delegates to property

    def getRequired(self) -> "BuildActionEnvironment":
        """
        AUTOSAR-compliant getter for required.

        Returns:
            The required value

        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def setRequired(self, value: "BuildActionEnvironment") -> "BuildAction":
        """
        AUTOSAR-compliant setter for required with method chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Note:
            Delegates to required property setter (gets validation automatically)
        """
        self.required = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_required(self, value: "BuildActionEnvironment") -> "BuildAction":
        """
        Set required and return self for chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required("value")
        """
        self.required = value  # Use property setter (gets validation)
        return self
