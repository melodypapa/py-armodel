from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwcExclusiveAreaPolicy(ARObject):
    """
    Options how to generate the ExclusiveArea related APIs. If no
    SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values
    apply.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 556, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies for this ExclusiveArea if either one common set and Exit APIs for
                # the whole software component from the Rte or if the set of Enter and Exit
                # expected per RunnableEntity.
        # The default value is.
        self._apiPrinciple: Optional["ApiPrincipleEnum"] = None

    @property
    def api_principle(self) -> Optional["ApiPrincipleEnum"]:
        """Get apiPrinciple (Pythonic accessor)."""
        return self._apiPrinciple

    @api_principle.setter
    def api_principle(self, value: Optional["ApiPrincipleEnum"]) -> None:
        """
        Set apiPrinciple with validation.

        Args:
            value: The apiPrinciple to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._apiPrinciple = None
            return

        if not isinstance(value, ApiPrincipleEnum):
            raise TypeError(
                f"apiPrinciple must be ApiPrincipleEnum or None, got {type(value).__name__}"
            )
        self._apiPrinciple = value
        self._exclusiveArea: Optional["ExclusiveArea"] = None

    @property
    def exclusive_area(self) -> Optional["ExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea

    @exclusive_area.setter
    def exclusive_area(self, value: Optional["ExclusiveArea"]) -> None:
        """
        Set exclusiveArea with validation.

        Args:
            value: The exclusiveArea to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exclusiveArea = None
            return

        if not isinstance(value, ExclusiveArea):
            raise TypeError(
                f"exclusiveArea must be ExclusiveArea or None, got {type(value).__name__}"
            )
        self._exclusiveArea = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApiPrinciple(self) -> "ApiPrincipleEnum":
        """
        AUTOSAR-compliant getter for apiPrinciple.

        Returns:
            The apiPrinciple value

        Note:
            Delegates to api_principle property (CODING_RULE_V2_00017)
        """
        return self.api_principle  # Delegates to property

    def setApiPrinciple(self, value: "ApiPrincipleEnum") -> "SwcExclusiveAreaPolicy":
        """
        AUTOSAR-compliant setter for apiPrinciple with method chaining.

        Args:
            value: The apiPrinciple to set

        Returns:
            self for method chaining

        Note:
            Delegates to api_principle property setter (gets validation automatically)
        """
        self.api_principle = value  # Delegates to property setter
        return self

    def getExclusiveArea(self) -> "ExclusiveArea":
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def setExclusiveArea(self, value: "ExclusiveArea") -> "SwcExclusiveAreaPolicy":
        """
        AUTOSAR-compliant setter for exclusiveArea with method chaining.

        Args:
            value: The exclusiveArea to set

        Returns:
            self for method chaining

        Note:
            Delegates to exclusive_area property setter (gets validation automatically)
        """
        self.exclusive_area = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_api_principle(self, value: Optional["ApiPrincipleEnum"]) -> "SwcExclusiveAreaPolicy":
        """
        Set apiPrinciple and return self for chaining.

        Args:
            value: The apiPrinciple to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_api_principle("value")
        """
        self.api_principle = value  # Use property setter (gets validation)
        return self

    def with_exclusive_area(self, value: Optional["ExclusiveArea"]) -> "SwcExclusiveAreaPolicy":
        """
        Set exclusiveArea and return self for chaining.

        Args:
            value: The exclusiveArea to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exclusive_area("value")
        """
        self.exclusive_area = value  # Use property setter (gets validation)
        return self
