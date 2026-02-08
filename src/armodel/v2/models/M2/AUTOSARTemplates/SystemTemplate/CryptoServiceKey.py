from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class CryptoServiceKey(ARElement):
    """
    This meta-class has the ability to represent a crypto key.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 377, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 58, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represent the description of the family of the algorithm.
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
        # This aggregation represents the ability to assign a value to the crypto key
        # as part of the system value can then be taken for the the respective ECU.
        self._development: Optional["ValueSpecification"] = None

    @property
    def development(self) -> Optional["ValueSpecification"]:
        """Get development (Pythonic accessor)."""
        return self._development

    @development.setter
    def development(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set development with validation.

        Args:
            value: The development to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._development = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"development must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._development = value
        # This attribute describes how a the specific cryptographic is created.
        self._keyGeneration: Optional["CryptoServiceKey"] = None

    @property
    def key_generation(self) -> Optional["CryptoServiceKey"]:
        """Get keyGeneration (Pythonic accessor)."""
        return self._keyGeneration

    @key_generation.setter
    def key_generation(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set keyGeneration with validation.

        Args:
            value: The keyGeneration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keyGeneration = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"keyGeneration must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._keyGeneration = value
        # This attribute describes where the enclosing shall be stored.
        # AUTOSAR reserves for this attributes but it is possible to insert as well.
        self._keyStorageType: Optional["String"] = None

    @property
    def key_storage_type(self) -> Optional["String"]:
        """Get keyStorageType (Pythonic accessor)."""
        return self._keyStorageType

    @key_storage_type.setter
    def key_storage_type(self, value: Optional["String"]) -> None:
        """
        Set keyStorageType with validation.

        Args:
            value: The keyStorageType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keyStorageType = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"keyStorageType must be String or None, got {type(value).__name__}"
            )
        self._keyStorageType = value
        # This attribute describes the length of the cryptographic bits.
        self._length: Optional["PositiveInteger"] = None

    @property
    def length(self) -> Optional["PositiveInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"length must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._length = value

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

    def setAlgorithmFamily(self, value: "String") -> "CryptoServiceKey":
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

    def getDevelopment(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for development.

        Returns:
            The development value

        Note:
            Delegates to development property (CODING_RULE_V2_00017)
        """
        return self.development  # Delegates to property

    def setDevelopment(self, value: "ValueSpecification") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for development with method chaining.

        Args:
            value: The development to set

        Returns:
            self for method chaining

        Note:
            Delegates to development property setter (gets validation automatically)
        """
        self.development = value  # Delegates to property setter
        return self

    def getKeyGeneration(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for keyGeneration.

        Returns:
            The keyGeneration value

        Note:
            Delegates to key_generation property (CODING_RULE_V2_00017)
        """
        return self.key_generation  # Delegates to property

    def setKeyGeneration(self, value: "CryptoServiceKey") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for keyGeneration with method chaining.

        Args:
            value: The keyGeneration to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_generation property setter (gets validation automatically)
        """
        self.key_generation = value  # Delegates to property setter
        return self

    def getKeyStorageType(self) -> "String":
        """
        AUTOSAR-compliant getter for keyStorageType.

        Returns:
            The keyStorageType value

        Note:
            Delegates to key_storage_type property (CODING_RULE_V2_00017)
        """
        return self.key_storage_type  # Delegates to property

    def setKeyStorageType(self, value: "String") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for keyStorageType with method chaining.

        Args:
            value: The keyStorageType to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_storage_type property setter (gets validation automatically)
        """
        self.key_storage_type = value  # Delegates to property setter
        return self

    def getLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "PositiveInteger") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["String"]) -> "CryptoServiceKey":
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

    def with_development(self, value: Optional["ValueSpecification"]) -> "CryptoServiceKey":
        """
        Set development and return self for chaining.

        Args:
            value: The development to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_development("value")
        """
        self.development = value  # Use property setter (gets validation)
        return self

    def with_key_generation(self, value: Optional["CryptoServiceKey"]) -> "CryptoServiceKey":
        """
        Set keyGeneration and return self for chaining.

        Args:
            value: The keyGeneration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_generation("value")
        """
        self.key_generation = value  # Use property setter (gets validation)
        return self

    def with_key_storage_type(self, value: Optional["String"]) -> "CryptoServiceKey":
        """
        Set keyStorageType and return self for chaining.

        Args:
            value: The keyStorageType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_storage_type("value")
        """
        self.key_storage_type = value  # Use property setter (gets validation)
        return self

    def with_length(self, value: Optional["PositiveInteger"]) -> "CryptoServiceKey":
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self
