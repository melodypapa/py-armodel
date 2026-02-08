from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SubElementRef import (
    SubElementRef,
)


class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """
    This meta-class represents the specialization of SubElementMapping with
    respect to Application CompositeDataTypes.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 138, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # DataPrototype.
        # implemented by: ApplicationComposite.
        self._application: Optional["ApplicationComposite"] = None

    @property
    def application(self) -> Optional["ApplicationComposite"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationComposite"]) -> None:
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

        if not isinstance(value, ApplicationComposite):
            raise TypeError(
                f"application must be ApplicationComposite or None, got {type(value).__name__}"
            )
        self._application = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "ApplicationComposite":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationComposite") -> "ApplicationCompositeDataTypeSubElementRef":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["ApplicationComposite"]) -> "ApplicationCompositeDataTypeSubElementRef":
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
