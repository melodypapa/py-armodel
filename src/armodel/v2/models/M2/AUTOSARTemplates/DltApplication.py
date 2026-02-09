from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DltApplication(Identifiable):
    """
    This meta-class represents the application from which the log and trace
    message originates.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2017, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 8, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used to describe the applicationId is used in the log
        # and trace message in more detail.
        self._application: Optional["String"] = None

    @property
    def application(self) -> Optional["String"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"application must be String or None, got {type(value).__name__}"
            )
        self._application = value
        self._applicationId: Optional["String"] = None

    @property
    def application_id(self) -> Optional["String"]:
        """Get applicationId (Pythonic accessor)."""
        return self._applicationId

    @application_id.setter
    def application_id(self, value: Optional["String"]) -> None:
        """
        Set applicationId with validation.

        Args:
            value: The applicationId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationId = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"applicationId must be String or None, got {type(value).__name__}"
            )
        self._applicationId = value
        # atpVariation.
        self._context: List["DltContext"] = []

    @property
    def context(self) -> List["DltContext"]:
        """Get context (Pythonic accessor)."""
        return self._context

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "String":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "String") -> "DltApplication":
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

    def getApplicationId(self) -> "String":
        """
        AUTOSAR-compliant getter for applicationId.

        Returns:
            The applicationId value

        Note:
            Delegates to application_id property (CODING_RULE_V2_00017)
        """
        return self.application_id  # Delegates to property

    def setApplicationId(self, value: "String") -> "DltApplication":
        """
        AUTOSAR-compliant setter for applicationId with method chaining.

        Args:
            value: The applicationId to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_id property setter (gets validation automatically)
        """
        self.application_id = value  # Delegates to property setter
        return self

    def getContext(self) -> List["DltContext"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["String"]) -> "DltApplication":
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

    def with_application_id(self, value: Optional["String"]) -> "DltApplication":
        """
        Set applicationId and return self for chaining.

        Args:
            value: The applicationId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_id("value")
        """
        self.application_id = value  # Use property setter (gets validation)
        return self
