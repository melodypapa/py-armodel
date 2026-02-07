from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestItemDefinition(Identifiable):
    """
    This meta-class provides the ability to define the handle definition or an
    auxiliary field of a binary manifest resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestItemDefinition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 920, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation is used to define structured Binary ManifestItemDefinitions.
        self._auxiliaryField: List["BinaryManifestItem"] = []

    @property
    def auxiliary_field(self) -> List["BinaryManifestItem"]:
        """Get auxiliaryField (Pythonic accessor)."""
        return self._auxiliaryField
        # If true, the handle definition or auxiliary field of a binary is optional and
        # may not be used in all to this BinaryManifest.
        self._isOptional: Optional["Boolean"] = None

    @property
    def is_optional(self) -> Optional["Boolean"]:
        """Get isOptional (Pythonic accessor)."""
        return self._isOptional

    @is_optional.setter
    def is_optional(self, value: Optional["Boolean"]) -> None:
        """
        Set isOptional with validation.

        Args:
            value: The isOptional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isOptional = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isOptional must be Boolean or None, got {type(value).__name__}"
            )
        self._isOptional = value
        # This attribute provides the ability to specify the size of the.
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

    def getIsOptional(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isOptional.

        Returns:
            The isOptional value

        Note:
            Delegates to is_optional property (CODING_RULE_V2_00017)
        """
        return self.is_optional  # Delegates to property

    def setIsOptional(self, value: "Boolean") -> "BinaryManifestItemDefinition":
        """
        AUTOSAR-compliant setter for isOptional with method chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_optional property setter (gets validation automatically)
        """
        self.is_optional = value  # Delegates to property setter
        return self

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "BinaryManifestItemDefinition":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_optional(self, value: Optional["Boolean"]) -> "BinaryManifestItemDefinition":
        """
        Set isOptional and return self for chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_optional("value")
        """
        self.is_optional = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional["PositiveInteger"]) -> "BinaryManifestItemDefinition":
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
