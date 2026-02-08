from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    MacAddressString,
    MacSecGlobalKay,
    MacSecKayParticipant,
    MacSecRoleEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecLocalKayProps(ARObject):
    """
    Configuration of the MAC Security Key Agreement Entity (KaY).

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecLocalKayProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 173, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the destination MAC Address that is to calculate the
        # ICV (Integrity Check Value).
        self._destinationMac: Optional["MacAddressString"] = None

    @property
    def destination_mac(self) -> Optional["MacAddressString"]:
        """Get destinationMac (Pythonic accessor)."""
        return self._destinationMac

    @destination_mac.setter
    def destination_mac(self, value: Optional["MacAddressString"]) -> None:
        """
        Set destinationMac with validation.

        Args:
            value: The destinationMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationMac = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"destinationMac must be MacAddressString or None, got {type(value).__name__}"
            )
        self._destinationMac = value
        # Reference to properties that are shared between MAC Key Agreement Entities.
        self._globalKayProps: Optional["MacSecGlobalKay"] = None

    @property
    def global_kay_props(self) -> Optional["MacSecGlobalKay"]:
        """Get globalKayProps (Pythonic accessor)."""
        return self._globalKayProps

    @global_kay_props.setter
    def global_kay_props(self, value: Optional["MacSecGlobalKay"]) -> None:
        """
        Set globalKayProps with validation.

        Args:
            value: The globalKayProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalKayProps = None
            return

        if not isinstance(value, MacSecGlobalKay):
            raise TypeError(
                f"globalKayProps must be MacSecGlobalKay or None, got {type(value).__name__}"
            )
        self._globalKayProps = value
        # This attribute defines the key-server priority.
        # atp.
        # Status=candidate.
        self._keyServer: Optional["PositiveInteger"] = None

    @property
    def key_server(self) -> Optional["PositiveInteger"]:
        """Get keyServer (Pythonic accessor)."""
        return self._keyServer

    @key_server.setter
    def key_server(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set keyServer with validation.

        Args:
            value: The keyServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keyServer = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"keyServer must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._keyServer = value
        # Reference to MKA participant settings supported on the 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._mkaParticipant: List["MacSecKayParticipant"] = []

    @property
    def mka_participant(self) -> List["MacSecKayParticipant"]:
        """Get mkaParticipant (Pythonic accessor)."""
        return self._mkaParticipant
        # Role of the MAC Security Key Agreement Entity.
        self._role: Optional["MacSecRoleEnum"] = None

    @property
    def role(self) -> Optional["MacSecRoleEnum"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["MacSecRoleEnum"]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, MacSecRoleEnum):
            raise TypeError(
                f"role must be MacSecRoleEnum or None, got {type(value).__name__}"
            )
        self._role = value
        # This attribute defines the source MAC Address that is to calculate the ICV
        # (Integrity Check Value).
        self._sourceMac: Optional["MacAddressString"] = None

    @property
    def source_mac(self) -> Optional["MacAddressString"]:
        """Get sourceMac (Pythonic accessor)."""
        return self._sourceMac

    @source_mac.setter
    def source_mac(self, value: Optional["MacAddressString"]) -> None:
        """
        Set sourceMac with validation.

        Args:
            value: The sourceMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceMac = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"sourceMac must be MacAddressString or None, got {type(value).__name__}"
            )
        self._sourceMac = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationMac(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for destinationMac.

        Returns:
            The destinationMac value

        Note:
            Delegates to destination_mac property (CODING_RULE_V2_00017)
        """
        return self.destination_mac  # Delegates to property

    def setDestinationMac(self, value: "MacAddressString") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for destinationMac with method chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_mac property setter (gets validation automatically)
        """
        self.destination_mac = value  # Delegates to property setter
        return self

    def getGlobalKayProps(self) -> "MacSecGlobalKay":
        """
        AUTOSAR-compliant getter for globalKayProps.

        Returns:
            The globalKayProps value

        Note:
            Delegates to global_kay_props property (CODING_RULE_V2_00017)
        """
        return self.global_kay_props  # Delegates to property

    def setGlobalKayProps(self, value: "MacSecGlobalKay") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for globalKayProps with method chaining.

        Args:
            value: The globalKayProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_kay_props property setter (gets validation automatically)
        """
        self.global_kay_props = value  # Delegates to property setter
        return self

    def getKeyServer(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for keyServer.

        Returns:
            The keyServer value

        Note:
            Delegates to key_server property (CODING_RULE_V2_00017)
        """
        return self.key_server  # Delegates to property

    def setKeyServer(self, value: "PositiveInteger") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for keyServer with method chaining.

        Args:
            value: The keyServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_server property setter (gets validation automatically)
        """
        self.key_server = value  # Delegates to property setter
        return self

    def getMkaParticipant(self) -> List["MacSecKayParticipant"]:
        """
        AUTOSAR-compliant getter for mkaParticipant.

        Returns:
            The mkaParticipant value

        Note:
            Delegates to mka_participant property (CODING_RULE_V2_00017)
        """
        return self.mka_participant  # Delegates to property

    def getRole(self) -> "MacSecRoleEnum":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "MacSecRoleEnum") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getSourceMac(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for sourceMac.

        Returns:
            The sourceMac value

        Note:
            Delegates to source_mac property (CODING_RULE_V2_00017)
        """
        return self.source_mac  # Delegates to property

    def setSourceMac(self, value: "MacAddressString") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for sourceMac with method chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_mac property setter (gets validation automatically)
        """
        self.source_mac = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_mac(self, value: Optional["MacAddressString"]) -> "MacSecLocalKayProps":
        """
        Set destinationMac and return self for chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_mac("value")
        """
        self.destination_mac = value  # Use property setter (gets validation)
        return self

    def with_global_kay_props(self, value: Optional["MacSecGlobalKay"]) -> "MacSecLocalKayProps":
        """
        Set globalKayProps and return self for chaining.

        Args:
            value: The globalKayProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_kay_props("value")
        """
        self.global_kay_props = value  # Use property setter (gets validation)
        return self

    def with_key_server(self, value: Optional["PositiveInteger"]) -> "MacSecLocalKayProps":
        """
        Set keyServer and return self for chaining.

        Args:
            value: The keyServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_server("value")
        """
        self.key_server = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["MacSecRoleEnum"]) -> "MacSecLocalKayProps":
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self

    def with_source_mac(self, value: Optional["MacAddressString"]) -> "MacSecLocalKayProps":
        """
        Set sourceMac and return self for chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_mac("value")
        """
        self.source_mac = value  # Use property setter (gets validation)
        return self
