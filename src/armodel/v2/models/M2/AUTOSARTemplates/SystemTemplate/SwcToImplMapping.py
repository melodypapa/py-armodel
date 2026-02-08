from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import SwcImplementation
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SwcToImplMapping(Identifiable):
    """
    Map instances of an AtomicSwComponentType to a specific Implementation.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::SwcToImplMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 199, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a specific Implementation description.
        # to be used by the specified SW This allows to achieve more precise the
                # resource consumption that results from instance of an atomic SW component
                # onto.
        self._component: Optional["SwcImplementation"] = None

    @property
    def component(self) -> Optional["SwcImplementation"]:
        """Get component (Pythonic accessor)."""
        return self._component

    @component.setter
    def component(self, value: Optional["SwcImplementation"]) -> None:
        """
        Set component with validation.

        Args:
            value: The component to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._component = None
            return

        if not isinstance(value, SwcImplementation):
            raise TypeError(
                f"component must be SwcImplementation or None, got {type(value).__name__}"
            )
        self._component = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> "SwcImplementation":
        """
        AUTOSAR-compliant getter for component.

        Returns:
            The component value

        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def setComponent(self, value: "SwcImplementation") -> "SwcToImplMapping":
        """
        AUTOSAR-compliant setter for component with method chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Note:
            Delegates to component property setter (gets validation automatically)
        """
        self.component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component(self, value: Optional["SwcImplementation"]) -> "SwcToImplMapping":
        """
        Set component and return self for chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component("value")
        """
        self.component = value  # Use property setter (gets validation)
        return self
