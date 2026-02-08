from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwComponentPrototypeAssignment(ARObject):
    """
    This meta-class is only required to allow for the variant modeling of an
    instanceRef.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 894, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CP Software Cluster.
        # This reference is used to belonging SWCs if the CP Software Cluster in the
                # context of a System, by: ComponentInSystem.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.

        Args:
            value: The swComponent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.

        Returns:
            The swComponent value

        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> "SwComponentPrototypeAssignment":
        """
        AUTOSAR-compliant setter for swComponent with method chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_component(self, value: Optional["SwComponent"]) -> "SwComponentPrototypeAssignment":
        """
        Set swComponent and return self for chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self
