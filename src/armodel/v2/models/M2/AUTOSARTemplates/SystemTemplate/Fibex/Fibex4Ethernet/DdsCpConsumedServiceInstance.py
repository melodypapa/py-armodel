from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpServiceInstance


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """
    This meta-class represents the ability to describe the existence and
    configuration of a consumed (required) service instance in a concrete
    implementation on top of DDS.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpConsumedServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 474, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of consumed events.
        # Stereotypes: atpSplitable; atpVariation.
        self._consumedDds: List["DdsCpServiceInstance"] = []

    @property
    def consumed_dds(self) -> List["DdsCpServiceInstance"]:
        """Get consumedDds (Pythonic accessor)."""
        return self._consumedDds
        # The local address over which the Service is consumed.
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
        # Minor Version of the ServiceInterface.
        # Value can be set to that represents the Minor Version of the or to ANY.
        self._minorVersion: Optional["AnyVersionString"] = None

    @property
    def minor_version(self) -> Optional["AnyVersionString"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["AnyVersionString"]) -> None:
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

        if not isinstance(value, AnyVersionString):
            raise TypeError(
                f"minorVersion must be AnyVersionString or None, got {type(value).__name__}"
            )
        self._minorVersion = value
        # This reference defines the remote unicast address of the provider.
        # shall ONLY be used if the remote unicast the server is determined from the
                # not at runtime.
        # atpVariation.
        self._staticRemote: Optional["ApplicationEndpoint"] = None

    @property
    def static_remote(self) -> Optional["ApplicationEndpoint"]:
        """Get staticRemote (Pythonic accessor)."""
        return self._staticRemote

    @static_remote.setter
    def static_remote(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set staticRemote with validation.

        Args:
            value: The staticRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._staticRemote = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"staticRemote must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._staticRemote = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsumedDds(self) -> List["DdsCpServiceInstance"]:
        """
        AUTOSAR-compliant getter for consumedDds.

        Returns:
            The consumedDds value

        Note:
            Delegates to consumed_dds property (CODING_RULE_V2_00017)
        """
        return self.consumed_dds  # Delegates to property

    def getLocalUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for localUnicast.

        Returns:
            The localUnicast value

        Note:
            Delegates to local_unicast property (CODING_RULE_V2_00017)
        """
        return self.local_unicast  # Delegates to property

    def setLocalUnicast(self, value: "ApplicationEndpoint") -> "DdsCpConsumedServiceInstance":
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

    def getMinorVersion(self) -> "AnyVersionString":
        """
        AUTOSAR-compliant getter for minorVersion.

        Returns:
            The minorVersion value

        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "AnyVersionString") -> "DdsCpConsumedServiceInstance":
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

    def getStaticRemote(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for staticRemote.

        Returns:
            The staticRemote value

        Note:
            Delegates to static_remote property (CODING_RULE_V2_00017)
        """
        return self.static_remote  # Delegates to property

    def setStaticRemote(self, value: "ApplicationEndpoint") -> "DdsCpConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for staticRemote with method chaining.

        Args:
            value: The staticRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to static_remote property setter (gets validation automatically)
        """
        self.static_remote = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_local_unicast(self, value: Optional["ApplicationEndpoint"]) -> "DdsCpConsumedServiceInstance":
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

    def with_minor_version(self, value: Optional["AnyVersionString"]) -> "DdsCpConsumedServiceInstance":
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

    def with_static_remote(self, value: Optional["ApplicationEndpoint"]) -> "DdsCpConsumedServiceInstance":
        """
        Set staticRemote and return self for chaining.

        Args:
            value: The staticRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_static_remote("value")
        """
        self.static_remote = value  # Use property setter (gets validation)
        return self
