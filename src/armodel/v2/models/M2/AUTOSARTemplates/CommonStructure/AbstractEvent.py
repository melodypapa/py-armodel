from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import ExecutableEntity
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AbstractEvent(Identifiable, ABC):
    """
    This meta-class represents the abstract ability to model an event that can
    be taken to implement application software or basic software in AUTOSAR.

    Package: M2::AUTOSARTemplates::CommonStructure::InternalBehavior::AbstractEvent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 541, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 204, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractEvent:
            raise TypeError("AbstractEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the activationReasonRepresentation is referenced from the enclosing
        # AbstractEvent this shall be taken as an that the latter contributes to the
        # activating this ExecutableEntity that owns the referenced.
        self._activation: Optional["ExecutableEntity"] = None

    @property
    def activation(self) -> Optional["ExecutableEntity"]:
        """Get activation (Pythonic accessor)."""
        return self._activation

    @activation.setter
    def activation(self, value: Optional["ExecutableEntity"]) -> None:
        """
        Set activation with validation.

        Args:
            value: The activation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._activation = None
            return

        if not isinstance(value, ExecutableEntity):
            raise TypeError(
                f"activation must be ExecutableEntity or None, got {type(value).__name__}"
            )
        self._activation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivation(self) -> "ExecutableEntity":
        """
        AUTOSAR-compliant getter for activation.

        Returns:
            The activation value

        Note:
            Delegates to activation property (CODING_RULE_V2_00017)
        """
        return self.activation  # Delegates to property

    def setActivation(self, value: "ExecutableEntity") -> "AbstractEvent":
        """
        AUTOSAR-compliant setter for activation with method chaining.

        Args:
            value: The activation to set

        Returns:
            self for method chaining

        Note:
            Delegates to activation property setter (gets validation automatically)
        """
        self.activation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_activation(self, value: Optional["ExecutableEntity"]) -> "AbstractEvent":
        """
        Set activation and return self for chaining.

        Args:
            value: The activation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_activation("value")
        """
        self.activation = value  # Use property setter (gets validation)
        return self
