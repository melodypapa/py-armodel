from typing import Optional


class CryptoSignatureScheme(ARElement):
    """
    This meta-class provides attributes to specify the TLS Signature Scheme.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoSignatureScheme

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 564, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the value of one specific TLS Signature Scheme.
        self._signature: Optional["PositiveInteger"] = None

    @property
    def signature(self) -> Optional["PositiveInteger"]:
        """Get signature (Pythonic accessor)."""
        return self._signature

    @signature.setter
    def signature(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set signature with validation.

        Args:
            value: The signature to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signature = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"signature must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._signature = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignature(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for signature.

        Returns:
            The signature value

        Note:
            Delegates to signature property (CODING_RULE_V2_00017)
        """
        return self.signature  # Delegates to property

    def setSignature(self, value: "PositiveInteger") -> "CryptoSignatureScheme":
        """
        AUTOSAR-compliant setter for signature with method chaining.

        Args:
            value: The signature to set

        Returns:
            self for method chaining

        Note:
            Delegates to signature property setter (gets validation automatically)
        """
        self.signature = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_signature(self, value: Optional["PositiveInteger"]) -> "CryptoSignatureScheme":
        """
        Set signature and return self for chaining.

        Args:
            value: The signature to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signature("value")
        """
        self.signature = value  # Use property setter (gets validation)
        return self
