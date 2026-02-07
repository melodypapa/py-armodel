from typing import Optional


class AssemblySwConnector(SwConnector):
    """
    AssemblySwConnectors are exclusively used to connect SwComponentPrototypes
    in the context of a CompositionSwComponentType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::AssemblySwConnector

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 289, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 80, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2000, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 423, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # implemented by: PPortInComposition.
        self._providerInstanceRef: Optional["AbstractProvidedPort"] = None

    @property
    def provider_instance_ref(self) -> Optional["AbstractProvidedPort"]:
        """Get providerInstanceRef (Pythonic accessor)."""
        return self._providerInstanceRef

    @provider_instance_ref.setter
    def provider_instance_ref(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set providerInstanceRef with validation.

        Args:
            value: The providerInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providerInstanceRef = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"providerInstanceRef must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._providerInstanceRef = value
        # implemented by: RPortInComposition.
        self._requesterInstanceRef: Optional["AbstractRequiredPort"] = None

    @property
    def requester_instance_ref(self) -> Optional["AbstractRequiredPort"]:
        """Get requesterInstanceRef (Pythonic accessor)."""
        return self._requesterInstanceRef

    @requester_instance_ref.setter
    def requester_instance_ref(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set requesterInstanceRef with validation.

        Args:
            value: The requesterInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requesterInstanceRef = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"requesterInstanceRef must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._requesterInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProviderInstanceRef(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for providerInstanceRef.

        Returns:
            The providerInstanceRef value

        Note:
            Delegates to provider_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.provider_instance_ref  # Delegates to property

    def setProviderInstanceRef(self, value: "AbstractProvidedPort") -> "AssemblySwConnector":
        """
        AUTOSAR-compliant setter for providerInstanceRef with method chaining.

        Args:
            value: The providerInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to provider_instance_ref property setter (gets validation automatically)
        """
        self.provider_instance_ref = value  # Delegates to property setter
        return self

    def getRequesterInstanceRef(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for requesterInstanceRef.

        Returns:
            The requesterInstanceRef value

        Note:
            Delegates to requester_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.requester_instance_ref  # Delegates to property

    def setRequesterInstanceRef(self, value: "AbstractRequiredPort") -> "AssemblySwConnector":
        """
        AUTOSAR-compliant setter for requesterInstanceRef with method chaining.

        Args:
            value: The requesterInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to requester_instance_ref property setter (gets validation automatically)
        """
        self.requester_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider_instance_ref(self, value: Optional["AbstractProvidedPort"]) -> "AssemblySwConnector":
        """
        Set providerInstanceRef and return self for chaining.

        Args:
            value: The providerInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provider_instance_ref("value")
        """
        self.provider_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_requester_instance_ref(self, value: Optional["AbstractRequiredPort"]) -> "AssemblySwConnector":
        """
        Set requesterInstanceRef and return self for chaining.

        Args:
            value: The requesterInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requester_instance_ref("value")
        """
        self.requester_instance_ref = value  # Use property setter (gets validation)
        return self
