from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CryptoCertificate,
    CryptoCertificateFormat,
    CryptoService,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceCertificate(ARElement):
    """
    This meta-class represents the ability to model a cryptographic certificate.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServiceCertificate

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 565, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a description of the family of algorithm used to
        # generate public key and the cryptographic certificate.
        self._algorithmFamily: Optional["CryptoCertificate"] = None

    @property
    def algorithm_family(self) -> Optional["CryptoCertificate"]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional["CryptoCertificate"]) -> None:
        """
        Set algorithmFamily with validation.

        Args:
            value: The algorithmFamily to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmFamily = None
            return

        if not isinstance(value, CryptoCertificate):
            raise TypeError(
                f"algorithmFamily must be CryptoCertificate or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        # This attribute can be used to provide information about format used to create
        # the certificate.
        self._format: Optional["CryptoCertificateFormat"] = None

    @property
    def format(self) -> Optional["CryptoCertificateFormat"]:
        """Get format (Pythonic accessor)."""
        return self._format

    @format.setter
    def format(self, value: Optional["CryptoCertificateFormat"]) -> None:
        """
        Set format with validation.

        Args:
            value: The format to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._format = None
            return

        if not isinstance(value, CryptoCertificateFormat):
            raise TypeError(
                f"format must be CryptoCertificateFormat or None, got {type(value).__name__}"
            )
        self._format = value
        # This attribute represents the ability to define the length of the certificate
        # in bytes.
        self._maximum: Optional["PositiveInteger"] = None

    @property
    def maximum(self) -> Optional["PositiveInteger"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maximum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maximum = value
        # The reference identifies the next higher certificate in the certificate
        # chain.
        self._nextHigher: Optional["CryptoService"] = None

    @property
    def next_higher(self) -> Optional["CryptoService"]:
        """Get nextHigher (Pythonic accessor)."""
        return self._nextHigher

    @next_higher.setter
    def next_higher(self, value: Optional["CryptoService"]) -> None:
        """
        Set nextHigher with validation.

        Args:
            value: The nextHigher to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nextHigher = None
            return

        if not isinstance(value, CryptoService):
            raise TypeError(
                f"nextHigher must be CryptoService or None, got {type(value).__name__}"
            )
        self._nextHigher = value
        # Server Name Indication (SNI) is needed if the IP address multiple servers (on
                # the same port), each of them different certificate.
        # client sends the SNI to the Server in the client hello, looks the SNI up in
                # its certificate list and uses identified by the SNI.
        self._serverName: Optional["String"] = None

    @property
    def server_name(self) -> Optional["String"]:
        """Get serverName (Pythonic accessor)."""
        return self._serverName

    @server_name.setter
    def server_name(self, value: Optional["String"]) -> None:
        """
        Set serverName with validation.

        Args:
            value: The serverName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serverName = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"serverName must be String or None, got {type(value).__name__}"
            )
        self._serverName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> "CryptoCertificate":
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: "CryptoCertificate") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for algorithmFamily with method chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_family property setter (gets validation automatically)
        """
        self.algorithm_family = value  # Delegates to property setter
        return self

    def getFormat(self) -> "CryptoCertificateFormat":
        """
        AUTOSAR-compliant getter for format.

        Returns:
            The format value

        Note:
            Delegates to format property (CODING_RULE_V2_00017)
        """
        return self.format  # Delegates to property

    def setFormat(self, value: "CryptoCertificateFormat") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for format with method chaining.

        Args:
            value: The format to set

        Returns:
            self for method chaining

        Note:
            Delegates to format property setter (gets validation automatically)
        """
        self.format = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "PositiveInteger") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getNextHigher(self) -> "CryptoService":
        """
        AUTOSAR-compliant getter for nextHigher.

        Returns:
            The nextHigher value

        Note:
            Delegates to next_higher property (CODING_RULE_V2_00017)
        """
        return self.next_higher  # Delegates to property

    def setNextHigher(self, value: "CryptoService") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for nextHigher with method chaining.

        Args:
            value: The nextHigher to set

        Returns:
            self for method chaining

        Note:
            Delegates to next_higher property setter (gets validation automatically)
        """
        self.next_higher = value  # Delegates to property setter
        return self

    def getServerName(self) -> "String":
        """
        AUTOSAR-compliant getter for serverName.

        Returns:
            The serverName value

        Note:
            Delegates to server_name property (CODING_RULE_V2_00017)
        """
        return self.server_name  # Delegates to property

    def setServerName(self, value: "String") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for serverName with method chaining.

        Args:
            value: The serverName to set

        Returns:
            self for method chaining

        Note:
            Delegates to server_name property setter (gets validation automatically)
        """
        self.server_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["CryptoCertificate"]) -> "CryptoServiceCertificate":
        """
        Set algorithmFamily and return self for chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_family("value")
        """
        self.algorithm_family = value  # Use property setter (gets validation)
        return self

    def with_format(self, value: Optional["CryptoCertificateFormat"]) -> "CryptoServiceCertificate":
        """
        Set format and return self for chaining.

        Args:
            value: The format to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_format("value")
        """
        self.format = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["PositiveInteger"]) -> "CryptoServiceCertificate":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_next_higher(self, value: Optional["CryptoService"]) -> "CryptoServiceCertificate":
        """
        Set nextHigher and return self for chaining.

        Args:
            value: The nextHigher to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_next_higher("value")
        """
        self.next_higher = value  # Use property setter (gets validation)
        return self

    def with_server_name(self, value: Optional["String"]) -> "CryptoServiceCertificate":
        """
        Set serverName and return self for chaining.

        Args:
            value: The serverName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_server_name("value")
        """
        self.server_name = value  # Use property setter (gets validation)
        return self
