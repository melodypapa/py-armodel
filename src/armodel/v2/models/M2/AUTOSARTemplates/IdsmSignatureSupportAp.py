from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class IdsmSignatureSupportAp(ARObject):
    """
    This meta-class defines, for the Adaptive Platform, the cryptographic
    algorithm and key to be used by the IdsM instance for providing signature
    information in QSEv messages.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the cryptographic algorithm to be providing
        # authentication information in QSEv content of this attribute shall comply to
        # Primitives Naming Convention".
        self._cryptoPrimitive: "String" = None

    @property
    def crypto_primitive(self) -> "String":
        """Get cryptoPrimitive (Pythonic accessor)."""
        return self._cryptoPrimitive

    @crypto_primitive.setter
    def crypto_primitive(self, value: "String") -> None:
        """
        Set cryptoPrimitive with validation.

        Args:
            value: The cryptoPrimitive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"cryptoPrimitive must be String, got {type(value).__name__}"
            )
        self._cryptoPrimitive = value
        # This reference denotes the cryptographic key to be used cryptographic
        # algorithm for providing in QSEv messages.
        self._keySlot: Optional["CryptoKeySlot"] = None

    @property
    def key_slot(self) -> Optional["CryptoKeySlot"]:
        """Get keySlot (Pythonic accessor)."""
        return self._keySlot

    @key_slot.setter
    def key_slot(self, value: Optional["CryptoKeySlot"]) -> None:
        """
        Set keySlot with validation.

        Args:
            value: The keySlot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySlot = None
            return

        if not isinstance(value, CryptoKeySlot):
            raise TypeError(
                f"keySlot must be CryptoKeySlot or None, got {type(value).__name__}"
            )
        self._keySlot = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCryptoPrimitive(self) -> "String":
        """
        AUTOSAR-compliant getter for cryptoPrimitive.

        Returns:
            The cryptoPrimitive value

        Note:
            Delegates to crypto_primitive property (CODING_RULE_V2_00017)
        """
        return self.crypto_primitive  # Delegates to property

    def setCryptoPrimitive(self, value: "String") -> "IdsmSignatureSupportAp":
        """
        AUTOSAR-compliant setter for cryptoPrimitive with method chaining.

        Args:
            value: The cryptoPrimitive to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_primitive property setter (gets validation automatically)
        """
        self.crypto_primitive = value  # Delegates to property setter
        return self

    def getKeySlot(self) -> "CryptoKeySlot":
        """
        AUTOSAR-compliant getter for keySlot.

        Returns:
            The keySlot value

        Note:
            Delegates to key_slot property (CODING_RULE_V2_00017)
        """
        return self.key_slot  # Delegates to property

    def setKeySlot(self, value: "CryptoKeySlot") -> "IdsmSignatureSupportAp":
        """
        AUTOSAR-compliant setter for keySlot with method chaining.

        Args:
            value: The keySlot to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_slot property setter (gets validation automatically)
        """
        self.key_slot = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crypto_primitive(self, value: "String") -> "IdsmSignatureSupportAp":
        """
        Set cryptoPrimitive and return self for chaining.

        Args:
            value: The cryptoPrimitive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_primitive("value")
        """
        self.crypto_primitive = value  # Use property setter (gets validation)
        return self

    def with_key_slot(self, value: Optional["CryptoKeySlot"]) -> "IdsmSignatureSupportAp":
        """
        Set keySlot and return self for chaining.

        Args:
            value: The keySlot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot("value")
        """
        self.key_slot = value  # Use property setter (gets validation)
        return self
