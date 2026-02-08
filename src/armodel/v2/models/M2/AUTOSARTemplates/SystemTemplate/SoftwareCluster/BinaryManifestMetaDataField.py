from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestAddressableObject,
)


class BinaryManifestMetaDataField(BinaryManifestAddressableObject):
    """
    This meta-class provides the ability to define a meta-data field for the
    binary manifest descriptor.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 923, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value of this attribute represents the size of the in bytes.
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"size must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._size = value
        # This attribute specifies the value of the meta-data field.
        self._value: Optional["VerbatimString"] = None

    @property
    def value(self) -> Optional["VerbatimString"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"value must be VerbatimString or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "BinaryManifestMetaDataField":
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    def getValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "VerbatimString") -> "BinaryManifestMetaDataField":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_size(self, value: Optional["PositiveInteger"]) -> "BinaryManifestMetaDataField":
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["VerbatimString"]) -> "BinaryManifestMetaDataField":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
