from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class MacSecKayParticipant(Identifiable):
    """
    This meta-class configures a MKA participant.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 175, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the key where the ckn (Connectivity is stored.
        self._ckn: Optional["CryptoServiceKey"] = None

    @property
    def ckn(self) -> Optional["CryptoServiceKey"]:
        """Get ckn (Pythonic accessor)."""
        return self._ckn

    @ckn.setter
    def ckn(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set ckn with validation.

        Args:
            value: The ckn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ckn = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"ckn must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._ckn = value
        # Cryptography that is used by the MKA Participant.
        # Tags: atp.
        # Status=candidate.
        self._cryptoAlgo: Optional["MacSecCryptoAlgo"] = None

    @property
    def crypto_algo(self) -> Optional["MacSecCryptoAlgo"]:
        """Get cryptoAlgo (Pythonic accessor)."""
        return self._cryptoAlgo

    @crypto_algo.setter
    def crypto_algo(self, value: Optional["MacSecCryptoAlgo"]) -> None:
        """
        Set cryptoAlgo with validation.

        Args:
            value: The cryptoAlgo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoAlgo = None
            return

        if not isinstance(value, MacSecCryptoAlgo):
            raise TypeError(
                f"cryptoAlgo must be MacSecCryptoAlgo or None, got {type(value).__name__}"
            )
        self._cryptoAlgo = value
        # Reference to the key where SAK shall be stored.
        self._sak: Optional["CryptoServiceKey"] = None

    @property
    def sak(self) -> Optional["CryptoServiceKey"]:
        """Get sak (Pythonic accessor)."""
        return self._sak

    @sak.setter
    def sak(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set sak with validation.

        Args:
            value: The sak to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sak = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"sak must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._sak = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCkn(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for ckn.

        Returns:
            The ckn value

        Note:
            Delegates to ckn property (CODING_RULE_V2_00017)
        """
        return self.ckn  # Delegates to property

    def setCkn(self, value: "CryptoServiceKey") -> "MacSecKayParticipant":
        """
        AUTOSAR-compliant setter for ckn with method chaining.

        Args:
            value: The ckn to set

        Returns:
            self for method chaining

        Note:
            Delegates to ckn property setter (gets validation automatically)
        """
        self.ckn = value  # Delegates to property setter
        return self

    def getCryptoAlgo(self) -> "MacSecCryptoAlgo":
        """
        AUTOSAR-compliant getter for cryptoAlgo.

        Returns:
            The cryptoAlgo value

        Note:
            Delegates to crypto_algo property (CODING_RULE_V2_00017)
        """
        return self.crypto_algo  # Delegates to property

    def setCryptoAlgo(self, value: "MacSecCryptoAlgo") -> "MacSecKayParticipant":
        """
        AUTOSAR-compliant setter for cryptoAlgo with method chaining.

        Args:
            value: The cryptoAlgo to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_algo property setter (gets validation automatically)
        """
        self.crypto_algo = value  # Delegates to property setter
        return self

    def getSak(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for sak.

        Returns:
            The sak value

        Note:
            Delegates to sak property (CODING_RULE_V2_00017)
        """
        return self.sak  # Delegates to property

    def setSak(self, value: "CryptoServiceKey") -> "MacSecKayParticipant":
        """
        AUTOSAR-compliant setter for sak with method chaining.

        Args:
            value: The sak to set

        Returns:
            self for method chaining

        Note:
            Delegates to sak property setter (gets validation automatically)
        """
        self.sak = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ckn(self, value: Optional["CryptoServiceKey"]) -> "MacSecKayParticipant":
        """
        Set ckn and return self for chaining.

        Args:
            value: The ckn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ckn("value")
        """
        self.ckn = value  # Use property setter (gets validation)
        return self

    def with_crypto_algo(self, value: Optional["MacSecCryptoAlgo"]) -> "MacSecKayParticipant":
        """
        Set cryptoAlgo and return self for chaining.

        Args:
            value: The cryptoAlgo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_algo("value")
        """
        self.crypto_algo = value  # Use property setter (gets validation)
        return self

    def with_sak(self, value: Optional["CryptoServiceKey"]) -> "MacSecKayParticipant":
        """
        Set sak and return self for chaining.

        Args:
            value: The sak to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sak("value")
        """
        self.sak = value  # Use property setter (gets validation)
        return self
