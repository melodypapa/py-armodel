from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SwcToApplicationPartitionMapping(Identifiable):
    """
    Allows to map a given SwComponentPrototype to a formally defined partition
    at a point in time when the corresponding EcuInstance is not yet known or
    defined.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 200, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ApplicationPartition to which a Sw is mapped.
        self._application: Optional["ApplicationPartition"] = None

    @property
    def application(self) -> Optional["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationPartition"]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationPartition):
            raise TypeError(
                f"application must be ApplicationPartition or None, got {type(value).__name__}"
            )
        self._application = value
        # mapped to the referenced ApplicationPartition.
        # If the referenced is a composition, this all atomic software components
                # within the mapped to the ApplicationPartition.
        # is additionally a mapping of some SwComponent the Composition to another
                # Application inner mapping overrides the outer mapping.
        # by: ComponentInSystem.
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

    def getApplication(self) -> "ApplicationPartition":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationPartition") -> "SwcToApplicationPartitionMapping":
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.

        Returns:
            The swComponent value

        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> "SwcToApplicationPartitionMapping":
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

    def with_application(self, value: Optional["ApplicationPartition"]) -> "SwcToApplicationPartitionMapping":
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_sw_component(self, value: Optional["SwComponent"]) -> "SwcToApplicationPartitionMapping":
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
