from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Implementation,
    PerInstanceMemory,
    String,
    SwcInternalBehavior,
)


class SwcImplementation(Implementation):
    """
    This meta-class represents a specialization of the general Implementation
    meta-class with respect to the usage in application software.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation::SwcImplementation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 344, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 623, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2069, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The internal behavior implemented by this 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._behavior: Optional["SwcInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set behavior with validation.

        Args:
            value: The behavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"behavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value
        # Allows a definition of the size of the per-instance memory for this
                # implementation.
        # The aggregation of PerInstance subject to variability with the purpose to in
                # the software components different algorithms in the requiring different
                # number of memory this case PerInstanceMemory.
        # atpVariation.
        self._perInstance: List["PerInstanceMemory"] = []

    @property
    def per_instance(self) -> List["PerInstanceMemory"]:
        """Get perInstance (Pythonic accessor)."""
        return self._perInstance
        # Identify a specific RTE vendor.
        # This information is important at the time of integrating (in the application
                # code with the RTE.
        # The that (if the association exists) the has been created to fit to the
                # provided by this specific vendor.
        # integrate the code with another RTE vendor mode is in general not possible.
        self._required: Optional["String"] = None

    @property
    def required(self) -> Optional["String"]:
        """Get required (Pythonic accessor)."""
        return self._required

    @required.setter
    def required(self, value: Optional["String"]) -> None:
        """
        Set required with validation.

        Args:
            value: The required to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._required = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"required must be String or None, got {type(value).__name__}"
            )
        self._required = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.

        Returns:
            The behavior value

        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "SwcInternalBehavior") -> "SwcImplementation":
        """
        AUTOSAR-compliant setter for behavior with method chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    def getPerInstance(self) -> List["PerInstanceMemory"]:
        """
        AUTOSAR-compliant getter for perInstance.

        Returns:
            The perInstance value

        Note:
            Delegates to per_instance property (CODING_RULE_V2_00017)
        """
        return self.per_instance  # Delegates to property

    def getRequired(self) -> "String":
        """
        AUTOSAR-compliant getter for required.

        Returns:
            The required value

        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def setRequired(self, value: "String") -> "SwcImplementation":
        """
        AUTOSAR-compliant setter for required with method chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Note:
            Delegates to required property setter (gets validation automatically)
        """
        self.required = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior(self, value: Optional["SwcInternalBehavior"]) -> "SwcImplementation":
        """
        Set behavior and return self for chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self

    def with_required(self, value: Optional["String"]) -> "SwcImplementation":
        """
        Set required and return self for chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required("value")
        """
        self.required = value  # Use property setter (gets validation)
        return self
