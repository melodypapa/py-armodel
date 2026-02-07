from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class LinSlaveConfig(ARObject):
    """
    Node attributes of LIN slaves that are handled by the LinMaster. In the
    System Description LIN slaves may be described in the context of the Lin
    Master. In an ECU Extract of the LinMaster the LinSlave Ecus shall not be
    available. The information that is described here is necessary in the ECU
    Extract for the configuration of the Lin Master. The values of attributes of
    LinSlaveConfig and the corresponding LinSlave shall be identical (if both
    are defined in a System Description).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinSlaveConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 94, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
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
        # This adds the ability to become referrable to LinSlave.
        self._ident: Optional["LinSlaveConfigIdent"] = None

    @property
    def ident(self) -> Optional["LinSlaveConfigIdent"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["LinSlaveConfigIdent"]) -> None:
        """
        Set ident with validation.
        
        Args:
            value: The ident to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        if not isinstance(value, LinSlaveConfigIdent):
            raise TypeError(
                f"ident must be LinSlaveConfigIdent or None, got {type(value).__name__}"
            )
        self._ident = value
        # Initial NAD of the LIN slave.
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
        # List of all frames that are processed by the slave node 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._linConfigurable: List["LinConfigurableFrame"] = []

    @property
    def lin_configurable(self) -> List["LinConfigurableFrame"]:
        """Get linConfigurable (Pythonic accessor)."""
        return self._linConfigurable
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
        # List of all frames (unconditional frames, event-triggered frames and sporadic
                # frames) processed by the slave This element is necessary for the LIN 2.
        # 1.
        self._linOrdered: List["LinOrderedConfigurable"] = []

    @property
    def lin_ordered(self) -> List["LinOrderedConfigurable"]:
        """Get linOrdered (Pythonic accessor)."""
        return self._linOrdered
        # Version specifier for a communication protocol.
        # Protocol the LinMaster and the LinSlaves may be.
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.
        
        Args:
            value: The protocolVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value
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

    def getConfiguredNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for configuredNad.
        
        Returns:
            The configuredNad value
        
        Note:
            Delegates to configured_nad property (CODING_RULE_V2_00017)
        """
        return self.configured_nad  # Delegates to property

    def setConfiguredNad(self, value: "Integer") -> "LinSlaveConfig":
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

    def setFunctionId(self, value: "PositiveInteger") -> "LinSlaveConfig":
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

    def getIdent(self) -> "LinSlaveConfigIdent":
        """
        AUTOSAR-compliant getter for ident.
        
        Returns:
            The ident value
        
        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "LinSlaveConfigIdent") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for ident with method chaining.
        
        Args:
            value: The ident to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
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

    def setInitialNad(self, value: "Integer") -> "LinSlaveConfig":
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

    def getLinConfigurable(self) -> List["LinConfigurableFrame"]:
        """
        AUTOSAR-compliant getter for linConfigurable.
        
        Returns:
            The linConfigurable value
        
        Note:
            Delegates to lin_configurable property (CODING_RULE_V2_00017)
        """
        return self.lin_configurable  # Delegates to property

    def getLinError(self) -> "LinErrorResponse":
        """
        AUTOSAR-compliant getter for linError.
        
        Returns:
            The linError value
        
        Note:
            Delegates to lin_error property (CODING_RULE_V2_00017)
        """
        return self.lin_error  # Delegates to property

    def setLinError(self, value: "LinErrorResponse") -> "LinSlaveConfig":
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

    def getLinOrdered(self) -> List["LinOrderedConfigurable"]:
        """
        AUTOSAR-compliant getter for linOrdered.
        
        Returns:
            The linOrdered value
        
        Note:
            Delegates to lin_ordered property (CODING_RULE_V2_00017)
        """
        return self.lin_ordered  # Delegates to property

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.
        
        Returns:
            The protocolVersion value
        
        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.
        
        Args:
            value: The protocolVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
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

    def setSupplierId(self, value: "PositiveInteger") -> "LinSlaveConfig":
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

    def setVariantId(self, value: "PositiveInteger") -> "LinSlaveConfig":
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

    def with_configured_nad(self, value: Optional["Integer"]) -> "LinSlaveConfig":
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

    def with_function_id(self, value: Optional["PositiveInteger"]) -> "LinSlaveConfig":
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

    def with_ident(self, value: Optional["LinSlaveConfigIdent"]) -> "LinSlaveConfig":
        """
        Set ident and return self for chaining.
        
        Args:
            value: The ident to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self

    def with_initial_nad(self, value: Optional["Integer"]) -> "LinSlaveConfig":
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

    def with_lin_error(self, value: Optional["LinErrorResponse"]) -> "LinSlaveConfig":
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

    def with_protocol_version(self, value: Optional["String"]) -> "LinSlaveConfig":
        """
        Set protocolVersion and return self for chaining.
        
        Args:
            value: The protocolVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self

    def with_supplier_id(self, value: Optional["PositiveInteger"]) -> "LinSlaveConfig":
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

    def with_variant_id(self, value: Optional["PositiveInteger"]) -> "LinSlaveConfig":
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