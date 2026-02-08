from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import BinaryManifestAddressableObject


class BinaryManifestItem(BinaryManifestAddressableObject):
    """
    This meta-class represents the ability to describe a specific handle or
    auxiliary field in the context of binary manifest resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestItem

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 919, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation is used to define structured Binary.
        self._auxiliaryField: List["BinaryManifestItem"] = []

    @property
    def auxiliary_field(self) -> List["BinaryManifestItem"]:
        """Get auxiliaryField (Pythonic accessor)."""
        return self._auxiliaryField
        # This aggregation represents the definition of a default for a binary manifest
                # handle or an auxiliaryField.
        # shall be taken if no connection for this possible.
        self._defaultValue: Optional["BinaryManifestItem"] = None

    @property
    def default_value(self) -> Optional["BinaryManifestItem"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["BinaryManifestItem"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, BinaryManifestItem):
            raise TypeError(
                f"defaultValue must be BinaryManifestItem or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # If true, the handle or auxiliary field in the context of binary relates to an
        # optional BinaryManifest is not used.
        self._isUnused: Optional["Boolean"] = None

    @property
    def is_unused(self) -> Optional["Boolean"]:
        """Get isUnused (Pythonic accessor)."""
        return self._isUnused

    @is_unused.setter
    def is_unused(self, value: Optional["Boolean"]) -> None:
        """
        Set isUnused with validation.

        Args:
            value: The isUnused to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isUnused = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isUnused must be Boolean or None, got {type(value).__name__}"
            )
        self._isUnused = value
        # This aggregation represents the definition of a value for a manifest handle
                # or an auxiliaryField.
        # shall be taken to establish a connection.
        self._value: Optional["BinaryManifestItem"] = None

    @property
    def value(self) -> Optional["BinaryManifestItem"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["BinaryManifestItem"]) -> None:
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

        if not isinstance(value, BinaryManifestItem):
            raise TypeError(
                f"value must be BinaryManifestItem or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuxiliaryField(self) -> List["BinaryManifestItem"]:
        """
        AUTOSAR-compliant getter for auxiliaryField.

        Returns:
            The auxiliaryField value

        Note:
            Delegates to auxiliary_field property (CODING_RULE_V2_00017)
        """
        return self.auxiliary_field  # Delegates to property

    def getDefaultValue(self) -> "BinaryManifestItem":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "BinaryManifestItem") -> "BinaryManifestItem":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getIsUnused(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isUnused.

        Returns:
            The isUnused value

        Note:
            Delegates to is_unused property (CODING_RULE_V2_00017)
        """
        return self.is_unused  # Delegates to property

    def setIsUnused(self, value: "Boolean") -> "BinaryManifestItem":
        """
        AUTOSAR-compliant setter for isUnused with method chaining.

        Args:
            value: The isUnused to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_unused property setter (gets validation automatically)
        """
        self.is_unused = value  # Delegates to property setter
        return self

    def getValue(self) -> "BinaryManifestItem":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "BinaryManifestItem") -> "BinaryManifestItem":
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

    def with_default_value(self, value: Optional["BinaryManifestItem"]) -> "BinaryManifestItem":
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_is_unused(self, value: Optional["Boolean"]) -> "BinaryManifestItem":
        """
        Set isUnused and return self for chaining.

        Args:
            value: The isUnused to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_unused("value")
        """
        self.is_unused = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["BinaryManifestItem"]) -> "BinaryManifestItem":
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
