from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsCpServiceInstance,
)


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """
    This meta-class represents the ability to describe the existence and
    configuration of a provided service instance in a concrete implementation on
    top of DDS.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 472, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The local address over which the Service is provided.
        # atpSplitable; atpVariation.
        self._localUnicast: Optional["ApplicationEndpoint"] = None

    @property
    def local_unicast(self) -> Optional["ApplicationEndpoint"]:
        """Get localUnicast (Pythonic accessor)."""
        return self._localUnicast

    @local_unicast.setter
    def local_unicast(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set localUnicast with validation.

        Args:
            value: The localUnicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localUnicast = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"localUnicast must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._localUnicast = value
        # Minor Version of the Service that is provided by this Dds.
        self._minorVersion: Optional["PositiveInteger"] = None

    @property
    def minor_version(self) -> Optional["PositiveInteger"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minorVersion with validation.

        Args:
            value: The minorVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minorVersion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minorVersion = value
        # Collection of provided events.
        # Stereotypes: atpSplitable; atpVariation Event Tags:.
        self._providedDds: List["DdsCpServiceInstance"] = []

    @property
    def provided_dds(self) -> List["DdsCpServiceInstance"]:
        """Get providedDds (Pythonic accessor)."""
        return self._providedDds
        # This reference defines the remote unicast addresses of consumers.
        # shall ONLY be used if the remote unicast the clients is determined from the
                # not at runtime.
        # atpVariation.
        self._staticRemote: List["ApplicationEndpoint"] = []

    @property
    def static_remote(self) -> List["ApplicationEndpoint"]:
        """Get staticRemote (Pythonic accessor)."""
        return self._staticRemote

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLocalUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for localUnicast.

        Returns:
            The localUnicast value

        Note:
            Delegates to local_unicast property (CODING_RULE_V2_00017)
        """
        return self.local_unicast  # Delegates to property

    def setLocalUnicast(self, value: "ApplicationEndpoint") -> "DdsCpProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for localUnicast with method chaining.

        Args:
            value: The localUnicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_unicast property setter (gets validation automatically)
        """
        self.local_unicast = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minorVersion.

        Returns:
            The minorVersion value

        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "PositiveInteger") -> "DdsCpProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    def getProvidedDds(self) -> List["DdsCpServiceInstance"]:
        """
        AUTOSAR-compliant getter for providedDds.

        Returns:
            The providedDds value

        Note:
            Delegates to provided_dds property (CODING_RULE_V2_00017)
        """
        return self.provided_dds  # Delegates to property

    def getStaticRemote(self) -> List["ApplicationEndpoint"]:
        """
        AUTOSAR-compliant getter for staticRemote.

        Returns:
            The staticRemote value

        Note:
            Delegates to static_remote property (CODING_RULE_V2_00017)
        """
        return self.static_remote  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_local_unicast(self, value: Optional["ApplicationEndpoint"]) -> "DdsCpProvidedServiceInstance":
        """
        Set localUnicast and return self for chaining.

        Args:
            value: The localUnicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_unicast("value")
        """
        self.local_unicast = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional["PositiveInteger"]) -> "DdsCpProvidedServiceInstance":
        """
        Set minorVersion and return self for chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self
