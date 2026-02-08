from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CryptoEllipticCurve,
    CryptoService,
    CryptoServicePrimitive,
    CryptoSignature,
    String,
    TlsPskIdentity,
    TlsVersionEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class TlsCryptoCipherSuite(Identifiable):
    """
    This meta-class represents a cipher suite for describing cryptographic
    operations in the context of establishing a connection of
    ApplicationEndpoints that is protected by TLS.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsCryptoCipherSuite

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 562, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the crypto service primitive for and verification
        # of MACs.
        self._authentication: Optional["CryptoServicePrimitive"] = None

    @property
    def authentication(self) -> Optional["CryptoServicePrimitive"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["CryptoServicePrimitive"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, CryptoServicePrimitive):
            raise TypeError(
                f"authentication must be CryptoServicePrimitive or None, got {type(value).__name__}"
            )
        self._authentication = value
        # This reference identifies the applicable local certificate.
        self._certificate: Optional["CryptoService"] = None

    @property
    def certificate(self) -> Optional["CryptoService"]:
        """Get certificate (Pythonic accessor)."""
        return self._certificate

    @certificate.setter
    def certificate(self, value: Optional["CryptoService"]) -> None:
        """
        Set certificate with validation.

        Args:
            value: The certificate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._certificate = None
            return

        if not isinstance(value, CryptoService):
            raise TypeError(
                f"certificate must be CryptoService or None, got {type(value).__name__}"
            )
        self._certificate = value
        # Identification of the CipherSuite according to the IANA.
        self._cipherSuiteId: Optional["PositiveInteger"] = None

    @property
    def cipher_suite_id(self) -> Optional["PositiveInteger"]:
        """Get cipherSuiteId (Pythonic accessor)."""
        return self._cipherSuiteId

    @cipher_suite_id.setter
    def cipher_suite_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set cipherSuiteId with validation.

        Args:
            value: The cipherSuiteId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cipherSuiteId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"cipherSuiteId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._cipherSuiteId = value
        # Name of the CipherSuite according to the IANA list.
        self._cipherSuite: Optional["String"] = None

    @property
    def cipher_suite(self) -> Optional["String"]:
        """Get cipherSuite (Pythonic accessor)."""
        return self._cipherSuite

    @cipher_suite.setter
    def cipher_suite(self, value: Optional["String"]) -> None:
        """
        Set cipherSuite with validation.

        Args:
            value: The cipherSuite to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cipherSuite = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"cipherSuite must be String or None, got {type(value).__name__}"
            )
        self._cipherSuite = value
        # This references point to the properties of elliptic curves.
        self._ellipticCurve: List["CryptoEllipticCurve"] = []

    @property
    def elliptic_curve(self) -> List["CryptoEllipticCurve"]:
        """Get ellipticCurve (Pythonic accessor)."""
        return self._ellipticCurve
        # This reference identifies the crypto service primitive for of encryption.
        self._encryption: Optional["CryptoServicePrimitive"] = None

    @property
    def encryption(self) -> Optional["CryptoServicePrimitive"]:
        """Get encryption (Pythonic accessor)."""
        return self._encryption

    @encryption.setter
    def encryption(self, value: Optional["CryptoServicePrimitive"]) -> None:
        """
        Set encryption with validation.

        Args:
            value: The encryption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._encryption = None
            return

        if not isinstance(value, CryptoServicePrimitive):
            raise TypeError(
                f"encryption must be CryptoServicePrimitive or None, got {type(value).__name__}"
            )
        self._encryption = value
        # This reference identifies the crypto service primitives for generation and
        # verification of signatures during the algorithm.
        self._keyExchange: List["CryptoServicePrimitive"] = []

    @property
    def key_exchange(self) -> List["CryptoServicePrimitive"]:
        """Get keyExchange (Pythonic accessor)."""
        return self._keyExchange
        # This attribute identifies the priority of the cipher suite.
        # Lower values represent higher.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value
        # The aggregated TlsCryptoCipherSuiteProps provide for the TLS Cipher Suite.
        self._props: Optional["TlsCryptoCipherSuite"] = None

    @property
    def props(self) -> Optional["TlsCryptoCipherSuite"]:
        """Get props (Pythonic accessor)."""
        return self._props

    @props.setter
    def props(self, value: Optional["TlsCryptoCipherSuite"]) -> None:
        """
        Set props with validation.

        Args:
            value: The props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._props = None
            return

        if not isinstance(value, TlsCryptoCipherSuite):
            raise TypeError(
                f"props must be TlsCryptoCipherSuite or None, got {type(value).__name__}"
            )
        self._props = value
        # Pre-shared key identity shared during the handshake communication parties, to
        # establish a TLS the handshake is based on the existence of key.
        self._pskIdentity: Optional["TlsPskIdentity"] = None

    @property
    def psk_identity(self) -> Optional["TlsPskIdentity"]:
        """Get pskIdentity (Pythonic accessor)."""
        return self._pskIdentity

    @psk_identity.setter
    def psk_identity(self, value: Optional["TlsPskIdentity"]) -> None:
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

        if not isinstance(value, TlsPskIdentity):
            raise TypeError(
                f"pskIdentity must be TlsPskIdentity or None, got {type(value).__name__}"
            )
        self._pskIdentity = value
        # This reference identifies the applicable remote certificate.
        self._remote: Optional["CryptoService"] = None

    @property
    def remote(self) -> Optional["CryptoService"]:
        """Get remote (Pythonic accessor)."""
        return self._remote

    @remote.setter
    def remote(self, value: Optional["CryptoService"]) -> None:
        """
        Set remote with validation.

        Args:
            value: The remote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remote = None
            return

        if not isinstance(value, CryptoService):
            raise TypeError(
                f"remote must be CryptoService or None, got {type(value).__name__}"
            )
        self._remote = value
        # This reference points to the properties of a TLS Signature Scheme.
        self._signature: List["CryptoSignature"] = []

    @property
    def signature(self) -> List["CryptoSignature"]:
        """Get signature (Pythonic accessor)."""
        return self._signature
        # This attribute supports the definition of the applicable TLS.
        self._version: Optional["TlsVersionEnum"] = None

    @property
    def version(self) -> Optional["TlsVersionEnum"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["TlsVersionEnum"]) -> None:
        """
        Set version with validation.

        Args:
            value: The version to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, TlsVersionEnum):
            raise TypeError(
                f"version must be TlsVersionEnum or None, got {type(value).__name__}"
            )
        self._version = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "CryptoServicePrimitive") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getCertificate(self) -> "CryptoService":
        """
        AUTOSAR-compliant getter for certificate.

        Returns:
            The certificate value

        Note:
            Delegates to certificate property (CODING_RULE_V2_00017)
        """
        return self.certificate  # Delegates to property

    def setCertificate(self, value: "CryptoService") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for certificate with method chaining.

        Args:
            value: The certificate to set

        Returns:
            self for method chaining

        Note:
            Delegates to certificate property setter (gets validation automatically)
        """
        self.certificate = value  # Delegates to property setter
        return self

    def getCipherSuiteId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for cipherSuiteId.

        Returns:
            The cipherSuiteId value

        Note:
            Delegates to cipher_suite_id property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite_id  # Delegates to property

    def setCipherSuiteId(self, value: "PositiveInteger") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for cipherSuiteId with method chaining.

        Args:
            value: The cipherSuiteId to set

        Returns:
            self for method chaining

        Note:
            Delegates to cipher_suite_id property setter (gets validation automatically)
        """
        self.cipher_suite_id = value  # Delegates to property setter
        return self

    def getCipherSuite(self) -> "String":
        """
        AUTOSAR-compliant getter for cipherSuite.

        Returns:
            The cipherSuite value

        Note:
            Delegates to cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite  # Delegates to property

    def setCipherSuite(self, value: "String") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for cipherSuite with method chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Note:
            Delegates to cipher_suite property setter (gets validation automatically)
        """
        self.cipher_suite = value  # Delegates to property setter
        return self

    def getEllipticCurve(self) -> List["CryptoEllipticCurve"]:
        """
        AUTOSAR-compliant getter for ellipticCurve.

        Returns:
            The ellipticCurve value

        Note:
            Delegates to elliptic_curve property (CODING_RULE_V2_00017)
        """
        return self.elliptic_curve  # Delegates to property

    def getEncryption(self) -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant getter for encryption.

        Returns:
            The encryption value

        Note:
            Delegates to encryption property (CODING_RULE_V2_00017)
        """
        return self.encryption  # Delegates to property

    def setEncryption(self, value: "CryptoServicePrimitive") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for encryption with method chaining.

        Args:
            value: The encryption to set

        Returns:
            self for method chaining

        Note:
            Delegates to encryption property setter (gets validation automatically)
        """
        self.encryption = value  # Delegates to property setter
        return self

    def getKeyExchange(self) -> List["CryptoServicePrimitive"]:
        """
        AUTOSAR-compliant getter for keyExchange.

        Returns:
            The keyExchange value

        Note:
            Delegates to key_exchange property (CODING_RULE_V2_00017)
        """
        return self.key_exchange  # Delegates to property

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getProps(self) -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant getter for props.

        Returns:
            The props value

        Note:
            Delegates to props property (CODING_RULE_V2_00017)
        """
        return self.props  # Delegates to property

    def setProps(self, value: "TlsCryptoCipherSuite") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for props with method chaining.

        Args:
            value: The props to set

        Returns:
            self for method chaining

        Note:
            Delegates to props property setter (gets validation automatically)
        """
        self.props = value  # Delegates to property setter
        return self

    def getPskIdentity(self) -> "TlsPskIdentity":
        """
        AUTOSAR-compliant getter for pskIdentity.

        Returns:
            The pskIdentity value

        Note:
            Delegates to psk_identity property (CODING_RULE_V2_00017)
        """
        return self.psk_identity  # Delegates to property

    def setPskIdentity(self, value: "TlsPskIdentity") -> "TlsCryptoCipherSuite":
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

    def getRemote(self) -> "CryptoService":
        """
        AUTOSAR-compliant getter for remote.

        Returns:
            The remote value

        Note:
            Delegates to remote property (CODING_RULE_V2_00017)
        """
        return self.remote  # Delegates to property

    def setRemote(self, value: "CryptoService") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for remote with method chaining.

        Args:
            value: The remote to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote property setter (gets validation automatically)
        """
        self.remote = value  # Delegates to property setter
        return self

    def getSignature(self) -> List["CryptoSignature"]:
        """
        AUTOSAR-compliant getter for signature.

        Returns:
            The signature value

        Note:
            Delegates to signature property (CODING_RULE_V2_00017)
        """
        return self.signature  # Delegates to property

    def getVersion(self) -> "TlsVersionEnum":
        """
        AUTOSAR-compliant getter for version.

        Returns:
            The version value

        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "TlsVersionEnum") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for version with method chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["CryptoServicePrimitive"]) -> "TlsCryptoCipherSuite":
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_certificate(self, value: Optional["CryptoService"]) -> "TlsCryptoCipherSuite":
        """
        Set certificate and return self for chaining.

        Args:
            value: The certificate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_certificate("value")
        """
        self.certificate = value  # Use property setter (gets validation)
        return self

    def with_cipher_suite_id(self, value: Optional["PositiveInteger"]) -> "TlsCryptoCipherSuite":
        """
        Set cipherSuiteId and return self for chaining.

        Args:
            value: The cipherSuiteId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cipher_suite_id("value")
        """
        self.cipher_suite_id = value  # Use property setter (gets validation)
        return self

    def with_cipher_suite(self, value: Optional["String"]) -> "TlsCryptoCipherSuite":
        """
        Set cipherSuite and return self for chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cipher_suite("value")
        """
        self.cipher_suite = value  # Use property setter (gets validation)
        return self

    def with_encryption(self, value: Optional["CryptoServicePrimitive"]) -> "TlsCryptoCipherSuite":
        """
        Set encryption and return self for chaining.

        Args:
            value: The encryption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_encryption("value")
        """
        self.encryption = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "TlsCryptoCipherSuite":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_props(self, value: Optional["TlsCryptoCipherSuite"]) -> "TlsCryptoCipherSuite":
        """
        Set props and return self for chaining.

        Args:
            value: The props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_props("value")
        """
        self.props = value  # Use property setter (gets validation)
        return self

    def with_psk_identity(self, value: Optional["TlsPskIdentity"]) -> "TlsCryptoCipherSuite":
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

    def with_remote(self, value: Optional["CryptoService"]) -> "TlsCryptoCipherSuite":
        """
        Set remote and return self for chaining.

        Args:
            value: The remote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote("value")
        """
        self.remote = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["TlsVersionEnum"]) -> "TlsCryptoCipherSuite":
        """
        Set version and return self for chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self
