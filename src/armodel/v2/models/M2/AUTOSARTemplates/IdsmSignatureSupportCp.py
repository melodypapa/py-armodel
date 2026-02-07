from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class IdsmSignatureSupportCp(ARObject):
    """
    This meta-class defines, for the Classic Platform, the cryptographic
    algorithm and key to be used by the IdsM instance for providing signature
    information in QSEv messages.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmSignatureSupportCp

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference dennotes the cryptographic primitives for information in QSEv
        # messages.
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
        # This reference denotes the cryptographic key to be used the cryptographic
        # algorithm for providing in QSEv messages.
        self._cryptoService: Optional["CryptoServiceKey"] = None

    @property
    def crypto_service(self) -> Optional["CryptoServiceKey"]:
        """Get cryptoService (Pythonic accessor)."""
        return self._cryptoService

    @crypto_service.setter
    def crypto_service(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set cryptoService with validation.

        Args:
            value: The cryptoService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoService = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"cryptoService must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._cryptoService = value

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

    def setAuthentication(self, value: "CryptoServicePrimitive") -> "IdsmSignatureSupportCp":
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

    def getCryptoService(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for cryptoService.

        Returns:
            The cryptoService value

        Note:
            Delegates to crypto_service property (CODING_RULE_V2_00017)
        """
        return self.crypto_service  # Delegates to property

    def setCryptoService(self, value: "CryptoServiceKey") -> "IdsmSignatureSupportCp":
        """
        AUTOSAR-compliant setter for cryptoService with method chaining.

        Args:
            value: The cryptoService to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_service property setter (gets validation automatically)
        """
        self.crypto_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["CryptoServicePrimitive"]) -> "IdsmSignatureSupportCp":
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

    def with_crypto_service(self, value: Optional["CryptoServiceKey"]) -> "IdsmSignatureSupportCp":
        """
        Set cryptoService and return self for chaining.

        Args:
            value: The cryptoService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_service("value")
        """
        self.crypto_service = value  # Use property setter (gets validation)
        return self
