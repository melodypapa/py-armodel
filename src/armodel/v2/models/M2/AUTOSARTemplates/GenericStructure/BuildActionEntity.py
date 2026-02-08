from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BuildActionEntity(Identifiable, ABC):
    """
    This meta-class represents the ability to describe a build action entity
    which might be specialized to environments as well as to individual build
    actions.

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 370, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is BuildActionEntity:
            raise TypeError("BuildActionEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the delivery artifacts for the entity for purposes.
        self._deliveryArtifact: List["AutosarEngineering"] = []

    @property
    def delivery_artifact(self) -> List["AutosarEngineering"]:
        """Get deliveryArtifact (Pythonic accessor)."""
        return self._deliveryArtifact
        # This specifies how to invoke a build action in the given.
        self._invocation: Optional["BuildActionInvocator"] = None

    @property
    def invocation(self) -> Optional["BuildActionInvocator"]:
        """Get invocation (Pythonic accessor)."""
        return self._invocation

    @invocation.setter
    def invocation(self, value: Optional["BuildActionInvocator"]) -> None:
        """
        Set invocation with validation.

        Args:
            value: The invocation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._invocation = None
            return

        if not isinstance(value, BuildActionInvocator):
            raise TypeError(
                f"invocation must be BuildActionInvocator or None, got {type(value).__name__}"
            )
        self._invocation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeliveryArtifact(self) -> List["AutosarEngineering"]:
        """
        AUTOSAR-compliant getter for deliveryArtifact.

        Returns:
            The deliveryArtifact value

        Note:
            Delegates to delivery_artifact property (CODING_RULE_V2_00017)
        """
        return self.delivery_artifact  # Delegates to property

    def getInvocation(self) -> "BuildActionInvocator":
        """
        AUTOSAR-compliant getter for invocation.

        Returns:
            The invocation value

        Note:
            Delegates to invocation property (CODING_RULE_V2_00017)
        """
        return self.invocation  # Delegates to property

    def setInvocation(self, value: "BuildActionInvocator") -> "BuildActionEntity":
        """
        AUTOSAR-compliant setter for invocation with method chaining.

        Args:
            value: The invocation to set

        Returns:
            self for method chaining

        Note:
            Delegates to invocation property setter (gets validation automatically)
        """
        self.invocation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_invocation(self, value: Optional["BuildActionInvocator"]) -> "BuildActionEntity":
        """
        Set invocation and return self for chaining.

        Args:
            value: The invocation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_invocation("value")
        """
        self.invocation = value  # Use property setter (gets validation)
        return self
