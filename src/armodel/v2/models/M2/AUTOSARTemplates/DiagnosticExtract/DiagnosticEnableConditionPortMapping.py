from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import DiagnosticSwMapping


class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports the DiagnosticEnableCondition is mapped.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEnableConditionPortMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 251, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the EnableCondition which is mapped to a service port.
        self._enableCondition: Optional["DiagnosticEnable"] = None

    @property
    def enable_condition(self) -> Optional["DiagnosticEnable"]:
        """Get enableCondition (Pythonic accessor)."""
        return self._enableCondition

    @enable_condition.setter
    def enable_condition(self, value: Optional["DiagnosticEnable"]) -> None:
        """
        Set enableCondition with validation.

        Args:
            value: The enableCondition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableCondition = None
            return

        if not isinstance(value, DiagnosticEnable):
            raise TypeError(
                f"enableCondition must be DiagnosticEnable or None, got {type(value).__name__}"
            )
        self._enableCondition = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
                # service ports.
        # This reference can in early stages of the development in order to
                # SwcServiceDependency without a full System.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.

        Args:
            value: The swcFlatService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.

        Args:
            value: The swcService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnableCondition(self) -> "DiagnosticEnable":
        """
        AUTOSAR-compliant getter for enableCondition.

        Returns:
            The enableCondition value

        Note:
            Delegates to enable_condition property (CODING_RULE_V2_00017)
        """
        return self.enable_condition  # Delegates to property

    def setEnableCondition(self, value: "DiagnosticEnable") -> "DiagnosticEnableConditionPortMapping":
        """
        AUTOSAR-compliant setter for enableCondition with method chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_condition property setter (gets validation automatically)
        """
        self.enable_condition = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.

        Returns:
            The swcFlatService value

        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> "DiagnosticEnableConditionPortMapping":
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.

        Returns:
            The swcService value

        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> "DiagnosticEnableConditionPortMapping":
        """
        AUTOSAR-compliant setter for swcService with method chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enable_condition(self, value: Optional["DiagnosticEnable"]) -> "DiagnosticEnableConditionPortMapping":
        """
        Set enableCondition and return self for chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_condition("value")
        """
        self.enable_condition = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> "DiagnosticEnableConditionPortMapping":
        """
        Set swcFlatService and return self for chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> "DiagnosticEnableConditionPortMapping":
        """
        Set swcService and return self for chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self
