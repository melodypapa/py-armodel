from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CryptoServiceKey,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TlsPskIdentity(ARObject):
    """
    This element is used to describe the pre-shared key shared during the
    handshake among the communication parties, to establish a TLS connection if
    the handshake is based on the existence of a pre-shared key.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsPskIdentity

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 563, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable cryptographic key.
        self._preSharedKey: Optional["CryptoServiceKey"] = None

    @property
    def pre_shared_key(self) -> Optional["CryptoServiceKey"]:
        """Get preSharedKey (Pythonic accessor)."""
        return self._preSharedKey

    @pre_shared_key.setter
    def pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set preSharedKey with validation.

        Args:
            value: The preSharedKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._preSharedKey = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"preSharedKey must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._preSharedKey = value
        # This attribute provides the key identification.
        self._pskIdentity: Optional["String"] = None

    @property
    def psk_identity(self) -> Optional["String"]:
        """Get pskIdentity (Pythonic accessor)."""
        return self._pskIdentity

    @psk_identity.setter
    def psk_identity(self, value: Optional["String"]) -> None:
        """
        Set pskIdentity with validation.

        Args:
            value: The pskIdentity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pskIdentity = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"pskIdentity must be String or None, got {type(value).__name__}"
            )
        self._pskIdentity = value
        # This attribute provides the identity hint for a pre-shared.
        self._pskIdentityHint: Optional["String"] = None

    @property
    def psk_identity_hint(self) -> Optional["String"]:
        """Get pskIdentityHint (Pythonic accessor)."""
        return self._pskIdentityHint

    @psk_identity_hint.setter
    def psk_identity_hint(self, value: Optional["String"]) -> None:
        """
        Set pskIdentityHint with validation.

        Args:
            value: The pskIdentityHint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pskIdentityHint = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"pskIdentityHint must be String or None, got {type(value).__name__}"
            )
        self._pskIdentityHint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPreSharedKey(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for preSharedKey.

        Returns:
            The preSharedKey value

        Note:
            Delegates to pre_shared_key property (CODING_RULE_V2_00017)
        """
        return self.pre_shared_key  # Delegates to property

    def setPreSharedKey(self, value: "CryptoServiceKey") -> "TlsPskIdentity":
        """
        AUTOSAR-compliant setter for preSharedKey with method chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to pre_shared_key property setter (gets validation automatically)
        """
        self.pre_shared_key = value  # Delegates to property setter
        return self

    def getPskIdentity(self) -> "String":
        """
        AUTOSAR-compliant getter for pskIdentity.

        Returns:
            The pskIdentity value

        Note:
            Delegates to psk_identity property (CODING_RULE_V2_00017)
        """
        return self.psk_identity  # Delegates to property

    def setPskIdentity(self, value: "String") -> "TlsPskIdentity":
        """
        AUTOSAR-compliant setter for pskIdentity with method chaining.

        Args:
            value: The pskIdentity to set

        Returns:
            self for method chaining

        Note:
            Delegates to psk_identity property setter (gets validation automatically)
        """
        self.psk_identity = value  # Delegates to property setter
        return self

    def getPskIdentityHint(self) -> "String":
        """
        AUTOSAR-compliant getter for pskIdentityHint.

        Returns:
            The pskIdentityHint value

        Note:
            Delegates to psk_identity_hint property (CODING_RULE_V2_00017)
        """
        return self.psk_identity_hint  # Delegates to property

    def setPskIdentityHint(self, value: "String") -> "TlsPskIdentity":
        """
        AUTOSAR-compliant setter for pskIdentityHint with method chaining.

        Args:
            value: The pskIdentityHint to set

        Returns:
            self for method chaining

        Note:
            Delegates to psk_identity_hint property setter (gets validation automatically)
        """
        self.psk_identity_hint = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> "TlsPskIdentity":
        """
        Set preSharedKey and return self for chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pre_shared_key("value")
        """
        self.pre_shared_key = value  # Use property setter (gets validation)
        return self

    def with_psk_identity(self, value: Optional["String"]) -> "TlsPskIdentity":
        """
        Set pskIdentity and return self for chaining.

        Args:
            value: The pskIdentity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_psk_identity("value")
        """
        self.psk_identity = value  # Use property setter (gets validation)
        return self

    def with_psk_identity_hint(self, value: Optional["String"]) -> "TlsPskIdentity":
        """
        Set pskIdentityHint and return self for chaining.

        Args:
            value: The pskIdentityHint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_psk_identity_hint("value")
        """
        self.psk_identity_hint = value  # Use property setter (gets validation)
        return self
