from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RptProfile(Identifiable):
    """
    The RptProfile describes the common properties of a Rapid Prototyping
    method.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 853, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Highest service point id useable for RTE generated points.
        self._maxService: Optional["PositiveInteger"] = None

    @property
    def max_service(self) -> Optional["PositiveInteger"]:
        """Get maxService (Pythonic accessor)."""
        return self._maxService

    @max_service.setter
    def max_service(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxService with validation.

        Args:
            value: The maxService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxService = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxService must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxService = value
        self._minServicePoint: Optional["PositiveInteger"] = None

    @property
    def min_service_point(self) -> Optional["PositiveInteger"]:
        """Get minServicePoint (Pythonic accessor)."""
        return self._minServicePoint

    @min_service_point.setter
    def min_service_point(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minServicePoint with validation.

        Args:
            value: The minServicePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minServicePoint = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minServicePoint must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minServicePoint = value
        # This symbol is used for post-build hooking 1228 Document ID 62:
                # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._servicePoint: Optional["CIdentifier"] = None

    @property
    def service_point(self) -> Optional["CIdentifier"]:
        """Get servicePoint (Pythonic accessor)."""
        return self._servicePoint

    @service_point.setter
    def service_point(self, value: Optional["CIdentifier"]) -> None:
        """
        Set servicePoint with validation.

        Args:
            value: The servicePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._servicePoint = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"servicePoint must be CIdentifier or None, got {type(value).__name__}"
            )
        self._servicePoint = value
        # stimEnabler is "none" then no is passed to the service function.
        # stimulation enabler will be passed as a.
        self._stimEnabler: Optional["RptEnablerImplType"] = None

    @property
    def stim_enabler(self) -> Optional["RptEnablerImplType"]:
        """Get stimEnabler (Pythonic accessor)."""
        return self._stimEnabler

    @stim_enabler.setter
    def stim_enabler(self, value: Optional["RptEnablerImplType"]) -> None:
        """
        Set stimEnabler with validation.

        Args:
            value: The stimEnabler to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stimEnabler = None
            return

        if not isinstance(value, RptEnablerImplType):
            raise TypeError(
                f"stimEnabler must be RptEnablerImplType or None, got {type(value).__name__}"
            )
        self._stimEnabler = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxService(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxService.

        Returns:
            The maxService value

        Note:
            Delegates to max_service property (CODING_RULE_V2_00017)
        """
        return self.max_service  # Delegates to property

    def setMaxService(self, value: "PositiveInteger") -> "RptProfile":
        """
        AUTOSAR-compliant setter for maxService with method chaining.

        Args:
            value: The maxService to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_service property setter (gets validation automatically)
        """
        self.max_service = value  # Delegates to property setter
        return self

    def getMinServicePoint(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minServicePoint.

        Returns:
            The minServicePoint value

        Note:
            Delegates to min_service_point property (CODING_RULE_V2_00017)
        """
        return self.min_service_point  # Delegates to property

    def setMinServicePoint(self, value: "PositiveInteger") -> "RptProfile":
        """
        AUTOSAR-compliant setter for minServicePoint with method chaining.

        Args:
            value: The minServicePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_service_point property setter (gets validation automatically)
        """
        self.min_service_point = value  # Delegates to property setter
        return self

    def getServicePoint(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for servicePoint.

        Returns:
            The servicePoint value

        Note:
            Delegates to service_point property (CODING_RULE_V2_00017)
        """
        return self.service_point  # Delegates to property

    def setServicePoint(self, value: "CIdentifier") -> "RptProfile":
        """
        AUTOSAR-compliant setter for servicePoint with method chaining.

        Args:
            value: The servicePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_point property setter (gets validation automatically)
        """
        self.service_point = value  # Delegates to property setter
        return self

    def getStimEnabler(self) -> "RptEnablerImplType":
        """
        AUTOSAR-compliant getter for stimEnabler.

        Returns:
            The stimEnabler value

        Note:
            Delegates to stim_enabler property (CODING_RULE_V2_00017)
        """
        return self.stim_enabler  # Delegates to property

    def setStimEnabler(self, value: "RptEnablerImplType") -> "RptProfile":
        """
        AUTOSAR-compliant setter for stimEnabler with method chaining.

        Args:
            value: The stimEnabler to set

        Returns:
            self for method chaining

        Note:
            Delegates to stim_enabler property setter (gets validation automatically)
        """
        self.stim_enabler = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_service(self, value: Optional["PositiveInteger"]) -> "RptProfile":
        """
        Set maxService and return self for chaining.

        Args:
            value: The maxService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_service("value")
        """
        self.max_service = value  # Use property setter (gets validation)
        return self

    def with_min_service_point(self, value: Optional["PositiveInteger"]) -> "RptProfile":
        """
        Set minServicePoint and return self for chaining.

        Args:
            value: The minServicePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_service_point("value")
        """
        self.min_service_point = value  # Use property setter (gets validation)
        return self

    def with_service_point(self, value: Optional["CIdentifier"]) -> "RptProfile":
        """
        Set servicePoint and return self for chaining.

        Args:
            value: The servicePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_point("value")
        """
        self.service_point = value  # Use property setter (gets validation)
        return self

    def with_stim_enabler(self, value: Optional["RptEnablerImplType"]) -> "RptProfile":
        """
        Set stimEnabler and return self for chaining.

        Args:
            value: The stimEnabler to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stim_enabler("value")
        """
        self.stim_enabler = value  # Use property setter (gets validation)
        return self
