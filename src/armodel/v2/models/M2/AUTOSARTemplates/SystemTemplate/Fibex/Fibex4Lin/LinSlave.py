from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class LinSlave(ARObject):
    """
    Describing the properties of the referring ecu as a LIN slave.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinSlave

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 97, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute has the ability to control whether the node ’Assign NAD’ is
        # supported.
        self._assignNad: Optional["Boolean"] = None

    @property
    def assign_nad(self) -> Optional["Boolean"]:
        """Get assignNad (Pythonic accessor)."""
        return self._assignNad

    @assign_nad.setter
    def assign_nad(self, value: Optional["Boolean"]) -> None:
        """
        Set assignNad with validation.

        Args:
            value: The assignNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignNad = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"assignNad must be Boolean or None, got {type(value).__name__}"
            )
        self._assignNad = value
        # To distinguish LIN slaves that are used twice or more same cluster.
        self._configuredNad: Optional["Integer"] = None

    @property
    def configured_nad(self) -> Optional["Integer"]:
        """Get configuredNad (Pythonic accessor)."""
        return self._configuredNad

    @configured_nad.setter
    def configured_nad(self, value: Optional["Integer"]) -> None:
        """
        Set configuredNad with validation.

        Args:
            value: The configuredNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configuredNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"configuredNad must be Integer or None, got {type(value).__name__}"
            )
        self._configuredNad = value
        # LIN function ID.
        self._functionId: Optional["PositiveInteger"] = None

    @property
    def function_id(self) -> Optional["PositiveInteger"]:
        """Get functionId (Pythonic accessor)."""
        return self._functionId

    @function_id.setter
    def function_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionId with validation.

        Args:
            value: The functionId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"functionId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._functionId = value
        # This attribute represents the initial NAD.
        self._initialNad: Optional["Integer"] = None

    @property
    def initial_nad(self) -> Optional["Integer"]:
        """Get initialNad (Pythonic accessor)."""
        return self._initialNad

    @initial_nad.setter
    def initial_nad(self, value: Optional["Integer"]) -> None:
        """
        Set initialNad with validation.

        Args:
            value: The initialNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"initialNad must be Integer or None, got {type(value).__name__}"
            )
        self._initialNad = value
        # Each slave node shall publish one response error in one its transmitted
        # unconditional frames.
        self._linError: Optional["LinErrorResponse"] = None

    @property
    def lin_error(self) -> Optional["LinErrorResponse"]:
        """Get linError (Pythonic accessor)."""
        return self._linError

    @lin_error.setter
    def lin_error(self, value: Optional["LinErrorResponse"]) -> None:
        """
        Set linError with validation.

        Args:
            value: The linError to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linError = None
            return

        if not isinstance(value, LinErrorResponse):
            raise TypeError(
                f"linError must be LinErrorResponse or None, got {type(value).__name__}"
            )
        self._linError = value
        # Value of the N_AS timeout.
        # Unit: seconds.
        self._nasTimeout: Optional["TimeValue"] = None

    @property
    def nas_timeout(self) -> Optional["TimeValue"]:
        """Get nasTimeout (Pythonic accessor)."""
        return self._nasTimeout

    @nas_timeout.setter
    def nas_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set nasTimeout with validation.

        Args:
            value: The nasTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nasTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nasTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._nasTimeout = value
        # LIN Supplier ID.
        self._supplierId: Optional["PositiveInteger"] = None

    @property
    def supplier_id(self) -> Optional["PositiveInteger"]:
        """Get supplierId (Pythonic accessor)."""
        return self._supplierId

    @supplier_id.setter
    def supplier_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set supplierId with validation.

        Args:
            value: The supplierId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supplierId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"supplierId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._supplierId = value
        # Specifies the Variant ID.
        self._variantId: Optional["PositiveInteger"] = None

    @property
    def variant_id(self) -> Optional["PositiveInteger"]:
        """Get variantId (Pythonic accessor)."""
        return self._variantId

    @variant_id.setter
    def variant_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set variantId with validation.

        Args:
            value: The variantId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variantId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"variantId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._variantId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignNad(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for assignNad.

        Returns:
            The assignNad value

        Note:
            Delegates to assign_nad property (CODING_RULE_V2_00017)
        """
        return self.assign_nad  # Delegates to property

    def setAssignNad(self, value: "Boolean") -> "LinSlave":
        """
        AUTOSAR-compliant setter for assignNad with method chaining.

        Args:
            value: The assignNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to assign_nad property setter (gets validation automatically)
        """
        self.assign_nad = value  # Delegates to property setter
        return self

    def getConfiguredNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for configuredNad.

        Returns:
            The configuredNad value

        Note:
            Delegates to configured_nad property (CODING_RULE_V2_00017)
        """
        return self.configured_nad  # Delegates to property

    def setConfiguredNad(self, value: "Integer") -> "LinSlave":
        """
        AUTOSAR-compliant setter for configuredNad with method chaining.

        Args:
            value: The configuredNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to configured_nad property setter (gets validation automatically)
        """
        self.configured_nad = value  # Delegates to property setter
        return self

    def getFunctionId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionId.

        Returns:
            The functionId value

        Note:
            Delegates to function_id property (CODING_RULE_V2_00017)
        """
        return self.function_id  # Delegates to property

    def setFunctionId(self, value: "PositiveInteger") -> "LinSlave":
        """
        AUTOSAR-compliant setter for functionId with method chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_id property setter (gets validation automatically)
        """
        self.function_id = value  # Delegates to property setter
        return self

    def getInitialNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for initialNad.

        Returns:
            The initialNad value

        Note:
            Delegates to initial_nad property (CODING_RULE_V2_00017)
        """
        return self.initial_nad  # Delegates to property

    def setInitialNad(self, value: "Integer") -> "LinSlave":
        """
        AUTOSAR-compliant setter for initialNad with method chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_nad property setter (gets validation automatically)
        """
        self.initial_nad = value  # Delegates to property setter
        return self

    def getLinError(self) -> "LinErrorResponse":
        """
        AUTOSAR-compliant getter for linError.

        Returns:
            The linError value

        Note:
            Delegates to lin_error property (CODING_RULE_V2_00017)
        """
        return self.lin_error  # Delegates to property

    def setLinError(self, value: "LinErrorResponse") -> "LinSlave":
        """
        AUTOSAR-compliant setter for linError with method chaining.

        Args:
            value: The linError to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_error property setter (gets validation automatically)
        """
        self.lin_error = value  # Delegates to property setter
        return self

    def getNasTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nasTimeout.

        Returns:
            The nasTimeout value

        Note:
            Delegates to nas_timeout property (CODING_RULE_V2_00017)
        """
        return self.nas_timeout  # Delegates to property

    def setNasTimeout(self, value: "TimeValue") -> "LinSlave":
        """
        AUTOSAR-compliant setter for nasTimeout with method chaining.

        Args:
            value: The nasTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to nas_timeout property setter (gets validation automatically)
        """
        self.nas_timeout = value  # Delegates to property setter
        return self

    def getSupplierId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for supplierId.

        Returns:
            The supplierId value

        Note:
            Delegates to supplier_id property (CODING_RULE_V2_00017)
        """
        return self.supplier_id  # Delegates to property

    def setSupplierId(self, value: "PositiveInteger") -> "LinSlave":
        """
        AUTOSAR-compliant setter for supplierId with method chaining.

        Args:
            value: The supplierId to set

        Returns:
            self for method chaining

        Note:
            Delegates to supplier_id property setter (gets validation automatically)
        """
        self.supplier_id = value  # Delegates to property setter
        return self

    def getVariantId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for variantId.

        Returns:
            The variantId value

        Note:
            Delegates to variant_id property (CODING_RULE_V2_00017)
        """
        return self.variant_id  # Delegates to property

    def setVariantId(self, value: "PositiveInteger") -> "LinSlave":
        """
        AUTOSAR-compliant setter for variantId with method chaining.

        Args:
            value: The variantId to set

        Returns:
            self for method chaining

        Note:
            Delegates to variant_id property setter (gets validation automatically)
        """
        self.variant_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assign_nad(self, value: Optional["Boolean"]) -> "LinSlave":
        """
        Set assignNad and return self for chaining.

        Args:
            value: The assignNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assign_nad("value")
        """
        self.assign_nad = value  # Use property setter (gets validation)
        return self

    def with_configured_nad(self, value: Optional["Integer"]) -> "LinSlave":
        """
        Set configuredNad and return self for chaining.

        Args:
            value: The configuredNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_configured_nad("value")
        """
        self.configured_nad = value  # Use property setter (gets validation)
        return self

    def with_function_id(self, value: Optional["PositiveInteger"]) -> "LinSlave":
        """
        Set functionId and return self for chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_id("value")
        """
        self.function_id = value  # Use property setter (gets validation)
        return self

    def with_initial_nad(self, value: Optional["Integer"]) -> "LinSlave":
        """
        Set initialNad and return self for chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_nad("value")
        """
        self.initial_nad = value  # Use property setter (gets validation)
        return self

    def with_lin_error(self, value: Optional["LinErrorResponse"]) -> "LinSlave":
        """
        Set linError and return self for chaining.

        Args:
            value: The linError to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_error("value")
        """
        self.lin_error = value  # Use property setter (gets validation)
        return self

    def with_nas_timeout(self, value: Optional["TimeValue"]) -> "LinSlave":
        """
        Set nasTimeout and return self for chaining.

        Args:
            value: The nasTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nas_timeout("value")
        """
        self.nas_timeout = value  # Use property setter (gets validation)
        return self

    def with_supplier_id(self, value: Optional["PositiveInteger"]) -> "LinSlave":
        """
        Set supplierId and return self for chaining.

        Args:
            value: The supplierId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supplier_id("value")
        """
        self.supplier_id = value  # Use property setter (gets validation)
        return self

    def with_variant_id(self, value: Optional["PositiveInteger"]) -> "LinSlave":
        """
        Set variantId and return self for chaining.

        Args:
            value: The variantId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variant_id("value")
        """
        self.variant_id = value  # Use property setter (gets validation)
        return self
