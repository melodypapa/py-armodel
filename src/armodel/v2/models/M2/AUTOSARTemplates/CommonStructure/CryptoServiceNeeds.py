from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ServiceNeeds,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceNeeds(ServiceNeeds):
    """
    Specifies the needs on the configuration of the CryptoServiceManager for one
    ConfigID (see Specification AUTOSAR_SWS_CSM.doc). An instance of this class
    is used to find out which ports of a software-component belong to this
    ConfigID.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::CryptoServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 235, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 733, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a description of the family (e.
        # g.
        # crypto algorithm implemented by the crypto case.
        self._algorithmFamily: Optional["String"] = None

    @property
    def algorithm_family(self) -> Optional["String"]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"algorithmFamily must be String or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        # This meta-class has the ability to represent a crypto case.
        self._algorithmMode: Optional["String"] = None

    @property
    def algorithm_mode(self) -> Optional["String"]:
        """Get algorithmMode (Pythonic accessor)."""
        return self._algorithmMode

    @algorithm_mode.setter
    def algorithm_mode(self, value: Optional["String"]) -> None:
        """
        Set algorithmMode with validation.

        Args:
            value: The algorithmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmMode = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"algorithmMode must be String or None, got {type(value).__name__}"
            )
        self._algorithmMode = value
        # This attribute allows for a verbal description of the cryptographic key.
        # The goal is to pass a hint for about how to treat the corresponding case.
        self._cryptoKey: Optional["String"] = None

    @property
    def crypto_key(self) -> Optional["String"]:
        """Get cryptoKey (Pythonic accessor)."""
        return self._cryptoKey

    @crypto_key.setter
    def crypto_key(self, value: Optional["String"]) -> None:
        """
        Set cryptoKey with validation.

        Args:
            value: The cryptoKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoKey = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"cryptoKey must be String or None, got {type(value).__name__}"
            )
        self._cryptoKey = value
        # The maximum length of a cryptographic key, that is used the
        # software-component or module for this bit.
        self._maximumKey: Optional["PositiveInteger"] = None

    @property
    def maximum_key(self) -> Optional["PositiveInteger"]:
        """Get maximumKey (Pythonic accessor)."""
        return self._maximumKey

    @maximum_key.setter
    def maximum_key(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maximumKey with validation.

        Args:
            value: The maximumKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumKey = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maximumKey must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maximumKey = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: "String") -> "CryptoServiceNeeds":
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

    def getAlgorithmMode(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmMode.

        Returns:
            The algorithmMode value

        Note:
            Delegates to algorithm_mode property (CODING_RULE_V2_00017)
        """
        return self.algorithm_mode  # Delegates to property

    def setAlgorithmMode(self, value: "String") -> "CryptoServiceNeeds":
        """
        AUTOSAR-compliant setter for algorithmMode with method chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_mode property setter (gets validation automatically)
        """
        self.algorithm_mode = value  # Delegates to property setter
        return self

    def getCryptoKey(self) -> "String":
        """
        AUTOSAR-compliant getter for cryptoKey.

        Returns:
            The cryptoKey value

        Note:
            Delegates to crypto_key property (CODING_RULE_V2_00017)
        """
        return self.crypto_key  # Delegates to property

    def setCryptoKey(self, value: "String") -> "CryptoServiceNeeds":
        """
        AUTOSAR-compliant setter for cryptoKey with method chaining.

        Args:
            value: The cryptoKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_key property setter (gets validation automatically)
        """
        self.crypto_key = value  # Delegates to property setter
        return self

    def getMaximumKey(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maximumKey.

        Returns:
            The maximumKey value

        Note:
            Delegates to maximum_key property (CODING_RULE_V2_00017)
        """
        return self.maximum_key  # Delegates to property

    def setMaximumKey(self, value: "PositiveInteger") -> "CryptoServiceNeeds":
        """
        AUTOSAR-compliant setter for maximumKey with method chaining.

        Args:
            value: The maximumKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum_key property setter (gets validation automatically)
        """
        self.maximum_key = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["String"]) -> "CryptoServiceNeeds":
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

    def with_algorithm_mode(self, value: Optional["String"]) -> "CryptoServiceNeeds":
        """
        Set algorithmMode and return self for chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_mode("value")
        """
        self.algorithm_mode = value  # Use property setter (gets validation)
        return self

    def with_crypto_key(self, value: Optional["String"]) -> "CryptoServiceNeeds":
        """
        Set cryptoKey and return self for chaining.

        Args:
            value: The cryptoKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_key("value")
        """
        self.crypto_key = value  # Use property setter (gets validation)
        return self

    def with_maximum_key(self, value: Optional["PositiveInteger"]) -> "CryptoServiceNeeds":
        """
        Set maximumKey and return self for chaining.

        Args:
            value: The maximumKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum_key("value")
        """
        self.maximum_key = value  # Use property setter (gets validation)
        return self
